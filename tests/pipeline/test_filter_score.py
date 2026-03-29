"""Tests for the filter_score pipeline stage."""

import json

from saim.config.schemas import (
    QuickFilterConfig,
    RubricLevel,
    ScoringCriteria,
    StageThreshold,
    TeamProfile,
)
from saim.pipeline.filter_score import (
    apply_weights,
    create_batches,
    filter_survivors,
    merge_stage_results,
    read_batch,
    read_scored_ideas,
    score_idea,
    staged_filter,
    write_batch_results,
    write_scored_idea,
)


def _make_criteria():
    return [
        ScoringCriteria(
            name="theory_of_impact",
            description="Impact theory",
            default_weight=1.5,
            rubric=[],
        ),
        ScoringCriteria(
            name="low_compute",
            description="Compute requirements",
            default_weight=1.5,
            rubric=[],
        ),
        ScoringCriteria(
            name="novelty",
            description="Novelty",
            default_weight=1.0,
            rubric=[],
        ),
    ]


def _make_team(criteria_weights=None):
    return TeamProfile(
        name="Test Team",
        team_type="mentor_novice",
        criteria_weights=criteria_weights or {},
    )


def _make_idea(idea_id="gen-001"):
    return {
        "idea_id": idea_id,
        "run_id": "2026-03-19T14-30-00",
        "title": "Test Idea",
        "problem": "A test problem",
        "direction": "A test direction",
        "subfield": "interpretability",
    }


def _make_scored_idea(idea_id="gen-001", weighted_score=3.5, novelty_class="mostly_novel"):
    criteria = _make_criteria()
    team = _make_team()
    idea = _make_idea(idea_id)
    scored = score_idea(idea, criteria, team)
    scored["scores"]["theory_of_impact"] = {"score": 4, "reasoning": "Good", "confidence": 0.8}
    scored["scores"]["low_compute"] = {"score": 3, "reasoning": "OK", "confidence": 0.7}
    scored["scores"]["novelty"] = {"score": 4, "reasoning": "Derived", "confidence": 0.6}
    scored["weighted_score"] = weighted_score
    scored["novelty_assessment"]["classification"] = novelty_class
    return scored


class TestScoreIdea:
    def test_creates_scored_skeleton(self):
        criteria = _make_criteria()
        team = _make_team()
        idea = _make_idea()
        scored = score_idea(idea, criteria, team)

        assert scored["idea_id"] == "gen-001"
        assert scored["stage"] == "filter_score"
        assert scored["title"] == "Test Idea"
        assert scored["original_idea"] == idea
        assert "theory_of_impact" in scored["scores"]
        assert "low_compute" in scored["scores"]
        assert "novelty" in scored["scores"]
        assert scored["eliminated"] is False
        assert scored["elimination_reason"] is None

    def test_scores_have_empty_defaults(self):
        criteria = _make_criteria()
        team = _make_team()
        idea = _make_idea()
        scored = score_idea(idea, criteria, team)

        for name in ["theory_of_impact", "low_compute", "novelty"]:
            assert scored["scores"][name]["score"] == 0
            assert scored["scores"][name]["reasoning"] == ""
            assert scored["scores"][name]["confidence"] == 0.0


class TestApplyWeights:
    def test_default_weights(self):
        criteria = _make_criteria()
        team = _make_team()
        scores = {
            "theory_of_impact": {"score": 4, "reasoning": "", "confidence": 0.8},
            "low_compute": {"score": 3, "reasoning": "", "confidence": 0.7},
            "novelty": {"score": 5, "reasoning": "", "confidence": 0.9},
        }
        # (4*1.5 + 3*1.5 + 5*1.0) / (1.5 + 1.5 + 1.0) = (6+4.5+5)/4 = 15.5/4 = 3.875
        result = apply_weights(scores, criteria, team)
        assert abs(result - 3.875) < 0.001

    def test_team_weight_overrides(self):
        criteria = _make_criteria()
        team = _make_team(criteria_weights={"novelty": 0.5})
        scores = {
            "theory_of_impact": {"score": 4, "reasoning": "", "confidence": 0.8},
            "low_compute": {"score": 3, "reasoning": "", "confidence": 0.7},
            "novelty": {"score": 5, "reasoning": "", "confidence": 0.9},
        }
        # (4*1.5 + 3*1.5 + 5*0.5) / (1.5 + 1.5 + 0.5) = (6+4.5+2.5)/3.5 = 13/3.5 = 3.714...
        result = apply_weights(scores, criteria, team)
        assert abs(result - 13.0 / 3.5) < 0.001

    def test_zero_scores_excluded(self):
        criteria = _make_criteria()
        team = _make_team()
        scores = {
            "theory_of_impact": {"score": 4, "reasoning": "", "confidence": 0.8},
            "low_compute": {"score": 0, "reasoning": "", "confidence": 0.0},
            "novelty": {"score": 0, "reasoning": "", "confidence": 0.0},
        }
        # Only theory_of_impact: 4*1.5 / 1.5 = 4.0
        result = apply_weights(scores, criteria, team)
        assert abs(result - 4.0) < 0.001

    def test_all_zero_returns_zero(self):
        criteria = _make_criteria()
        team = _make_team()
        scores = {
            "theory_of_impact": {"score": 0, "reasoning": "", "confidence": 0.0},
        }
        result = apply_weights(scores, criteria, team)
        assert result == 0.0


