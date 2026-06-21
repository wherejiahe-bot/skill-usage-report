// skill-usage-report/data.js
// Generated: 2026-06-21T22:02:25.478678
// 10 days | Tools: 20970 | Skills: 56

const daily_data = {
  "generated_at": "2026-06-21T22:02:25.478678",
  "date_range": [
    "2026-06-12",
    "2026-06-21"
  ],
  "total_skills_registered": 61,
  "total_archived_skills": 61,
  "daily": [
    {
      "date": "2026-06-12",
      "total_tools": 1298,
      "total_skills": 20,
      "unique_tools": 17
    },
    {
      "date": "2026-06-13",
      "total_tools": 1939,
      "total_skills": 23,
      "unique_tools": 18
    },
    {
      "date": "2026-06-14",
      "total_tools": 2290,
      "total_skills": 18,
      "unique_tools": 19
    },
    {
      "date": "2026-06-15",
      "total_tools": 2600,
      "total_skills": 12,
      "unique_tools": 19
    },
    {
      "date": "2026-06-16",
      "total_tools": 2523,
      "total_skills": 11,
      "unique_tools": 21
    },
    {
      "date": "2026-06-17",
      "total_tools": 2992,
      "total_skills": 9,
      "unique_tools": 21
    },
    {
      "date": "2026-06-18",
      "total_tools": 2805,
      "total_skills": 12,
      "unique_tools": 21
    },
    {
      "date": "2026-06-19",
      "total_tools": 2468,
      "total_skills": 9,
      "unique_tools": 21
    },
    {
      "date": "2026-06-20",
      "total_tools": 1563,
      "total_skills": 7,
      "unique_tools": 17
    },
    {
      "date": "2026-06-21",
      "total_tools": 492,
      "total_skills": 4,
      "unique_tools": 19
    }
  ],
  "top_tools": [
    {
      "rank": 1,
      "name": "Bash",
      "count": 8204
    },
    {
      "rank": 2,
      "name": "Read",
      "count": 4273
    },
    {
      "rank": 3,
      "name": "Edit",
      "count": 2200
    },
    {
      "rank": 4,
      "name": "Write",
      "count": 1024
    },
    {
      "rank": 5,
      "name": "Grep",
      "count": 948
    },
    {
      "rank": 6,
      "name": "automation_update",
      "count": 758
    },
    {
      "rank": 7,
      "name": "Glob",
      "count": 678
    },
    {
      "rank": 8,
      "name": "Skill",
      "count": 624
    },
    {
      "rank": 9,
      "name": "TaskOutput",
      "count": 379
    },
    {
      "rank": 10,
      "name": "PowerShell",
      "count": 358
    },
    {
      "rank": 11,
      "name": "WebFetch",
      "count": 345
    },
    {
      "rank": 12,
      "name": "DeferExecuteTool",
      "count": 272
    },
    {
      "rank": 13,
      "name": "WebSearch",
      "count": 230
    },
    {
      "rank": 14,
      "name": "TaskUpdate",
      "count": 164
    },
    {
      "rank": 15,
      "name": "ToolSearch",
      "count": 133
    },
    {
      "rank": 16,
      "name": "present_files",
      "count": 116
    },
    {
      "rank": 17,
      "name": "TaskCreate",
      "count": 106
    },
    {
      "rank": 18,
      "name": "AskUserQuestion",
      "count": 82
    },
    {
      "rank": 19,
      "name": "conversation_search",
      "count": 34
    },
    {
      "rank": 20,
      "name": "Agent",
      "count": 30
    }
  ]
};

// Display-friendly arrays
// === index.html 需要的变量名 ===
const DATA_DATE_LABELS = ["2026-06-12", "2026-06-13", "2026-06-14", "2026-06-15", "2026-06-16", "2026-06-17", "2026-06-18", "2026-06-19", "2026-06-20", "2026-06-21"];
const DATA_DATE_FULL = [...DATA_DATE_LABELS];
const DATA_TOTAL_DAILY = [1298, 1939, 2290, 2600, 2523, 2992, 2805, 2468, 1563, 492];
const DATA_TOTAL_CUMULATIVE = [1298, 3237, 5527, 8127, 10650, 13642, 16447, 18915, 20478, 20970];

