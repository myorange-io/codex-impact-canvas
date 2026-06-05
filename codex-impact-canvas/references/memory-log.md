# MEMORY.md Logging

`MEMORY.md` records how the team made the MVP. It is process evidence for later review and teaching.

## Principles

- Append only. Do not rewrite earlier entries except to update a live URL or correct clearly wrong metadata.
- Record process, not only results.
- Be concrete about decisions, rejected options, blocked points, error messages, commands, and fixes.
- Write in Korean in human language.
- Use the date from `date +%Y-%m-%d`.
- Do not include secrets, tokens, personal data, internal raw data, or permission details.

## First File Template

If `MEMORY.md` does not exist, create:

```markdown
# 만들기 기록 - [프로젝트 이름]

> 이 파일은 이 MVP를 어떤 과정으로 만들었는지 남기는 기록입니다.
> 나중에 복기하거나 사회혁신 AI Agent Workflow 사례로 정리할 때 씁니다.

## 한눈에 보기
- 무엇을: [PLAN.md 한 줄 요약]
- 누구를 위해: [주 사용자/수혜자]
- 핵심 흐름: [입력 -> AI Agent -> 사람 검토 -> 산출물]
- 스택/도구: [Codex/ChatGPT/API/MCP/CLI/외부 서비스]
- 시작: [YYYY-MM-DD]

---

## 기록
```

## Entry Template

Append entries in this shape:

```markdown
### [YYYY-MM-DD] [단계 이름]
- **정한 것 / 한 것**: [이 단계에서 실제로 만든 것 또는 결정한 것]
- **왜**: [그 선택의 이유와 버린 선택지]
- **어떻게**: [구체적 방법, 도구, 명령, 연결 방식]
- **막힌 점 / 바꾼 점**: [증상, 원인, 해결. 없으면 "없음"]
- **배운 것 / 다음**: [다음에 이어서 할 것]
```

Recommended stage names:

- `문제 정의`
- `MVP 범위 합의`
- `구현`
- `검수`
- `워크플로 분석`
- `사례 정리`
