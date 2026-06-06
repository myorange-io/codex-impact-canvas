---
name: codex-impact-canvas
description: 사회문제 해결 해커톤 팀이 준비해 온 현장 문제와 샘플 자료를 3시간 MVP 1개로 압축하고, 필수 마크다운 산출물 작성을 반응형 질문으로 진행하도록 돕는 스킬입니다. 사용자가 /codex-impact-canvas라고 입력하거나, 현장 업무를 하나의 AI 에이전트 MVP 기능으로 수렴하고, PLAN.md와 MEMORY.md를 작성하고, WORKFLOW_ANALYSIS.md로 AI 에이전트 워크플로를 분석하고, 공개 가능한 CASE_STUDY.md를 만들 때 사용합니다.
---

# Codex Impact Canvas

이 스킬은 2인 워크숍 팀이 준비해 온 현장 문제와 샘플 자료를 바탕으로 3시간 안에 보여줄 수 있는 AI 에이전트 MVP 1개로 범위를 압축하고, 아래 네 개의 필수 마크다운 산출물을 만들도록 안내합니다.

- `PLAN.md`: 팀 합의, 3시간 MVP 실행 계획, 빠르게 끝났을 때 이어서 할 작업 후보 2개
- `MEMORY.md`: 구현 과정 누적 기록
- `WORKFLOW_ANALYSIS.md`: AI 에이전트 워크플로 구조화 분석
- `CASE_STUDY.md`: 공개 가능한 익명화 사례 요약

## 커맨드처럼 사용하기

아래 중 하나를 사용자가 입력하면 이 스킬을 시작합니다.

- `/codex-impact-canvas`
- `codex-impact-canvas 시작`
- `임팩트 캔버스 시작`

이것은 플러그인의 공식 slash command가 아니라, 스킬 트리거를 커맨드처럼 사용하는 방식입니다.

## 진행 흐름

1. 사용자가 `/codex-impact-canvas`라고만 입력해도 이 스킬을 시작합니다.
2. 먼저 팀 시작 정보를 받습니다: 사회혁신가 이름, 개발자 이름.
3. `references/canvas-flow.md`와 `references/problem-archetypes.md`를 읽고 문제 확인 -> 유형 분기 -> MVP 압축 흐름을 진행합니다.
4. 처음 세 질문 안에 문제 유형, 샘플 입력 1개, 기대 출력 1개를 확정합니다. 이미 답한 내용은 다시 묻지 않고 빠진 정보만 묻습니다.
5. 범위는 3시간 안에 보여줄 수 있는 기능 1개로 좁힙니다. 핵심 기능을 먼저 끝낸 뒤 시간이 남으면 이어서 할 작업 후보 2개도 시작 조건, 구현 내용, 데모 산출물, 예상 추가 시간, 검수 기준까지 정리합니다.
6. 산출물을 쓰기 전에 `references/output-consistency.md`를 읽고 제목, 필드명, 상태값, 미정 표기를 일관되게 유지합니다.
7. 네 개의 필수 마크다운 산출물을 모두 생성합니다. 답변을 JSON으로 정규화했다면 `scripts/write_workshop_outputs.py`를 우선 사용합니다.
8. 산출물을 확정하기 전에 `references/intent-check.md`를 읽고 합의한 MVP 의도와 `PLAN.md`, `WORKFLOW_ANALYSIS.md`, `CASE_STUDY.md` 반영 내용이 어긋나지 않는지 확인합니다.
9. 구현이나 큰 변경이 끝날 때마다 `MEMORY.md` 파일 끝에 새 항목을 추가합니다. 이전 항목은 덮어쓰지 않습니다. 형식은 `references/memory-log.md`를 따릅니다.
10. 완료 시 `references/workflow-analysis.md`를 읽고 `WORKFLOW_ANALYSIS.md`와 `CASE_STUDY.md`가 재사용 가능한 워크플로 라이브러리 자료로 충분한지 확인합니다.

## 규칙

- 한 번에 하나의 질문만 묻습니다. 답변을 받은 뒤 1-2문장으로 요약하고, 부족하면 후속 질문을 합니다.
- 기존 여섯 개 앵커 질문은 순서대로 반복하는 질문지가 아니라 체크리스트입니다. 사용자가 준비해 온 설명에서 이미 확인된 내용은 묻지 않습니다.
- 답변이 추상적이거나, 사용자/업무/데이터 형태가 빠졌거나, 3시간 안에 구현하기 어렵다면 유형별 후속 질문으로 좁힙니다.
- 워크숍 중 질문은 짧게 유지합니다. 목표는 긴 인터뷰가 아니라 준비된 고민을 구현 가능한 범위로 수렴하는 것입니다.
- 제품 PRD, 시장성, 가격 전략, GTM 검토로 확장하지 않습니다. 현장 업무, 샘플 데이터, 사람 검토, 공개 가능성, 데모 산출물에 집중합니다.
- 사용자의 실제 업무 표현은 기록에 보존하되, 산출물 섹션과 필드 라벨은 표준 형식으로 정규화합니다.
- `CASE_STUDY.md`에는 개인정보, 내부 문서 원문, 원본 데이터, 비밀값, 토큰, 접근권한 세부 정보를 넣지 않습니다.
- 알 수 없는 필드는 `미정`, 해당하지 않는 필드는 `해당 없음`으로 씁니다. 필수 제목은 비워두거나 삭제하지 않습니다.

## 참고 자료

- `references/canvas-flow.md`: 반응형 질문 흐름과 완료 기준
- `references/problem-archetypes.md`: 문제 유형별 필수 질문과 범위 축소 규칙
- `references/intent-check.md`: 합의한 MVP 의도와 산출물 반영 내용 검증
- `references/output-consistency.md`: 산출물 구조, 표준 상태값, 일관성 점검 기준
- `references/plan-template.md`: `PLAN.md` 필수 구조
- `references/workflow-analysis.md`: `WORKFLOW_ANALYSIS.md`와 `CASE_STUDY.md` 필수 필드
- `references/memory-log.md`: 누적 과정 기록 규칙
- `scripts/write_workshop_outputs.py`: 정규화한 JSON에서 일관된 마크다운 산출물 생성
