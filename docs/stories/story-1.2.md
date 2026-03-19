# Story 1.2: Configuration Management Skill & Participant Profiles

## Story Info

- **Epic:** Epic 1 - Project Foundation & Team Configuration
- **Story ID:** story-1.2
- **Status:** review_complete
- **Created:** 2026-03-16
- **FRs Covered:** FR52, FR53, FR54, FR55, FR56, FR57, FR66

## User Story

As a coordinator,
I want to manage team profiles, scoring criteria, pipeline settings, and participant profiles through conversation or direct YAML editing,
So that the pipeline is calibrated to BAISH's teams and individual researchers.

## Acceptance Criteria

### AC1: Configuration Management Skill

**Given** the config schemas and loader from Story 1.1 exist
**When** the coordinator invokes `/configure-teams`
**Then** the skill displays current team profiles, scoring criteria, and the current default participant (if set)
**And** the coordinator can add, edit, or remove team profiles through conversation
**And** the coordinator can modify scoring criteria weights per team type
**And** the coordinator can add custom scoring criteria beyond the default set (FR54)
**And** the coordinator can configure pipeline settings including model assignments per stage (FR55)
**And** the coordinator can set or clear the default participant (used when no participant is specified at pipeline runtime)
**And** all changes are written back to the appropriate YAML config files
**And** changes are validated against Pydantic schemas before saving
**And** updated config persists across sessions (FR57)

### AC2: Participant Profile Loading & Validation

**Given** a participant profile YAML file is created in `config/participants/<name>.yaml`
**When** the profile is loaded
**Then** it is validated against the ParticipantProfile Pydantic schema
**And** contains: name, experience_level, technical_background (list of skills), compute_resources, time_availability

### AC3: Automatic Profile-Based Tailoring

**Given** a participant profile exists for a user
**When** an idea generation or brainstorming skill is invoked
**Then** the system loads the matching participant profile automatically and uses it to tailor generation

### AC4: Conversational Fallback Without Profile

**Given** no participant profile exists for a user
**When** an idea generation or brainstorming skill is invoked
**Then** the system falls back to conversational discovery, guiding the user through describing their constraints

## Technical Notes

### Architecture References

- All config access through Pydantic models -- never raw YAML parsing in pipeline code
- YAML as source of truth (FR56) -- Pydantic validates on load, YAML files are canonical
- Claude Code skills (markdown) for pipeline orchestration; Python for programmatic components
- Skills invoke Python via `uv run python -m safety_ideas.<module>`
- Configuration persists across sessions via YAML files on disk (FR57)
- Participant profiles stored in `config/participants/` as individual YAML files

### Key Design Decisions

- **Skill-based configuration management:** The `/configure-teams` skill provides a conversational interface for editing config, but all changes ultimately write to YAML files that can also be edited directly.
- **Validation before save:** All config changes are validated against Pydantic schemas before writing to disk. Invalid changes are rejected with clear error messages.
- **Participant profile auto-detection:** When a skill is invoked, the system checks `config/participants/` for a matching profile. If found, it loads and applies constraints automatically. If not found, it falls back to conversational discovery (FR66).
- **Default participant:** A `default_participant` setting in `teams.yaml` allows selecting one participant profile as the default, used when no participant is specified at pipeline runtime. Configurable via `set-default-participant` / `clear-default-participant` CLI commands.
- **Separation of team profiles and participant profiles:** Team profiles define team-level constraints (compute budget, team type, criteria weights). Participant profiles define individual-level constraints (experience, skills, resources, availability). Both influence idea generation and brainstorming.

### File Structure

```
config/
  teams.yaml              # Team profiles, default_team, default_participant (edited via /configure-teams or directly)
  criteria.yaml           # Scoring criteria with weights (edited via /configure-teams or directly)
  pipeline.yaml           # Pipeline settings, model assignments (edited via /configure-teams or directly)
  kb-criteria.yaml        # KB inclusion criteria
  participants/
    <name>.yaml           # Individual participant profiles
.claude/commands/
  configure-teams.md      # Claude Code skill for configuration management
```

### NFRs Addressed

- **NFR11:** Modular skill design -- configuration management is independent of pipeline stages
- **NFR12:** All configurable parameters externalized in YAML
- **NFR13:** Config schemas define interfaces; changes validated before save

## Dependencies

- **Story 1.1:** Requires project structure, Pydantic schemas, config loader, and default configuration files

## Test Strategy

- Unit tests for config write-back: modify config in memory, save to YAML, reload and verify
- Unit tests for participant profile validation: valid profiles, missing fields, invalid values
- Unit tests for profile auto-detection: profile exists, profile missing, multiple profiles
- Integration test: invoke `/configure-teams`, modify a team profile, verify YAML file updated
- Integration test: create participant profile YAML, load via config loader, verify Pydantic validation
- Verify conversational fallback behavior when no participant profile exists

## Story Validation Checklist

- [ ] All acceptance criteria have clear Given/When/Then format
- [ ] Each AC is independently testable
- [ ] Technical notes reference architecture decisions
- [ ] Dependencies are identified (Story 1.1)
- [ ] NFRs addressed are listed
- [ ] Story is implementable in a single sprint
- [ ] No ambiguous requirements -- file paths, schema fields, and skill behavior are specified
