#!/usr/bin/env python3
"""Generate consistent Codex Impact Workshop Markdown outputs from JSON."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path
from typing import Any


UNKNOWN = "미정"
NA = "해당 없음"


def text(value: Any, default: str = UNKNOWN) -> str:
    if value is None:
        return default
    if isinstance(value, list):
        return "\n".join(f"- {text(item)}" for item in value) if value else default
    value = str(value).strip()
    return value if value else default


def pick(data: dict[str, Any], path: str, default: str = UNKNOWN) -> str:
    current: Any = data
    for part in path.split("."):
        if not isinstance(current, dict) or part not in current:
            return default
        current = current[part]
    return text(current, default)


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = value.strip("-")
    return value or "case"


def metadata(data: dict[str, Any]) -> dict[str, str]:
    today = dt.date.today().isoformat()
    project_name = pick(data, "project.name")
    team_name = pick(data, "team.name")
    created_date = pick(data, "project.created_date", today)
    event = pick(data, "project.event", "Codex Impact Workshop")
    date_compact = created_date.replace("-", "")
    case_slug = slugify(pick(data, "project.slug", project_name))
    return {
        "team_name": team_name,
        "project_name": project_name,
        "created_date": created_date,
        "event": event,
        "version": "1",
        "case_id": f"impact-agent-{date_compact}-{case_slug}",
    }


def frontmatter(meta: dict[str, str]) -> str:
    return "\n".join(
        [
            "---",
            f'team_name: "{meta["team_name"]}"',
            f'project_name: "{meta["project_name"]}"',
            f'created_date: "{meta["created_date"]}"',
            f'event: "{meta["event"]}"',
            f'version: "{meta["version"]}"',
            "---",
            "",
        ]
    )


def render_plan(data: dict[str, Any], meta: dict[str, str]) -> str:
    return frontmatter(meta) + f"""# {meta["project_name"]} PLAN

## Team
- 사회혁신가: {pick(data, "team.social_innovator")}
- 개발자: {pick(data, "team.developer")}

## Problem
- 실제 업무 문제: {pick(data, "problem.actual_work_problem")}
- 가장 어려움을 겪는 사람: {pick(data, "problem.people_affected")}
- 문제가 발생하는 순간: {pick(data, "problem.blocked_moment")}

## Current Workflow
- 입력 자료: {pick(data, "current_workflow.inputs")}
- 처리 순서: {pick(data, "current_workflow.steps")}
- 판단 기준: {pick(data, "current_workflow.judgment")}
- 현재 산출물: {pick(data, "current_workflow.outputs")}
- 현재 사용 도구: {pick(data, "current_workflow.tools")}

## Expected Change
- 기대 변화: {pick(data, "expected_change.summary")}
- 관찰 가능한 개선: {pick(data, "expected_change.observable_improvement")}

## 3-Hour MVP
- 핵심 기능 1개: {pick(data, "mvp.single_feature")}
- 데모 입력: {pick(data, "mvp.demo_input")}
- 데모 산출물: {pick(data, "mvp.demo_output")}
- 성공 기준: {pick(data, "mvp.success_criterion")}

## Out of Scope
- 오늘 하지 않을 것: {pick(data, "scope.not_today", NA)}
- 다음 단계 아이디어: {pick(data, "scope.next_ideas", NA)}

## Build Plan
- 0-30분: {pick(data, "build_plan.0_30")}
- 30-90분: {pick(data, "build_plan.30_90")}
- 90-150분: {pick(data, "build_plan.90_150")}
- 150-180분: {pick(data, "build_plan.150_180")}
"""


def render_workflow(data: dict[str, Any], meta: dict[str, str]) -> str:
    return frontmatter(meta) + f"""# {meta["project_name"]} Workflow Analysis

## Library Metadata
- case_id: {meta["case_id"]}
- sector: {pick(data, "library_metadata.sector")}
- workflow_type: {pick(data, "library_metadata.workflow_type")}
- agent_role: {pick(data, "library_metadata.agent_role")}
- data_type: {pick(data, "library_metadata.data_type")}
- privacy_level: {pick(data, "library_metadata.privacy_level")}
- integration_level: {pick(data, "library_metadata.integration_level")}
- human_review: {pick(data, "library_metadata.human_review")}
- reuse_level: {pick(data, "library_metadata.reuse_level")}
- output_format: {pick(data, "library_metadata.output_format")}

