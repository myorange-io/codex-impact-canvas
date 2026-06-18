#!/usr/bin/env python3
"""JSON에서 일관된 Codex Impact Workshop 마크다운 산출물을 생성합니다."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
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
    raw_value = value.strip() or "case"
    slug = raw_value.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = slug.strip("-")
    if slug:
        return slug
    fallback = hashlib.sha1(raw_value.encode("utf-8")).hexdigest()[:8]
    return f"case-{fallback}"


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
    return frontmatter(meta) + f"""# {meta["project_name"]} 실행 계획

## 팀
- 사회혁신가: {pick(data, "team.social_innovator")}
- 개발자: {pick(data, "team.developer")}

## 문제
- 실제 업무 문제: {pick(data, "problem.actual_work_problem")}
- 가장 어려움을 겪는 사람: {pick(data, "problem.people_affected")}
- 문제가 발생하는 순간: {pick(data, "problem.blocked_moment")}

## 자료 확인
- 자료 상태: {pick(data, "materials.source_status", "미정")}
- 샘플 입력: {pick(data, "materials.sample_input", pick(data, "mvp.demo_input"))}
- 개인정보 처리: {pick(data, "materials.privacy_action", pick(data, "data_and_access.privacy_action"))}
- 자료 유효성 확인: {pick(data, "materials.validity_check", "3시간 안에 처리할 수 있고 공개 가능한 수준으로 비식별화했는지 확인한다.")}

## 현재 업무 흐름
- 입력 자료: {pick(data, "current_workflow.inputs")}
- 처리 순서: {pick(data, "current_workflow.steps")}
- 판단 기준: {pick(data, "current_workflow.judgment")}
- 현재 산출물: {pick(data, "current_workflow.outputs")}
- 현재 사용 도구: {pick(data, "current_workflow.tools")}

## 결과물 형태
- 문제 유형: {pick(data, "output_choice.problem_archetype", pick(data, "library_metadata.workflow_type"))}
- 선택한 결과물 형태: {pick(data, "output_choice.output_type", pick(data, "library_metadata.output_format"))}
- 선택 이유: {pick(data, "output_choice.selection_reason", "업무 문제와 3시간 데모 범위에 맞는 형태로 선택했다.")}

## 기대 변화
- 기대 변화: {pick(data, "expected_change.summary")}
- 관찰 가능한 개선: {pick(data, "expected_change.observable_improvement")}

## 3시간 MVP
- 핵심 기능 1개: {pick(data, "mvp.single_feature")}
- 데모 입력: {pick(data, "mvp.demo_input")}
- 데모 산출물: {pick(data, "mvp.demo_output")}
- AI 역할: {pick(data, "mvp.ai_role", pick(data, "library_metadata.agent_role"))}
- 사람 검토 지점: {pick(data, "mvp.human_review_point", pick(data, "human_in_the_loop.key_review_points", pick(data, "human_in_the_loop.review_points")))}
- 성공 기준: {pick(data, "mvp.success_criterion")}
- 실패 신호: {pick(data, "mvp.failure_signal", pick(data, "human_in_the_loop.error_types"))}

## 제외 범위
- 오늘 하지 않을 것: {pick(data, "scope.not_today", NA)}
- 다음 단계 아이디어: {pick(data, "scope.next_ideas", NA)}

## 3시간 구현 계획
- 0-30분: {pick(data, "build_plan.0_30")}
- 30-90분: {pick(data, "build_plan.30_90")}
- 90-150분: {pick(data, "build_plan.90_150")}
- 150-180분: {pick(data, "build_plan.150_180")}

## 빠르게 끝났을 때 이어서 할 작업 후보
- 후보 1 작업: {pick(data, "follow_up_candidates.candidate_1.task")}
- 후보 1 시작 조건: {pick(data, "follow_up_candidates.candidate_1.start_condition")}
- 후보 1 구현 내용: {pick(data, "follow_up_candidates.candidate_1.implementation")}
- 후보 1 데모 산출물: {pick(data, "follow_up_candidates.candidate_1.demo_output")}
- 후보 1 예상 추가 시간: {pick(data, "follow_up_candidates.candidate_1.timebox")}
- 후보 1 검수 기준: {pick(data, "follow_up_candidates.candidate_1.success_check")}
- 후보 2 작업: {pick(data, "follow_up_candidates.candidate_2.task")}
- 후보 2 시작 조건: {pick(data, "follow_up_candidates.candidate_2.start_condition")}
- 후보 2 구현 내용: {pick(data, "follow_up_candidates.candidate_2.implementation")}
- 후보 2 데모 산출물: {pick(data, "follow_up_candidates.candidate_2.demo_output")}
- 후보 2 예상 추가 시간: {pick(data, "follow_up_candidates.candidate_2.timebox")}
- 후보 2 검수 기준: {pick(data, "follow_up_candidates.candidate_2.success_check")}

