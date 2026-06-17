#!/usr/bin/env python3
"""Scan WorkBuddy logs for 2026-06-17 and generate skill-usage report."""
import json, os, re
from collections import defaultdict
from datetime import datetime

LOG_DIR = os.path.expanduser("~/.workbuddy/logs/2026-06-17/")
OUT_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "daily_data.json")
OUT_JS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.js")
EXISTING_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "skill-usage-data.json")

TOOL_NAMES = [
    "Bash", "Read", "Edit", "Write", "PowerShell", "Grep", "Glob",
    "Skill", "DeferExecuteTool", "TaskOutput", "automation_update",
    "ToolSearch", "TaskUpdate", "TaskCreate", "WebFetch", "WebSearch",
    "conversation_search", "Agent", "present_files",
    "AskUserQuestion", "TaskList", "TaskStop", "Skill,",
]

STATUS_MAP = {
    "lobster-mem0": "经常使用",
    "wechat-clawbot-notify": "经常使用",
    "daily-wechat-reminder": "经常使用",
    "lobster-comm": "经常使用",
    "skill-manage": "建议保留",
    "browserharness": "建议保留",
    "skill-usage-updater": "建议保留",
    "qq-mail": "建议保留",
    "karpathy-guidelines": "建议保留",
    "uumit-auto-apply": "建议保留",
    "amruta-daily-push": "建议保留",
    "translate": "建议保留",
    "glass-project-report": "建议保留",
    "writing-plans": "建议保留",
    "headroom": "建议保留",
    "ppvi": "建议保留",
    "long-task-detach": "建议保留",
    "brainstorming": "建议保留",
    "subagent-driven-development": "建议保留",
    "sahaja-rag-to-ima": "建议保留",
    "uma_understand_dashboard": "建议保留",
    "execution_planning": "建议保留",
    "using_superpowers": "建议保留",
    "verification_before_completion": "建议保留",
    "using_git_worktrees": "建议保留",
    "tdd": "建议保留",
    "test_driven_development": "建议保留",
    "using_supperpowers": "建议保留",
    "executing_plans": "建议保留",
    "finishing_a_development_branch": "建议保留",
    "receiving_code_review": "建议保留",
    "requesting_code_review": "建议保留",
    "subagent_driven_development": "建议保留",
    "sahaja_x_evaluation": "建议保留",
    "esther_design_system": "建议保留",
    "brainstorming": "建议保留",
    "ima_skills": "建议保留",
    "marketplace_skill_installer": "建议保留",
    "money_init": "建议保留",
    "money_find": "建议保留",
    "money_verify": "建议保留",
    "money_plan": "建议保留",
    "astro_consult_framework": "建议保留",
    "国内旅行聚合查询": "建议保留",
    "web_deploy_github": "建议保留",
    "skill_creator": "建议保留",
    "mem0_setup": "建议保留",
    "scan_new_projects": "建议保留",
}

SOURCE_MAP = {
    "lobster-mem0": "builtin",
    "wechat-clawbot-notify": "builtin",
    "daily-wechat-reminder": "builtin",
    "lobster-comm": "self-made",
    "skill-manage": "builtin",
    "browserharness": "builtin",
    "skill-usage-updater": "builtin",
    "qq-mail": "connector",
    "karpathy-guidelines": "builtin",
    "uumit-auto-apply": "builtin",
    "amruta-daily-push": "builtin",
    "translate": "builtin",
    "glass-project-report": "builtin",
    "writing-plans": "builtin",
    "headroom": "builtin",
    "ppvi": "builtin",
    "long-task-detach": "builtin",
    "brainstorming": "builtin",
    "subagent-driven-development": "builtin",
    "sahaja-rag-to-ima": "builtin",
}

