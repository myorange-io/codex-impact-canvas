# Output Consistency

Use this reference before writing or updating workshop Markdown outputs. Consistency matters because the files may later become an AI Agent social-impact casebook or workflow library.

## Required Files

Always create or maintain these files:

- `PLAN.md`
- `MEMORY.md`
- `WORKFLOW_ANALYSIS.md`
- `CASE_STUDY.md`

Do not rename required files. Do not make `CASE_STUDY.md` optional.

## Canonical Values

Use these exact Korean placeholders:

- Unknown: `미정`
- Not applicable: `해당 없음`
- Needs review: `검토 필요`
- Public shareability: `공개 가능`, `익명화 후 공개 가능`, `내부 공유만`, `공개 불가`
- Privacy level: `공개 데이터`, `내부자료`, `익명화 필요`, `개인정보 포함`, `민감정보 포함`
- Data type: `정형`, `반정형`, `비정형`, `혼합`, `미정`
- Integration level: `수동 업로드`, `CLI`, `MCP`, `API`, `브라우저`, `SaaS`, `미정`
- Human review: `최종 검토`, `중간 검토`, `예외 검토`, `검토 없음`, `미정`
- Reuse level: `그대로 재사용 가능`, `템플릿 재사용 가능`, `도메인 특화`, `일회성`, `미정`

## Output Order

Within each file, keep section order stable. If information is missing, keep the heading and write `미정`.

Use compact bullet lists and tables. Avoid long narrative paragraphs except in `CASE_STUDY.md` sections meant for public explanation.

## Front Matter

Add this YAML front matter to `PLAN.md`, `WORKFLOW_ANALYSIS.md`, and `CASE_STUDY.md`:

```yaml
---
team_name: ""
project_name: ""
created_date: "YYYY-MM-DD"
event: "Codex Impact Workshop"
version: "1"
---
```

Use the same `team_name`, `project_name`, `created_date`, and `event` across all three files.

## Stable IDs

For library use, add a `case_id` in `WORKFLOW_ANALYSIS.md` and `CASE_STUDY.md`.

Format:

```text
impact-agent-[YYYYMMDD]-[short-slug]
```

Use lowercase ASCII for the slug, replacing spaces with hyphens.

## Quality Checks

Before finishing, verify:

- All four required files exist.
- `PLAN.md` contains exactly one selected 3-hour MVP feature.
- `WORKFLOW_ANALYSIS.md` includes input, output, agent role, human review, privacy, failure handoff, and reuse fields.
- `CASE_STUDY.md` does not include raw personal data, secrets, internal document contents, access instructions, tokens, or unredacted source data.
- Unknown fields use `미정`; headings are not silently removed.
- Extra ideas are recorded as out-of-scope or next iteration, not mixed into the MVP.

## Preferred Automation

When possible, normalize answers into JSON and run:

```bash
python3 codex-impact-canvas/scripts/write_workshop_outputs.py --input workshop.json --output-dir .
```

The script preserves stable headings and values across all teams.
