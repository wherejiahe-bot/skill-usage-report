#!/usr/bin/env python3
"""Scan WorkBuddy logs for a given date and generate skill-usage report."""
import json, os, re, sys
from collections import defaultdict
from datetime import datetime

BASE_DIR = os.path.expanduser("~/.workbuddy/")
REPORT_DIR = os.path.join(BASE_DIR, "skills/skill-usage-report") if os.path.isdir(os.path.join(BASE_DIR, "skills/skill-usage-report")) else os.path.join(os.path.dirname(os.path.abspath(__file__)), "skill-usage-report")

# Determine report directory
current_dir = os.path.dirname(os.path.abspath(__file__))
if "skill-usage-report" in current_dir.lower() or "skills" not in current_dir.lower():
    REPORT_DIR = current_dir
else:
    REPORT_DIR = current_dir

LOG_PATTERN = r"(\d{4}-\d{2}-\d{2})/"

def get_log_dir(date_str="2026-06-17"):
    log_path = os.path.join(BASE_DIR, f"logs/{date_str}/")
    return log_path if os.path.isdir(log_path) else None

def scan_logs(log_dir):
    tool_pattern = re.compile(r'toolName=(Bash|Read|Edit|Write|PowerShell|Grep|Glob|Skill|DeferExecuteTool|TaskOutput|automation_update|ToolSearch|TaskUpdate|TaskCreate|WebFetch|WebSearch|conversation_search|Agent|present_files|AskUserQuestion|TaskList|TaskStop)')
    skill_pattern = re.compile(r'Skill "([^"]+)"')
    tool_counts = defaultdict(int)
    skill_counts = defaultdict(int)

    for fname in os.listdir(log_dir):
        fpath = os.path.join(log_dir, fname)
        if not os.path.isfile(fpath):
            continue
        try:
            with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    tool_match = tool_pattern.search(line)
                    if tool_match:
                        tool_counts[tool_match.group(1)] += 1

                    skill_match = skill_pattern.search(line)
                    if skill_match:
                        skill_name = skill_match.group(1)
                        if skill_name:
                            skill_counts[skill_name] += 1
        except Exception as e:
            pass

    return dict(tool_counts), dict(skill_counts)

def generate_report():
    log_dir = get_log_dir("2026-06-17")
    if not log_dir:
        print("Log directory not found")
        sys.exit(1)

    tool_counts, skill_counts = scan_logs(log_dir)

    total_tools = sum(tool_counts.values())
    total_skills = sum(skill_counts.values())

    output = {
        "generated_at": datetime.now().isoformat(),
        "date": "2026-06-17",
        "total_tools": total_tools,
        "total_skills": total_skills,
        "tool_counts": tool_counts,
        "skill_counts": skill_counts
    }

    with open(os.path.join(REPORT_DIR, "daily_data.json"), "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"Generated: daily_data.json")
    print(f"Date: 2026-06-17 | Total Tools: {total_tools} | Total Skills: {total_skills}")
    print(f"Unique tools used: {len(tool_counts)}")
    print(f"Unique skills used: {len(skill_counts)}")
    if total_tools > 0:
        top_tool = max(tool_counts.items(), key=lambda x: x[1])
        print(f"Top tool: {top_tool[0]} ({top_tool[1]} calls)")
    if total_skills > 0:
        top_skill = max(skill_counts.items(), key=lambda x: x[1])
        print(f"Top skill: {top_skill[0]} ({top_skill[1]} calls)")

if __name__ == "__main__":
    generate_report()
