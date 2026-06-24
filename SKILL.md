---
name: codex-impact-canvas
description: 사회문제 해결 해커톤 팀이 준비해 온 현장 문제를 자연스러운 질문 순서로 확인하고, 자료와 결과물 형태를 정한 뒤 3시간 MVP 1개와 AI Agent Workflow 자산으로 압축하도록 돕는 스킬입니다. 사용자가 $codex-impact-canvas 또는 /codex-impact-canvas라고 입력하거나, 현장 업무를 하나의 AI 에이전트 MVP 기능으로 수렴하고, PLAN.md, workshop.json, MEMORY.md, WORKFLOW_ANALYSIS.md, CASE_STUDY.md를 만들 때 사용합니다.
---

# Codex Impact Canvas

이 스킬은 2인 워크숍 팀이 준비해 온 현장 문제를 바탕으로 실제 업무, 자료 상태, 결과물 형태를 차례로 확인한 뒤 3시간 안에 보여줄 수 있는 AI 에이전트 MVP 1개로 범위를 압축합니다. 동시에 워크숍 결과를 나중에 AI Agent Workflow 자산으로 재사용할 수 있도록 아래 산출물을 남깁니다.

- `PLAN.md`: 문제정의 단계의 팀 합의, 3시간 MVP 실행 계획, 빠르게 끝났을 때 이어서 할 작업 후보 2개
- `workshop.json`: 질문 답변과 구현 결과를 표준 필드로 정규화한 제출/아카이빙 기준 데이터
- `MEMORY.md`: 구현 중 결정, 변경, 막힌 점, 검증 내용을 누적하는 append-only 기록
- `WORKFLOW_ANALYSIS.md`: 완료 후 결과물과 기록을 분석한 AI 에이전트 워크플로 구조화 자료
- `CASE_STUDY.md`: 완료 후 공개 가능한 수준으로 익명화한 사례 요약

## 진행 흐름

1. 사용자가 `$codex-impact-canvas`라고 입력하면 이 스킬을 시작합니다. `/codex-impact-canvas`도 호환 호출로 인정합니다.
2. 먼저 `references/pre-workshop-guide.md`를 기준으로 준비 안내를 짧게 확인합니다. 현장 문제, 반복 업무, 샘플 자료, 개인정보 비식별화, 제출 산출물 기준을 안내하되 길게 설명하지 않습니다.
3. `references/canvas-flow.md`, `references/problem-archetypes.md`, `references/output-types.md`, `references/mvp-scope.md`, `references/multiple-choice.md`를 읽고 기본 정보 확인 -> 업무 문제 확인 -> 자료 확인 -> 결과물 선택 -> 3시간 MVP 좁히기 -> 다음 단계 안내 순서로 진행합니다.
4. 처음에는 샘플 입력이나 기대 산출물을 강요하지 않습니다. 사회혁신가 이름, 개발자 이름, 팀/프로젝트 이름은 한 번에 묻지 않고 `request_user_input`으로 하나씩 순차 질문한 뒤, 업무 문제와 실제 자료 유무, 결과물 형태를 단계적으로 정합니다.
5. 자료가 있으면 개인정보 제거 샘플 기준을 확인하고, 자료가 없으면 가상 샘플을 만들어도 되는지 확인합니다.
6. 문제를 들은 뒤 자동화 도구, 웹앱, 온보딩 페이지, admin 화면, 대시보드, 문서/메시지 초안 등 가능한 결과물 후보를 2-4개 제안하고 하나를 고릅니다.
7. 범위는 3시간 안에 보여줄 수 있는 완결형 업무 흐름 1개로 좁힙니다. `references/mvp-scope.md` 기준으로 해결할 좁은 문제, 포함할 업무 단계, 오늘 할 것/하지 않을 것, AI 역할, 사람 검토 지점, 성공/실패 기준, 3시간 안/밖 판단을 분리합니다.
8. 문제정의가 끝나면 `PLAN.md`와 `workshop.json` 초안을 생성합니다. 답변을 JSON으로 정규화했다면 `scripts/write_workshop_outputs.py`를 우선 사용합니다.
9. 구현이나 큰 변경이 끝날 때마다 `MEMORY.md` 파일 끝에 새 항목을 추가하고 `workshop.json`을 갱신합니다. 이전 항목은 덮어쓰지 않습니다. 형식은 `references/memory-log.md`를 따릅니다.
10. 완료 시 `references/output-consistency.md`, `references/intent-check.md`, `references/workflow-analysis.md`를 읽고 구현 결과와 기록을 분석해 `WORKFLOW_ANALYSIS.md`, `CASE_STUDY.md`, 최종 `workshop.json`이 제출/아카이빙 기준을 만족하는지 확인합니다.

## 규칙

