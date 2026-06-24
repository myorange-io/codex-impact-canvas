# Codex Impact Canvas

사회문제 해결 해커톤 팀이 준비해 온 현장 문제를 바탕으로, 3시간 안에 보여줄 수 있는 AI 에이전트 MVP 기능 1개로 범위를 좁히고, 결과를 워크숍 표준 산출물과 5장 발표자료로 남기도록 돕는 Codex 스킬입니다.

## 언제 쓰나

- 사회혁신가와 개발자가 2인 1팀으로 문제를 정의할 때
- 업무 문제를 너무 넓게 잡아 3시간 MVP 범위로 좁혀야 할 때
- 샘플 자료가 있거나, 자료가 없어서 가상 샘플로 시작해야 할 때
- 자동화 도구, 웹앱, 온보딩 페이지, admin 화면, 대시보드, 문서/메시지 초안 중 어떤 결과물이 맞는지 고를 때
- 결과물을 나중에 "AI 에이전트를 활용한 사회문제 해결 사례집" 또는 "사회혁신가를 위한 AI 에이전트 워크플로 라이브러리"로 모으고 싶을 때
- 같은 스킬 설치만으로 워크숍 기록부터 5장 Google Slides 발표자료 제작까지 이어가고 싶을 때

## 기본 사용법

Codex에서 아래처럼 호출합니다.

```text
$codex-impact-canvas
```


`$codex-impact-canvas`라고만 입력하면 워크숍 흐름이 시작됩니다. 스킬은 먼저 사회혁신가와 개발자 정보를 받고, 업무 문제를 확인한 뒤 자료 상태와 결과물 형태를 단계적으로 정합니다. 처음부터 샘플 입력이나 기대 산출물을 확정하라고 요구하지 않습니다.

워크숍 중 사용자에게 질문할 때는 현재 모드에서 `request_user_input` 도구가 활성화되어 있으면 그 도구를 우선 사용합니다. Default mode처럼 도구가 비활성화되어 있으면 Plan mode 전환이 필요하다는 점을 짧게 알리고, 사용자가 바로 진행하길 원하거나 전환할 수 없으면 일반 채팅 질문으로 같은 흐름을 이어갑니다.

## 사전 준비

참여자는 아래 네 가지를 한 문장씩 생각해 오면 충분합니다.

- 현장 문제: 지금 반복해서 처리하느라 불편한 업무
- 반복 업무: 사람이 읽고, 옮기고, 판단하고, 다시 쓰는 지점
- 자료 상태: 실제 자료, 익명화 샘플, 더미 데이터, 가상 샘플 중 무엇을 쓸 수 있는지
- 기대 결과: 발표장에서 어떤 형태의 결과물을 보면 도움이 되는지

개인정보와 내부자료는 원본 그대로 넣지 않습니다. 이름, 연락처, 주소, 주민등록번호, 계좌번호, 이메일, 상담 원문, 비밀값, 토큰, 접근권한 세부 정보는 익명화, 마스킹, 삭제, 더미 생성, 화면 시연 중 하나로 처리합니다. 샘플이 아직 익명화되어 있지 않으면 오렌지필터를 설치해 익명화한 뒤 사용합니다.

- 오렌지필터 설치: https://chromewebstore.google.com/detail/%EC%98%A4%EB%A0%8C%EC%A7%80%ED%95%84%ED%84%B0orange-filter-ai-%ED%94%84%EB%9D%BC%EC%9D%B4/gnkcbdgbajeboglkplllicdghlcghjai

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

설치 후 새 Codex 세션을 열고 `$codex-impact-canvas`를 입력해 시작합니다.

## 실행 구조

스킬은 아래 순서로 움직입니다.