## Existing Workflow
- workflow_trigger: {pick(data, "existing_workflow.workflow_trigger")}
- baseline_volume: {pick(data, "existing_workflow.baseline_volume")}
- baseline_time: {pick(data, "existing_workflow.baseline_time")}
- input_sources: {pick(data, "existing_workflow.input_sources")}
- current_steps: {pick(data, "existing_workflow.current_steps")}
- current_outputs: {pick(data, "existing_workflow.current_outputs")}
- current_pain_points: {pick(data, "existing_workflow.current_pain_points")}

## Automation Target
- selected_task: {pick(data, "automation_target.selected_task")}
- reason_for_selection: {pick(data, "automation_target.reason_for_selection")}
- excluded_tasks: {pick(data, "automation_target.excluded_tasks", NA)}

## AI Agent Design
- agent_input_contract: {pick(data, "ai_agent_design.agent_input_contract")}
- agent_output_contract: {pick(data, "ai_agent_design.agent_output_contract")}
- decision_boundary: {pick(data, "ai_agent_design.decision_boundary")}
- tools_used: {pick(data, "ai_agent_design.tools_used")}
- changed_workflow: {pick(data, "ai_agent_design.changed_workflow")}

## Human-in-the-Loop
- review_points: {pick(data, "human_in_the_loop.review_points")}
- handoff_protocol: {pick(data, "human_in_the_loop.handoff_protocol")}
- error_types: {pick(data, "human_in_the_loop.error_types")}
- evaluation_samples: {pick(data, "human_in_the_loop.evaluation_samples")}

## Data and Access
- privacy_action: {pick(data, "data_and_access.privacy_action")}
- permission_issues: {pick(data, "data_and_access.permission_issues", NA)}
- shareability: {pick(data, "data_and_access.shareability")}

## Impact and Reuse
- expected_time_change: {pick(data, "impact_and_reuse.expected_time_change")}
- quality_change: {pick(data, "impact_and_reuse.quality_change")}
- case_reuse_recipe: {pick(data, "impact_and_reuse.case_reuse_recipe")}
- maintenance_owner: {pick(data, "impact_and_reuse.maintenance_owner")}
- next_iteration: {pick(data, "impact_and_reuse.next_iteration")}
"""


def render_case_study(data: dict[str, Any], meta: dict[str, str]) -> str:
    title = pick(data, "case_study.title", meta["project_name"])
    return frontmatter(meta) + f"""# {title}

## Case Metadata
- case_id: {meta["case_id"]}
- 공개 범위: {pick(data, "data_and_access.shareability")}
- 분야: {pick(data, "library_metadata.sector")}
- 재사용 수준: {pick(data, "library_metadata.reuse_level")}

## Problem Summary
{pick(data, "case_study.problem_summary", pick(data, "problem.actual_work_problem"))}

## Before
{pick(data, "case_study.before", pick(data, "existing_workflow.current_steps"))}

## AI Agent Workflow
{pick(data, "case_study.ai_agent_workflow", pick(data, "ai_agent_design.changed_workflow"))}

## Human Review
{pick(data, "case_study.human_review", pick(data, "human_in_the_loop.review_points"))}

## Tools
{pick(data, "case_study.tools", pick(data, "ai_agent_design.tools_used"))}

## MVP Result
{pick(data, "case_study.mvp_result", pick(data, "mvp.demo_output"))}

## Success Criterion
{pick(data, "case_study.success_criterion", pick(data, "mvp.success_criterion"))}

## Lessons
{pick(data, "case_study.lessons")}

## Reuse Guide
{pick(data, "case_study.reuse_guide", pick(data, "impact_and_reuse.case_reuse_recipe"))}

## Redaction Notes
{pick(data, "case_study.redaction_notes", pick(data, "data_and_access.privacy_action"))}
"""


def memory_header(data: dict[str, Any], meta: dict[str, str]) -> str:
    return f"""# 만들기 기록 - {meta["project_name"]}

> 이 파일은 이 MVP를 어떤 과정으로 만들었는지 남기는 기록입니다.
> 나중에 복기하거나 사회혁신 AI Agent Workflow 사례로 정리할 때 씁니다.

## 한눈에 보기
- 무엇을: {pick(data, "problem.actual_work_problem")}
- 누구를 위해: {pick(data, "problem.people_affected")}
- 핵심 흐름: {pick(data, "ai_agent_design.changed_workflow")}
- 스택/도구: {pick(data, "ai_agent_design.tools_used")}
- 시작: {meta["created_date"]}

