---
name: codex-impact-canvas
description: 한국어 사회문제 해결 해커톤 팀이 문제 정의, 3시간 MVP 범위 합의, 필수 Markdown 산출물 작성을 반응형 질문으로 진행하도록 돕는 스킬입니다. 사회문제를 정의하고, 하나의 AI 에이전트 MVP 기능으로 수렴하고, PLAN.md와 MEMORY.md를 작성하고, WORKFLOW_ANALYSIS.md로 AI 에이전트 워크플로를 분석하고, 공개 가능한 CASE_STUDY.md를 만들 때 사용합니다.
---

# Codex Impact Canvas

이 스킬은 2인 워크숍 팀이 막연한 사회문제에서 출발해 3시간 안에 보여줄 수 있는 AI 에이전트 MVP로 범위를 좁히고, 아래 네 개의 필수 Markdown 산출물을 만들도록 안내합니다.

- `PLAN.md`: 팀 합의와 3시간 MVP 실행 계획
- `MEMORY.md`: 구현 과정 append-only 기록
- `WORKFLOW_ANALYSIS.md`: AI 에이전트 워크플로 구조화 분석
- `CASE_STUDY.md`: 공개 가능한 익명화 사례 요약

## 진행 흐름

1. 먼저 팀 시작 정보를 받습니다: 사회혁신가 이름, 개발자 이름.
2. `references/canvas-flow.md`를 읽고 한국어 반응형 질문 흐름을 진행합니다.
3. 현재 답변이 `PLAN.md`에 기록 가능한 수준이 되기 전에는 다음 앵커 질문으로 넘어가지 않습니다.
4. 범위는 3시간 안에 보여줄 수 있는 기능 1개로 좁힙니다. 추가 아이디어는 제외 범위나 다음 단계로 옮깁니다.
5. 산출물을 쓰기 전에 `references/output-consistency.md`를 읽고 제목, 필드명, 상태값, 미정 표기를 일관되게 유지합니다.
6. 네 개의 필수 Markdown 산출물을 모두 생성합니다. 답변을 JSON으로 정규화했다면 `scripts/write_workshop_outputs.py`를 우선 사용합니다.
7. 구현이나 큰 변경이 끝날 때마다 `MEMORY.md`에 새 항목을 append합니다. 이전 항목은 덮어쓰지 않습니다. 형식은 `references/memory-log.md`를 따릅니다.
8. 완료 시 `references/workflow-analysis.md`를 읽고 `WORKFLOW_ANALYSIS.md`와 `CASE_STUDY.md`가 재사용 가능한 워크플로 라이브러리 자료로 충분한지 확인합니다.

## 규칙

- 한 번에 하나의 질문만 묻습니다. 답변을 받은 뒤 1-2문장으로 요약하고, 부족하면 후속 질문을 합니다.
- 여섯 개 앵커 질문은 상한이 아닙니다. 답변이 추상적이거나, 사용자/업무/데이터 형태가 빠졌거나, 3시간 안에 구현하기 어렵다면 후속 질문을 합니다.
- 워크숍 중 질문은 짧게 유지합니다. 목표는 긴 인터뷰가 아니라 합의 가능한 범위로 수렴하는 것입니다.
- 사용자의 실제 업무 표현은 기록에 보존하되, 산출물 섹션과 필드 라벨은 표준 형식으로 정규화합니다.
- `CASE_STUDY.md`에는 개인정보, 내부 문서 원문, 원본 데이터, 비밀값, 토큰, 접근권한 세부 정보를 넣지 않습니다.
- 알 수 없는 필드는 `미정`, 해당하지 않는 필드는 `해당 없음`으로 씁니다. 필수 제목은 비워두거나 삭제하지 않습니다.

## 참고 자료

- `references/canvas-flow.md`: 반응형 질문 흐름과 완료 기준
- `references/output-consistency.md`: 산출물 구조, 표준 상태값, 일관성 점검 기준
- `references/plan-template.md`: `PLAN.md` 필수 구조
- `references/workflow-analysis.md`: `WORKFLOW_ANALYSIS.md`와 `CASE_STUDY.md` 필수 필드
- `references/memory-log.md`: append-only 과정 기록 규칙
- `scripts/write_workshop_outputs.py`: 정규화한 JSON에서 일관된 Markdown 산출물 생성
