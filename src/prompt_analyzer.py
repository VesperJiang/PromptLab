def diagnose_prompt(prompt: str) -> list:
    """
    Diagnose common problems in a prompt.
    Return a list of problems.
    """
    problems = []

    if not prompt or len(prompt.strip()) == 0:
        problems.append("The prompt is empty.")
        return problems

    prompt_lower = prompt.lower()

    if len(prompt.strip()) < 20:
        problems.append("The prompt is too short and may be unclear.")

    role_keywords = [
        "you are", "act as", "as a",
        "你是", "作为", "扮演"
    ]
    if not any(keyword in prompt_lower for keyword in role_keywords):
        problems.append("Missing role setting.")

    task_keywords = [
        "write", "summarize", "explain", "analyze", "generate", "compare",
        "写", "总结", "解释", "分析", "生成", "比较"
    ]
    if not any(keyword in prompt_lower for keyword in task_keywords):
        problems.append("The task is not clear enough.")

    format_keywords = [
        "markdown", "table", "json", "bullet points", "list",
        "表格", "格式", "列表", "分点", "markdown"
    ]
    if not any(keyword in prompt_lower for keyword in format_keywords):
        problems.append("Missing output format.")

    constraint_keywords = [
        "within", "less than", "no more than", "at least", "must", "should",
        "不超过", "不少于", "必须", "请", "要求", "字"
    ]
    if not any(keyword in prompt_lower for keyword in constraint_keywords):
        problems.append("Missing clear constraints or requirements.")

    context_keywords = [
        "background", "context", "target user", "audience",
        "背景", "上下文", "对象", "受众", "目的"
    ]
    if not any(keyword in prompt_lower for keyword in context_keywords):
        problems.append("Missing background or context.")

    return problems


def score_prompt(prompt: str) -> dict:
    """
    Score a prompt based on rule-based criteria.
    """
    problems = diagnose_prompt(prompt)

    score = 100
    score -= len(problems) * 12
    score = max(score, 0)

    return {
        "score": score,
        "problems": problems
    }