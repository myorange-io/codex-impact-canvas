---
name: codex-impact-canvas
description: Guide Korean social-impact hackathon teams through responsive problem definition, 3-hour MVP scoping, and required Markdown outputs. Use when a team needs to define a social problem, converge on one AI Agent MVP feature, write PLAN.md and MEMORY.md, analyze the AI Agent Workflow in WORKFLOW_ANALYSIS.md, and create a public-safe CASE_STUDY.md.
---

# Codex Impact Canvas

Use this skill to guide a two-person workshop team from a vague social-impact problem to a scoped AI Agent MVP and four required Markdown outputs:

- `PLAN.md`: team agreement and 3-hour MVP plan
- `MEMORY.md`: append-only build process log
- `WORKFLOW_ANALYSIS.md`: structured AI Agent Workflow analysis
- `CASE_STUDY.md`: public-safe, anonymized case-study summary

## Workflow

1. Start with the team setup: social innovator name and developer name.
2. Read `references/canvas-flow.md` and run the responsive question flow in Korean.
3. Do not move to the next anchor question until the current answer can be recorded in `PLAN.md`.
4. Narrow scope to one feature that can be shown in 3 hours. Move extra ideas to out-of-scope or next iteration.
5. Before writing outputs, read `references/output-consistency.md` and keep headings, field names, status values, and unknown placeholders consistent.
6. Generate all four required Markdown outputs. Prefer `scripts/write_workshop_outputs.py` when the answers have been normalized into JSON.
7. After implementation or substantial changes, append to `MEMORY.md` instead of rewriting prior entries. Follow `references/memory-log.md`.
8. At completion, read `references/workflow-analysis.md` and make sure `WORKFLOW_ANALYSIS.md` and `CASE_STUDY.md` are complete enough for a reusable workflow library.

## Rules

- Ask one question at a time. Summarize each answer in one or two sentences before asking follow-up questions.
- The six anchor questions are not a hard limit. Ask follow-ups whenever an answer is too abstract, missing the user/workflow/data shape, or not implementable in 3 hours.
- Keep workshop questions short. The goal is convergence, not a long interview.
- Keep the user's raw domain language in the notes, but normalize output sections and field labels.
- Do not include personal data, internal documents, raw source data, secrets, tokens, or permission details in `CASE_STUDY.md`.
- If a field is unknown, write `미정`. If a field does not apply, write `해당 없음`. Do not leave required headings blank.

## Resources

- `references/canvas-flow.md`: responsive question flow and completion criteria.
- `references/output-consistency.md`: canonical output structure, stable values, and consistency checks.
- `references/plan-template.md`: required `PLAN.md` structure.
- `references/workflow-analysis.md`: required `WORKFLOW_ANALYSIS.md` and `CASE_STUDY.md` fields.
- `references/memory-log.md`: append-only process logging rules.
- `scripts/write_workshop_outputs.py`: generate consistent Markdown outputs from normalized JSON.
