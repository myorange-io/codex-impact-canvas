# 발표자료 핸드오프

이 문서는 같은 `codex-impact-canvas` 스킬 안에서 발표자료 제작 단계로 넘어가기 전에 확인합니다. 전체 흐름의 끝은 기록 파일 생성이 아니라, 참가팀이 발표할 수 있는 5장 발표자료 제작까지입니다. 발표자료 제작 요청을 받았을 때 `WORKFLOW_ANALYSIS.md` 또는 `CASE_STUDY.md`가 없으면, 발표자료를 만들기 전에 두 파일부터 생성합니다.

## 기준 스킬

발표자료 제작은 별도 스킬을 설치하지 않고 이 스킬의 `references/presentation-build.md` 흐름으로 진행합니다.

참가자 입력 폴더는 이 스킬이 만든 산출물 폴더입니다. 폴더 안에는 최소한 아래 파일이 있어야 합니다.

- `workshop.json`
- `PLAN.md`
- `MEMORY.md`
- `WORKFLOW_ANALYSIS.md`
- `CASE_STUDY.md`

`WORKFLOW_ANALYSIS.md` 또는 `CASE_STUDY.md`가 없으면 `workshop.json`을 기준으로 아래 명령을 먼저 실행합니다.

```bash
python3 scripts/write_workshop_outputs.py --input <participant-folder>/workshop.json --output-dir <participant-folder> --phase final --stage "발표자료 제작 전 정리"
```

`workshop.json`이 없고 `input.json`만 있으면 `--input <participant-folder>/input.json`을 사용합니다.

## 최종 기준 데이터

발표자료 제작에 넘길 기준 데이터는 최종 `workshop.json`입니다.

- `workshop.json`은 문제정의, 구현 기록, 완료 후 분석 결과가 반영된 최종 파일이어야 합니다.
- 참가자 폴더에 `input.json`이 있으면 주의합니다. 이 스킬의 발표자료 스크립트는 `workshop.json`을 먼저 읽지만, `input.json`이 오래된 초기 입력이면 혼란을 줄 수 있습니다.
- `input.json`을 유지해야 한다면 최종 `workshop.json`과 같은 내용으로 갱신합니다.
- `input.json`이 단순 초기 입력 파일이라면 발표자료 제작 전 제거하거나 최종 `workshop.json`과 같은 내용으로 갱신합니다.

## 결과물 캡처

결과물이 화면, 웹앱, admin 화면, 대시보드, 시각화, 자동화 도구 UI처럼 눈으로 확인하는 형태라면 공개 가능한 캡처를 준비합니다.

권장 경로:

```text
presentation-assets/result_screenshot.png
```

캡처 기준:

- 개인정보, 민감정보, 내부 원문, 계정 정보, 접근권한 세부 정보가 보이면 사용하지 않습니다.
- 실제 화면을 공개할 수 없으면 더미 데이터 화면이나 익명화 화면을 캡처합니다.
- 결과물이 문서/메시지 초안처럼 화면 캡처가 핵심이 아니면 캡처 없이 진행할 수 있습니다.

## 발표자료 제작 전 점검

- `workshop.json`이 최종 기준 데이터입니다.
- `PLAN.md`, `MEMORY.md`, `WORKFLOW_ANALYSIS.md`, `CASE_STUDY.md`가 같은 프로젝트와 같은 사례 ID를 가리킵니다.
- `WORKFLOW_ANALYSIS.md` 또는 `CASE_STUDY.md`가 없으면 발표자료 제작 전에 먼저 생성했습니다.
- `CASE_STUDY.md`에는 공개 불가 정보가 없습니다.
- `input.json`이 있으면 최종 `workshop.json`과 충돌하지 않습니다.
- 필요한 경우 `presentation-assets/result_screenshot.png`가 공개 가능한 이미지로 준비되어 있습니다.
- 발표자 한줄소개는 발표자료 제작 단계에서 사회혁신가와 개발자에게 한 명씩 따로 받습니다. 캔버스 스킬에서 임의로 추론하지 않습니다.
- 발표자료 Google Slides 사본은 생성 후 `링크가 있는 모든 사용자`가 `뷰어` 권한으로 볼 수 있게 공유 설정해야 합니다.

## 안내 문구

완료 후 사용자에게 아래처럼 안내합니다.

```text
워크숍 기록과 사례 정리가 끝났습니다. 최종 기준 파일은 `workshop.json`입니다.
이제 같은 참가자 폴더를 기준으로 이 스킬의 발표자료 제작 단계를 이어가 5장 Google Slides를 만들 수 있습니다.
발표자료 제작 전에 `input.json`이 최종 `workshop.json`과 충돌하지 않는지, 필요한 경우 `presentation-assets/result_screenshot.png`가 준비되어 있는지 확인하세요.
`WORKFLOW_ANALYSIS.md` 또는 `CASE_STUDY.md`가 없다면 발표자료를 만들기 전에 먼저 생성하세요.
생성한 Google Slides 사본은 링크가 있는 모든 사용자가 뷰어 권한으로 볼 수 있도록 공유 설정하세요.
```