## 제출과 아카이빙
- 문제정의 산출물: {pick(data, "submission.problem_definition_outputs", "PLAN.md, workshop.json 초안")}
- 구현 기록: {pick(data, "submission.build_records", "MEMORY.md")}
- 완료 후 산출물: {pick(data, "submission.final_outputs", "WORKFLOW_ANALYSIS.md, CASE_STUDY.md, 최종 workshop.json")}
- 아카이빙 기준: {pick(data, "submission.archive_criteria", "필수 산출물의 핵심 MVP, 자료 상태, 사람 검토, 공개 범위가 서로 일치해야 한다.")}
"""


def render_workflow(data: dict[str, Any], meta: dict[str, str]) -> str:
    return frontmatter(meta) + f"""# {meta["project_name"]} 워크플로 분석

## 라이브러리 메타데이터
- 사례 ID: {meta["case_id"]}
- 분야: {pick(data, "library_metadata.sector")}
- 업무 유형: {pick(data, "library_metadata.workflow_type")}
- 에이전트 역할: {pick(data, "library_metadata.agent_role")}
- 결과물 형태: {pick(data, "output_choice.output_type", pick(data, "library_metadata.output_format"))}
- 자료 상태: {pick(data, "materials.source_status")}
- 데이터 특성: {pick(data, "library_metadata.data_characteristics", pick(data, "current_workflow.inputs"))}
- 정형/비정형 여부: {pick(data, "library_metadata.data_type")}
- 개인정보 포함 여부: {pick(data, "library_metadata.privacy_included", pick(data, "library_metadata.privacy_level"))}
- 연결 수준: {pick(data, "library_metadata.integration_level")}
- MCP/CLI 연결 여부: {pick(data, "library_metadata.mcp_cli_connection", pick(data, "library_metadata.integration_level"))}
- 사람 검토: {pick(data, "library_metadata.human_review")}
- 재사용 가능성: {pick(data, "library_metadata.reuse_level")}
- 산출물 형식: {pick(data, "library_metadata.output_format")}

## 기존 업무 흐름
- 업무 시작 조건: {pick(data, "existing_workflow.workflow_trigger")}
- 데이터 수: {pick(data, "existing_workflow.data_count", pick(data, "existing_workflow.baseline_volume"))}
- 반복 빈도: {pick(data, "existing_workflow.repeat_frequency", pick(data, "existing_workflow.baseline_time"))}
- 기존 소요 시간: {pick(data, "existing_workflow.baseline_time")}
- 입력 데이터 출처: {pick(data, "existing_workflow.input_sources")}
- 기존 단계: {pick(data, "existing_workflow.current_steps")}
- 기존 산출물: {pick(data, "existing_workflow.current_outputs")}
- 불편한 지점: {pick(data, "existing_workflow.current_pain_points")}

## 자동화 대상
- 선정한 업무: {pick(data, "automation_target.selected_task")}
- 선정 이유: {pick(data, "automation_target.reason_for_selection")}
- 제외한 업무: {pick(data, "automation_target.excluded_tasks", NA)}

## AI 에이전트 설계
- 에이전트 입력 조건: {pick(data, "ai_agent_design.agent_input_contract")}
- 에이전트 산출물 조건: {pick(data, "ai_agent_design.agent_output_contract")}
- 판단 경계: {pick(data, "ai_agent_design.decision_boundary")}
- 사용 도구: {pick(data, "ai_agent_design.tools_used")}
- 바뀐 업무 흐름: {pick(data, "ai_agent_design.changed_workflow")}