class TestStagedFilter:
    def test_stage1_eliminates_low_scores(self):
        criteria = _make_criteria()
        team = _make_team()
        thresholds = StageThreshold(min_score=2.5, max_ideas=500)

        scored = _make_scored_idea(weighted_score=1.5)
        # Override scores so apply_weights returns < 2.0
        scored["scores"] = {
            "theory_of_impact": {"score": 1, "reasoning": "Bad", "confidence": 0.5},
            "low_compute": {"score": 1, "reasoning": "Bad", "confidence": 0.5},
            "novelty": {"score": 1, "reasoning": "Bad", "confidence": 0.5},
        }

        result = staged_filter([scored], criteria, thresholds, team)
        assert len(result) == 0
        assert scored["eliminated"] is True
        assert "Stage 1" in scored["elimination_reason"]

    def test_stage2_eliminates_below_threshold(self):
        criteria = _make_criteria()
        team = _make_team()
        thresholds = StageThreshold(min_score=3.5, max_ideas=500)

        scored = _make_scored_idea()
        # Scores that give weighted avg between 2.0 and 3.5
        scored["scores"] = {
            "theory_of_impact": {"score": 3, "reasoning": "OK", "confidence": 0.7},
            "low_compute": {"score": 2, "reasoning": "Low", "confidence": 0.6},
            "novelty": {"score": 3, "reasoning": "OK", "confidence": 0.6},
        }

        result = staged_filter([scored], criteria, thresholds, team)
        assert len(result) == 0
        assert scored["eliminated"] is True
        assert "Stage 2" in scored["elimination_reason"]

    def test_stage3_eliminates_already_solved(self):
        criteria = _make_criteria()
        team = _make_team()
        thresholds = StageThreshold(min_score=2.5, max_ideas=500)

        scored = _make_scored_idea(novelty_class="already_solved")
        scored["scores"] = {
            "theory_of_impact": {"score": 5, "reasoning": "Great", "confidence": 0.9},
            "low_compute": {"score": 5, "reasoning": "Great", "confidence": 0.9},
            "novelty": {"score": 1, "reasoning": "Solved", "confidence": 0.9},
        }
        scored["novelty_assessment"]["classification"] = "already_solved"

        result = staged_filter([scored], criteria, thresholds, team)
        assert len(result) == 0
        assert scored["eliminated"] is True
        assert "already_solved" in scored["elimination_reason"]
        assert scored["filter_stage_passed"] == 2

    def test_surviving_ideas_pass_all_stages(self):
        criteria = _make_criteria()
        team = _make_team()
        thresholds = StageThreshold(min_score=2.5, max_ideas=500)

        scored = _make_scored_idea(novelty_class="mostly_novel")
        scored["scores"] = {
            "theory_of_impact": {"score": 4, "reasoning": "Good", "confidence": 0.8},
            "low_compute": {"score": 4, "reasoning": "Good", "confidence": 0.8},
            "novelty": {"score": 4, "reasoning": "Good", "confidence": 0.8},
        }

        result = staged_filter([scored], criteria, thresholds, team)
        assert len(result) == 1
        assert result[0]["filter_stage_passed"] == 3
        assert result[0]["eliminated"] is False

    def test_stage1_uses_custom_threshold(self):
        criteria = _make_criteria()
        team = _make_team()
        thresholds = StageThreshold(min_score=2.0, max_ideas=500)
        qf = QuickFilterConfig(threshold=3.5)

        scored = _make_scored_idea()
        # Scores that give weighted avg ~3.0 (above default 2.0, below custom 3.5)
        scored["scores"] = {
            "theory_of_impact": {"score": 3, "reasoning": "OK", "confidence": 0.7},
            "low_compute": {"score": 3, "reasoning": "OK", "confidence": 0.7},
            "novelty": {"score": 3, "reasoning": "OK", "confidence": 0.7},
        }

        result = staged_filter([scored], criteria, thresholds, team, quick_filter=qf)
        assert len(result) == 0
        assert scored["eliminated"] is True
        assert "Stage 1" in scored["elimination_reason"]
        assert "3.5" in scored["elimination_reason"]

    def test_stage1_default_threshold_when_none(self):
        criteria = _make_criteria()
        team = _make_team()
        thresholds = StageThreshold(min_score=2.0, max_ideas=500)

        scored = _make_scored_idea()
        scored["scores"] = {
            "theory_of_impact": {"score": 1, "reasoning": "Bad", "confidence": 0.5},
            "low_compute": {"score": 1, "reasoning": "Bad", "confidence": 0.5},
            "novelty": {"score": 1, "reasoning": "Bad", "confidence": 0.5},
        }

        # No quick_filter arg — should default to threshold=2.0
        result = staged_filter([scored], criteria, thresholds, team)
        assert len(result) == 0
        assert scored["eliminated"] is True
        assert "Stage 1" in scored["elimination_reason"]

    def test_max_ideas_limit(self):
        criteria = _make_criteria()
        team = _make_team()
        thresholds = StageThreshold(min_score=2.0, max_ideas=2)

        ideas = []
        for i, score_val in enumerate([5, 3, 4], start=1):
            scored = _make_scored_idea(f"gen-{i:03d}", novelty_class="novel")
            scored["scores"] = {
                "theory_of_impact": {"score": score_val, "reasoning": "X", "confidence": 0.8},
                "low_compute": {"score": score_val, "reasoning": "X", "confidence": 0.8},
                "novelty": {"score": score_val, "reasoning": "X", "confidence": 0.8},
            }
            ideas.append(scored)

        result = staged_filter(ideas, criteria, thresholds, team)
        assert len(result) == 2
        # Top two by weighted score should survive
        surviving_ids = {r["idea_id"] for r in result}
        assert "gen-001" in surviving_ids  # score 5
        assert "gen-003" in surviving_ids  # score 4


