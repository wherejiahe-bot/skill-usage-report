#!/usr/bin/env python3
"""Scan WorkBuddy logs for all dates and generate cumulative skill-usage report."""
import json, os, re, sys
from collections import defaultdict
from datetime import datetime, date

BASE_DIR = os.path.expanduser("~/.workbuddy/")
REPORT_DIR = os.path.dirname(os.path.abspath(__file__))

TOOL_PATTERN = re.compile(
    r'toolName=(Bash|Read|Edit|Write|PowerShell|Grep|Glob|Skill|'
    r'DeferExecuteTool|TaskOutput|automation_update|ToolSearch|'
    r'TaskUpdate|TaskCreate|WebFetch|WebSearch|conversation_search|'
    r'Agent|present_files|AskUserQuestion|TaskList|TaskStop)'
)
SKILL_PATTERN = re.compile(r'Skill "([^"]+)"')


# ── SOURCE_MAP: skill_name → source category ──
SOURCE_MAP = {
    # 自制技能
    "100-days-spirit-huangting": "self-made",
    "add-project-to-evaluation": "self-made",
    "amruta-daily-push": "self-made",
    "amruta-fix-loop": "self-made",
    "api-integration-debug": "self-made",
    "brainstorming": "self-made",
    "browserharness": "self-made",
    "daily-task-reminder": "self-made",
    "daily-wechat-reminder": "self-made",
    "dispatching-parallel-agents": "self-made",
    "esther-design-system": "self-made",
    "executing-plans": "self-made",
    "finishing-a-development-branch": "self-made",
    "flowsint": "self-made",
    "flowsint-enricher-builder": "self-made",
    "hallmark": "self-made",
    "karpathy-guidelines": "self-made",
    "kb-deep-search": "self-made",
    "long-task-detach": "self-made",
    "money-find": "self-made",
    "money-init": "self-made",
    "money-plan": "self-made",
    "money-retro": "self-made",
    "money-status": "self-made",
    "money-verify": "self-made",
    "ponytail": "self-made",
    "ppvi": "self-made",
    "push-amruta-devlog": "self-made",
    "receiving-code-review": "self-made",
    "requesting-code-review": "self-made",
    "sahaja-rag-to-ima": "self-made",
    "sahaja-x-evaluation": "self-made",
    "scan-new-projects": "self-made",
    "skill-manage": "self-made",
    "skill-reminder": "self-made",
    "speed-testing-fix": "self-made",
    "subagent-driven-development": "self-made",
    "systematic-debugging": "self-made",
    "tdd": "self-made",
    "test-driven-development": "self-made",
    "using-git-worktrees": "self-made",
    "using-superpowers": "self-made",
    "uumit-agent": "self-made",
    "uumit-auto-apply": "self-made",
    "uumit-create-products": "self-made",
    "uumit-static-json-api": "self-made",
    "verification-before-completion": "self-made",
    "wechat-clawbot-notify": "self-made",
    "workbuddy-available-models": "self-made",
    "writing-plans": "self-made",
    "writing-skills": "self-made",
    # GitHub / 市场来源
    "cheat-on-money": "github",
    "lobster-comm": "github",
    "nvidia_key_full_collector": "self-made",
    "nvidia_key_incremental_runner": "self-made",
    # 内置技能
    "cloudstudio-deploy": "builtin",
    "expert-manager": "builtin",
    "marketplace-skill-installer": "builtin",
    "skill-creator": "builtin",
    "多模态内容生成": "builtin",
    # 连接器技能
    "github": "connector",
}

