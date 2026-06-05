# Workflow Analysis and Case Study

Use this reference after the MVP is scoped or built. The goal is to create material that can become an AI Agent social-impact casebook or workflow library.

## Contents

- WORKFLOW_ANALYSIS.md Required Fields
- CASE_STUDY.md Required Fields

## WORKFLOW_ANALYSIS.md Required Fields

Keep these fields in this order.

```markdown
---
team_name: "[팀 이름]"
project_name: "[프로젝트 이름]"
created_date: "[YYYY-MM-DD]"
event: "Codex Impact Workshop"
version: "1"
---

# [프로젝트 이름] Workflow Analysis

## Library Metadata
- case_id: impact-agent-[YYYYMMDD]-[short-slug]
- sector: [복지/교육/환경/지역/모금/운영/행정/기타]
- workflow_type: [문서작성/데이터정리/신청서검토/분류/요약/챗봇/리포트생성/기타]
- agent_role: [추출/요약/분류/초안작성/검토보조/라우팅/자동실행/기타]
- data_type: [정형/반정형/비정형/혼합/미정]
- privacy_level: [공개 데이터/내부자료/익명화 필요/개인정보 포함/민감정보 포함]
- integration_level: [수동 업로드/CLI/MCP/API/브라우저/SaaS/미정]
- human_review: [최종 검토/중간 검토/예외 검토/검토 없음/미정]
- reuse_level: [그대로 재사용 가능/템플릿 재사용 가능/도메인 특화/일회성/미정]
- output_format: [md/docx/sheet/webapp/email/pdf/dashboard/prompt/기타]

## Existing Workflow
- workflow_trigger: [업무가 시작되는 조건이나 이벤트]
- baseline_volume: [한 번에 처리하는 데이터/문서 수]
- baseline_time: [기존 방식의 소요 시간과 빈도]
- input_sources: [입력 데이터 출처]
- current_steps: [기존 업무 단계]
- current_outputs: [기존 산출물]
- current_pain_points: [지연/반복/오류/누락 지점]

## Automation Target
- selected_task: [자동화 대상으로 선정한 업무]
- reason_for_selection: [왜 이 업무를 골랐는지]
- excluded_tasks: [이번 MVP에서 제외한 업무]

## AI Agent Design
- agent_input_contract: [AI Agent가 받는 입력 형식과 최소 조건]
- agent_output_contract: [AI Agent가 내야 하는 산출물 형식과 품질 기준]
- decision_boundary: [AI가 판단해도 되는 것과 사람이 판단해야 하는 것]
- tools_used: [Codex/ChatGPT/API/MCP/CLI/외부 서비스 등]
- changed_workflow: [AI 도입 후 업무 흐름]

## Human-in-the-Loop
- review_points: [사람이 검토하거나 개입하는 지점]
- handoff_protocol: [실패 시 사람이 이어받는 절차]
- error_types: [자주 틀릴 수 있는 오류 유형]
- evaluation_samples: [테스트에 사용한 샘플 입력과 기대 결과]

## Data and Access
- privacy_action: [익명화/마스킹/삭제/접근 제한 등 실제 조치]
- permission_issues: [권한/접근 이슈]
- shareability: [공개 가능/익명화 후 공개 가능/내부 공유만/공개 불가]

## Impact and Reuse
- expected_time_change: [기존 대비 소요 시간 변화]
- quality_change: [정확성/일관성/누락 방지 등 변화]
- case_reuse_recipe: [다른 조직이 재사용할 때 바꿔야 하는 입력, 프롬프트, 연결 도구]
- maintenance_owner: [행사 이후 관리 주체]
- next_iteration: [3시간 MVP 이후 가장 먼저 개선할 것]
```

## CASE_STUDY.md Required Fields

`CASE_STUDY.md` is public-safe by default. Do not include personal data, raw internal data, secrets, tokens, access details, or unredacted source content.

```markdown
---
team_name: "[팀 이름]"
project_name: "[프로젝트 이름]"
created_date: "[YYYY-MM-DD]"
event: "Codex Impact Workshop"
version: "1"
---

# [사례 제목]

## Case Metadata
- case_id: impact-agent-[YYYYMMDD]-[short-slug]
- 공개 범위: [공개 가능/익명화 후 공개 가능/내부 공유만/공개 불가]
- 분야: [분야]
- 재사용 수준: [재사용 수준]

## Problem Summary
[사회문제/업무문제 한 줄 요약]

## Before
[기존 업무 방식]

## AI Agent Workflow
[AI Agent Workflow로 바뀐 흐름]

## Human Review
[사람이 검토하거나 개입한 지점]

## Tools
[사용한 도구]

## MVP Result
[MVP 결과물]

## Success Criterion
[성공 판단 기준]

## Lessons
[배운 점]

## Reuse Guide
[다른 조직이 재사용하려면 바꿔야 할 것]

## Redaction Notes
[공개 제외 정보와 익명화 처리 내용]
```