1. 사용자가 `$codex-impact-canvas`라고 입력합니다. `/codex-impact-canvas`도 호환 호출로 인정합니다.
2. 기본 정보 확인: 사회혁신가 이름, 개발자 이름, 팀 또는 프로젝트 이름을 하나씩 순차 질문합니다. `request_user_input`이 활성화되어 있으면 도구로 묻고, 비활성화되어 있으면 일반 채팅으로 묻습니다.
3. 업무 문제 확인: 반복 처리 업무, 불편을 겪는 사람, 문제가 발생하는 순간
4. 자료 확인: 실제 자료 유무, 개인정보 제거 샘플, 익명화되지 않은 샘플은 오렌지필터 안내, 자료가 없을 경우 가상 샘플 생성
5. 결과물 선택: 문제를 들은 뒤 자동화 도구, 웹앱, 온보딩 페이지, admin 화면, 대시보드, 문서/메시지 초안 등 가능한 후보 제안
6. 3시간 MVP 좁히기: 해결할 좁은 문제, 포함할 업무 단계, 오늘 할 것/하지 않을 것, AI 역할, 사람 검토 지점, 성공/실패 기준, 3시간 안/밖 판단
7. 다음 단계 안내: `PLAN.md`, `workshop.json` 초안 생성 후 스킬은 직접 구현하지 않고 사용자에게 구현을 넘김
8. 발표자료 제작: 최종 `workshop.json`을 기준으로 입력 폴더를 점검하고, 필요한 경우 `presentation-assets/result_screenshot.png`를 준비한 뒤 이 스킬 안에서 5장 Google Slides를 만듭니다.

## 팀 시작

처음에 받는 정보입니다.

- 사회혁신가 이름
- 개발자 이름
- 팀 이름 또는 프로젝트 이름. 없으면 문제 설명에서 임시 제목을 만듭니다.

실제 진행 시 한 번에 묶어 묻지 않고 아래 순서로 각각 묻습니다. `request_user_input`이 활성화되어 있으면 각 질문을 별도 도구 호출로 보내고, 비활성화되어 있으면 같은 문구를 일반 채팅 질문으로 보냅니다.

```text
사회혁신가 이름은 무엇인가요?
```

답변을 받은 뒤:

```text
개발자 이름은 무엇인가요?
```

답변을 받은 뒤:

```text
정해진 팀 또는 프로젝트 이름이 있나요?
```

## 질문 흐름

아래 질문들은 실제 진행 시 `request_user_input`이 활성화되어 있으면 도구 호출로 전달합니다. 도구가 비활성화되어 있으면 일반 채팅 질문으로 전달합니다. 이미 확인된 내용은 건너뛰고, 빈칸을 채울 때만 한 번에 하나씩 묻습니다.

### 1. 기본 정보 확인

```text
오늘 작업할 팀 정보를 먼저 확인하겠습니다. 사회혁신가 이름, 개발자 이름, 정해진 팀/프로젝트 이름을 알려주세요.
```

### 2. 업무 문제 확인

```text
지금 반복해서 처리하느라 불편한 업무는 무엇이고, 누가 어떤 순간에 가장 막히나요?
```

완료 기준:

- 반복 처리 업무가 드러납니다.
- 불편을 겪는 사람이 구분됩니다.
- 문제가 발생하는 순간이 한 문장으로 정리됩니다.

### 3. 자료 확인

```text
오늘 써볼 실제 자료가 있나요? 있다면 개인정보를 제거한 샘플로 쓸 수 있고, 아직 익명화되지 않았다면 오렌지필터로 익명화한 뒤 사용합니다. 자료가 없다면 가상 샘플로 시작해도 됩니다.
```

완료 기준:

- 실제 자료, 익명화 샘플, 가상 샘플 중 무엇을 쓸지 정합니다.
- 자료 형태와 개인정보 처리 방식을 기록합니다.
- 익명화되지 않은 샘플은 원본 그대로 쓰지 않고 오렌지필터 설치 후 익명화하도록 안내합니다.
- 자료가 없으면 스킬이 만들 가상 샘플 조건을 정합니다.

### 4. 결과물 선택

스킬은 문제를 들은 뒤 아래 결과물 후보 중 2-4개를 제안하고 하나를 확정합니다.

- 자동화 도구
- 웹앱
- 온보딩 페이지
- admin 화면
- 대시보드
- 문서/메시지 초안

### 5. 3시간 MVP 압축

```text
3시간 안에 보여줄 핵심 흐름 1개만 남기면, 어떤 입력을 넣어 어떤 결과를 보여주고 사람이 어디를 검토하면 될까요?
```

완료 기준:

- 입력 1개와 출력 1개가 고정됩니다.
- 사람이 반복해서 읽고, 옮기고, 판단하고, 다시 쓰는 지점 하나가 자동화 대상으로 정리됩니다.
- AI가 할 일, 사람이 검토할 일, 실패 시 사람이 이어받는 방식이 분리됩니다.
- 오늘 하지 않을 것과 다음 단계 아이디어가 분리됩니다.

### 6. 다음 단계 안내

문제정의가 끝나면 `PLAN.md`와 `workshop.json` 초안을 만들고, 스킬은 직접 구현으로 넘어가지 않습니다. 다음 단계는 사용자가 `PLAN.md`의 3시간 구현 계획을 기준으로 구현하는 것입니다. `PLAN.md`에는 새 세션에서 구현하더라도 구현 중 결정, 변경, 막힌 점, 검증 결과를 `MEMORY.md`에 append-only로 기록하라는 구현자 지침을 포함합니다. 구현 완료 후 다시 요청하면 산출물 범위를 묻지 않고 워크숍 표준 흐름에 따라 `WORKFLOW_ANALYSIS.md`, `CASE_STUDY.md`, 최종 `workshop.json`, 5장 Google Slides 발표자료 제작으로 이어갑니다.

## 필수 산출물

산출물 범위는 질문하지 않고 워크숍 표준 흐름을 기본으로 적용합니다.

### PLAN.md

문제정의 단계의 팀 합의와 3시간 MVP 실행 계획입니다.

포함 내용:

- 팀 정보
- 실제 업무 문제
- 어려움을 겪는 사람
- 자료 상태와 개인정보 처리
- 현재 업무 흐름
- 결과물 형태
- 기대 변화
- 해결할 좁은 문제
- 3시간 MVP 기능 1개
- 포함할 업무 단계
- 데모 입력과 데모 산출물
- 성공 기준
- 실패 신호
- 3시간 안/밖 판단
- 제외 범위
- 3시간 구현 계획
- 구현자 지침
- 빠르게 끝났을 때 이어서 할 작업 후보 2개
- 제출/아카이빙 기준

### workshop.json

질문 답변과 구현 결과를 표준 필드로 정규화한 기준 데이터입니다. 제출, 아카이빙, 마크다운 재생성, 여러 팀 결과 분석에 사용합니다.

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
- 자료 상태와 데이터 특성
- 정형/비정형 여부
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

### 발표자료

최종 산출물 작성 후 같은 스킬 안에서 만드는 5장 Google Slides 발표자료입니다.

포함 내용:

- 최종 기준 데이터는 `workshop.json`입니다.
- 참가자 폴더에 `input.json`이 있으면 최종 `workshop.json`과 같은 내용인지 확인합니다. 내장 발표 스크립트는 `workshop.json`을 먼저 읽습니다.
- 화면, 웹앱, admin 화면, 대시보드처럼 시각 결과물이 있으면 공개 가능한 캡처만 `presentation-assets/result_screenshot.png`에 둡니다.
- 발표자 한줄소개는 사회혁신가와 개발자에게 한 명씩 따로 받습니다. 파일에서 임의로 추론하지 않습니다.
- Google Slides 사본은 생성 후 링크가 있는 모든 사용자가 뷰어 권한으로 볼 수 있게 공유 설정합니다.
- 자세한 기준은 `references/presentation-handoff.md`와 `references/presentation-build.md`를 따릅니다.

발표 문구와 Google Slides 요청 파일은 아래 스크립트로 만듭니다.

```bash
node scripts/prepare-presentation-content.mjs --input-dir /path/to/team-folder
node scripts/build-google-slides-requests.mjs --input-dir /path/to/team-folder
```

최종 산출물은 로컬 PPTX가 아니라 복사한 Google Slides deck입니다. `outputs/google-drive-permission.json`의 permission body를 복사한 deck 파일 ID에 적용해 `링크가 있는 모든 사용자` + `뷰어` 권한으로 공유합니다.

## 출력 일관성 규칙

결과물을 여러 팀의 사례로 모으기 위해 아래 규칙을 지킵니다.