class TestWriteRead:
    def test_write_creates_json(self, tmp_path):
        scored = _make_scored_idea()
        path = write_scored_idea(tmp_path, scored)

        assert path.exists()
        assert path.parent.name == "scored"
        assert path.name == "gen-001.json"

    def test_write_read_roundtrip(self, tmp_path):
        scored = _make_scored_idea("gen-001")
        write_scored_idea(tmp_path, scored)

        results = read_scored_ideas(tmp_path)
        assert len(results) == 1
        assert results[0]["idea_id"] == "gen-001"
        assert results[0]["stage"] == "filter_score"

    def test_read_multiple(self, tmp_path):
        for i in range(3):
            scored = _make_scored_idea(f"gen-{i + 1:03d}")
            write_scored_idea(tmp_path, scored)

        results = read_scored_ideas(tmp_path)
        assert len(results) == 3
        ids = [r["idea_id"] for r in results]
        assert ids == ["gen-001", "gen-002", "gen-003"]

    def test_read_empty_dir(self, tmp_path):
        assert read_scored_ideas(tmp_path) == []

    def test_write_content_valid_json(self, tmp_path):
        scored = _make_scored_idea()
        path = write_scored_idea(tmp_path, scored)

        with open(path) as f:
            data = json.load(f)

        assert data["idea_id"] == "gen-001"
        assert data["stage"] == "filter_score"
        assert "scores" in data
        assert "novelty_assessment" in data
        assert "citation_verification" in data


class TestQuickFilterConfig:
    def test_default_threshold(self):
        qf = QuickFilterConfig()
        assert qf.threshold == 2.0
        assert qf.rubric == []

    def test_custom_threshold_and_rubric(self):
        qf = QuickFilterConfig(
            threshold=3.0,
            rubric=[
                RubricLevel(score=1, label="Off-topic", description="Not AI Safety"),
                RubricLevel(score=3, label="Relevant", description="Clearly AI Safety"),
                RubricLevel(score=5, label="Precise", description="Well-scoped AI Safety"),
            ],
        )
        assert qf.threshold == 3.0
        assert len(qf.rubric) == 3
        assert qf.rubric[0].label == "Off-topic"
        assert qf.rubric[2].score == 5


def _write_generate_ideas(run_dir, count):
    """Write fake idea markdown files to generate/ for batch testing."""
    gen_dir = run_dir / "generate"
    gen_dir.mkdir(parents=True, exist_ok=True)
    for i in range(1, count + 1):
        idea_id = f"gen-{i:03d}"
        content = (
            f"---\n"
            f"idea_id: {idea_id}\n"
            f"run_id: test-run\n"
            f"title: Idea {i}\n"
            f"subfield: interpretability\n"
            f"---\n"
            f"Problem: Test problem {i}\n"
            f"Direction: Test direction {i}\n"
        )
        (gen_dir / f"{idea_id}.md").write_text(content)


class TestCreateBatches:
    def test_partitions_evenly(self, tmp_path):
        _write_generate_ideas(tmp_path, 10)
        paths = create_batches(tmp_path, stage=1, batch_size=5)
        assert len(paths) == 2
        batch1 = read_batch(paths[0])
        batch2 = read_batch(paths[1])
        assert len(batch1) == 5
        assert len(batch2) == 5

    def test_handles_remainder(self, tmp_path):
        _write_generate_ideas(tmp_path, 7)
        paths = create_batches(tmp_path, stage=1, batch_size=3)
        assert len(paths) == 3
        sizes = [len(read_batch(p)) for p in paths]
        assert sizes == [3, 3, 1]

    def test_single_batch(self, tmp_path):
        _write_generate_ideas(tmp_path, 3)
        paths = create_batches(tmp_path, stage=1, batch_size=100)
        assert len(paths) == 1
        assert len(read_batch(paths[0])) == 3

    def test_stage2_reads_from_survivors(self, tmp_path):
        survivors = [
            {"idea_id": "gen-001", "title": "Survivor 1"},
            {"idea_id": "gen-002", "title": "Survivor 2"},
        ]
        survivors_dir = tmp_path / "filter_score" / "survivors"
        survivors_dir.mkdir(parents=True)
        with open(survivors_dir / "stage1_survivors.json", "w") as f:
            json.dump(survivors, f)

        paths = create_batches(tmp_path, stage=2, batch_size=10)
        assert len(paths) == 1
        batch = read_batch(paths[0])
        assert len(batch) == 2
        assert batch[0]["idea_id"] == "gen-001"


class TestReadBatch:
    def test_reads_written_batch(self, tmp_path):
        ideas = [{"idea_id": "gen-001"}, {"idea_id": "gen-002"}]
        path = tmp_path / "batch.json"
        with open(path, "w") as f:
            json.dump(ideas, f)
        result = read_batch(path)
        assert len(result) == 2
        assert result[0]["idea_id"] == "gen-001"


class TestWriteBatchResults:
    def test_writes_results(self, tmp_path):
        results = [
            {"idea_id": "gen-001", "quick_score": 4, "eliminated": False},
            {"idea_id": "gen-002", "quick_score": 1, "eliminated": True},
        ]
        result_path = tmp_path / "results" / "stage1" / "batch_001_results.json"
        write_batch_results(result_path, results)
        assert result_path.exists()
        with open(result_path) as f:
            loaded = json.load(f)
        assert len(loaded) == 2

    def test_creates_parent_dirs(self, tmp_path):
        result_path = tmp_path / "deep" / "nested" / "results.json"
        write_batch_results(result_path, [{"idea_id": "gen-001"}])
        assert result_path.exists()


class TestMergeStageResults:
    def test_merges_multiple_batches(self, tmp_path):
        results_dir = tmp_path / "filter_score" / "results" / "stage1"
        results_dir.mkdir(parents=True)
        with open(results_dir / "batch_001_results.json", "w") as f:
            json.dump([{"idea_id": "gen-002"}, {"idea_id": "gen-001"}], f)
        with open(results_dir / "batch_002_results.json", "w") as f:
            json.dump([{"idea_id": "gen-003"}], f)

        merged = merge_stage_results(tmp_path, stage=1)
        assert len(merged) == 3
        # Should be sorted by idea_id
        assert [m["idea_id"] for m in merged] == ["gen-001", "gen-002", "gen-003"]

    def test_empty_when_no_results(self, tmp_path):
        assert merge_stage_results(tmp_path, stage=1) == []


