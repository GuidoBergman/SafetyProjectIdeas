#!/usr/bin/env python3
"""Batch process agent JSONL output files to extract JSON ideas and write them to the run directory."""

import json
import re
import sys
import subprocess
from pathlib import Path

TASK_DIR = Path("/tmp/claude-1000/-home-gbergman-YDKHHICF-SafetyProjectIdeas/32c03bc7-4af0-4413-be97-69499ac33b84/tasks")
RUN_DIR = "data/runs/2026-03-19T19-58-40"
RUN_ID = "2026-03-19T19-58-40"

def extract_text_from_jsonl(filepath):
    """Extract all assistant text content from a JSONL conversation file."""
    texts = []
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                msg = json.loads(line)
                if msg.get('type') == 'assistant' and 'message' in msg:
                    content = msg['message'].get('content', [])
                    if isinstance(content, list):
                        for block in content:
                            if isinstance(block, dict) and block.get('type') == 'text':
                                texts.append(block.get('text', ''))
                    elif isinstance(content, str):
                        texts.append(content)
            except json.JSONDecodeError:
                continue
    return '\n'.join(texts)

def extract_json_arrays(text):
    """Extract all JSON arrays from text, handling markdown code blocks."""
    arrays = []
    # Find JSON arrays in code blocks
    pattern = r'```(?:json)?\s*(\[[\s\S]*?\])\s*```'
    matches = re.findall(pattern, text)
    for match in matches:
        try:
            parsed = json.loads(match)
            if isinstance(parsed, list) and len(parsed) > 0:
                if isinstance(parsed[0], dict) and 'title' in parsed[0]:
                    arrays.append(parsed)
        except json.JSONDecodeError:
            continue
    return arrays

def main():
    output_files = sorted(TASK_DIR.glob("*.output"))
    print(f"Found {len(output_files)} output files")

    all_ideas = []
    warnings = []
    files_with_ideas = 0
    files_without = 0

    for fpath in output_files:
        try:
            text = extract_text_from_jsonl(fpath)
            if not text:
                continue

            arrays = extract_json_arrays(text)
            if arrays:
                # Take the largest array (the main result)
                best = max(arrays, key=len)
                count_before = len(all_ideas)
                for idea in best:
                    if isinstance(idea, dict) and 'title' in idea:
                        all_ideas.append(idea)
                added = len(all_ideas) - count_before
                if added > 0:
                    files_with_ideas += 1
                    print(f"  {fpath.name}: {added} ideas")
            else:
                files_without += 1
        except Exception as e:
            warnings.append(f"Error processing {fpath.name}: {e}")

    print(f"\nFiles with ideas: {files_with_ideas}")
    print(f"Files without ideas: {files_without}")
    print(f"Total extracted: {len(all_ideas)} ideas")
    print(f"Warnings: {len(warnings)}")
    for w in warnings:
        print(f"  - {w}")

    # Deduplicate by title
    seen_titles = set()
    unique_ideas = []
    duplicates = 0
    for idea in all_ideas:
        title = idea.get('title', '').strip()
        if title and title not in seen_titles:
            seen_titles.add(title)
            unique_ideas.append(idea)
        else:
            duplicates += 1

    print(f"\nAfter dedup: {len(unique_ideas)} unique ideas ({duplicates} duplicates removed)")

    # Count by subfield and strategy
    subfield_counts = {}
    strategy_counts = {}
    for idea in unique_ideas:
        sf = idea.get('subfield', 'unknown')
        st = idea.get('generation_strategy', 'unknown')
        subfield_counts[sf] = subfield_counts.get(sf, 0) + 1
        strategy_counts[st] = strategy_counts.get(st, 0) + 1

    print("\nIdeas per subfield:")
    for sf, count in sorted(subfield_counts.items(), key=lambda x: -x[1]):
        print(f"  {sf}: {count}")

    print("\nIdeas per strategy:")
    for st, count in sorted(strategy_counts.items(), key=lambda x: -x[1]):
        print(f"  {st}: {count}")

    # Save summary for metadata
    summary = {
        'total_ideas': len(unique_ideas),
        'subfield_counts': subfield_counts,
        'strategy_counts': strategy_counts,
        'duplicates_removed': duplicates,
        'warnings': warnings
    }
    summary_path = Path(RUN_DIR) / "generate" / "_summary.json"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    with open(summary_path, 'w') as f:
        json.dump(summary, f, indent=2)

    # Write ideas to run directory
    print(f"\nWriting {len(unique_ideas)} ideas to {RUN_DIR}/generate/...")

    success = 0
    errors = 0
    for i, idea in enumerate(unique_ideas):
        idea_id = f"gen-{i+1:04d}"
        idea['idea_id'] = idea_id
        idea['run_id'] = RUN_ID

        json_str = json.dumps(idea)
        # Escape for shell
        json_str_escaped = json_str.replace("'", "'\\''")

        cmd = f"uv run python -m saim.pipeline.generate write {RUN_DIR} '{json_str_escaped}'"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)

        if result.returncode == 0:
            success += 1
        else:
            errors += 1
            if errors <= 3:
                print(f"  Error on {idea_id}: {result.stderr[:200]}")

        if (i + 1) % 200 == 0:
            print(f"  Progress: {i+1}/{len(unique_ideas)} ({success} success, {errors} errors)")

    print(f"\nDone! {success} written, {errors} errors out of {len(unique_ideas)} total")

    # Update summary
    summary['ideas_written'] = success
    summary['write_errors'] = errors
    with open(summary_path, 'w') as f:
        json.dump(summary, f, indent=2)

    return summary

if __name__ == "__main__":
    main()