# ── STATUS_MAP: skill_name → status ──
STATUS_MAP = {
    # 经常使用
    "amruta-daily-push": "经常使用",
    "amruta-fix-loop": "经常使用",
    "brainstorming": "经常使用",
    "browserharness": "经常使用",
    "daily-task-reminder": "经常使用",
    "daily-wechat-reminder": "经常使用",
    "dispatching-parallel-agents": "经常使用",
    "executing-plans": "经常使用",
    "finishing-a-development-branch": "经常使用",
    "hallmark": "经常使用",
    "karpathy-guidelines": "经常使用",
    "kb-deep-search": "经常使用",
    "long-task-detach": "经常使用",
    "ponytail": "经常使用",
    "receiving-code-review": "经常使用",
    "requesting-code-review": "经常使用",
    "sahaja-rag-to-ima": "经常使用",
    "sahaja-x-evaluation": "经常使用",
    "scan-new-projects": "经常使用",
    "skill-manage": "经常使用",
    "skill-reminder": "经常使用",
    "speed-testing-fix": "经常使用",
    "subagent-driven-development": "经常使用",
    "systematic-debugging": "经常使用",
    "tdd": "经常使用",
    "test-driven-development": "经常使用",
    "using-git-worktrees": "经常使用",
    "using-superpowers": "经常使用",
    "verification-before-completion": "经常使用",
    "wechat-clawbot-notify": "经常使用",
    "writing-plans": "经常使用",
    "writing-skills": "经常使用",
    "uumit-agent": "经常使用",
    "uumit-auto-apply": "经常使用",
    "uumit-create-products": "经常使用",
    "uumit-static-json-api": "经常使用",
    # 建议保留
    "100-days-spirit-huangting": "建议保留",
    "add-project-to-evaluation": "建议保留",
    "api-integration-debug": "建议保留",
    "esther-design-system": "建议保留",
    "flowsint": "建议保留",
    "flowsint-enricher-builder": "建议保留",
    "money-find": "建议保留",
    "money-init": "建议保留",
    "money-plan": "建议保留",
    "money-retro": "建议保留",
    "money-status": "建议保留",
    "money-verify": "建议保留",
    "ppvi": "建议保留",
    "push-amruta-devlog": "建议保留",
    "workbuddy-available-models": "建议保留",
    # 内置/连接器
    "cloudstudio-deploy": "建议保留",
    "expert-manager": "建议保留",
    "marketplace-skill-installer": "建议保留",
    "skill-creator": "建议保留",
    "多模态内容生成": "建议保留",
    "github": "建议保留",
    # 已删除/已合并
    "cheat-on-money": "已合并",
    "lobster-comm": "已删除",
    "nvidia_key_full_collector": "已删除",
    "nvidia_key_incremental_runner": "已删除",
}

SKILL_DESC = {
    "amruta-daily-push": "每日 Amruta 文章推送流水线",
    "browserharness": "浏览器 CDP 自动化控制",
    "daily-wechat-reminder": "每日微信节拍器提醒",
    "sahaja-rag-to-ima": "霎哈嘉 RAG 搜索推送 IMA",
    "kb-deep-search": "本地知识库深度语义检索",
    "systematic-debugging": "系统化 Bug 排查根因",
    "skill-manage": "Skill 列表/创建/删除管理",
    "skill-reminder": "提示当前对话可用 Skill",
    "writing-plans": "多步任务执行方案编写",
    "writing-skills": "WorkBuddy Skill 创建编辑",
    "using-superpowers": "在所有对话中先加载技能",
    "hallmark": "反 AI 味前端设计规范",
    "karpathy-guidelines": "LLM 编码行为准则",
    "ponytail": "最懒但可行的解决方案",
    "tdd": "测试驱动开发红绿重构",
    "subagent-driven-development": "Subagent 隔离执行开发",
    "verification-before-completion": "任务完成前最终验证",
    "scan-new-projects": "扫描新项目并评估优先级",
    "sahaja-x-evaluation": "霎哈嘉+X 项目评估矩阵",
    "long-task-detach": "长任务沙箱脱离超时执行",
    "dispatching-parallel-agents": "并行任务分发执行",
    "executing-plans": "执行已完成的实现方案",
    "finishing-a-development-branch": "完成开发分支并合入",
    "receiving-code-review": "接收代码审查反馈",
    "requesting-code-review": "请求代码审查",
    "wechat-clawbot-notify": "ClawBot 微信消息推送",
    "brainstorming": "创意探索和方案设计",
    "browserharness": "浏览器 CDP 自动化控制",
    "speed-testing-fix": "修复 llm-retry-guard 测速逻辑",
    "api-integration-debug": "调试外部 API 集成问题",
    "100-days-spirit-huangting": "100 天神意照黄庭打卡",
    "add-project-to-evaluation": "霎哈嘉+X 评估添加项目",
    "amruta-fix-loop": "自动化循环修复 amruta-actions 问题",
    "using-git-worktrees": "使用 Git Worktrees 隔离开发",
    "daily-task-reminder": "管理今日任务清单",
    "esther-design-system": "不二个人 IP 设计系统",
    "flowsint": "OSINT 可视化关系图谱",
    "flowsint-enricher-builder": "Flowsint 富化器构建指南",
    "ppvi": "拼拼视觉美学设计体系",
    "push-amruta-devlog": "推送 Amruta 开发日志",
    "workbuddy-available-models": "查看可用模型列表",
    "money-find": "需求反推法找副业机会",
    "money-init": "cheat-on-money 首次配置",
    "money-plan": "副业执行方案生成",
    "money-retro": "副业复盘和经验沉淀",
    "money-status": "cheat-on-money 状态看板",
    "money-verify": "副业反诈 rubric 打分",
    "cheat-on-money": "副业机会探索套件（已合并为子技能）",
    "lobster-comm": "龙虾通信工具（已删除）",
    "cloudstudio-deploy": "部署静态站点到 CloudStudio",
    "expert-manager": "专家包生命周期管理",
    "marketplace-skill-installer": "市场 Skill 一键安装",
    "skill-creator": "创建有效的 WorkBuddy Skill",
    "多模态内容生成": "文生视频/3D 模型",
    "github": "GitHub 连接器",
    "uumit-agent": "UUMit 智能接单代理",
    "uumit-auto-apply": "UUMit 自动接任务+巡航",
    "uumit-create-products": "UUMit 批量创建知识商品",
    "uumit-static-json-api": "UUMit 静态 JSON 数据接口",
    "nvidia_key_full_collector": "NVIDIA 密钥收集（已删除）",
    "nvidia_key_incremental_runner": "NVIDIA 增量收集（已删除）",
}


