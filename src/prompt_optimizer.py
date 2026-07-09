def optimize_prompt(prompt: str) -> str:
    """
    Generate a structured optimized prompt based on the original prompt.
    This is a rule-based version for the MVP.
    """

    optimized_prompt = f"""
You are a professional AI assistant.

Task:
{prompt}

Please improve the response according to the following requirements:

1. Understand the user's real intention.
2. Provide a clear and structured answer.
3. Use Markdown format.
4. Explain key points step by step.
5. Give practical examples when necessary.
6. Keep the answer concise, accurate, and easy to understand.
"""

    return optimized_prompt.strip()


def explain_optimization() -> list:
    """
    Explain what has been improved in the optimized prompt.
    """

    explanations = [
        "Added a clear role setting.",
        "Clarified the task structure.",
        "Added output format requirements.",
        "Added constraints for clarity and usefulness.",
        "Encouraged step-by-step explanation and practical examples."
    ]

    return explanations