class TestFilterSurvivors:
    def test_filters_eliminated(self, tmp_path):
        results_dir = tmp_path / "filter_score" / "results" / "stage1"
        results_dir.mkdir(parents=True)
        results = [
            {"idea_id": "gen-001", "eliminated": False, "title": "Good"},
            {"idea_id": "gen-002", "eliminated": True, "title": "Bad"},
            {"idea_id": "gen-003", "eliminated": False, "title": "Also good"},
        ]
        with open(results_dir / "batch_001_results.json", "w") as f:
            json.dump(results, f)

        survivors = filter_survivors(tmp_path, stage=1)
        assert len(survivors) == 2
        assert {s["idea_id"] for s in survivors} == {"gen-001", "gen-003"}

        # Verify file was written
        survivors_file = tmp_path / "filter_score" / "survivors" / "stage1_survivors.json"
        assert survivors_file.exists()
        with open(survivors_file) as f:
            loaded = json.load(f)
        assert len(loaded) == 2

    def test_all_eliminated(self, tmp_path):
        results_dir = tmp_path / "filter_score" / "results" / "stage1"
        results_dir.mkdir(parents=True)
        results = [
            {"idea_id": "gen-001", "eliminated": True},
        ]
        with open(results_dir / "batch_001_results.json", "w") as f:
            json.dump(results, f)

        survivors = filter_survivors(tmp_path, stage=1)
        assert len(survivors) == 0


# --- Edge case tests ---


class TestScoreIdeaEdgeCases:
    def test_missing_idea_id_defaults_to_unknown(self):
        criteria = _make_criteria()
        team = _make_team()
        idea = {"title": "No ID", "problem": "test"}
        scored = score_idea(idea, criteria, team)
        assert scored["idea_id"] == "unknown"
        assert scored["run_id"] == "unknown"

    def test_missing_title_defaults_to_empty(self):
        criteria = _make_criteria()
        team = _make_team()
        idea = {"idea_id": "gen-001", "run_id": "run-1"}
        scored = score_idea(idea, criteria, team)
        assert scored["title"] == ""

    def test_empty_criteria_list(self):
        team = _make_team()
        idea = _make_idea()
        scored = score_idea(idea, [], team)
        assert scored["scores"] == {}

    def test_original_idea_preserved_with_extra_fields(self):
        criteria = _make_criteria()
        team = _make_team()
        idea = _make_idea()
        idea["custom_field"] = "extra_data"
        idea["nested"] = {"key": "value"}
        scored = score_idea(idea, criteria, team)
        assert scored["original_idea"]["custom_field"] == "extra_data"
        assert scored["original_idea"]["nested"]["key"] == "value"

    def test_single_criterion(self):
        criteria = [
            ScoringCriteria(name="only_one", description="Single", default_weight=2.0, rubric=[]),
        ]
        team = _make_team()
        idea = _make_idea()
        scored = score_idea(idea, criteria, team)
        assert len(scored["scores"]) == 1
        assert "only_one" in scored["scores"]


class TestApplyWeightsEdgeCases:
    def test_empty_scores_dict(self):
        criteria = _make_criteria()
        team = _make_team()
        result = apply_weights({}, criteria, team)
        assert result == 0.0

    def test_score_entry_missing_score_key(self):
        criteria = _make_criteria()
        team = _make_team()
        scores = {
            "theory_of_impact": {"reasoning": "No score key", "confidence": 0.5},
        }
        # Missing "score" key defaults to 0 via .get("score", 0), so excluded
        result = apply_weights(scores, criteria, team)
        assert result == 0.0

    def test_unknown_criterion_uses_fallback_weight(self):
        criteria = _make_criteria()
        team = _make_team()
        scores = {
            "theory_of_impact": {"score": 4, "reasoning": "", "confidence": 0.8},
            "unknown_criterion": {"score": 2, "reasoning": "", "confidence": 0.5},
        }
        # theory_of_impact: 4*1.5=6, unknown: 2*1.0=2 (fallback), total: 8/(1.5+1.0)=3.2
        result = apply_weights(scores, criteria, team)
        assert abs(result - 8.0 / 2.5) < 0.001

    def test_team_weight_override_zero_excludes_criterion(self):
        criteria = _make_criteria()
        team = _make_team(criteria_weights={"novelty": 0.0})
        scores = {
            "theory_of_impact": {"score": 4, "reasoning": "", "confidence": 0.8},
            "novelty": {"score": 5, "reasoning": "", "confidence": 0.9},
        }
        # novelty has weight 0.0, so: 4*1.5 + 5*0.0 = 6, total_weight = 1.5+0.0 = 1.5
        result = apply_weights(scores, criteria, team)
        assert abs(result - 4.0) < 0.001

    def test_single_criterion_single_score(self):
        criteria = [
            ScoringCriteria(name="only", description="Only", default_weight=3.0, rubric=[]),
        ]
        team = _make_team()
        scores = {"only": {"score": 5, "reasoning": "", "confidence": 1.0}}
        result = apply_weights(scores, criteria, team)
        assert abs(result - 5.0) < 0.001

    def test_all_scores_have_same_value(self):
        criteria = _make_criteria()
        team = _make_team()
        scores = {
            "theory_of_impact": {"score": 3, "reasoning": "", "confidence": 0.5},
            "low_compute": {"score": 3, "reasoning": "", "confidence": 0.5},
            "novelty": {"score": 3, "reasoning": "", "confidence": 0.5},
        }
        # All 3 → weighted avg is 3.0 regardless of weights
        result = apply_weights(scores, criteria, team)
        assert abs(result - 3.0) < 0.001


