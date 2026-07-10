def check_clarity(prompt: str) -> tuple:
    """
    Check whether the prompt is clear and specific.
    """
    if len(prompt.strip()) < 20:
        return 50, "The prompt is too short and may be unclear."
    if len(prompt.strip()) < 50:
        return 70, "The prompt is understandable but could be more specific."
    return 90, "The prompt is relatively clear."


def check_role(prompt: str) -> tuple:
    """
    Check whether the prompt includes a role setting.
    """
    role_keywords = [
        "you are", "act as", "as a",
        "你是", "作为", "扮演"
    ]

    prompt_lower = prompt.lower()

    if any(keyword in prompt_lower for keyword in role_keywords):
        return 90, "The prompt includes a role setting."
    return 50, "Missing role setting."


def check_task(prompt: str) -> tuple:
    """
    Check whether the task is clear.
    """
    task_keywords = [
        "write", "summarize", "explain", "analyze", "generate", "compare",
        "create", "design", "evaluate",
        "写", "总结", "解释", "分析", "生成", "比较", "设计", "评价"
    ]

    prompt_lower = prompt.lower()

    if any(keyword in prompt_lower for keyword in task_keywords):
        return 90, "The task is clear."
    return 55, "The task is not clear enough."


def check_context(prompt: str) -> tuple:
    """
    Check whether the prompt provides background or context.
    """
    context_keywords = [
        "background", "context", "target user", "audience", "purpose",
        "背景", "上下文", "对象", "受众", "目的", "场景"
    ]

    prompt_lower = prompt.lower()

    if any(keyword in prompt_lower for keyword in context_keywords):
        return 90, "The prompt provides useful context."
    return 50, "Missing background or context."


def check_constraints(prompt: str) -> tuple:
    """
    Check whether the prompt includes constraints or requirements.
    """
    constraint_keywords = [
        "within", "less than", "no more than", "at least", "must", "should",
        "requirements", "limit",
        "不超过", "不少于", "必须", "要求", "限制", "字"
    ]

    prompt_lower = prompt.lower()

    if any(keyword in prompt_lower for keyword in constraint_keywords):
        return 90, "The prompt includes constraints or requirements."
    return 50, "Missing clear constraints or requirements."


def check_output_format(prompt: str) -> tuple:
    """
    Check whether the prompt specifies output format.
    """
    format_keywords = [
        "markdown", "table", "json", "bullet points", "list", "outline",
        "表格", "格式", "列表", "分点", "大纲"
    ]

    prompt_lower = prompt.lower()

    if any(keyword in prompt_lower for keyword in format_keywords):
        return 90, "The prompt specifies an output format."
    return 50, "Missing output format."


def check_executability(prompt: str) -> tuple:
    """
    Check whether the prompt is executable for an AI model.
    """
    if not prompt or len(prompt.strip()) == 0:
        return 0, "The prompt is empty and cannot be executed."
    if "?" in prompt or "请" in prompt or "please" in prompt.lower():
        return 85, "The prompt is executable."
    return 70, "The prompt is executable but could be more direct."


def analyze_prompt(prompt: str) -> dict:
    """
    Analyze a prompt across six dimensions.
    """

    if not prompt or len(prompt.strip()) == 0:
        return {
            "score": 0,
            "dimension_scores": {},
            "feedback": ["The prompt is empty."]
        }

    checks = {
        "Clarity": check_clarity(prompt),
        "Role": check_role(prompt),
        "Task": check_task(prompt),
        "Context": check_context(prompt),
        "Constraints": check_constraints(prompt),
        "Output Format": check_output_format(prompt),
        "Executability": check_executability(prompt)
    }

    dimension_scores = {}
    feedback = []

    for dimension, result in checks.items():
        score, message = result
        dimension_scores[dimension] = score
        feedback.append(f"{dimension}: {message}")

    final_score = round(sum(dimension_scores.values()) / len(dimension_scores))

    return {
        "score": final_score,
        "dimension_scores": dimension_scores,
        "feedback": feedback
    }


def diagnose_prompt(prompt: str) -> list:
    """
    Return only the problems found in the prompt.
    This function is used by app.py.
    """
    analysis = analyze_prompt(prompt)
    problems = []

    for item in analysis["feedback"]:
        if "Missing" in item or "not clear" in item or "too short" in item or "empty" in item:
            problems.append(item)

    return problems


def score_prompt(prompt: str) -> dict:
    """
    Return final score, problems, and dimension scores.
    This function is used by app.py.
    """
    analysis = analyze_prompt(prompt)

    return {
        "score": analysis["score"],
        "problems": diagnose_prompt(prompt),
        "dimension_scores": analysis["dimension_scores"],
        "feedback": analysis["feedback"]
    }