# 발표자료 제작

이 문서는 `codex-impact-canvas` 스킬 안에서 5장짜리 3분 발표용 Google Slides를 만들 때 사용합니다. 별도 `codex-impact-presentation` 스킬을 설치하거나 호출하지 않습니다.

## 목표

워크숍 산출물 폴더를 바탕으로 "현장 문제 -> AI 에이전트 MVP -> 적용 효과"를 보여주는 5장 발표자료를 만듭니다.

기준 입력 폴더에는 아래 파일이 있을 수 있습니다.

- `workshop.json`
- `input.json`
- `PLAN.md`
- `MEMORY.md`
- `WORKFLOW_ANALYSIS.md`
- `CASE_STUDY.md`
- `presentation-input.json`
- `presentation-assets/result_screenshot.png`

입력 우선순위는 반드시 아래 순서입니다.

1. `workshop.json`
2. `input.json`
3. Markdown 파일

`workshop.json`은 구현과 분석이 반영된 최종 기준 데이터입니다. `input.json`이 있더라도 `workshop.json`보다 먼저 읽지 않습니다.

## Google Slides 템플릿

항상 아래 Google Slides 템플릿을 복사해서 사용합니다.

https://docs.google.com/presentation/d/13pVNcDsFf1DX6emPLjOt1NvtPE9xpkh02GQAbs3IT1g/edit?usp=sharing

템플릿 원본은 직접 수정하지 않습니다. 반드시 사본을 만든 뒤 사본에 내용을 채웁니다.

템플릿은 정확히 5장입니다.

1. Cover: 프로젝트 제목, 부제, 발표자 이름과 한줄소개
2. Field Problem: 문제 헤드라인과 근거 3줄
3. Solution: 기존 방식과 AI 도입 후 비교
4. Workflow: 3단계 작동 흐름과 선택적 결과물 캡처
5. Field Application: 기대 효과 헤드라인과 효과 카드 2개

## 필수 진행 순서

1. 참가자 입력 폴더를 확인합니다.
2. Google Slides에 텍스트와 이미지를 업로드해도 되는지 사용자에게 명시적으로 확인합니다.
3. 표지용 한줄소개를 사회혁신가와 개발자에게 한 명씩 따로 묻습니다. 두 질문을 한 메시지에 묶지 않습니다.
4. 사회혁신가 한줄소개를 묻기 전 정확히 아래 문구로 설명합니다.

```text
표지에 발표자를 소개하기 위해 한줄소개가 필요합니다.
```

5. 사회혁신가 한줄소개는 정확히 아래 문구로 묻습니다.

```text
사회혁신가 한줄소개를 입력해주세요. (공백 포함 65자 이내)
```

6. 답변이 65자 이내이면 개발자 한줄소개를 정확히 아래 문구로 묻습니다.

```text
개발자 한줄소개를 입력해주세요. (공백 포함 65자 이내)
```

7. 각 한줄소개는 공백 포함 65자 이하여야 합니다. 넘으면 줄여달라고 묻고 진행을 멈춥니다.
8. 한줄소개는 파일에서 추론하지 않습니다. 사용자가 확인한 그대로 `presentation-input.json`의 `social_innovator_intro`, `developer_intro`에 저장합니다.
9. `scripts/prepare-presentation-content.mjs --input-dir <participant-folder>`를 실행합니다.
10. Google Drive/Slides connector로 템플릿을 복사합니다.
11. 복사한 프레젠테이션을 읽어 5장인지 확인합니다.
12. `scripts/build-google-slides-requests.mjs --input-dir <participant-folder>`를 실행합니다.
13. 생성된 `outputs/google-slides-requests.json`을 복사한 deck에 `batchUpdate`로 적용합니다.
14. `outputs/google-slides-image-uris.txt`가 있으면 그 내용을 image URI로 함께 넘깁니다.
15. 편집된 deck을 다시 읽어 템플릿 샘플 문구가 교체되었는지 확인합니다.
16. 5장 썸네일을 새로 가져와 텍스트 넘침, 겹침, 미교체 placeholder가 없는지 눈으로 확인합니다.