## 사람 검토와 개입
- 주요 검수 포인트: {pick(data, "human_in_the_loop.key_review_points", pick(data, "human_in_the_loop.review_points"))}
- 실패 시 사람이 이어받는 방식: {pick(data, "human_in_the_loop.handoff_protocol")}
- 예상 오류 유형: {pick(data, "human_in_the_loop.error_types")}
- 평가 샘플: {pick(data, "human_in_the_loop.evaluation_samples")}

## 데이터와 접근
- 샘플 자료: {pick(data, "materials.sample_input", pick(data, "mvp.demo_input"))}
- 개인정보 처리: {pick(data, "data_and_access.privacy_action")}
- 권한/접근 이슈: {pick(data, "data_and_access.permission_issues", NA)}
- 결과물의 공유 가능 범위: {pick(data, "data_and_access.shareability")}

## 영향과 재사용
- 기존 대비 소요 시간 변화: {pick(data, "impact_and_reuse.expected_time_change")}
- 품질 변화: {pick(data, "impact_and_reuse.quality_change")}
- 재사용 방법: {pick(data, "impact_and_reuse.case_reuse_recipe")}
- 유지관리 주체: {pick(data, "impact_and_reuse.maintenance_owner")}
- 다음 개선: {pick(data, "impact_and_reuse.next_iteration")}
"""


def render_case_study(data: dict[str, Any], meta: dict[str, str]) -> str:
    title = pick(data, "case_study.title", meta["project_name"])
    return frontmatter(meta) + f"""# {title}

## 사례 메타데이터
- 사례 ID: {meta["case_id"]}
- 공개 범위: {pick(data, "data_and_access.shareability")}
- 분야: {pick(data, "library_metadata.sector")}
- 재사용 수준: {pick(data, "library_metadata.reuse_level")}

## 문제 요약
{pick(data, "case_study.problem_summary", pick(data, "problem.actual_work_problem"))}

## 기존 방식
{pick(data, "case_study.before", pick(data, "existing_workflow.current_steps"))}

## AI 에이전트 워크플로
{pick(data, "case_study.ai_agent_workflow", pick(data, "ai_agent_design.changed_workflow"))}

## 사람 검토
{pick(data, "case_study.human_review", pick(data, "human_in_the_loop.review_points"))}

## 사용 도구
{pick(data, "case_study.tools", pick(data, "ai_agent_design.tools_used"))}

## MVP 결과물
{pick(data, "case_study.mvp_result", pick(data, "mvp.demo_output"))}

## 성공 기준
{pick(data, "case_study.success_criterion", pick(data, "mvp.success_criterion"))}

## 배운 점
{pick(data, "case_study.lessons")}

## 재사용 가이드
{pick(data, "case_study.reuse_guide", pick(data, "impact_and_reuse.case_reuse_recipe"))}

## 익명화와 공개 제외
{pick(data, "case_study.redaction_notes", pick(data, "data_and_access.privacy_action"))}
"""


def memory_header(data: dict[str, Any], meta: dict[str, str]) -> str:
    return f"""# 만들기 기록 - {meta["project_name"]}

