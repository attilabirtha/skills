# Repository Agent Instructions

This is a multi-skill repository. Each skill is self-contained under `skills/<skill-name>/`.

## For AI Agents

When the user asks to use or modify a skill:

1. Identify the relevant folder under `skills/`.
2. Read that skill's `SKILL.md`.
3. If present, read that skill's `AGENTS.md`.
4. Use only that skill's bundled `assets/`, `scripts/`, and `references/` unless the task explicitly requires repository-wide changes.
5. Keep each skill portable; do not add dependencies on local absolute paths.

## Current Skills

- `skills/proclick-price-offer` - generate branded ProClick commercial offer PDFs.

## Validation

For Codex skills, validate with Codex's `quick_validate.py` when available:

```bash
python3 /path/to/quick_validate.py skills/<skill-name>
```

For script-based skills, also run the skill's main script from inside its folder.
