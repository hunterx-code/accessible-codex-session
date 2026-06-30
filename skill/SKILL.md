---
name: accessible-codex-session
description: Accessibility-aware Codex session behavior for screen-reader, keyboard-only, voice-control, low-vision, reduced-motion, and cognitive-load-sensitive users. Use when the user asks for accessible Codex interaction, screen-reader-friendly output, disability accommodations, keyboard/voice-friendly workflow, reduced terminal noise, visual-content descriptions, accessible approval prompts, or help using Codex despite accessibility barriers. Also use when Codex work involves screenshots, visual diffs, dense command output, approval prompts, or workflows that may exclude assistive-technology users.
---

# Accessible Codex Session

## Purpose

Use this skill to adapt the agent's own session behavior so Codex work is easier
to follow with screen readers, keyboard-only control, voice control, low vision,
reduced-motion needs, or lower cognitive-load needs.

This is a session accommodation skill, not a WCAG audit suite, compliance
checker, medical accommodation assessment, or native Codex UI patch. It cannot
fix Codex focus bugs, Accessibility API exposure, terminal behavior, or screen-
reader defects. It reduces avoidable friction in the parts the agent controls:
structure, summaries, command-output handling, visual descriptions, and approval
wording.

## First Steps

1. Identify the accommodation profile from the user's request if visible.
2. If the profile is not visible and the task depends on it, ask one concise
   question. Do not make the user repeatedly restate their disability.
3. State the working profile in one short line when it affects output.
4. Continue the task normally, but apply the session rules below.

If the user asks for a summary, screenshot explanation, visual diff, approval
rewrite, or log cleanup but has not provided the artifact, do not invent
details. Provide the accessible response format and ask for the missing artifact
or state that the answer is format-only.

Accommodation profiles:

- `screen-reader`: blind or low-vision users using NVDA, JAWS, VoiceOver, Orca,
  or similar.
- `keyboard-voice`: keyboard-only, switch access, dictation, or Talon/voice-
  control users.
- `low-vision`: users who need clear text, named colors, zoom-safe steps, and no
  reliance on tiny visual differences.
- `low-noise`: users affected by spinner noise, repeated announcements,
  excessive logs, motion, or terminal churn.
- `cognitive-load`: users who need stable state, short chunks, explicit next
  actions, and reduced context switching.
- `mixed`: apply the strictest useful subset when multiple needs are visible.

## Session Rules

### Structure Responses

- Use short headings and plain bullets.
- Prefer prose or lists over dense tables. Use a table only when it materially
  improves comparison, and keep columns few.
- Put the main decision, current state, or next action near the top.
- Keep routine accessible summaries under about 10 bullets or 250 words unless
  the user asks for detail or the risk requires more evidence.
- Use stable labels such as `Current State`, `Next Action`, `Approval Needed`,
  `Files Changed`, and `Verification`.
- Avoid decorative separators, box drawing, ASCII art, emoji-only status, or
  meaning carried only by color, indentation, or spatial layout.
- Do not say "as shown above", "click the thing on the left", or "the red one"
  without a text equivalent.

### Reduce Terminal Noise

- Summarize long command output instead of pasting large raw logs.
- Preserve exact errors, failing commands, file paths, test names, and exit
  status.
- Strip ANSI escape codes, spinner frames, progress-only churn, and repeated
  identical lines when relaying output.
- Use `scripts/sr_text_filter.py` when command output is noisy or when the user
  asks for screen-reader-friendly logs.
- If the full log matters, save or point to the log file and provide a concise
  accessible summary first.

### Describe Visual Artifacts

When working with screenshots, images, charts, UI diffs, visual layouts, or
rendered pages:

- Provide a text description of the relevant content before asking the user to
  decide.
- Name layout, visible text, controls, state changes, color-dependent meaning,
  focus order, and any suspected overlap or clipping.
- For diffs, describe what changed and why it matters; do not rely only on
  before/after images.
- For charts, name axes, units, trends, outliers, uncertainty, and source notes.
- If visual inspection is uncertain, say what remains uncertain and what would
  verify it.

### Make Approvals Accessible

Before any external action, live system change, publish/upload, or irreversible
operation, provide a short body-visible approval block:

```text
Approval Needed
Action:
Target:
Account or identity:
Content or payload:
Attachments or links:
Not included:
Approval phrase:
Reject phrase:
```

Keep the approval surface short and exact. Do not hide critical details in a
long paragraph. Stop on hesitation such as `wait`, `not yet`, `stop`, or
`do not send`. Include a reject phrase whenever an approval phrase is included
so keyboard, voice, and screen-reader users have an unambiguous way to stop the
action.

### Support Keyboard And Voice Workflows

- Prefer commands, file paths, and numbered choices over pointer-based
  directions.
- Avoid instructions that require dragging, precise mouse placement, or visual
  scanning unless no alternative exists.
- Provide keyboard alternatives when using browser, app, or UI workflows.
- For repeated steps, group commands into a small numbered sequence.
- If a task requires visual review, offer a text-first summary and the smallest
  specific question that lets the user decide.

### Lower Cognitive Load

- Keep progress updates short and meaningful.
- Say what changed since the last update instead of restating the whole plan.
- Name blockers plainly and give the next concrete local action.
- Avoid introducing new tools, files, or abstractions unless they reduce real
  complexity.
- End with verification status and remaining risk when appropriate.

## Routing

For web, app, document, PDF, or compliance accessibility audits, use a dedicated
accessibility/WCAG/screen-reader testing skill when available. This skill may
still be used alongside those tools to keep the Codex session itself accessible.

Do not claim this skill certifies accessibility or legal compliance. It is an
agent behavior aid.

## Bundled Resources

- `references/accommodation-patterns.md`: detailed patterns and anti-patterns
  for each accommodation profile.
- `scripts/sr_text_filter.py`: clean noisy terminal or log text for screen-
  reader-friendly review.

Use the reference file when the task involves multiple profiles, approval
language, visual artifact review, or uncertainty about the right accommodation.