> 이 파일은 이 MVP를 어떤 과정으로 만들었는지 남기는 기록입니다.
> 나중에 복기하거나 사회혁신 AI 에이전트 워크플로 사례로 정리할 때 씁니다.

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
- **정한 것 / 한 것**: {pick(data, "memory_entry.did", "필수 산출물 구조와 3시간 MVP 범위를 정리했다.")}
- **왜**: {pick(data, "memory_entry.why", "팀별 결과물을 같은 구조로 남겨 이후 사례집과 워크플로 라이브러리로 재사용하기 위해서다.")}
- **어떻게**: {pick(data, "memory_entry.how", "반응형 질문 답변을 표준 필드로 정규화해 PLAN.md, workshop.json, WORKFLOW_ANALYSIS.md, CASE_STUDY.md, MEMORY.md에 기록했다.")}
- **막힌 점 / 바꾼 점**: {pick(data, "memory_entry.blocked", "없음")}
- **배운 것 / 다음**: {pick(data, "memory_entry.next", "샘플 데이터로 MVP를 구현하고 검수 포인트를 보완한다.")}
"""


def sample_data() -> dict[str, Any]:
    return {
        "team": {"name": "샘플팀", "social_innovator": "사회혁신가", "developer": "개발자"},
        "project": {"name": "샘플 임팩트 에이전트", "slug": "sample-impact-agent"},
        "problem": {
            "actual_work_problem": "신청서 내용을 사람이 반복해서 읽고 누락 여부를 확인한다.",
            "people_affected": "사업 담당자와 신청자",
            "blocked_moment": "신청 마감 직후 서류가 몰릴 때",
        },
        "materials": {
            "source_status": "익명화 샘플",
            "sample_input": "이름과 연락처를 제거한 신청서 텍스트 1개",
            "privacy_action": "이름과 연락처를 제거한 샘플만 사용",
            "validity_check": "신청서 필수 항목과 누락 여부를 확인할 최소 정보가 남아 있다.",
        },
        "output_choice": {
            "problem_archetype": "문서/콘텐츠 초안 또는 변환",
            "output_type": "문서/메시지 초안",
            "selection_reason": "담당자가 최종 발송 전에 검토할 누락 목록과 안내 초안을 바로 볼 수 있다.",
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
            "ai_role": "검토보조",
            "human_review_point": "담당자가 누락 항목과 안내 문구를 발송 전 최종 확인한다.",
            "success_criterion": "핵심 누락 3개 중 2개 이상을 찾고 사람이 수정 가능한 초안을 만든다.",
            "failure_signal": "필수 항목 누락을 놓치거나 개인정보가 출력에 남아 있으면 실패로 본다.",
        },
        "scope": {"not_today": "자동 이메일 발송", "next_ideas": "신청서 일괄 처리"},
        "build_plan": {
            "0_30": "샘플 입력과 출력 형식을 고정한다.",
            "30_90": "프롬프트와 처리 흐름을 만든다.",
            "90_150": "간단한 UI 또는 CLI 데모를 만든다.",
            "150_180": "샘플로 테스트하고 발표 흐름을 정리한다.",
        },
        "follow_up_candidates": {
            "candidate_1": {
                "task": "샘플 여러 건을 한 번에 처리하는 일괄 입력을 추가한다.",
                "start_condition": "핵심 기능 1개가 샘플 1건에서 통과하고 40분 이상 남았을 때",
                "implementation": "텍스트 구분자로 여러 입력을 나누고 같은 출력 형식으로 표를 만든다.",
                "demo_output": "샘플 3건의 누락 항목 요약표",
                "timebox": "40분",
                "success_check": "각 샘플마다 누락 항목과 안내 초안이 빠짐없이 나온다.",
            },
            "candidate_2": {
                "task": "담당자 검토 체크리스트를 산출물에 추가한다.",
                "start_condition": "핵심 기능 결과 형식이 안정되고 25분 이상 남았을 때",
                "implementation": "AI 산출물 끝에 사람이 확인할 체크박스와 수정 메모 칸을 붙인다.",
                "demo_output": "검토 체크리스트가 포함된 안내 초안",
                "timebox": "25분",
                "success_check": "담당자가 발송 전 확인해야 할 항목을 바로 볼 수 있다.",
            },
        },
        "submission": {
            "problem_definition_outputs": "PLAN.md, workshop.json 초안",
            "build_records": "MEMORY.md append 기록",
            "final_outputs": "WORKFLOW_ANALYSIS.md, CASE_STUDY.md, 최종 workshop.json",
            "archive_criteria": "자료 상태, 핵심 MVP, 사람 검토, 공개 범위가 모든 산출물에서 일치해야 한다.",
        },
        "library_metadata": {
            "sector": "운영",
            "workflow_type": "신청서검토",
            "agent_role": "검토보조",
            "data_characteristics": "신청서 PDF에서 추출한 텍스트와 필수 항목 목록",
            "data_type": "비정형",
            "privacy_included": "개인정보 포함 가능. 샘플은 익명화 필요",
            "privacy_level": "익명화 필요",
            "integration_level": "수동 업로드",
            "mcp_cli_connection": "MCP/CLI 연결 없음. 수동 업로드로 처리",
            "human_review": "최종 검토",
            "reuse_level": "템플릿 재사용 가능",
            "output_format": "md",
        },
        "existing_workflow": {
            "workflow_trigger": "신청서 접수",
            "baseline_volume": "한 번에 10-30건",
            "data_count": "데모 1건, 실제 업무 한 번에 10-30건",
            "repeat_frequency": "신청 접수 기간마다 반복",
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
            "key_review_points": "누락 항목이 실제 필수 항목인지, 안내 문구가 과도하지 않은지 확인",
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
            "title": "신청서 누락 검토 AI 에이전트",
            "lessons": "3시간 MVP는 자동 발송보다 검토 초안 생성에 집중할 때 완성도가 높았다.",
        },
    }


def write_outputs(data: dict[str, Any], output_dir: Path, stage: str) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    meta = metadata(data)
    normalized_data = dict(data)
    normalized_data["generated_metadata"] = meta
    (output_dir / "workshop.json").write_text(
        json.dumps(normalized_data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
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
    entry = memory_entry(data, stage).rstrip() + "\n"
    existing_memory = memory_path.read_text(encoding="utf-8")
    if entry not in existing_memory:
        with memory_path.open("a", encoding="utf-8") as handle:
            handle.write(entry)


def read_output(output_dir: Path, name: str) -> str:
    path = output_dir / name
    return path.read_text(encoding="utf-8") if path.exists() else ""


def extract_field(content: str, label: str) -> str:
    match = re.search(rf"^- {re.escape(label)}:\s*(.*)$", content, re.MULTILINE)
    return match.group(1).strip() if match else ""


def is_quality_missing(value: str) -> bool:
    normalized = value.strip()
    return normalized in {"", UNKNOWN, NA, "검토 필요"}


def looks_like_multiple_mvp(value: str) -> bool:
    if is_quality_missing(value):
        return False
    numbered_markers = re.findall(r"(?:^|\s)(?:[0-9]+\.|제안\s*[0-9]+|첫째|둘째|셋째)", value)
    if len(numbered_markers) >= 2:
        return True
    if value.count(",") >= 2 or value.count("、") >= 2:
        return True
    return bool(re.search(r"(동시에|그리고)\s+.*(하고|만들고|구축)", value))


def validate_quality_warnings(output_dir: Path) -> list[str]:
    warnings: list[str] = []
    plan = read_output(output_dir, "PLAN.md")
    workflow = read_output(output_dir, "WORKFLOW_ANALYSIS.md")
    case = read_output(output_dir, "CASE_STUDY.md")

    mvp_feature = extract_field(plan, "핵심 기능 1개")
    if is_quality_missing(mvp_feature):
        warnings.append("PLAN.md의 핵심 기능 1개가 아직 구체화되지 않았습니다")
    elif looks_like_multiple_mvp(mvp_feature):
        warnings.append("PLAN.md의 핵심 기능 1개가 여러 기능이나 시스템 범위를 포함할 수 있습니다")

    for label in ["데모 입력", "데모 산출물", "성공 기준"]:
        if is_quality_missing(extract_field(plan, label)):
            warnings.append(f"PLAN.md의 {label}이 샘플 기준으로 구체화되지 않았습니다")

    for label in ["자료 상태", "선택한 결과물 형태", "사람 검토 지점", "실패 신호"]:
        if is_quality_missing(extract_field(plan, label)):
            warnings.append(f"PLAN.md의 {label}이 비어 있거나 검토가 필요합니다")

    for label in ["주요 검수 포인트", "실패 시 사람이 이어받는 방식", "개인정보 처리", "결과물의 공유 가능 범위"]:
        if is_quality_missing(extract_field(workflow, label)):
            warnings.append(f"WORKFLOW_ANALYSIS.md의 {label} 필드가 비어 있거나 검토가 필요합니다")

    sensitive_patterns = [
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        r"\b\d{2,3}-\d{3,4}-\d{4}\b",
        r"(주민등록번호|계좌번호|비밀번호|패스워드|토큰|api\s*key|secret|원본 데이터|내부 문서 원문|접근 방법)",
    ]
    for pattern in sensitive_patterns:
        if re.search(pattern, case, re.IGNORECASE):
            warnings.append("CASE_STUDY.md에 공개 제외가 필요한 개인정보/비밀/원문 표현이 있을 수 있습니다")
            break

    return warnings


def validate_outputs(output_dir: Path) -> list[str]:
    issues: list[str] = []
    for name in ["PLAN.md", "MEMORY.md", "WORKFLOW_ANALYSIS.md", "CASE_STUDY.md"]:
        if not (output_dir / name).exists():
            issues.append(f"필수 파일이 없습니다: {name}")
    workshop_json = output_dir / "workshop.json"
    if not workshop_json.exists():
        issues.append("필수 파일이 없습니다: workshop.json")
    else:
        try:
            json.loads(workshop_json.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            issues.append(f"workshop.json을 JSON으로 읽을 수 없습니다: {error}")
    plan = read_output(output_dir, "PLAN.md")
    if "## 3시간 MVP" not in plan:
        issues.append("PLAN.md에 ## 3시간 MVP 섹션이 없습니다")
    for field in [
        "## 자료 확인",
        "자료 상태",
        "샘플 입력",
        "개인정보 처리",
        "자료 유효성 확인",
        "## 결과물 형태",
        "문제 유형",
        "선택한 결과물 형태",
        "선택 이유",
        "## 빠르게 끝났을 때 이어서 할 작업 후보",
        "AI 역할",
        "사람 검토 지점",
        "실패 신호",
        "후보 1 작업",
        "후보 1 시작 조건",
        "후보 1 구현 내용",
        "후보 1 데모 산출물",
        "후보 1 예상 추가 시간",
        "후보 1 검수 기준",
        "후보 2 작업",
        "후보 2 시작 조건",
        "후보 2 구현 내용",
        "후보 2 데모 산출물",
        "후보 2 예상 추가 시간",
        "후보 2 검수 기준",
        "## 제출과 아카이빙",
        "문제정의 산출물",
        "구현 기록",
        "완료 후 산출물",
        "아카이빙 기준",
    ]:
        if field not in plan:
            issues.append(f"PLAN.md에 {field} 필드가 없습니다")
    workflow = read_output(output_dir, "WORKFLOW_ANALYSIS.md")
    for field in [
        "사례 ID",
        "결과물 형태",
        "자료 상태",
        "데이터 특성",
        "정형/비정형 여부",
        "데이터 수",
        "개인정보 포함 여부",
        "MCP/CLI 연결 여부",
        "입력 데이터 출처",
        "산출물 형식",
        "반복 빈도",
        "기존 대비 소요 시간 변화",
        "주요 검수 포인트",
        "권한/접근 이슈",
        "재사용 가능성",
        "실패 시 사람이 이어받는 방식",
        "결과물의 공유 가능 범위",
        "에이전트 입력 조건",
        "샘플 자료",
        "재사용 방법",
    ]:
        if field not in workflow:
            issues.append(f"WORKFLOW_ANALYSIS.md에 {field} 필드가 없습니다")
    case = read_output(output_dir, "CASE_STUDY.md")
    for heading in ["## 문제 요약", "## AI 에이전트 워크플로", "## 익명화와 공개 제외"]:
        if heading not in case:
            issues.append(f"CASE_STUDY.md에 {heading} 섹션이 없습니다")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, help="정규화한 워크숍 답변 JSON 파일")
    parser.add_argument("--output-dir", type=Path, default=Path("."), help="마크다운 산출물을 쓸 디렉터리")
    parser.add_argument("--demo", action="store_true", help="내장 샘플 데이터로 산출물을 생성합니다")
    parser.add_argument("--stage", default="문제 정의", help="MEMORY.md에 추가할 단계 이름")
    parser.add_argument("--validate-only", action="store_true", help="기존 산출물 검증만 실행합니다")
    args = parser.parse_args()

    if args.validate_only:
        issues = validate_outputs(args.output_dir)
        warnings = validate_quality_warnings(args.output_dir)
        if issues:
            for issue in issues:
                print(f"[오류] {issue}")
            return 1
        for warning in warnings:
            print(f"[경고] {warning}")
        print("[완료] 필수 워크숍 산출물 구조가 일관됩니다")
        return 0

    if args.demo:
        data = sample_data()
    elif args.input:
        data = json.loads(args.input.read_text(encoding="utf-8"))
    else:
        parser.error("--input 또는 --demo를 제공하세요")

    write_outputs(data, args.output_dir, args.stage)
    issues = validate_outputs(args.output_dir)
    warnings = validate_quality_warnings(args.output_dir)
    if issues:
        for issue in issues:
            print(f"[오류] {issue}")
        return 1
    for warning in warnings:
        print(f"[경고] {warning}")
    print(f"[완료] 워크숍 산출물을 생성했습니다: {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
