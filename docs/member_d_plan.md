# PromptLab 项目方案与成员 D 工作计划

## 一、项目概述

- 项目名称：PromptLab：AI Prompt Engineering Studio
- 项目定位：一个帮助用户分析、优化、测试和管理 Prompt 的网页工具。
- 用户目标：输入一个 Prompt 后，系统可以
  1. 诊断 Prompt 存在的问题
  2. 给 Prompt 打分
  3. 自动生成优化版本
  4. 展示优化原因
  5. 保存 Prompt 历史版本
  6. 通过模板库帮助用户快速写出更好的 Prompt

## 二、要解决的问题

现在很多用户会使用 ChatGPT、DeepSeek、Gemini 等 AI 工具，但常常不知道如何写好 Prompt。常见问题包括：

- Prompt 太模糊
- 没有明确任务
- 没有指定角色
- 没有输出格式
- 没有约束条件
- 不知道为什么 AI 回答不好
- 不会比较不同 Prompt 的效果

示例：

原始 Prompt：`帮我写一篇文章`

优化后：

```
你是一位大学写作老师。请帮我写一篇关于“AI 对大学生学习方式影响”的中文议论文。
要求：
1. 字数约 800 字；
2. 结构包括引言、主体和结论；
3. 语气正式；
4. 至少提出 3 个观点；
5. 使用 Markdown 格式输出。
```

## 三、核心功能设计

### 功能一：Prompt 诊断器

Prompt Lint 类似代码 Lint 工具，用来检查 Prompt 的问题。

系统检测项：

- 是否有明确任务？
- 是否有角色设定？
- 是否有背景信息？
- 是否有输出格式？
- 是否有约束条件？
- 是否有示例？
- 是否表达清晰？

输出示例：

```
Prompt 诊断结果：
❌ 缺少角色设定
❌ 缺少输出格式
❌ 缺少字数或范围限制
⚠️ 任务描述较模糊
✅ 有基本任务目标
```

### 功能二：Prompt 评分

Prompt Score 系统从多个维度给 Prompt 打分。

评分维度：

- Clarity 明确性
- Completeness 完整性
- Context 上下文
- Constraints 约束条件
- Output Format 输出格式
- Usefulness 可执行性

输出示例：

```
综合评分：62 / 100
明确性：70
完整性：55
上下文：40
约束条件：30
输出格式：20
可执行性：75
```

### 功能三：Prompt 自动优化系统

根据诊断结果自动生成一个更好的 Prompt。

输出示例：

优化后 Prompt：

```
你是一位专业的 Python 教师。请帮我写一个 Python 程序，用于统计一段文本中每个单词出现的次数。
要求：
1. 使用 Python 3；
2. 添加必要注释；
3. 给出示例输入和输出；
4. 用 Markdown 代码块输出完整代码。
```

修改说明：

```
本次优化增加了：
1. 角色设定：Python 教师；
2. 明确任务：统计单词出现次数；
3. 技术限制：使用 Python 3；
4. 输出格式：Markdown 代码块；
5. 示例要求：输入和输出。
```

### 功能四：Prompt 模板库

提供常用场景模板。

模板类别：

- 学习类：总结论文、生成复习提纲、制作 Quiz、解释概念
- 编程类：Debug、代码解释、代码优化、README 生成
- 办公类：写邮件、会议纪要、周报总结
- 创作类：小红书文案、视频脚本、标题生成

模板示例：

```
请你作为一名{角色}，帮我完成{任务}。
背景信息是：{背景}
要求包括：{要求}
请用{输出格式}输出。
```

### 功能五：Prompt 历史记录与版本管理

保存用户的 Prompt 修改过程。

例：

- V1：帮我写代码
- V2：增加 Python 角色
- V3：增加输出格式
- V4：增加示例输入输出

展示 Diff：

```
+ 增加了角色设定
+ 增加了输出格式
+ 增加了约束条件
- 删除了模糊表达
```

## 四、技术方案推荐

### 技术栈

- 前端：Streamlit
- 后端：Python
- 主要模块：
  - `prompt_analyzer.py`
  - `prompt_optimizer.py`
  - `prompt_abtest.py`
  - `prompt_library.py`
  - `database.py`
  - `app.py`
- AI 模型：
  - OpenAI API
  - DeepSeek API
  - Gemini API
- 数据存储：
  - SQLite
  - CSV
  - JSON
- 可视化：
  - Streamlit chart
  - Matplotlib
  - Pandas
- 主要展示内容：
  - Prompt 得分
  - 问卷结果
  - 用户痛点分布
  - 优化前后对比

## 五、伪代码设计

### Prompt 评分伪代码

