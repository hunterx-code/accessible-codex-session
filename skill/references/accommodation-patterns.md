# Accommodation Patterns

Use this reference when the task needs more detail than the core `SKILL.md`.

## Screen-Reader Profile

Prefer:

- concise headings
- single-level bullets
- exact file paths and commands
- explicit state changes
- text descriptions of screenshots, layouts, and visual diffs
- summaries before raw logs

Avoid:

- dense tables with many columns
- emoji-only state markers
- box drawing and visual separators
- "above/below/left/right" without textual anchors
- meaning carried only by color, spacing, or indentation
- unfiltered terminal animation output

Good response shape:

```text
Current State
The failing test is `test_filter_repeated_spinner_lines`.

Relevant Output
The script preserved the error line, but it also preserved three spinner-only
progress lines.

Next Action
I will update the spinner-line detector and rerun the fixture test.
```

## Keyboard And Voice Profile

Prefer:

- numbered choices
- commands that can be copied or spoken
- exact menu names or UI labels
- small repeatable steps
- explicit focus target when UI focus matters

Avoid:

- "click around until..."
- drag-only workflows
- pointer position instructions without alternatives
- long lists of similar commands without grouping

When a visual UI step is unavoidable, describe the target by label, role, and
surrounding text.

## Low-Vision Profile

Prefer:

- named colors plus meaning, not color alone
- zoom-safe descriptions
- clear control names
- text equivalents for small visual differences
- warning about low-contrast or clipped text when seen in screenshots

Avoid:

- relying on subtle color, tiny icons, or position-only descriptions
- saying "the green item" without naming the item

## Low-Noise Profile

Prefer:

- summarized command output
- filtered logs
- only meaningful progress updates
- stable state messages instead of repeated live narration

Use `scripts/sr_text_filter.py` when raw output contains:

- ANSI escape sequences
- spinner frames
- repeated progress percentages
- repeated identical status lines
- long logs where only errors and summaries matter

## Cognitive-Load Profile

Prefer:

- one current goal
- one current blocker
- one next action
- short verification notes
- stable terms across the conversation

Avoid:

- repeatedly restating old context
- adding broad options after a decision has been made
- changing labels for the same state
- ending with vague offers instead of concrete status

## Accessible Approval Prompts

Use short, body-visible approval prompts:

```text
Approval Needed
Action: send one email
Target: jane@example.com
Account or identity: founder@example.com
Content or payload: the email body shown below
Attachments or links: none
Not included: follow-ups, calendar invites, public posts
Approval phrase: Send this exact email
Reject phrase: Do not send
```

Do not put the approval phrase before the action details. Do not bury target,
account, or attachments in prose. Include a reject phrase whenever an approval
phrase is present.

## Missing Artifacts

Do not fabricate log output, screenshot contents, visual diffs, approval bodies,
or external-action details.

When the user asks for an accessible transformation but has not provided the
source artifact, choose one:

- Ask for the missing artifact if the real content matters.
- Provide a format-only template and clearly label it as a template.
- Explain what evidence would be needed to verify the result.

Example:

```text
Current State
I do not have the screenshot, so I cannot describe the actual UI change.

Format I Will Use
- What changed:
- Visible text:
- Controls:
- Keyboard/focus uncertainty:
- Approval question:

Next Action
Send the screenshot or paste the UI text, and I will fill this in without
relying on visual-only references.
```

## Visual Artifact Descriptions

For screenshots or rendered UI, cover:

- purpose of the screen
- visible text
- interactive controls
- current focus or selected state if visible
- layout order
- color-dependent meaning
- warnings: overlap, clipping, contrast, missing labels

For charts, cover:

- chart type
- axes and units
- trend or comparison
- outliers
- uncertainty or caveats
- source notes

For visual diffs, cover:

- what changed
- where it changed
- why it matters
- whether the change is visible, semantic, behavioral, or only cosmetic

## Boundaries

This skill does not:

- certify WCAG conformance
- replace assistive-technology testing
- provide legal compliance advice
- fix native Codex UI accessibility defects
- guarantee that a screen reader will announce a specific interface correctly

Say these limits plainly when relevant.