class TestStagedFilterEdgeCases:
    def test_empty_ideas_list(self):
        criteria = _make_criteria()
        team = _make_team()
        thresholds = StageThreshold(min_score=2.5, max_ideas=500)
        result = staged_filter([], criteria, thresholds, team)
        assert result == []

    def test_idea_missing_scores_key(self):
        criteria = _make_criteria()
        team = _make_team()
        thresholds = StageThreshold(min_score=2.5, max_ideas=500)
        idea = {"idea_id": "gen-001", "eliminated": False}
        # No "scores" key → apply_weights gets {} → returns 0.0 → eliminated at Stage 1
        result = staged_filter([idea], criteria, thresholds, team)
        assert len(result) == 0
        assert idea["eliminated"] is True
        assert "Stage 1" in idea["elimination_reason"]

    def test_idea_missing_novelty_assessment_passes_stage3(self):
        criteria = _make_criteria()
        team = _make_team()
        thresholds = StageThreshold(min_score=2.0, max_ideas=500)
        scored = _make_scored_idea(novelty_class="novel")
        scored["scores"] = {
            "theory_of_impact": {"score": 4, "reasoning": "Good", "confidence": 0.8},
            "low_compute": {"score": 4, "reasoning": "Good", "confidence": 0.8},
            "novelty": {"score": 4, "reasoning": "Good", "confidence": 0.8},
        }
        # Remove novelty_assessment entirely
        del scored["novelty_assessment"]
        result = staged_filter([scored], criteria, thresholds, team)
        # Missing novelty_assessment → classification "" → not "already_solved" → passes
        assert len(result) == 1
        assert result[0]["filter_stage_passed"] == 3

    def test_score_exactly_at_stage1_threshold_passes(self):
        criteria = _make_criteria()
        team = _make_team()
        thresholds = StageThreshold(min_score=2.5, max_ideas=500)
        qf = QuickFilterConfig(threshold=2.0)
        scored = _make_scored_idea(novelty_class="novel")
        # Scores that give weighted avg exactly 2.0
        scored["scores"] = {
            "theory_of_impact": {"score": 2, "reasoning": "OK", "confidence": 0.5},
            "low_compute": {"score": 2, "reasoning": "OK", "confidence": 0.5},
            "novelty": {"score": 2, "reasoning": "OK", "confidence": 0.5},
        }
        result = staged_filter([scored], criteria, thresholds, team, quick_filter=qf)
        # 2.0 is NOT < 2.0, so passes Stage 1
        # But 2.0 < 2.5 (min_score), so eliminated at Stage 2
        assert len(result) == 0
        assert "Stage 2" in scored["elimination_reason"]
        assert scored["filter_stage_passed"] == 1

    def test_score_exactly_at_stage2_threshold_passes(self):
        criteria = _make_criteria()
        team = _make_team()
        thresholds = StageThreshold(min_score=2.5, max_ideas=500)
        scored = _make_scored_idea(novelty_class="novel")
        # Scores that give weighted avg exactly 2.5
        scored["scores"] = {
            "theory_of_impact": {"score": 3, "reasoning": "OK", "confidence": 0.5},
            "low_compute": {"score": 2, "reasoning": "OK", "confidence": 0.5},
            "novelty": {"score": 3, "reasoning": "OK", "confidence": 0.5},
        }
        # (3*1.5 + 2*1.5 + 3*1.0) / (1.5+1.5+1.0) = (4.5+3+3)/4 = 10.5/4 = 2.625
        result = staged_filter([scored], criteria, thresholds, team)
        # 2.625 >= 2.5 → passes Stage 2
        assert len(result) == 1
        assert result[0]["filter_stage_passed"] == 3

    def test_mixed_elimination_stages(self):
        criteria = _make_criteria()
        team = _make_team()
        thresholds = StageThreshold(min_score=3.0, max_ideas=500)

        # Idea 1: fails Stage 1 (score 1)
        idea1 = _make_scored_idea("gen-001", novelty_class="novel")
        idea1["scores"] = {
            "theory_of_impact": {"score": 1, "reasoning": "", "confidence": 0.5},
            "low_compute": {"score": 1, "reasoning": "", "confidence": 0.5},
            "novelty": {"score": 1, "reasoning": "", "confidence": 0.5},
        }

        # Idea 2: passes Stage 1, fails Stage 2 (score ~2.625)
        idea2 = _make_scored_idea("gen-002", novelty_class="novel")
        idea2["scores"] = {
            "theory_of_impact": {"score": 3, "reasoning": "", "confidence": 0.5},
            "low_compute": {"score": 2, "reasoning": "", "confidence": 0.5},
            "novelty": {"score": 3, "reasoning": "", "confidence": 0.5},
        }

        # Idea 3: passes Stage 1 & 2, fails Stage 3 (already_solved)
        idea3 = _make_scored_idea("gen-003", novelty_class="already_solved")
        idea3["scores"] = {
            "theory_of_impact": {"score": 5, "reasoning": "", "confidence": 0.9},
            "low_compute": {"score": 5, "reasoning": "", "confidence": 0.9},
            "novelty": {"score": 1, "reasoning": "", "confidence": 0.9},
        }

        # Idea 4: passes all stages
        idea4 = _make_scored_idea("gen-004", novelty_class="novel")
        idea4["scores"] = {
            "theory_of_impact": {"score": 5, "reasoning": "", "confidence": 0.9},
            "low_compute": {"score": 4, "reasoning": "", "confidence": 0.8},
            "novelty": {"score": 4, "reasoning": "", "confidence": 0.8},
        }

        result = staged_filter([idea1, idea2, idea3, idea4], criteria, thresholds, team)
        assert len(result) == 1
        assert result[0]["idea_id"] == "gen-004"

        assert idea1["filter_stage_passed"] == 0
        assert idea2["filter_stage_passed"] == 1
        assert idea3["filter_stage_passed"] == 2
        assert idea4["filter_stage_passed"] == 3

    def test_max_ideas_equal_to_survivors_keeps_all(self):
        criteria = _make_criteria()
        team = _make_team()
        thresholds = StageThreshold(min_score=2.0, max_ideas=3)

        ideas = []
        for i in range(1, 4):
            scored = _make_scored_idea(f"gen-{i:03d}", novelty_class="novel")
            scored["scores"] = {
                "theory_of_impact": {"score": 4, "reasoning": "X", "confidence": 0.8},
                "low_compute": {"score": 4, "reasoning": "X", "confidence": 0.8},
                "novelty": {"score": 4, "reasoning": "X", "confidence": 0.8},
            }
            ideas.append(scored)

        result = staged_filter(ideas, criteria, thresholds, team)
        assert len(result) == 3
        assert all(not r["eliminated"] for r in result)

    def test_max_ideas_dropped_ideas_marked_eliminated(self):
        criteria = _make_criteria()
        team = _make_team()
        thresholds = StageThreshold(min_score=2.0, max_ideas=1)

        ideas = []
        for i, score_val in enumerate([5, 3], start=1):
            scored = _make_scored_idea(f"gen-{i:03d}", novelty_class="novel")
            scored["scores"] = {
                "theory_of_impact": {"score": score_val, "reasoning": "X", "confidence": 0.8},
                "low_compute": {"score": score_val, "reasoning": "X", "confidence": 0.8},
                "novelty": {"score": score_val, "reasoning": "X", "confidence": 0.8},
            }
            ideas.append(scored)

        result = staged_filter(ideas, criteria, thresholds, team)
        assert len(result) == 1
        assert result[0]["idea_id"] == "gen-001"  # higher score
        assert ideas[1]["eliminated"] is True
        assert "max_ideas" in ideas[1]["elimination_reason"]

    def test_novelty_classifications_that_pass_stage3(self):
        """All novelty classifications except 'already_solved' should pass."""
        criteria = _make_criteria()
        team = _make_team()
        thresholds = StageThreshold(min_score=2.0, max_ideas=500)

        for classification in [
            "novel",
            "mostly_novel",
            "partially_addressed",
            "largely_addressed",
        ]:
            scored = _make_scored_idea("gen-001", novelty_class=classification)
            scored["scores"] = {
                "theory_of_impact": {"score": 4, "reasoning": "Good", "confidence": 0.8},
                "low_compute": {"score": 4, "reasoning": "Good", "confidence": 0.8},
                "novelty": {"score": 4, "reasoning": "Good", "confidence": 0.8},
            }
            result = staged_filter([scored], criteria, thresholds, team)
            assert len(result) == 1, f"Failed for classification={classification}"

    def test_weighted_score_updated_in_place(self):
        criteria = _make_criteria()
        team = _make_team()
        thresholds = StageThreshold(min_score=2.0, max_ideas=500)
        scored = _make_scored_idea(novelty_class="novel")
        scored["scores"] = {
            "theory_of_impact": {"score": 4, "reasoning": "Good", "confidence": 0.8},
            "low_compute": {"score": 3, "reasoning": "OK", "confidence": 0.7},
            "novelty": {"score": 5, "reasoning": "Novel", "confidence": 0.9},
        }
        scored["weighted_score"] = 0.0  # should be overwritten

        staged_filter([scored], criteria, thresholds, team)
        # (4*1.5 + 3*1.5 + 5*1.0) / (1.5+1.5+1.0) = 15.5/4 = 3.875
        assert abs(scored["weighted_score"] - 3.875) < 0.001