```text
Function score_prompt(prompt):
    criteria = [
        clarity,
        completeness,
        context,
        constraints,
        output_format,
        executability
    ]
    For each criterion in criteria:
        ask LLM to evaluate prompt on this criterion
        return score from 0 to 100
    final_score = average(all scores)
    return final_score, detailed_feedback
```

### Prompt 优化伪代码

```text
Function optimize_prompt(original_prompt):
    diagnosis = analyze_prompt(original_prompt)
    missing_parts = find_missing_elements(diagnosis)
    optimized_prompt = LLM.generate(
        original_prompt,
        missing_parts,
        prompt_engineering_rules
    )
    explanation = compare(original_prompt, optimized_prompt)
    return optimized_prompt, explanation
```

### 历史记录伪代码

```text
Function save_prompt_version(user_id, prompt, score, optimized_prompt):
    version_id = generate_new_version_id()
    record = {
        user_id,
        version_id,
        original_prompt,
        optimized_prompt,
        score,
        timestamp
    }
    save_to_database(record)
    return success
```

## 六、团队分工建议

老师希望团队分工要体现开发、数据、产品、展示、报告等多方面协作，而不是四个人都写代码。

### 成员 A：技术负责人 / AI Backend

主要职责：AI 逻辑和后端功能。

任务：

- 设计 Prompt 评分标准
- 编写 Prompt 分析函数
- 编写 Prompt 优化函数
- 调用 LLM API
- 处理 API 报错和 fallback
- 写技术部分伪代码

需要提交的 Git 内容：

- `feat: add prompt scoring function`
- `feat: implement prompt optimizer`
- `fix: handle api error`
- `docs: add backend pseudocode`

### 成员 B：前端负责人 / UI & Demo

主要职责：Streamlit 页面和用户交互。

任务：

- 搭建首页
- 设计输入框
- 展示 Prompt Score
- 展示诊断结果
- 展示优化后 Prompt
- 准备现场 Demo

需要提交的 Git 内容：

- `feat: create streamlit homepage`
- `feat: add prompt input form`
- `feat: add score visualization`
- `style: improve layout`
- `fix: demo display issue`

### 成员 C：数据与评估负责人 / Survey & Evaluation

主要职责：问卷调查、测试数据和评估结果。

任务：

- 设计问卷星问卷
- 收集 30—50 份问卷
- 分析用户是否需要 Prompt 优化工具
- 整理用户痛点
- 准备 10—20 个测试 Prompt
- 比较优化前后的效果
- 画图表
- 写 Evaluation 部分

问卷问题建议：

1. 你是否经常使用 AI 工具？
2. 你使用 AI 的主要场景是什么？
3. 你觉得写 Prompt 困难吗？
4. 你遇到过 AI 回答不符合预期的情况吗？
5. 你是否知道如何优化 Prompt？
6. 你最希望 Prompt 工具提供什么功能？
7. 你是否愿意使用 PromptLab？

可产出的图表：

- AI 使用频率
- Prompt 写作困难程度
- 用户最常见痛点
- 最受欢迎功能
- 是否愿意使用本产品

需要提交的 Git 内容：

- `docs: add survey questions`
- `data: add survey results`
- `analysis: add survey charts`
- `eval: add prompt test cases`
- `eval: compare before and after optimization`

### 成员 D：产品经理 / 报告与营销负责人

主要职责：产品故事、最终报告、营销规划和项目整合。

任务：

- 写项目背景
- 写 Problem Statement
- 整理用户故事
- 写系统设计说明
- 整理 Git History
- 写 Marketing Plan
- 整理最终 PDF 报告
- 准备 Pitch Talk 结构

Marketing Plan 内容建议：

- 目标用户：
  - 大学生
  - AI 初学者
  - 程序员
  - 自媒体创作者
  - 办公人员
- 推广渠道：
  - 小红书
  - B站
  - 知乎
  - GitHub
  - 学校社群
  - AI 工具导航网站
- 产品形态：
  - Web 版
  - Chrome 插件
  - VS Code 插件
  - 企业内部 Prompt 管理工具
- 商业模式：
  - 免费基础版
  - 高级模板库
  - 团队协作版
  - API 服务

需要提交的 Git 内容：

- `docs: add project introduction`
- `docs: add product story`
- `docs: add marketing plan`
- `docs: add final report draft`
- `docs: update git contribution section`

### Pitch Talk 分工建议

- 成员 A：介绍系统核心逻辑：输入 Prompt → 分析 → 评分 → 优化
- 成员 B：现场演示页面效果和交互：差 Prompt 的诊断、评分、优化过程
- 成员 C：介绍用户调研结果和评估结论
- 成员 D：总结项目价值、产品定位和未来计划
