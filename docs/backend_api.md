# Backend API

This document describes the backend functions used by PromptLab.

## `src.prompt_analyzer`

### `analyze_prompt(prompt: str) -> dict`

Analyzes a prompt across PromptLab quality dimensions.

Returns:

- `score`: final average score from 0 to 100.
- `dimension_scores`: score by dimension.
- `feedback`: full feedback messages for each dimension.

### `diagnose_prompt(prompt: str) -> list`

Returns only the detected prompt problems.

This function is used by the app diagnosis workflow and can also be passed to
the optimizer.

### `score_prompt(prompt: str) -> dict`

Returns the main analyzer result.

Returned keys:

- `score`
- `problems`
- `dimension_scores`
- `feedback`

## `src.prompt_optimizer`

### `optimize_prompt(prompt: str, diagnosis: Optional[list] = None) -> str`

Generates a structured optimized prompt.

The optimizer is diagnosis-aware:

- If `diagnosis` is provided, the optimized prompt adapts to those issues.
- If `diagnosis` is omitted, the optimizer calls `diagnose_prompt(prompt)`
  internally.

The app-compatible call still works:

```python
optimized = optimize_prompt(user_prompt)
```

Diagnosis-aware usage:

```python
problems = diagnose_prompt(user_prompt)
optimized = optimize_prompt(user_prompt, problems)
```

### `explain_optimization(diagnosis: Optional[list] = None) -> list`

Returns short explanation messages for the optimization.

When diagnosis is provided, the explanation can include problem-specific
improvements.

## App Compatibility

The backend remains compatible with the original Streamlit integration:

```python
result = score_prompt(user_prompt)
optimized = optimize_prompt(user_prompt)
explanations = explain_optimization()
```

No frontend layout changes are required.