- 알 수 없는 값은 `미정`으로 씁니다.
- 해당하지 않는 값은 `해당 없음`으로 씁니다.
- 공개 범위는 `공개 가능`, `익명화 후 공개 가능`, `내부 공유만`, `공개 불가` 중 하나로 씁니다.
- 개인정보 수준은 `공개 데이터`, `내부자료`, `익명화 필요`, `개인정보 포함`, `민감정보 포함` 중 하나로 씁니다.
- 자료 상태는 `실제 자료`, `익명화 샘플`, `가상 샘플`, `자료 없음`, `미정` 중 하나로 씁니다.
- 결과물 형태는 `자동화 도구`, `웹앱`, `온보딩 페이지`, `admin 화면`, `대시보드`, `문서/메시지 초안`, `기타`, `미정` 중 하나로 씁니다.
- 재사용 수준은 `그대로 재사용 가능`, `템플릿 재사용 가능`, `분야 특화`, `일회성`, `미정` 중 하나로 씁니다.
- `PLAN.md`, `WORKFLOW_ANALYSIS.md`, `CASE_STUDY.md`의 YAML 메타데이터는 같은 값을 사용합니다.
- `WORKFLOW_ANALYSIS.md`와 `CASE_STUDY.md`에는 같은 사례 ID를 사용합니다.

사례 ID 형식:

```text
impact-agent-[YYYYMMDD]-[short-slug]
```

## 스크립트로 산출물 생성하기

답변을 JSON으로 정리했다면 아래 명령으로 필수 산출물을 만들 수 있습니다.

```bash
python3 scripts/write_workshop_outputs.py --input workshop.json --output-dir . --phase all
```

이 명령은 마크다운 산출물과 함께 표준화된 `workshop.json`도 출력 디렉터리에 저장합니다.

문제정의 직후 `PLAN.md`, `MEMORY.md`, `workshop.json` 초안만 만들 때는 아래처럼 실행합니다.

```bash
python3 scripts/write_workshop_outputs.py --input workshop.json --output-dir . --phase plan
```

구현 완료 후 `WORKFLOW_ANALYSIS.md`, `CASE_STUDY.md`, 최종 `workshop.json`을 만들 때는 아래처럼 실행합니다.

```bash
python3 scripts/write_workshop_outputs.py --input workshop.json --output-dir . --phase final --stage "워크플로 분석"
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
  "materials": {
    "source_status": "익명화 샘플",
    "sample_input": "워크숍에서 쓸 입력 자료",
    "privacy_action": "개인정보 처리 방식",
    "validity_check": "샘플 유효성 확인 기준"
  },
  "output_choice": {
    "problem_archetype": "데이터 정리/분석/대시보드",
    "output_type": "대시보드",
    "selection_reason": "발표장에서 반복 업무 절감 효과를 바로 보여줄 수 있기 때문"
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
    "single_feature": "3시간 MVP 기능 1개",
    "included_workflow_steps": "포함할 업무 단계",
    "demo_input": "데모 입력",
    "demo_output": "데모 산출물",
    "ai_role": "AI 역할",
    "human_review_point": "사람 검토 지점",
    "success_criterion": "성공 기준",
    "failure_signal": "실패 신호",
    "three_hour_decision": "안/축소 필요/밖 - 근거"
  },
  "submission": {
    "problem_definition_outputs": "PLAN.md, workshop.json 초안",
    "build_records": "MEMORY.md",
    "final_outputs": "WORKFLOW_ANALYSIS.md, CASE_STUDY.md, 최종 workshop.json, 5장 Google Slides 발표자료",
    "archive_criteria": "제출/아카이빙 기준"
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
│   ├── intent-check.md
│   ├── memory-log.md
│   ├── output-consistency.md
│   ├── output-types.md
│   ├── plan-template.md
│   ├── pre-workshop-guide.md
│   ├── problem-archetypes.md
│   └── workflow-analysis.md
├── samples/
│   ├── case1-food-aid-review/
│   ├── case2-mentoring-note-summary/
│   └── case3-neighborhood-repair-routing/
└── scripts/
    └── write_workshop_outputs.py
```

`samples/`에는 가상 사례 3개의 `input.json`, `workshop.json`, `PLAN.md`, `MEMORY.md`, `WORKFLOW_ANALYSIS.md`, `CASE_STUDY.md`가 들어 있습니다. 복지, 교육, 지역 사례를 각각 다르게 구성해 개인정보 수준, 공유 가능 범위, 재사용 수준이 어떻게 기록되는지 확인할 수 있습니다.
