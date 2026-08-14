# Skills

Reusable AI-agent skills maintained by Attila Birtha.

This repository is structured as a multi-skill catalog. Each skill lives in its own folder under `skills/` and can be copied, installed, or referenced independently by Codex, OpenClaw, Claude Code, Cursor, or other coding agents.

## Available Skills

### `proclick-price-offer`

Generate ProClick-style commercial offer PDFs using the look and feel of the ProClick agency presentation.

Path:

```bash
skills/proclick-price-offer
```

Run directly:

```bash
cd skills/proclick-price-offer
python3 scripts/generate_offer.py --output outputs/proclick_offer.pdf
```

Install for Codex:

```bash
cp -R skills/proclick-price-offer ~/.codex/skills/
```

Then invoke:

```text
Use $proclick-price-offer to create a branded ProClick commercial offer PDF.
```

### `proclick-ssh-servers`

Connect to Proclick's servers (`services-proclick`, `agents-proclick`)
and the `birtha` home server over SSH via the `ssh-mcp` toolset.

Path:

```bash
skills/proclick-ssh-servers
```

Requirements: the `ssh-mcp` MCP server configured with
`~/.config/ssh-mcp/config.toml`, access to the headscale tailnet, and
SSH key / password credentials (see the skill's `README.md`).

Then invoke:

```text
Use $proclick-ssh-servers to check the servers / run a command / transfer files.
```

## Repository Layout

```text
skills/
  proclick-price-offer/
    SKILL.md
    AGENTS.md
    agents/openai.yaml
    assets/
    scripts/
    requirements.txt
  proclick-ssh-servers/
    SKILL.md
    AGENTS.md
    README.md
```

## Adding A New Skill

Create a new folder under `skills/<skill-name>/` with:

- `SKILL.md` for Codex-compatible instructions
- `AGENTS.md` for generic AI-agent usage
- optional `agents/openai.yaml`
- optional `assets/`, `scripts/`, `references/`
- optional `requirements.txt` for Python dependencies

Keep each skill self-contained so agents can copy or use only the folder they need.
