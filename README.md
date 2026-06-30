# Accessible Codex Session

An Agent Skill that helps Codex communicate in a screen-reader-friendly,
keyboard/voice-friendly, low-noise session style.

This is an unofficial community package. It is not an OpenAI product and is not
affiliated with or endorsed by OpenAI.

This is not a WCAG audit suite, compliance checker, medical accommodation
assessment, or native Codex accessibility patch. It is a practical session
behavior aid: it helps the agent structure responses, summarize noisy terminal
output, write accessible approval prompts, describe visual artifacts, and avoid
workflows that rely only on pointing or visual scanning.

## Why This Exists

Accessibility tooling for generated web apps and UI audits is already strong.
The gap this skill targets is narrower: disabled users can hit friction while
using Codex itself, before there is any generated app to audit.

Examples of session-level friction:

- noisy terminal output and spinner churn
- screen-reader-unfriendly approval prompts
- screenshot-only or visual-diff-only explanations
- workflows that assume mouse use, visual scanning, or drag actions
- long status prose that obscures the current state and next action

## What It Provides

- accommodation profiles for screen-reader, keyboard/voice, low-vision,
  low-noise, cognitive-load, and mixed use
- response-structure rules for accessible Codex sessions
- accessible approval prompt template with both approval and reject phrases
- visual artifact description guidance
- `sr_text_filter.py`, a small helper that removes ANSI, spinner/progress noise,
  and repeated log lines while preserving meaningful errors and file paths

## Package Layout

```text
skill/
|-- SKILL.md
|-- agents/
|   `-- openai.yaml
|-- references/
|   `-- accommodation-patterns.md
`-- scripts/
    |-- noisy_terminal_sample.txt
    |-- sr_text_filter.py
    `-- test_sr_text_filter.py
```

## Install

Copy or symlink `skill/` into your Codex skills directory as
`accessible-codex-session`.

Example:

```bash
mkdir -p ~/.codex/skills
rm -rf ~/.codex/skills/accessible-codex-session
cp -R skill ~/.codex/skills/accessible-codex-session
```

Then start a new Codex session and ask:

```text
Use $accessible-codex-session to run this task with screen-reader-friendly,
keyboard-friendly, low-noise session behavior.
```

## Validate

From the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s skill/scripts -p 'test_*.py'
python3 skill/scripts/sr_text_filter.py skill/scripts/noisy_terminal_sample.txt
```

When using OpenAI's skill validator locally:

```bash
python3 /path/to/quick_validate.py skill
```

## Scope And Limits

This skill does not:

- certify WCAG conformance
- replace assistive-technology testing
- provide legal compliance advice
- fix native Codex UI accessibility defects
- guarantee that a screen reader will announce a specific interface correctly

For web, app, document, PDF, or compliance accessibility audits, use a dedicated
accessibility testing skill or WCAG audit workflow. This skill can still be used
alongside those tools to keep the Codex session itself accessible.

## Development Notes

The helper is standard-library Python. Tests use `unittest`.

The package intentionally keeps examples synthetic and avoids private project
history, credentials, or live account details.
