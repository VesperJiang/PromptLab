from typing import Optional

from src.prompt_analyzer import diagnose_prompt


def _normalize_diagnosis(diagnosis: Optional[list]) -> list:
    """
    Convert optional diagnosis input into a predictable list.
    """
    if diagnosis is None:
        return []
    return [item for item in diagnosis if isinstance(item, str)]


def _has_problem(diagnosis: list, keyword: str) -> bool:
    """
    Check whether any diagnosis item mentions a dimension or issue.
    """
    keyword = keyword.lower()
    return any(keyword in item.lower() for item in diagnosis)


def optimize_prompt(prompt: str, diagnosis: Optional[list] = None) -> str:
    """
    Generate a structured optimized prompt based on the original prompt.

    This optimizer is diagnosis-aware. Callers may pass problems returned by
    diagnose_prompt(), or omit diagnosis and let the optimizer diagnose the
    prompt automatically. The original one-argument call remains supported.
    """

    problems = _normalize_diagnosis(diagnosis)
    if diagnosis is None:
        problems = diagnose_prompt(prompt)

    role_instruction = "Act as a helpful specialist for this request."
    task_instruction = "Turn the user's request into a clear, complete answer."
    context_instruction = "Use the provided context. If key context is missing, state a reasonable assumption."
    format_instruction = "Format the response in Markdown so it is easy to scan."
    constraint_instruction = "Keep the response practical, focused, and easy to use."

    if _has_problem(problems, "role"):
        role_instruction = "Act as a subject-matter specialist who can guide this task clearly."
    if _has_problem(problems, "task") or _has_problem(problems, "not clear"):
        task_instruction = "Clarify the user's goal first, then complete the task in a direct way."
    if _has_problem(problems, "context"):
        context_instruction = "Ask for missing background when needed, and state assumptions before answering."
    if _has_problem(problems, "output format"):
        format_instruction = "Return the answer in Markdown using headings, lists, or tables when useful."
    if _has_problem(problems, "constraints"):
        constraint_instruction = "Follow explicit requirements, avoid unnecessary detail, and note any limits."

    optimized_prompt = f"""
{role_instruction}

Original request:
{prompt}

Instructions:
1. {task_instruction}
2. {context_instruction}
3. {format_instruction}
4. Explain key points step by step when helpful.
5. Give practical examples when necessary.
6. {constraint_instruction}
"""

    return optimized_prompt.strip()


def explain_optimization(diagnosis: Optional[list] = None) -> list:
    """
    Explain what has been improved in the optimized prompt.
    """

    problems = _normalize_diagnosis(diagnosis)
    explanations = [
        "Added a clear role setting.",
        "Clarified the task structure.",
        "Added output format requirements.",
        "Added constraints for clarity and usefulness.",
        "Encouraged step-by-step explanation and practical examples."
    ]

    if _has_problem(problems, "context"):
        explanations.append("Added guidance for missing context and assumptions.")
    if _has_problem(problems, "task") or _has_problem(problems, "not clear"):
        explanations.append("Made the task easier for the AI model to execute.")

    return explanations