def main():
    if not os.path.exists(LOG_DIR):
        print(f"Log dir not found: {LOG_DIR}")
        return

    daily = {"date": "2026-06-17", "total_tools": 0, "total_skills": 0, "unique_tools": 0}
    tool_counts = defaultdict(int)
    skill_counts = defaultdict(int)

    # Scan tool calls
    for fname in os.listdir(LOG_DIR):
        fpath = os.path.join(LOG_DIR, fname)
        if not os.path.isfile(fpath):
            continue
        try:
            with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    # Count tools
                    for tool in TOOL_NAMES:
                        pattern = f'toolName={tool}\\b|toolName="{tool}"|tool={tool}\\b|tool="{tool}"|tool={tool},|tool="{tool},"'
                        matches = re.findall(pattern, line)
                        if matches:
                            tool_counts[tool] += len(matches)

                    # Count Skill invocations
                    skill_match = re.search(r'Skill "([^"]+)"', line)
                    if skill_match:
                        skill_name = skill_match.group(1)
                        if skill_name and skill_name != "(none)":
                            skill_counts[skill_name] += 1
        except Exception as e:
            print(f"Error reading {fname}: {e}")

    total_tools = sum(tool_counts.values())
    total_skills = sum(skill_counts.values())
    unique_tools = len(tool_counts)

    daily["total_tools"] = total_tools
    daily["total_skills"] = total_skills
    daily["unique_tools"] = unique_tools

    # Load existing data to append
    existing_json = None
    if os.path.exists(OUT_JSON):
        with open(OUT_JSON, "r") as f:
            existing_json = json.load(f)

    all_daily = []
    total_old_tools = 0
    total_old_skills = 0
    unique_old_tools = 0
    unique_old_skills = 0

    if existing_json and isinstance(existing_json, dict) and "daily" in existing_json:
        all_daily = existing_json["daily"]
        total_old_tools = existing_json.get("summary", {}).get("total_tool_calls", 0)
        total_old_skills = existing_json.get("summary", {}).get("total_skill_calls", 0)
        unique_old_tools = existing_json.get("summary", {}).get("unique_tools_used", 0)
        unique_old_skills = existing_json.get("summary", {}).get("unique_skills_used", 0)
        # Append new date if not already present
        if not any(d["date"] == "2026-06-17" for d in all_daily):
            all_daily.append(daily)
    elif existing_json and isinstance(existing_json, list):
        # Old format: skill-usage-data.json is a list of skill entries
        # Still need daily_data.json for daily records
        print("Existing JSON is in old format (list). Starting fresh.")
    else:
        all_daily = [daily]

    all_top_tools = sorted(tool_counts.items(), key=lambda x: -x[1])[:50]
    top_tools = [{"rank": i+1, "name": name, "count": cnt} for i, (name, cnt) in enumerate(all_top_tools)]

    all_skill_usage = []
    for name, cnt in sorted(skill_counts.items(), key=lambda x: -x[1]):
        entry = {
            "rank": len(all_skill_usage)+1,
            "name": name,
            "total_calls": cnt,
        }
        all_skill_usage.append(entry)

    output = {
        "generated_at": datetime.now().isoformat(),
        "date_range": existing_json.get("date_range", ["2026-06-07", "2026-06-17"]) if isinstance(existing_json, dict) else ["2026-06-07", "2026-06-17"],
        "total_skills_registered": existing_json.get("total_skills_registered", 47) if isinstance(existing_json, dict) else 47,
        "total_archived_skills": existing_json.get("total_archived_skills", 60) if isinstance(existing_json, dict) else 60,
        "daily": all_daily,
        "top_tools": top_tools,
        "skill_usage": all_skill_usage,
        "summary": {
            "total_days": len(all_daily),
            "total_tool_calls": total_old_tools + total_tools,
            "total_skill_calls": total_old_skills + total_skills,
            "unique_tools_used": unique_old_tools + len(tool_counts),
            "unique_skills_used": unique_old_skills + len(skill_counts),
        }
    }

    with open(OUT_JSON, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"Generated: {OUT_JSON}")
    print(f"Date: 2026-06-17 | Tools: {total_tools} | Skills: {total_skills} | Unique tools: {unique_tools}")
    if top_tools:
        print(f"Top tool: {top_tools[0]['name']} ({top_tools[0]['count']} calls)")
    if all_skill_usage:
        print(f"Top skill: {all_skill_usage[0]['name']} ({all_skill_usage[0]['total_calls']} calls)")

if __name__ == "__main__":
    main()
