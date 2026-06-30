# Marketing Copy

## GitHub Description

Screen-reader-friendly, keyboard/voice-friendly Codex session behavior skill.

## GitHub Topics

```text
codex
agent-skills
accessibility
screen-reader
keyboard-accessibility
voice-control
assistive-technology
developer-tools
```

## Short Launch Post

I made a small Agent Skill for making Codex sessions easier to use with screen
readers, keyboard-only workflows, voice control, low-vision needs, and reduced
terminal noise.

It is not a WCAG audit suite or a native Codex accessibility patch. It focuses
on the parts the agent controls: concise state summaries, screen-reader-friendly
approval prompts, visual artifact descriptions, keyboard/voice-friendly
alternatives, and a tiny terminal log filter.

Repo: https://github.com/hunterx-code/accessible-codex-session

## Longer Launch Post

Many accessibility tools focus on auditing the apps agents build. This one
targets the session itself.

`accessible-codex-session` is an Agent Skill for Codex that helps the agent
communicate in a screen-reader-friendly, keyboard/voice-friendly, low-noise
style. It includes accommodation profiles, accessible approval prompt patterns,
visual artifact description guidance, and a small Python helper for filtering
spinner/progress noise out of terminal logs.

It does not claim to fix native Codex UI accessibility bugs or certify WCAG
compliance. It is a practical session behavior aid that can work alongside
dedicated accessibility audit tools.

Repo: https://github.com/hunterx-code/accessible-codex-session