// 技能数据
const DATA_SKILLS = [{"n": " | head -50", "t": 4, "s": "self-made", "st": "建议保留", "d": "", "da": [0, 0, 0, 0, 4, 0, 0, 0, 0, 0]}, {"n": "([^", "t": 12, "s": "self-made", "st": "建议保留", "d": "", "da": [0, 0, 0, 0, 12, 0, 0, 0, 0, 0]}, {"n": "[^", "t": 12, "s": "self-made", "st": "建议保留", "d": "", "da": [0, 0, 0, 0, 0, 12, 0, 0, 0, 0]}, {"n": "amruta-daily-push", "t": 2, "s": "self-made", "st": "经常使用", "d": "每日 Amruta 文章推送流水线", "da": [0, 0, 1, 1, 0, 0, 0, 0, 0, 0]}, {"n": "ardot-design-assistant", "t": 4, "s": "self-made", "st": "建议保留", "d": "", "da": [2, 0, 0, 0, 0, 0, 0, 0, 0, 2]}, {"n": "astro-consult-framework", "t": 1, "s": "self-made", "st": "建议保留", "d": "", "da": [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "browserharness", "t": 29, "s": "self-made", "st": "经常使用", "d": "浏览器 CDP 自动化控制", "da": [0, 6, 2, 6, 0, 8, 5, 1, 1, 0]}, {"n": "daily-review-ssh-push", "t": 1, "s": "self-made", "st": "建议保留", "d": "", "da": [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]}, {"n": "daily-wechat-reminder", "t": 55, "s": "self-made", "st": "经常使用", "d": "每日微信节拍器提醒", "da": [3, 3, 3, 6, 6, 7, 9, 6, 10, 2]}, {"n": "github", "t": 4, "s": "connector", "st": "建议保留", "d": "GitHub 连接器", "da": [2, 1, 0, 1, 0, 0, 0, 0, 0, 0]}, {"n": "glass-project-report", "t": 2, "s": "self-made", "st": "建议保留", "d": "", "da": [1, 1, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "grill-me", "t": 2, "s": "self-made", "st": "建议保留", "d": "", "da": [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]}, {"n": "headroom", "t": 5, "s": "self-made", "st": "建议保留", "d": "", "da": [0, 3, 2, 0, 0, 0, 0, 0, 0, 0]}, {"n": "ima-skill", "t": 2, "s": "self-made", "st": "建议保留", "d": "", "da": [1, 0, 1, 0, 0, 0, 0, 0, 0, 0]}, {"n": "karpathy-guidelines", "t": 8, "s": "self-made", "st": "经常使用", "d": "LLM 编码行为准则", "da": [3, 1, 0, 3, 1, 0, 0, 0, 0, 0]}, {"n": "kb-deep-search", "t": 2, "s": "self-made", "st": "经常使用", "d": "本地知识库深度语义检索", "da": [0, 0, 0, 1, 1, 0, 0, 0, 0, 0]}, {"n": "lobster-comm", "t": 14, "s": "github", "st": "已删除", "d": "龙虾通信工具（已删除）", "da": [5, 3, 2, 2, 2, 0, 0, 0, 0, 0]}, {"n": "lobster-mem0", "t": 53, "s": "self-made", "st": "建议保留", "d": "", "da": [11, 9, 10, 12, 11, 0, 0, 0, 0, 0]}, {"n": "lobster-persona", "t": 1, "s": "self-made", "st": "建议保留", "d": "", "da": [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]}, {"n": "long-task-detach", "t": 1, "s": "self-made", "st": "经常使用", "d": "长任务沙箱脱离超时执行", "da": [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]}, {"n": "marketplace-skill-installer", "t": 1, "s": "builtin", "st": "建议保留", "d": "市场 Skill 一键安装", "da": [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "mem0-setup", "t": 1, "s": "self-made", "st": "建议保留", "d": "", "da": [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "money-find", "t": 1, "s": "self-made", "st": "建议保留", "d": "需求反推法找副业机会", "da": [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "money-init", "t": 1, "s": "self-made", "st": "建议保留", "d": "cheat-on-money 首次配置", "da": [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "money-plan", "t": 1, "s": "self-made", "st": "建议保留", "d": "副业执行方案生成", "da": [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "money-verify", "t": 1, "s": "self-made", "st": "建议保留", "d": "副业反诈 rubric 打分", "da": [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "nvidia-free-models-scraper", "t": 2, "s": "self-made", "st": "建议保留", "d": "", "da": [0, 0, 0, 0, 0, 0, 2, 0, 0, 0]}, {"n": "nvidia-nim-model-scraper", "t": 12, "s": "self-made", "st": "建议保留", "d": "", "da": [0, 0, 0, 0, 0, 8, 4, 0, 0, 0]}, {"n": "nvidia_key_extractor", "t": 1, "s": "self-made", "st": "建议保留", "d": "", "da": [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]}, {"n": "nvidia_key_full_collector", "t": 1, "s": "self-made", "st": "已删除", "d": "NVIDIA 密钥收集（已删除）", "da": [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]}, {"n": "nvidia_key_incremental_collector", "t": 2, "s": "self-made", "st": "建议保留", "d": "", "da": [0, 0, 0, 0, 0, 0, 2, 0, 0, 0]}, {"n": "ppvi", "t": 2, "s": "self-made", "st": "建议保留", "d": "拼拼视觉美学设计体系", "da": [0, 0, 1, 0, 0, 0, 0, 0, 1, 0]}, {"n": "qq-mail", "t": 4, "s": "self-made", "st": "建议保留", "d": "", "da": [0, 0, 2, 2, 0, 0, 0, 0, 0, 0]}, {"n": "sahaj-yoga-universal", "t": 4, "s": "self-made", "st": "建议保留", "d": "", "da": [0, 1, 1, 0, 2, 0, 0, 0, 0, 0]}, {"n": "sahaja-rag-to-ima", "t": 1, "s": "self-made", "st": "经常使用", "d": "霎哈嘉 RAG 搜索推送 IMA", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]}, {"n": "scan-new-projects", "t": 1, "s": "self-made", "st": "经常使用", "d": "扫描新项目并评估优先级", "da": [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]}, {"n": "skill-creator", "t": 10, "s": "builtin", "st": "建议保留", "d": "创建有效的 WorkBuddy Skill", "da": [0, 1, 0, 0, 0, 1, 8, 0, 0, 0]}, {"n": "skill-manage", "t": 21, "s": "self-made", "st": "经常使用", "d": "Skill 列表/创建/删除管理", "da": [2, 8, 1, 1, 0, 2, 3, 2, 2, 0]}, {"n": "skill-usage-updater", "t": 3, "s": "self-made", "st": "建议保留", "d": "", "da": [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]}, {"n": "soul-checker", "t": 7, "s": "self-made", "st": "建议保留", "d": "", "da": [0, 0, 0, 0, 0, 0, 7, 0, 0, 0]}, {"n": "speed-testing-fix", "t": 9, "s": "self-made", "st": "经常使用", "d": "修复 llm-retry-guard 测速逻辑", "da": [0, 0, 0, 0, 0, 0, 0, 9, 0, 0]}, {"n": "subagent-driven-development", "t": 1, "s": "self-made", "st": "经常使用", "d": "Subagent 隔离执行开发", "da": [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "systematic-debugging", "t": 4, "s": "self-made", "st": "经常使用", "d": "系统化 Bug 排查根因", "da": [2, 2, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "translate", "t": 1, "s": "self-made", "st": "建议保留", "d": "", "da": [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]}, {"n": "uumit-agent", "t": 6, "s": "self-made", "st": "经常使用", "d": "UUMit 智能接单代理", "da": [0, 2, 0, 0, 1, 0, 0, 3, 0, 0]}, {"n": "uumit-auto-apply", "t": 10, "s": "self-made", "st": "经常使用", "d": "UUMit 自动接任务+巡航", "da": [0, 5, 2, 0, 0, 0, 0, 3, 0, 0]}, {"n": "uumit-create-products", "t": 3, "s": "self-made", "st": "经常使用", "d": "UUMit 批量创建知识商品", "da": [0, 3, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "uumit-static-json-api", "t": 1, "s": "self-made", "st": "经常使用", "d": "UUMit 静态 JSON 数据接口", "da": [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]}, {"n": "verification-before-completion", "t": 2, "s": "self-made", "st": "经常使用", "d": "任务完成前最终验证", "da": [0, 2, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "volcano-progress", "t": 1, "s": "self-made", "st": "建议保留", "d": "", "da": [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]}, {"n": "web-deploy-github", "t": 1, "s": "self-made", "st": "建议保留", "d": "", "da": [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "wechat-clawbot-notify", "t": 76, "s": "self-made", "st": "经常使用", "d": "ClawBot 微信消息推送", "da": [7, 8, 7, 9, 8, 5, 7, 8, 15, 2]}, {"n": "workbuddy-available-models", "t": 25, "s": "self-made", "st": "建议保留", "d": "查看可用模型列表", "da": [0, 0, 0, 0, 0, 0, 6, 18, 1, 0]}, {"n": "workbuddy-workspace-manager", "t": 1, "s": "self-made", "st": "建议保留", "d": "", "da": [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]}, {"n": "writing-plans", "t": 5, "s": "self-made", "st": "经常使用", "d": "多步任务执行方案编写", "da": [2, 2, 0, 0, 1, 0, 0, 0, 0, 0]}, {"n": "国内旅行聚合查询", "t": 1, "s": "self-made", "st": "建议保留", "d": "", "da": [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "amruta-fix-loop", "t": 0, "s": "self-made", "st": "经常使用", "d": "自动化循环修复 amruta-actions 问题", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "brainstorming", "t": 0, "s": "self-made", "st": "经常使用", "d": "创意探索和方案设计", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "daily-task-reminder", "t": 0, "s": "self-made", "st": "经常使用", "d": "管理今日任务清单", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "dispatching-parallel-agents", "t": 0, "s": "self-made", "st": "经常使用", "d": "并行任务分发执行", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "executing-plans", "t": 0, "s": "self-made", "st": "经常使用", "d": "执行已完成的实现方案", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "finishing-a-development-branch", "t": 0, "s": "self-made", "st": "经常使用", "d": "完成开发分支并合入", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "hallmark", "t": 0, "s": "self-made", "st": "经常使用", "d": "反 AI 味前端设计规范", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "ponytail", "t": 0, "s": "self-made", "st": "经常使用", "d": "最懒但可行的解决方案", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "receiving-code-review", "t": 0, "s": "self-made", "st": "经常使用", "d": "接收代码审查反馈", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "requesting-code-review", "t": 0, "s": "self-made", "st": "经常使用", "d": "请求代码审查", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "sahaja-x-evaluation", "t": 0, "s": "self-made", "st": "经常使用", "d": "霎哈嘉+X 项目评估矩阵", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "skill-reminder", "t": 0, "s": "self-made", "st": "经常使用", "d": "提示当前对话可用 Skill", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "tdd", "t": 0, "s": "self-made", "st": "经常使用", "d": "测试驱动开发红绿重构", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "test-driven-development", "t": 0, "s": "self-made", "st": "经常使用", "d": "", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "using-git-worktrees", "t": 0, "s": "self-made", "st": "经常使用", "d": "使用 Git Worktrees 隔离开发", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "using-superpowers", "t": 0, "s": "self-made", "st": "经常使用", "d": "在所有对话中先加载技能", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "writing-skills", "t": 0, "s": "self-made", "st": "经常使用", "d": "WorkBuddy Skill 创建编辑", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "100-days-spirit-huangting", "t": 0, "s": "self-made", "st": "建议保留", "d": "100 天神意照黄庭打卡", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "add-project-to-evaluation", "t": 0, "s": "self-made", "st": "建议保留", "d": "霎哈嘉+X 评估添加项目", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "api-integration-debug", "t": 0, "s": "self-made", "st": "建议保留", "d": "调试外部 API 集成问题", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "esther-design-system", "t": 0, "s": "self-made", "st": "建议保留", "d": "不二个人 IP 设计系统", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "flowsint", "t": 0, "s": "self-made", "st": "建议保留", "d": "OSINT 可视化关系图谱", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "flowsint-enricher-builder", "t": 0, "s": "self-made", "st": "建议保留", "d": "Flowsint 富化器构建指南", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "money-retro", "t": 0, "s": "self-made", "st": "建议保留", "d": "副业复盘和经验沉淀", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "money-status", "t": 0, "s": "self-made", "st": "建议保留", "d": "cheat-on-money 状态看板", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "push-amruta-devlog", "t": 0, "s": "self-made", "st": "建议保留", "d": "推送 Amruta 开发日志", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "cloudstudio-deploy", "t": 0, "s": "builtin", "st": "建议保留", "d": "部署静态站点到 CloudStudio", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "expert-manager", "t": 0, "s": "builtin", "st": "建议保留", "d": "专家包生命周期管理", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "多模态内容生成", "t": 0, "s": "builtin", "st": "建议保留", "d": "文生视频/3D 模型", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "cheat-on-money", "t": 0, "s": "github", "st": "已合并", "d": "副业机会探索套件（已合并为子技能）", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}, {"n": "nvidia_key_incremental_runner", "t": 0, "s": "self-made", "st": "已删除", "d": "NVIDIA 增量收集（已删除）", "da": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}];

// 工具数据
const TOOLS_DATA = [{"rank": 1, "name": "Bash", "count": 8204}, {"rank": 2, "name": "Read", "count": 4273}, {"rank": 3, "name": "Edit", "count": 2200}, {"rank": 4, "name": "Write", "count": 1024}, {"rank": 5, "name": "Grep", "count": 948}, {"rank": 6, "name": "automation_update", "count": 758}, {"rank": 7, "name": "Glob", "count": 678}, {"rank": 8, "name": "Skill", "count": 624}, {"rank": 9, "name": "TaskOutput", "count": 379}, {"rank": 10, "name": "PowerShell", "count": 358}, {"rank": 11, "name": "WebFetch", "count": 345}, {"rank": 12, "name": "DeferExecuteTool", "count": 272}, {"rank": 13, "name": "WebSearch", "count": 230}, {"rank": 14, "name": "TaskUpdate", "count": 164}, {"rank": 15, "name": "ToolSearch", "count": 133}, {"rank": 16, "name": "present_files", "count": 116}, {"rank": 17, "name": "TaskCreate", "count": 106}, {"rank": 18, "name": "AskUserQuestion", "count": 82}, {"rank": 19, "name": "conversation_search", "count": 34}, {"rank": 20, "name": "Agent", "count": 30}, {"rank": 21, "name": "TaskList", "count": 12}];