def scan_date_log(date_str):
    """Scan logs for a single date. Returns (tool_counts, skill_counts)."""
    log_dir = os.path.join(BASE_DIR, f"logs/{date_str}/")
    if not os.path.isdir(log_dir):
        return None, None

    tool_counts = defaultdict(int)
    skill_counts = defaultdict(int)

    for fname in os.listdir(log_dir):
        fpath = os.path.join(log_dir, fname)
        if not os.path.isfile(fpath):
            continue
        try:
            with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    m = TOOL_PATTERN.search(line)
                    if m:
                        tool_counts[m.group(1)] += 1
                    m2 = SKILL_PATTERN.search(line)
                    if m2:
                        name = m2.group(1)
                        if name:
                            skill_counts[name] += 1
        except Exception:
            pass

    return dict(tool_counts), dict(skill_counts)


def generate_report():
    # Find all available log date dirs
    logs_root = os.path.join(BASE_DIR, "logs")
    all_dirs = sorted(
        d for d in os.listdir(logs_root)
        if os.path.isdir(os.path.join(logs_root, d)) and re.match(r"^\d{4}-\d{2}-\d{2}$", d)
    )
    if not all_dirs:
        print("No log date directories found")
        sys.exit(1)

    print(f"Found {len(all_dirs)} log date directories: {all_dirs[0]} to {all_dirs[-1]}")

    # Scan each date
    daily_tool_counts = {}  # date → {tool: count}
    daily_skill_counts = {}  # date → {skill: count}
    daily_totals = {}       # date → total_tools
    all_skills_seen = set()

    for d in all_dirs:
        tc, sc = scan_date_log(d)
        if tc is None:
            continue
        daily_tool_counts[d] = tc
        daily_skill_counts[d] = sc
        daily_totals[d] = sum(tc.values())
        all_skills_seen.update(sc.keys())
        print(f"  {d}: {daily_totals[d]} tools, {len(sc)} skills")

    # Build cumulative arrays for data.js
    date_labels = sorted(daily_totals.keys())
    total_daily = [daily_totals[d] for d in date_labels]
    total_cumulative = []
    running = 0
    for v in total_daily:
        running += v
        total_cumulative.append(running)

    # Build cumulative skill counts (across all dates)
    cum_skill = defaultdict(int)
    for d in date_labels:
        sc = daily_skill_counts.get(d, {})
        for skill, cnt in sc.items():
            cum_skill[skill] += cnt

    # Build skill daily arrays for DATA_SKILLS
    skill_objects = []
    # Normalize skill names for matching
    source_keys = {k.lower(): k for k in SOURCE_MAP}
    status_keys = {k.lower(): k for k in STATUS_MAP}
    desc_keys = {k.lower(): k for k in SKILL_DESC}

    for skill_name in sorted(all_skills_seen):
        key = skill_name.lower()
        src = SOURCE_MAP.get(skill_name, source_keys.get(key, "self-made"))
        st = STATUS_MAP.get(skill_name, status_keys.get(key, "建议保留"))
        desc = SKILL_DESC.get(skill_name, desc_keys.get(key, ""))
        total_calls = sum(daily_skill_counts.get(d, {}).get(skill_name, 0) for d in date_labels)
        # per-day array
        da = [daily_skill_counts.get(d, {}).get(skill_name, 0) for d in date_labels]
        skill_objects.append({
            "n": skill_name,
            "t": total_calls,
            "s": src,
            "st": st,
            "d": desc,
            "da": da,
        })

    # Add skills that were never called (in STATUS_MAP but not in logs)
    for skill_name, st in STATUS_MAP.items():
        if skill_name not in all_skills_seen:
            key = skill_name.lower()
            src = SOURCE_MAP.get(skill_name, source_keys.get(key, "self-made"))
            desc = SKILL_DESC.get(skill_name, desc_keys.get(key, ""))
            da = [0] * len(date_labels)
            skill_objects.append({
                "n": skill_name,
                "t": 0,
                "s": src,
                "st": st,
                "d": desc,
                "da": da,
            })

    # ── Build top_tools ranking ──
    cum_tool = defaultdict(int)
    for d in date_labels:
        tc = daily_tool_counts.get(d, {})
        for tool, cnt in tc.items():
            cum_tool[tool] += cnt
    sorted_tools = sorted(cum_tool.items(), key=lambda x: -x[1])
    top_tools = [{"rank": i + 1, "name": n, "count": c} for i, (n, c) in enumerate(sorted_tools)]

    now_iso = datetime.now().isoformat()
    last_date = date_labels[-1]

    # ── Write daily_data.json (cumulative) ──
    daily_json = {
        "generated_at": now_iso,
        "date_range": [date_labels[0], last_date],
        "total_skills_registered": len(SOURCE_MAP),
        "total_archived_skills": len(STATUS_MAP),
        "daily": [
            {
                "date": d,
                "total_tools": daily_totals[d],
                "total_skills": len(daily_skill_counts.get(d, {})),
                "unique_tools": len(daily_tool_counts.get(d, {})),
            }
            for d in date_labels
        ],
        "top_tools": top_tools[:20],
    }
    with open(os.path.join(REPORT_DIR, "daily_data.json"), "w", encoding="utf-8") as f:
        json.dump(daily_json, f, indent=2, ensure_ascii=False)

    # ── Write data.js ──
    labels_json = json.dumps(date_labels)
    daily_json_arr = json.dumps(total_daily)
    cum_json_arr = json.dumps(total_cumulative)
    skills_json = json.dumps(skill_objects, ensure_ascii=False)
    tools_json = json.dumps(top_tools)

    js_content = f"""// skill-usage-report/data.js
// Generated: {now_iso}
// {len(date_labels)} days | Tools: {total_cumulative[-1]} | Skills: {len(all_skills_seen)}

const daily_data = {json.dumps(daily_json, indent=2, ensure_ascii=False)};

// Display-friendly arrays
// === index.html 需要的变量名 ===
const DATA_DATE_LABELS = {labels_json};
const DATA_DATE_FULL = [...DATA_DATE_LABELS];
const DATA_TOTAL_DAILY = {daily_json_arr};
const DATA_TOTAL_CUMULATIVE = {cum_json_arr};

// 技能数据
const DATA_SKILLS = {skills_json};

// 工具数据
const TOOLS_DATA = {tools_json};
"""
    with open(os.path.join(REPORT_DIR, "data.js"), "w", encoding="utf-8") as f:
        f.write(js_content)

    # ── Summary ──
    print(f"\n=== Summary ===")
    print(f"Dates scanned: {date_labels[0]} → {last_date} ({len(date_labels)} days)")
    print(f"Total tool calls: {total_cumulative[-1]}")
    print(f"Total unique tools: {len(cum_tool)}")
    print(f"Total unique skills seen in logs: {len(all_skills_seen)}")
    print(f"Skills registered (SOURCE_MAP): {len(SOURCE_MAP)}")
    print(f"Skills archived (STATUS_MAP): {len(STATUS_MAP)}")
    print(f"Today ({last_date}): {daily_totals.get(last_date, 0)} tool calls")
    if sorted_tools:
        print(f"Top tool: {sorted_tools[0][0]} ({sorted_tools[0][1]} calls)")
    print(f"Files: daily_data.json, data.js")
    print(f"Output: {REPORT_DIR}")


if __name__ == "__main__":
    generate_report()