class TestWriteReadEdgeCases:
    def test_overwrite_existing_file(self, tmp_path):
        scored1 = _make_scored_idea("gen-001")
        scored1["weighted_score"] = 1.0
        write_scored_idea(tmp_path, scored1)

        scored2 = _make_scored_idea("gen-001")
        scored2["weighted_score"] = 5.0
        write_scored_idea(tmp_path, scored2)

        results = read_scored_ideas(tmp_path)
        assert len(results) == 1
        assert results[0]["weighted_score"] == 5.0

    def test_missing_idea_id_uses_unknown(self, tmp_path):
        scored = {"stage": "filter_score", "scores": {}}
        path = write_scored_idea(tmp_path, scored)
        assert path.name == "unknown.json"

    def test_read_ignores_subdirectories(self, tmp_path):
        scored = _make_scored_idea("gen-001")
        write_scored_idea(tmp_path, scored)
        # Create a subdirectory in filter_score/scored/
        sub = tmp_path / "filter_score" / "scored" / "nested"
        sub.mkdir()
        (sub / "extra.json").write_text("[]")

        results = read_scored_ideas(tmp_path)
        # Should only read top-level JSON files in scored/
        assert len(results) == 1
        assert results[0]["idea_id"] == "gen-001"


class TestCreateBatchesEdgeCases:
    def test_zero_ideas_returns_empty(self, tmp_path):
        gen_dir = tmp_path / "generate"
        gen_dir.mkdir(parents=True)
        paths = create_batches(tmp_path, stage=1, batch_size=10)
        assert paths == []

    def test_batch_size_one(self, tmp_path):
        _write_generate_ideas(tmp_path, 3)
        paths = create_batches(tmp_path, stage=1, batch_size=1)
        assert len(paths) == 3
        for p in paths:
            assert len(read_batch(p)) == 1

    def test_batch_size_equal_to_count(self, tmp_path):
        _write_generate_ideas(tmp_path, 5)
        paths = create_batches(tmp_path, stage=1, batch_size=5)
        assert len(paths) == 1
        assert len(read_batch(paths[0])) == 5

    def test_stage3_reads_from_stage2_survivors(self, tmp_path):
        survivors = [{"idea_id": "gen-010", "title": "Survivor from stage 2"}]
        survivors_dir = tmp_path / "filter_score" / "survivors"
        survivors_dir.mkdir(parents=True)
        with open(survivors_dir / "stage2_survivors.json", "w") as f:
            json.dump(survivors, f)

        paths = create_batches(tmp_path, stage=3, batch_size=10)
        assert len(paths) == 1
        batch = read_batch(paths[0])
        assert batch[0]["idea_id"] == "gen-010"

    def test_batch_files_numbered_sequentially(self, tmp_path):
        _write_generate_ideas(tmp_path, 10)
        paths = create_batches(tmp_path, stage=1, batch_size=3)
        names = [p.name for p in paths]
        assert names == ["batch_001.json", "batch_002.json", "batch_003.json", "batch_004.json"]

    def test_all_ideas_accounted_for_across_batches(self, tmp_path):
        _write_generate_ideas(tmp_path, 23)
        paths = create_batches(tmp_path, stage=1, batch_size=7)
        total = sum(len(read_batch(p)) for p in paths)
        assert total == 23

    def test_batch_content_preserves_idea_fields(self, tmp_path):
        _write_generate_ideas(tmp_path, 1)
        paths = create_batches(tmp_path, stage=1, batch_size=10)
        batch = read_batch(paths[0])
        idea = batch[0]
        assert idea["idea_id"] == "gen-001"
        assert idea["run_id"] == "test-run"
        assert idea["title"] == "Idea 1"
        assert "body" in idea  # from read_idea_sketches