---

## 기록
"""


def memory_entry(data: dict[str, Any], stage: str) -> str:
    today = dt.date.today().isoformat()
    return f"""
### {today} {stage}
- **정한 것 / 한 것**: {pick(data, "memory_entry.did", "필수 Markdown 산출물 구조와 3시간 MVP 범위를 정리했다.")}
- **왜**: {pick(data, "memory_entry.why", "팀별 결과물을 같은 구조로 남겨 이후 사례집과 Workflow 라이브러리로 재사용하기 위해서다.")}
- **어떻게**: {pick(data, "memory_entry.how", "반응형 질문 답변을 표준 필드로 정규화해 PLAN.md, WORKFLOW_ANALYSIS.md, CASE_STUDY.md, MEMORY.md에 기록했다.")}
- **막힌 점 / 바꾼 점**: {pick(data, "memory_entry.blocked", "없음")}
- **배운 것 / 다음**: {pick(data, "memory_entry.next", "샘플 데이터로 MVP를 구현하고 검수 포인트를 보완한다.")}
"""


def sample_data() -> dict[str, Any]:
    return {
        "team": {"name": "샘플팀", "social_innovator": "사회혁신가", "developer": "개발자"},
        "project": {"name": "Sample Impact Agent", "slug": "sample-impact-agent"},
        "problem": {
            "actual_work_problem": "신청서 내용을 사람이 반복해서 읽고 누락 여부를 확인한다.",
            "people_affected": "사업 담당자와 신청자",
            "blocked_moment": "신청 마감 직후 서류가 몰릴 때",
        },
        "current_workflow": {
            "inputs": "신청서 PDF",
            "steps": "접수 -> 항목 확인 -> 누락 표시 -> 안내문 작성",
            "judgment": "필수 항목 누락 여부",
            "outputs": "누락 목록과 안내 초안",
            "tools": "이메일, 스프레드시트",
        },
        "expected_change": {
            "summary": "누락 확인 시간을 줄이고 안내 품질을 일정하게 만든다.",
            "observable_improvement": "샘플 신청서 1개에서 누락 항목과 안내 초안이 바로 나온다.",
        },
        "mvp": {
            "single_feature": "신청서 텍스트를 넣으면 누락 항목과 안내 초안을 생성한다.",
            "demo_input": "익명화한 신청서 텍스트 1개",
            "demo_output": "누락 항목 목록과 이메일 안내 초안",
            "success_criterion": "핵심 누락 3개 중 2개 이상을 찾고 사람이 수정 가능한 초안을 만든다.",
        },
        "scope": {"not_today": "자동 이메일 발송", "next_ideas": "신청서 일괄 처리"},
        "build_plan": {
            "0_30": "샘플 입력과 출력 형식을 고정한다.",
            "30_90": "프롬프트와 처리 흐름을 만든다.",
            "90_150": "간단한 UI 또는 CLI 데모를 만든다.",
            "150_180": "샘플로 테스트하고 발표 흐름을 정리한다.",
        },
        "library_metadata": {
            "sector": "운영",
            "workflow_type": "신청서검토",
            "agent_role": "검토보조",
            "data_type": "비정형",
            "privacy_level": "익명화 필요",
            "integration_level": "수동 업로드",
            "human_review": "최종 검토",
            "reuse_level": "템플릿 재사용 가능",
            "output_format": "md",
        },
        "existing_workflow": {
            "workflow_trigger": "신청서 접수",
            "baseline_volume": "한 번에 10-30건",
            "baseline_time": "건당 5-10분",
            "input_sources": "이메일 첨부 PDF",
            "current_steps": "사람이 PDF를 열고 필수 항목을 확인한다.",
            "current_outputs": "누락 목록과 안내문",
            "current_pain_points": "반복 확인과 안내문 품질 편차",
        },
        "automation_target": {
            "selected_task": "신청서 누락 확인과 안내 초안 작성",
            "reason_for_selection": "입력과 출력이 분명하고 3시간 안에 데모 가능하다.",
            "excluded_tasks": "원본 시스템 연동과 자동 발송",
        },
        "ai_agent_design": {
            "agent_input_contract": "익명화한 신청서 텍스트",
            "agent_output_contract": "누락 항목 목록과 안내 초안",
            "decision_boundary": "AI는 초안을 만들고 담당자가 최종 판단한다.",
            "tools_used": "Codex, ChatGPT",
            "changed_workflow": "신청서 텍스트 입력 -> AI 검토 초안 -> 담당자 최종 검토 -> 안내",
        },
        "human_in_the_loop": {
            "review_points": "발송 전 담당자 최종 검토",
            "handoff_protocol": "AI 결과가 비어 있으면 기존 수동 검토로 진행한다.",
            "error_types": "누락 오탐, 표현 부정확",
            "evaluation_samples": "익명화 샘플 1개와 기대 누락 목록",
        },
        "data_and_access": {
            "privacy_action": "이름과 연락처를 제거한 샘플만 사용",
            "permission_issues": "해당 없음",
            "shareability": "익명화 후 공개 가능",
        },
        "impact_and_reuse": {
            "expected_time_change": "건당 5-10분에서 초안 생성 1분 이내",
            "quality_change": "안내문 형식 일관성 향상",
            "case_reuse_recipe": "필수 항목 목록과 안내 문구를 조직별로 교체한다.",
            "maintenance_owner": "사업 담당자",
            "next_iteration": "일괄 처리와 이메일 발송 전 검수 화면",
        },
        "case_study": {
            "title": "신청서 누락 검토 AI Agent",
            "lessons": "3시간 MVP는 자동 발송보다 검토 초안 생성에 집중할 때 완성도가 높았다.",
        },
    }


def write_outputs(data: dict[str, Any], output_dir: Path, stage: str) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    meta = metadata(data)
    files = {
        "PLAN.md": render_plan(data, meta),
        "WORKFLOW_ANALYSIS.md": render_workflow(data, meta),
        "CASE_STUDY.md": render_case_study(data, meta),
    }
    for name, content in files.items():
        (output_dir / name).write_text(content.rstrip() + "\n", encoding="utf-8")

    memory_path = output_dir / "MEMORY.md"
    if not memory_path.exists():
        memory_path.write_text(memory_header(data, meta).rstrip() + "\n", encoding="utf-8")
    with memory_path.open("a", encoding="utf-8") as handle:
        handle.write(memory_entry(data, stage).rstrip() + "\n")


def validate_outputs(output_dir: Path) -> list[str]:
    issues: list[str] = []
    for name in ["PLAN.md", "MEMORY.md", "WORKFLOW_ANALYSIS.md", "CASE_STUDY.md"]:
        if not (output_dir / name).exists():
            issues.append(f"missing required file: {name}")
    plan = (output_dir / "PLAN.md").read_text(encoding="utf-8") if (output_dir / "PLAN.md").exists() else ""
    if "## 3-Hour MVP" not in plan:
        issues.append("PLAN.md missing ## 3-Hour MVP")
    workflow = (output_dir / "WORKFLOW_ANALYSIS.md").read_text(encoding="utf-8") if (output_dir / "WORKFLOW_ANALYSIS.md").exists() else ""
    for field in ["case_id", "agent_input_contract", "handoff_protocol", "case_reuse_recipe"]:
        if field not in workflow:
            issues.append(f"WORKFLOW_ANALYSIS.md missing {field}")
    case = (output_dir / "CASE_STUDY.md").read_text(encoding="utf-8") if (output_dir / "CASE_STUDY.md").exists() else ""
    for heading in ["## Problem Summary", "## AI Agent Workflow", "## Redaction Notes"]:
        if heading not in case:
            issues.append(f"CASE_STUDY.md missing {heading}")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, help="JSON file with normalized workshop answers")
    parser.add_argument("--output-dir", type=Path, default=Path("."), help="Directory for Markdown outputs")
    parser.add_argument("--demo", action="store_true", help="Generate outputs from built-in sample data")
    parser.add_argument("--stage", default="문제 정의", help="MEMORY.md entry stage name")
    parser.add_argument("--validate-only", action="store_true", help="Only validate existing outputs")
    args = parser.parse_args()

    if args.validate_only:
        issues = validate_outputs(args.output_dir)
        if issues:
            for issue in issues:
                print(f"[ERROR] {issue}")
            return 1
        print("[OK] required workshop outputs are consistent")
        return 0

    if args.demo:
        data = sample_data()
    elif args.input:
        data = json.loads(args.input.read_text(encoding="utf-8"))
    else:
        parser.error("provide --input or --demo")

    write_outputs(data, args.output_dir, args.stage)
    issues = validate_outputs(args.output_dir)
    if issues:
        for issue in issues:
            print(f"[ERROR] {issue}")
        return 1
    print(f"[OK] wrote workshop outputs to {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