- 사용자에게 묻는 모든 워크숍 질문은 일반 채팅 문장으로 끝내지 말고 `request_user_input` 도구 호출로 보냅니다.
- 한 번에 하나의 질문만 묻습니다. 답변을 받은 뒤 1-2문장으로 요약하고, 부족하면 후속 질문을 합니다.
- 한 번의 `request_user_input` 호출에는 질문 1개만 담습니다. 다음 질문은 사용자 답변을 받은 뒤에만 호출합니다.
- 기본 정보도 한 번에 묶어 묻지 않습니다. `사회혁신가 이름은 무엇인가요?`를 먼저 묻고, 답변을 받은 뒤 개발자 이름, 팀/프로젝트 이름을 순차적으로 묻습니다.
- 질문에 필요한 정보가 이미 사용자 설명이나 파일에서 확인되면 `request_user_input`을 호출하지 않고 다음 단계로 넘어갑니다.
- 자유 서술이 필요한 질문도 `request_user_input`으로 묻습니다. 이때 선택지는 답변 방식을 고르는 2-4개 옵션으로 만들고, 마지막에는 사용자가 다른 내용을 쓸 수 있는 `직접 입력` 옵션을 둡니다.
- 범위 축소나 유형 선택을 위해 선택지를 줄 때는 모든 선택지가 실제로 실행 가능한 선택이어야 합니다. 명백한 정답 하나와 들러리 선택지를 만들지 않습니다.
- 답변이 추상적이거나 여러 방향이 섞이면 `references/multiple-choice.md`를 사용해 객관식 프롬프팅 또는 객관식 플래닝으로 수렴합니다.
- 질문과 선택지 문구는 한국어로 짧게 씁니다. 선택지 설명에는 그 선택을 고르면 무엇이 확정되는지 한 줄로 적습니다.
- 기존 여섯 개 앵커 질문은 순서대로 반복하는 질문지가 아니라 체크리스트입니다. 사용자가 준비해 온 설명에서 이미 확인된 내용은 묻지 않습니다.
- 사회혁신가가 답하기 어려운 `샘플 입력`, `기대 산출물`, `도구 형태`는 처음부터 요구하지 않습니다. 업무 문제를 들은 뒤 스킬이 후보를 제안해 함께 고릅니다.
- 실제 자료가 없으면 워크숍을 멈추지 않습니다. 비식별 가상 샘플을 만들고 `workshop.json`과 산출물에 가상 샘플임을 표시합니다.
- 답변이 추상적이거나, 사용자/업무/데이터 형태가 빠졌거나, 3시간 안에 구현하기 어렵다면 유형별 후속 질문으로 좁힙니다.
- 워크숍 중 질문은 짧게 유지합니다. 목표는 긴 인터뷰가 아니라 준비된 고민을 구현 가능한 범위로 수렴하는 것입니다.
- 제품 PRD, 시장성, 가격 전략, GTM 검토로 확장하지 않습니다. 현장 업무, 샘플 데이터, 사람 검토, 공개 가능성, 데모 산출물에 집중합니다.
- 사용자의 실제 업무 표현은 기록에 보존하되, 산출물 섹션과 필드 라벨은 표준 형식으로 정규화합니다.
- `CASE_STUDY.md`에는 개인정보, 내부 문서 원문, 원본 데이터, 비밀값, 토큰, 접근권한 세부 정보를 넣지 않습니다.
- 알 수 없는 필드는 `미정`, 해당하지 않는 필드는 `해당 없음`으로 씁니다. 필수 제목은 비워두거나 삭제하지 않습니다.

## 참고 자료

- `references/pre-workshop-guide.md`: 사전 안내, 샘플 준비, 개인정보 비식별화, 제출 산출물 기준
- `references/canvas-flow.md`: 반응형 질문 흐름과 완료 기준
- `references/problem-archetypes.md`: 문제 유형별 필수 질문과 범위 축소 규칙
- `references/output-types.md`: 문제에 맞는 결과물 형태 후보와 선택 기준
- `references/mvp-scope.md`: 3시간 완결형 MVP 범위 판단과 축소 기준
- `references/multiple-choice.md`: 실행 가능한 선택지 구성과 객관식 수렴 규칙
- `references/intent-check.md`: 합의한 MVP 의도와 산출물 반영 내용 검증
- `references/output-consistency.md`: 산출물 구조, 표준 상태값, 일관성 점검 기준
- `references/plan-template.md`: `PLAN.md` 필수 구조
- `references/workflow-analysis.md`: `WORKFLOW_ANALYSIS.md`와 `CASE_STUDY.md` 필수 필드
- `references/memory-log.md`: 누적 과정 기록 규칙
- `scripts/write_workshop_outputs.py`: 정규화한 JSON에서 일관된 마크다운 산출물 생성