class TestReadBatchEdgeCases:
    def test_empty_batch_file(self, tmp_path):
        path = tmp_path / "empty.json"
        path.write_text("[]")
        result = read_batch(path)
        assert result == []


class TestWriteBatchResultsEdgeCases:
    def test_empty_results_list(self, tmp_path):
        result_path = tmp_path / "empty_results.json"
        write_batch_results(result_path, [])
        with open(result_path) as f:
            loaded = json.load(f)
        assert loaded == []

    def test_overwrite_existing_results(self, tmp_path):
        result_path = tmp_path / "results.json"
        write_batch_results(result_path, [{"idea_id": "gen-001", "score": 1}])
        write_batch_results(result_path, [{"idea_id": "gen-001", "score": 5}])
        with open(result_path) as f:
            loaded = json.load(f)
        assert len(loaded) == 1
        assert loaded[0]["score"] == 5

    def test_results_roundtrip_with_batch_read(self, tmp_path):
        results = [
            {"idea_id": "gen-001", "scores": {"a": 1}, "nested": {"x": [1, 2, 3]}},
        ]
        result_path = tmp_path / "results.json"
        write_batch_results(result_path, results)
        loaded = read_batch(result_path)  # read_batch works on any JSON array file
        assert loaded[0]["nested"]["x"] == [1, 2, 3]


class TestMergeStageResultsEdgeCases:
    def test_single_batch(self, tmp_path):
        results_dir = tmp_path / "filter_score" / "results" / "stage2"
        results_dir.mkdir(parents=True)
        with open(results_dir / "batch_001_results.json", "w") as f:
            json.dump([{"idea_id": "gen-005"}], f)
        merged = merge_stage_results(tmp_path, stage=2)
        assert len(merged) == 1
        assert merged[0]["idea_id"] == "gen-005"

    def test_ignores_non_matching_files(self, tmp_path):
        results_dir = tmp_path / "filter_score" / "results" / "stage1"
        results_dir.mkdir(parents=True)
        with open(results_dir / "batch_001_results.json", "w") as f:
            json.dump([{"idea_id": "gen-001"}], f)
        # Create a non-matching file
        with open(results_dir / "metadata.json", "w") as f:
            json.dump({"info": "not a batch"}, f)
        with open(results_dir / "summary.txt", "w") as f:
            f.write("not json")

        merged = merge_stage_results(tmp_path, stage=1)
        assert len(merged) == 1
        assert merged[0]["idea_id"] == "gen-001"

    def test_empty_batch_result_files(self, tmp_path):
        results_dir = tmp_path / "filter_score" / "results" / "stage1"
        results_dir.mkdir(parents=True)
        with open(results_dir / "batch_001_results.json", "w") as f:
            json.dump([], f)
        with open(results_dir / "batch_002_results.json", "w") as f:
            json.dump([{"idea_id": "gen-001"}], f)

        merged = merge_stage_results(tmp_path, stage=1)
        assert len(merged) == 1

    def test_sorts_across_batches(self, tmp_path):
        results_dir = tmp_path / "filter_score" / "results" / "stage1"
        results_dir.mkdir(parents=True)
        with open(results_dir / "batch_002_results.json", "w") as f:
            json.dump([{"idea_id": "gen-001"}], f)
        with open(results_dir / "batch_001_results.json", "w") as f:
            json.dump([{"idea_id": "gen-003"}, {"idea_id": "gen-002"}], f)

        merged = merge_stage_results(tmp_path, stage=1)
        ids = [m["idea_id"] for m in merged]
        assert ids == ["gen-001", "gen-002", "gen-003"]

    def test_different_stages_independent(self, tmp_path):
        for stage in [1, 2]:
            results_dir = tmp_path / "filter_score" / "results" / f"stage{stage}"
            results_dir.mkdir(parents=True)
            with open(results_dir / "batch_001_results.json", "w") as f:
                json.dump([{"idea_id": f"stage{stage}-idea"}], f)

        merged1 = merge_stage_results(tmp_path, stage=1)
        merged2 = merge_stage_results(tmp_path, stage=2)
        assert merged1[0]["idea_id"] == "stage1-idea"
        assert merged2[0]["idea_id"] == "stage2-idea"


