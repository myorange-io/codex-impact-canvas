# Codex Impact Canvas

사회문제 해결 해커톤 팀이 준비해 온 현장 문제와 샘플 자료를 바탕으로, 3시간 안에 보여줄 수 있는 완결형 AI 에이전트 MVP로 범위를 좁히고, 사례집/워크플로 라이브러리로 재사용 가능한 마크다운 산출물을 남기도록 돕는 Codex 스킬입니다.

## 설치

이 저장소 전체가 하나의 Codex 스킬 디렉터리입니다. `SKILL.md`뿐 아니라 `references/`, `scripts/`, `agents/`도 함께 있어야 정상 동작합니다.

### 전역 설치

모든 Codex 작업에서 이 스킬을 쓰려면 아래처럼 전역 스킬 폴더에 설치합니다.

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/myorange-io/codex-impact-canvas.git ~/.codex/skills/codex-impact-canvas
```

이미 설치된 스킬을 최신 상태로 갱신하려면 아래 명령을 실행합니다.

```bash
cd ~/.codex/skills/codex-impact-canvas
git pull
```

### 프로젝트별 설치

특정 프로젝트에서만 쓰려면 해당 프로젝트 루트에서 아래처럼 설치합니다.

```bash
mkdir -p .agents/skills
git clone https://github.com/myorange-io/codex-impact-canvas.git .agents/skills/codex-impact-canvas
```

설치 후 새 Codex 세션을 열고 `/codex-impact-canvas`를 입력해 시작합니다.

## 언제 쓰나

- 사회혁신가와 개발자가 2인 1팀으로 문제를 정의할 때
- 업무 문제를 너무 넓게 잡아 3시간 MVP 범위로 좁혀야 할 때
- "AI로 무엇을 만들었다"를 넘어 기존 업무, 자동화 대상, 에이전트 역할, 사람 검토 지점까지 기록해야 할 때
- 결과물을 나중에 "AI 에이전트를 활용한 사회문제 해결 사례집" 또는 "사회혁신가를 위한 AI 에이전트 워크플로 라이브러리"로 모으고 싶을 때

## 기본 사용법

Codex에서 아래처럼 호출합니다.

```text
/codex-impact-canvas
```

`/codex-impact-canvas`라고만 입력하면 워크숍 흐름이 시작됩니다. 스킬은 먼저 사회혁신가 이름과 개발자 이름을 받고, 오늘 가져온 현장 문제, 샘플 입력, 기대 산출물을 확인합니다. 이미 준비된 설명은 다시 묻지 않고, 문제 유형을 고른 뒤 좁은 문제 하나를 끝까지 해결하는 3시간 MVP로 압축하는 데 필요한 빈칸만 짧게 묻습니다.

## 커맨드처럼 사용하기

이 스킬은 플러그인의 공식 slash command가 아니라, 스킬 트리거를 커맨드처럼 사용하는 방식입니다. 아래 중 하나를 입력하면 워크숍 흐름을 시작합니다.

```text
/codex-impact-canvas
codex-impact-canvas 시작
임팩트 캔버스 시작
```

## 실행 구조

스킬은 아래 순서로 움직입니다.

1. 사용자가 `/codex-impact-canvas`라고 입력합니다.
2. 팀 시작 정보를 받습니다.
3. 현장 문제, 샘플 입력, 기대 산출물을 3문장으로 확인합니다.
4. 문제 유형을 고르고 유형별 필수 질문으로 빈칸만 보완합니다.
5. 샘플 입력 업무 묶음과 검토 가능한 최종 산출물을 고정합니다.
6. 사람이 반복해서 읽고, 옮기고, 판단하고, 다시 쓰는 지점 하나로 병목을 압축합니다.
7. AI가 할 일, 사람이 검토할 일, 실패 시 이어받는 방식을 분리합니다.
8. 좁은 문제를 끝까지 해결하는 3시간 MVP 흐름과 제외 범위, 빠르게 끝났을 때 할 후보 2개를 정합니다.
9. 필수 산출물 네 개를 같은 구조로 생성합니다.
10. 합의한 MVP 의도와 산출물 내용이 일치하는지 검증합니다.

## 팀 시작

처음에 받는 정보입니다.

- 사회혁신가 이름
- 개발자 이름
- 팀 이름 또는 프로젝트 이름. 없으면 문제 설명에서 임시 제목을 만듭니다.

## 질문 흐름

### 1. 문제 요약

첫 질문:

```text
오늘 가져온 현장 문제와 샘플 자료는 무엇인가요? 현장 문제, 샘플 입력, 기대 산출물을 각각 한 문장으로 말해주세요.
```

완료 기준:

- 현장 문제가 한 문장으로 드러납니다.
- 행사 당일 쓸 샘플 입력 자료가 1개 이상 드러납니다.
- 발표장에서 보여줄 기대 산출물이 드러납니다.

### 2. 문제 유형 선택

스킬은 아래 유형 중 가장 가까운 후보를 제안하고 하나를 확정합니다.

- 문서/콘텐츠 초안 또는 변환
- 데이터 정리/분석/대시보드
- 문의응대/매뉴얼/상담 보조
- 분류/추천/매칭/리서치
- 웹앱/시스템 구축 욕구
- MVP 미정형

### 3. 유형별 필수 질문

유형마다 꼭 확인하는 질문이 다릅니다.

- 문서/콘텐츠: 원본 1개, 최종 문서 1개, 사람이 수정할 기준
- 데이터/대시보드: 원본 표 1개, 계산/분류 기준, 보여줄 지표 1개
- 문의응대/매뉴얼: 질문 예시 3개, 답변 근거, 위험 답변 검토 기준
- 분류/추천/리서치: 좋은 결과/나쁜 결과 예시, 분류 기준, 예외 처리
- 웹앱/시스템: 오늘 만들 화면 1개, 수동으로 남길 부분, 다음 단계
- MVP 미정형: 가장 자주 반복되는 업무 1개

### 4. 3시간 완결형 MVP 압축

기본 질문:

```text
좁은 문제 하나를 끝까지 해결한다고 할 때, 발표 때 반드시 보여줄 완결형 업무 흐름은 무엇인가요?
```

완료 기준:

- 입력 업무 묶음과 검토 가능한 최종 산출물이 고정됩니다.
- 사람이 반복해서 읽고, 옮기고, 판단하고, 다시 쓰는 지점 하나가 자동화 대상으로 정리됩니다.
- AI가 할 일, 사람이 검토할 일, 실패 시 사람이 이어받는 방식이 분리됩니다.
- 결과가 단순 초안에 머물지 않고 근거, 예외, 검토 체크리스트, 다음 행동 중 하나 이상을 포함합니다.
- 3시간 안/밖 판단이 `안`, `축소 필요`, `밖` 중 하나로 기록됩니다.
- 오늘 하지 않을 것과 다음 단계 아이디어가 분리됩니다.

### 5. 성공 판단 기준

기본 질문:

```text
샘플 입력 업무 묶음을 넣었을 때 어떤 결과가 나오면 성공이고, 어떤 결과가 나오면 실패인가요?
```

완료 기준:

- 발표장에서 확인 가능한 기준이 있습니다.
- 샘플 입력과 기대 산출물이 연결됩니다.
- 실패 신호가 적어도 1개 있습니다.

## 필요할 때 추가로 묻는 질문

답변이 충분하지 않거나 사례집/워크플로 라이브러리 기록에 필요한 정보가 빠졌다면 아래 질문을 짧게 추가합니다.

- 데이터: 행사 당일 사용할 샘플 데이터나 문서가 있나요? 민감정보는 제거됐나요?
- 도구: 이 업무가 지금 어떤 도구에서 시작되고, 결과는 어디에 남아야 하나요?
- 검수: AI가 만든 결과를 사람이 반드시 확인해야 하는 지점은 어디인가요?
- 실패 대응: AI 결과가 틀리거나 비어 있으면 사람이 어떻게 이어받으면 되나요?
- 공유 범위: 이 사례를 공개할 때 어떤 정보는 반드시 숨겨야 하나요?
- 재사용성: 다른 조직도 비슷하게 쓸 수 있으려면 무엇을 바꿔 끼우면 되나요?

## 필수 산출물

### PLAN.md

팀 합의와 3시간 MVP 실행 계획입니다.

포함 내용:

- 팀 정보
- 실제 업무 문제
- 어려움을 겪는 사람
- 현재 업무 흐름
- 기대 변화
- 해결할 좁은 문제
- 3시간 MVP 핵심 기능 1개
- 포함할 업무 단계
- 데모 입력과 데모 산출물
- 성공 기준
- 3시간 안/밖 판단
- 제외 범위
- 3시간 구현 계획
- 빠르게 끝났을 때 이어서 할 작업 후보 2개
- 각 후보의 시작 조건, 구현 내용, 데모 산출물, 예상 추가 시간, 검수 기준

### MEMORY.md

구현 과정 기록입니다. 기존 내용을 덮어쓰지 않고 파일 끝에 새 항목을 추가합니다.

포함 내용:

- 정한 것 또는 한 것
- 왜 그렇게 정했는지
- 어떻게 했는지
- 막힌 점과 바꾼 점
- 배운 것과 다음 단계

### WORKFLOW_ANALYSIS.md

AI 에이전트 워크플로 라이브러리용 구조화 분석입니다.

포함 내용:

- 사례 ID
- 분야, 업무 유형, 에이전트 역할
- 데이터 특성
- 정형/비정형 여부
- 데이터 수
- 개인정보 포함 여부
- MCP/CLI 연결 여부
- 입력 데이터 출처
- 산출물 형식
- 반복 빈도
- 기존 업무 흐름
- 자동화 대상으로 선정한 업무
- 에이전트 입력 조건과 산출물 조건
- AI가 판단해도 되는 것과 사람이 판단해야 하는 것
- 기존 대비 소요 시간 변화
- 주요 검수 포인트
- 권한/접근 이슈
- 재사용 가능성
- 실패 시 사람이 이어받는 방식
- 예상 오류 유형
- 평가 샘플
- 결과물의 공유 가능 범위
- 재사용 방법

### CASE_STUDY.md

공개 가능한 사례집용 요약입니다. 개인정보, 내부 원본 데이터, 비밀값, 토큰, 접근권한 세부 정보, 익명화되지 않은 원문은 넣지 않습니다.

포함 내용:

- 사례 메타데이터
- 문제 요약
- 기존 방식
- AI 에이전트 워크플로
- 사람 검토
- 사용 도구
- MVP 결과물
- 성공 기준
- 배운 점
- 재사용 가이드
- 익명화와 공개 제외 내용

## 출력 일관성 규칙

결과물을 여러 팀의 사례로 모으기 위해 아래 규칙을 지킵니다.

- 알 수 없는 값은 `미정`으로 씁니다.
- 해당하지 않는 값은 `해당 없음`으로 씁니다.
- 공개 범위는 `공개 가능`, `익명화 후 공개 가능`, `내부 공유만`, `공개 불가` 중 하나로 씁니다.
- 개인정보 수준은 `공개 데이터`, `내부자료`, `익명화 필요`, `개인정보 포함`, `민감정보 포함` 중 하나로 씁니다.
- 재사용 수준은 `그대로 재사용 가능`, `템플릿 재사용 가능`, `분야 특화`, `일회성`, `미정` 중 하나로 씁니다.
- `PLAN.md`, `WORKFLOW_ANALYSIS.md`, `CASE_STUDY.md`의 YAML 메타데이터는 같은 값을 사용합니다.
- `WORKFLOW_ANALYSIS.md`와 `CASE_STUDY.md`에는 같은 사례 ID를 사용합니다.

사례 ID 형식:

```text
impact-agent-[YYYYMMDD]-[short-slug]
```

## 스크립트로 산출물 생성하기

답변을 JSON으로 정리했다면 아래 명령으로 네 개의 필수 산출물을 만들 수 있습니다.

```bash
python3 scripts/write_workshop_outputs.py --input workshop.json --output-dir .
```

내장 샘플 데이터로 구조를 확인하려면 아래 명령을 실행합니다.

```bash
python3 scripts/write_workshop_outputs.py --demo --output-dir /tmp/codex-impact-canvas-demo
```

이미 생성된 산출물의 필수 구조를 확인하려면 아래 명령을 실행합니다.

```bash
python3 scripts/write_workshop_outputs.py --validate-only --output-dir /tmp/codex-impact-canvas-demo
```

## JSON 입력 구조

스크립트는 아래와 같은 큰 구조를 기대합니다. 일부 값이 비어 있으면 `미정` 또는 `해당 없음`으로 채웁니다.

```json
{
  "team": {
    "name": "팀 이름",
    "social_innovator": "사회혁신가 이름",
    "developer": "개발자 이름"
  },
  "project": {
    "name": "프로젝트 이름",
    "slug": "project-slug",
    "created_date": "2026-06-05"
  },
  "problem": {
    "actual_work_problem": "실제 업무 문제",
    "people_affected": "어려움을 겪는 사람",
    "blocked_moment": "문제가 발생하는 순간"
  },
  "current_workflow": {
    "inputs": "입력 자료",
    "steps": "처리 순서",
    "judgment": "판단 기준",
    "outputs": "현재 산출물",
    "tools": "현재 사용 도구"
  },
  "mvp": {
    "problem_slice": "3시간 안에 끝까지 해결할 좁은 문제",
    "single_feature": "3시간 MVP 핵심 기능 1개",
    "included_workflow_steps": "포함할 업무 단계",
    "demo_input": "데모 입력",
    "demo_output": "데모 산출물",
    "success_criterion": "성공 기준",
    "three_hour_decision": "안/축소 필요/밖 - 근거"
  },
  "follow_up_candidates": {
    "candidate_1": {
      "task": "이어 할 작업 후보 1",
      "start_condition": "후보 1 시작 조건",
      "implementation": "후보 1 구현 내용",
      "demo_output": "후보 1 데모 산출물",
      "timebox": "후보 1 예상 추가 시간",
      "success_check": "후보 1 검수 기준"
    },
    "candidate_2": {
      "task": "이어 할 작업 후보 2",
      "start_condition": "후보 2 시작 조건",
      "implementation": "후보 2 구현 내용",
      "demo_output": "후보 2 데모 산출물",
      "timebox": "후보 2 예상 추가 시간",
      "success_check": "후보 2 검수 기준"
    }
  },
  "library_metadata": {
    "data_characteristics": "데이터 특성",
    "data_type": "정형/반정형/비정형/혼합",
    "privacy_included": "개인정보 포함 여부",
    "mcp_cli_connection": "MCP/CLI 연결 여부",
    "output_format": "산출물 형식",
    "reuse_level": "재사용 가능성"
  },
  "existing_workflow": {
    "data_count": "데이터 수",
    "repeat_frequency": "반복 빈도",
    "input_sources": "입력 데이터 출처",
    "baseline_time": "기존 소요 시간"
  },
  "human_in_the_loop": {
    "key_review_points": "주요 검수 포인트",
    "handoff_protocol": "실패 시 사람이 이어받는 방식"
  },
  "data_and_access": {
    "permission_issues": "권한/접근 이슈",
    "shareability": "결과물의 공유 가능 범위"
  },
  "impact_and_reuse": {
    "expected_time_change": "기존 대비 소요 시간 변화"
  }
}
```

`project.slug`는 사례 ID에 들어가는 짧은 영문 식별자입니다. 가능하면 직접 넣는 것이 좋습니다. 비워두면 스크립트가 프로젝트 이름을 기준으로 `case-xxxxxxxx` 형태의 안정적인 대체 slug를 만듭니다.

## 파일 구조

```text
.
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── canvas-flow.md
│   ├── memory-log.md
│   ├── output-consistency.md
│   ├── plan-template.md
│   └── workflow-analysis.md
├── samples/
│   ├── case1-food-aid-review/
│   ├── case2-mentoring-note-summary/
│   └── case3-neighborhood-repair-routing/
└── scripts/
    └── write_workshop_outputs.py
```

`samples/`에는 가상 사례 3개의 `input.json`, `PLAN.md`, `MEMORY.md`, `WORKFLOW_ANALYSIS.md`, `CASE_STUDY.md`가 들어 있습니다. 복지, 교육, 지역 사례를 각각 다르게 구성해 개인정보 수준, 공유 가능 범위, 재사용 수준이 어떻게 기록되는지 확인할 수 있습니다.
