#!/usr/bin/env python3
"""Batch process agent JSONL output files to extract JSON ideas and write them to the run directory."""

import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from saim.pipeline.generate import write_idea_sketch

RUN_DIR = Path("/home/gbergman/YDKHHICF/saim/data/runs/2026-04-07T15-12-49")
RUN_ID = "2026-04-07T15-12-49"

AGENT_FILES = [
    "/tmp/claude-1000/-home-gbergman-YDKHHICF-saim/78e7e2b3-6b91-4fe1-a351-0ce7f33b7c05/tasks/a6f3184e10194a445.output",
    "/tmp/claude-1000/-home-gbergman-YDKHHICF-saim/78e7e2b3-6b91-4fe1-a351-0ce7f33b7c05/tasks/ae7a3201eff1765bf.output",
    "/tmp/claude-1000/-home-gbergman-YDKHHICF-saim/78e7e2b3-6b91-4fe1-a351-0ce7f33b7c05/tasks/a0c7f59ff001ef945.output",
    "/tmp/claude-1000/-home-gbergman-YDKHHICF-saim/78e7e2b3-6b91-4fe1-a351-0ce7f33b7c05/tasks/a6bca2b6474e87fe7.output",
    "/tmp/claude-1000/-home-gbergman-YDKHHICF-saim/78e7e2b3-6b91-4fe1-a351-0ce7f33b7c05/tasks/ab5a5fe5c60bc474c.output",
    "/tmp/claude-1000/-home-gbergman-YDKHHICF-saim/78e7e2b3-6b91-4fe1-a351-0ce7f33b7c05/tasks/a688731737b97e660.output",
]


def extract_text_from_jsonl(filepath: str) -> str:
    """Read JSONL file and concatenate all assistant text blocks."""
    all_text = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            msg = obj.get("message", {})
            content = msg.get("content", "")
            if isinstance(content, str):
                all_text.append(content)
            elif isinstance(content, list):
                for block in content:
                    if isinstance(block, dict) and block.get("type") == "text":
                        all_text.append(block.get("text", ""))
    return "\n".join(all_text)


def extract_json_array(text: str) -> list[dict]:
    """Extract the largest JSON array from text containing markdown code blocks."""
    text = html.unescape(text)
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', text)

    # Split on ```json markers and try each block
    blocks = text.split("```json")
    all_results = []

    for block_text in blocks[1:]:  # Skip text before first marker
        # Find the end of the code block
        end_marker = block_text.find("\n```")
        if end_marker > 0:
            json_text = block_text[:end_marker].strip()
        else:
            json_text = block_text.strip()

        if not json_text.startswith("["):
            continue

        decoder = json.JSONDecoder(strict=False)
        try:
            result, _ = decoder.raw_decode(json_text)
            if isinstance(result, list) and len(result) > 0:
                all_results.append(result)
        except json.JSONDecodeError:
            continue

    if all_results:
        # Return the largest array
        return max(all_results, key=len)
    return []


def main():
    all_ideas = []
    subfield_counts: dict[str, int] = {}
    strategy_counts: dict[str, int] = {}
    seen_titles: set[str] = set()

    for fpath in AGENT_FILES:
        p = Path(fpath)
        if not p.exists():
            print(f"SKIP (not found): {p.name}")
            continue

        text = extract_text_from_jsonl(fpath)
        ideas = extract_json_array(text)

        if not ideas:
            print(f"WARN: No JSON array found in {p.name} (text len: {len(text)})")
            continue

        new_ideas = []
        for idea in ideas:
            if not isinstance(idea, dict):
                continue
            title = idea.get("title", "").strip()
            if not title:
                continue
            norm_title = title.lower().strip()
            if norm_title in seen_titles:
                continue
            seen_titles.add(norm_title)
            new_ideas.append(idea)

        subfield = new_ideas[0].get("subfield", "unknown") if new_ideas else "unknown"
        print(f"Loaded {len(new_ideas)} unique ideas from {p.name} (subfield: {subfield})")
        all_ideas.extend(new_ideas)

    print(f"\nTotal unique ideas: {len(all_ideas)}")

    written = 0
    errors = 0
    for i, idea in enumerate(all_ideas, 1):
        idea_id = f"gen-{i:04d}"
        idea["idea_id"] = idea_id
        idea["run_id"] = RUN_ID

        try:
            idea["confidence"] = float(idea.get("confidence", 0.5))
        except (ValueError, TypeError):
            idea["confidence"] = 0.5

        for key in [
            "title", "problem", "direction", "why_it_matters",
            "relevant_context", "subfield", "generation_strategy",
        ]:
            if key in idea and isinstance(idea[key], str):
                idea[key] = html.unescape(idea[key])

        sf = idea.get("subfield", "unknown")
        subfield_counts[sf] = subfield_counts.get(sf, 0) + 1
        gs = idea.get("generation_strategy", "unknown")
        strategy_counts[gs] = strategy_counts.get(gs, 0) + 1

        try:
            write_idea_sketch(RUN_DIR, idea)
            written += 1
        except Exception as e:
            errors += 1
            if errors <= 5:
                print(f"  ERROR writing {idea_id}: {e}")

    print(f"\nWritten: {written}, Errors: {errors}")
    print("\nPer subfield:")
    for sf, count in sorted(subfield_counts.items()):
        print(f"  {sf}: {count}")
    print("\nPer strategy:")
    for gs, count in sorted(strategy_counts.items()):
        print(f"  {gs}: {count}")


if __name__ == "__main__":
    main()