최종 산출물은 로컬 PPTX가 아니라 편집 가능한 Google Slides 사본입니다.

## 스크립트

발표 문구 생성:

```bash
node scripts/prepare-presentation-content.mjs --input-dir <participant-folder>
```

Google Slides batchUpdate 요청 생성:

```bash
node scripts/build-google-slides-requests.mjs --input-dir <participant-folder>
```

요청 생성 스크립트는 아래 파일을 만듭니다.

- `outputs/google-slides-requests.json`
- `outputs/google-slides-image-uris.txt` when a result screenshot exists

## 결과물 캡처

4장에는 결과물 캡처 영역이 있습니다.

- 캡처가 있으면 `presentation-assets/result_screenshot.png`에 둡니다.
- 캡처가 없으면 deck은 생성하고 템플릿 placeholder를 남깁니다.
- 공개 불가 정보, 개인정보, 내부 원문, 계정 정보가 보이는 캡처는 사용하지 않습니다.
- 캡처를 임의로 찾거나 새로 꾸며내지 않습니다.

## 발표 시간

발표자료는 엄격한 3분 발표용입니다. 모든 장표 발표자 노트에 아래 시간을 넣습니다.

- Slide 1: 25 seconds, 0:00-0:25
- Slide 2: 35 seconds, 0:25-1:00
- Slide 3: 45 seconds, 1:00-1:45
- Slide 4: 40 seconds, 1:45-2:25
- Slide 5: 35 seconds, 2:25-3:00

Slide 1 발표자 노트는 아래 문구로 시작해야 합니다.

```text
[전체 발표 시간: 3분]
시간 관계상 각 슬라이드별 권장 시간을 지켜 발표해 주세요.
```

## 문체

- 각 장표는 짧고 듬성하게 씁니다.
- 표지에는 사회혁신가를 먼저, 개발자를 두 번째로 둡니다.
- 긴 워크숍 답변을 그대로 붙이지 않습니다.
- 2장 문제 근거는 각 한 문장으로 씁니다.
- 4장 작동 흐름은 세 단계로 줄입니다.
- 4장 단계에 `작동 1단계` 같은 일반 라벨을 붙이지 않습니다.
- 5장 효과 설명은 카드 안에 들어갈 만큼 짧게 씁니다.
- footer quote는 사례에 맞게 새로 만듭니다.
- 발표자 노트는 실제 발표 대본이어야 하며, 제작 안내나 placeholder 설명을 넣지 않습니다.
- 중심 메시지는 "AI가 출발점을 정리하고, 사람은 책임 있게 최종 결정한다"입니다.

## 검증

마무리 전 아래를 확인합니다.

- 최종 URL은 원본 템플릿이 아니라 복사한 deck입니다.
- 복사한 deck은 5장입니다.
- `긴급식품지원`, `김무재`, `평균 주말 누적 접수 건수 30~50건` 같은 템플릿 샘플 문구가 남아 있지 않습니다. 단, 참가자 사례 내용이면 예외입니다.
- footer quote는 템플릿 샘플 문구가 아니라 이 사례에 맞는 문구입니다.
- 표지는 사회혁신가를 개발자보다 먼저 보여주고, 두 사람의 사용자 제공 한줄소개가 들어 있습니다.
- 모든 발표자 한줄소개는 공백 포함 65자 이내입니다.
- 모든 장표에 3분 발표자 노트가 있고, 장표별 초와 시간 범위가 들어 있습니다.
- 4장은 제공된 캡처를 포함하거나 캡처 없음이 의도적으로 남아 있습니다.
- 새 썸네일 기준으로 넘침, 겹침, 미교체 placeholder가 없습니다.