class TestFilterSurvivorsEdgeCases:
    def test_missing_eliminated_key_treated_as_survivor(self, tmp_path):
        results_dir = tmp_path / "filter_score" / "results" / "stage1"
        results_dir.mkdir(parents=True)
        results = [
            {"idea_id": "gen-001", "title": "No eliminated key"},
        ]
        with open(results_dir / "batch_001_results.json", "w") as f:
            json.dump(results, f)

        survivors = filter_survivors(tmp_path, stage=1)
        assert len(survivors) == 1
        assert survivors[0]["idea_id"] == "gen-001"

    def test_all_survive(self, tmp_path):
        results_dir = tmp_path / "filter_score" / "results" / "stage1"
        results_dir.mkdir(parents=True)
        results = [
            {"idea_id": "gen-001", "eliminated": False},
            {"idea_id": "gen-002", "eliminated": False},
        ]
        with open(results_dir / "batch_001_results.json", "w") as f:
            json.dump(results, f)

        survivors = filter_survivors(tmp_path, stage=1)
        assert len(survivors) == 2

    def test_survivors_from_multiple_batches(self, tmp_path):
        results_dir = tmp_path / "filter_score" / "results" / "stage2"
        results_dir.mkdir(parents=True)
        with open(results_dir / "batch_001_results.json", "w") as f:
            json.dump(
                [
                    {"idea_id": "gen-001", "eliminated": False},
                    {"idea_id": "gen-002", "eliminated": True},
                ],
                f,
            )
        with open(results_dir / "batch_002_results.json", "w") as f:
            json.dump(
                [
                    {"idea_id": "gen-003", "eliminated": True},
                    {"idea_id": "gen-004", "eliminated": False},
                ],
                f,
            )

        survivors = filter_survivors(tmp_path, stage=2)
        assert len(survivors) == 2
        assert {s["idea_id"] for s in survivors} == {"gen-001", "gen-004"}

    def test_survivors_file_readable_by_create_batches(self, tmp_path):
        """Integration: filter_survivors output can feed create_batches for next stage."""
        results_dir = tmp_path / "filter_score" / "results" / "stage1"
        results_dir.mkdir(parents=True)
        results = [
            {"idea_id": "gen-001", "eliminated": False, "title": "Survivor A"},
            {"idea_id": "gen-002", "eliminated": True, "title": "Dead"},
            {"idea_id": "gen-003", "eliminated": False, "title": "Survivor B"},
        ]
        with open(results_dir / "batch_001_results.json", "w") as f:
            json.dump(results, f)

        filter_survivors(tmp_path, stage=1)

        # Now create_batches for stage 2 should read from stage1 survivors
        paths = create_batches(tmp_path, stage=2, batch_size=10)
        assert len(paths) == 1
        batch = read_batch(paths[0])
        assert len(batch) == 2
        assert {b["idea_id"] for b in batch} == {"gen-001", "gen-003"}

    def test_create_batches_stage2_enriches_with_original_idea(self, tmp_path):
        """Stage 2+ batches include original_idea from the generate stage."""
        from saim.pipeline.generate import write_idea_sketch

        # Write generate-stage ideas with full body
        idea_data = {
            "idea_id": "gen-001",
            "run_id": "test-run",
            "subfield": "interpretability",
            "generation_strategy": "novel_direction",
            "confidence": 0.8,
            "title": "Full Idea Title",
            "problem": "A detailed problem description",
            "direction": "A detailed approach direction",
            "why_it_matters": "Impact explanation",
            "relevant_context": "Paper A. Paper B.",
        }
        write_idea_sketch(tmp_path, idea_data)

        # Create stage 1 survivors (minimal output, no body)
        results_dir = tmp_path / "filter_score" / "results" / "stage1"
        results_dir.mkdir(parents=True)
        results = [
            {
                "idea_id": "gen-001",
                "title": "Full Idea Title",
                "run_id": "test-run",
                "quick_score": 4,
                "eliminated": False,
            },
        ]
        with open(results_dir / "batch_001_results.json", "w") as f:
            json.dump(results, f)

        filter_survivors(tmp_path, stage=1)

        # Create stage 2 batches — should be enriched
        paths = create_batches(tmp_path, stage=2, batch_size=10)
        batch = read_batch(paths[0])

        assert len(batch) == 1
        item = batch[0]
        assert "original_idea" in item
        assert item["original_idea"]["body"] is not None
        assert "detailed problem" in item["original_idea"]["body"]
        assert item["original_idea"]["idea_id"] == "gen-001"

    def test_create_batches_stage2_without_generate_data(self, tmp_path):
        """Stage 2+ batches work even if generate data is missing for some ideas."""
        results_dir = tmp_path / "filter_score" / "results" / "stage1"
        results_dir.mkdir(parents=True)
        results = [
            {"idea_id": "gen-099", "eliminated": False, "title": "Unknown Idea"},
        ]
        with open(results_dir / "batch_001_results.json", "w") as f:
            json.dump(results, f)

        filter_survivors(tmp_path, stage=1)

        # No generate directory exists — should still work, just no enrichment
        paths = create_batches(tmp_path, stage=2, batch_size=10)
        batch = read_batch(paths[0])
        assert len(batch) == 1
        assert "original_idea" not in batch[0]

    def test_empty_results_writes_empty_survivors(self, tmp_path):
        results_dir = tmp_path / "filter_score" / "results" / "stage1"
        results_dir.mkdir(parents=True)
        with open(results_dir / "batch_001_results.json", "w") as f:
            json.dump([], f)

        survivors = filter_survivors(tmp_path, stage=1)
        assert survivors == []

        survivors_file = tmp_path / "filter_score" / "survivors" / "stage1_survivors.json"
        assert survivors_file.exists()
        with open(survivors_file) as f:
            loaded = json.load(f)
        assert loaded == []
