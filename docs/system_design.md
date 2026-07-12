# System Design — PromptLab

## Overview
PromptLab is a lightweight web application for analyzing, scoring, optimizing, and managing prompts for LLMs. It consists of a Streamlit frontend, a Python backend providing core prompt services and APIs, a small relational store for prompt/version/evaluation history, and integrations to external LLM providers.

## High-level Architecture

```mermaid
flowchart LR
  User[User / Frontend (Streamlit)] -->|HTTP| Backend[Backend API (FastAPI / Flask)]
  Backend -->|LLM calls| LLM[LLM Providers (OpenAI, DeepSeek, Gemini)]
  Backend --> DB[(SQLite / Postgres)]
  Backend -->|Queue| Worker[(Background Workers: Celery / RQ)]
  Worker --> LLM
  Backend -->|Static| Storage[(S3 / local filesystem)]
  User -->|Browser| StaticFiles
```

## Components

- Frontend: `app.py` (Streamlit) — UI for prompt input, template library, optimization results, A/B test dashboard.
- Backend API: a small REST or FastAPI layer (can be integrated into `app.py` or separated as `src/api.py`).
- Core modules (in `src/`):
  - `prompt_analyzer.py` — scoring and evaluation logic.
  - `prompt_optimizer.py` — generates optimized prompts and explanations.
  - `prompt_templates.py` — template management and tagging.
  - `survey_analysis.py` — processes `data/survey_results.csv` and reporting utilities.
- Background Workers: handle batch scoring, long-running optimization, and A/B testing jobs.
- Storage:
  - Prototype: SQLite (file `data/promptlab.db`) for prompts, versions, experiments, users, evaluations.
  - Production: Postgres + S3 for artifacts.

## Data Model (suggested tables)

- `users` (id, username, email, role, created_at)
- `prompts` (id, user_id, title, created_at)
- `prompt_versions` (id, prompt_id, version, text, metadata_json, created_at)
- `evaluations` (id, prompt_version_id, metric_json, score, model, cost, created_at)
- `experiments` (id, name, description, config_json, created_at)
- `ab_results` (id, experiment_id, prompt_version_a, prompt_version_b, winner, metrics_json, created_at)

## Core APIs (REST)

- `POST /api/score` — body: {prompt_text, model, options} -> returns {score_breakdown, overall_score, explanations}
- `POST /api/optimize` — body: {prompt_text, target_style, constraints} -> returns {optimized_prompt, explanation, delta_score}
- `POST /api/prompts` — create a new prompt record
- `GET /api/prompts/{id}/versions` — list versions and evaluations
- `POST /api/abtest` — run A/B compare job (async)
- `GET /api/export?format=csv` — export history/metrics

## Key Algorithms & Pseudocode

### score_prompt(prompt)
- Metrics: relevance, clarity, specificity, constraints, robustness, token_cost
- Approach: policy-based rubric (combine heuristics + small LLM eval)

Pseudocode:

```
def score_prompt(prompt_text, model='gpt-4'):
    heuristics = compute_heuristics(prompt_text)
    llm_eval = call_llm_for_evaluation(prompt_text, rubric)
    combined = weighted_sum(heuristics, llm_eval)
    return {
      'score': combined.score,
      'breakdown': combined.breakdown,
      'explanation': llm_eval.explanation
    }
```

### optimize_prompt(original_prompt)

```
def optimize_prompt(original_prompt, style=None, constraints=None):
    diagnosis = call_llm('analyze and list issues', original_prompt)
    suggestions = generate_rewrites(original_prompt, style, constraints)
    best_candidate = rank_candidates([original_prompt] + suggestions)
    return {
      'optimized_prompt': best_candidate.text,
      'explanation': diagnosis,
      'score_delta': score_prompt(best_candidate).score - score_prompt(original_prompt).score
    }
```

### save_prompt_version(user_id, prompt_id, prompt_text, metadata)

- Insert into `prompt_versions` with timestamp and metadata (source, model, score)

## Batch Processing & Background Jobs

- Use Celery / RQ with Redis for queueing. Tasks:
  - Batch scoring (for uploaded CSV of prompts)
  - Long LLM optimizations (multi-step rewrite)
  - Running A/B experiments and aggregating results

## Evaluation Metrics

- Numeric metrics: overall_score (0-100), token_cost, latency
- Subscores: clarity, specificity, context_coverage, instruction_quality, determinism
- Store raw LLM explanations for auditability

## Security & Config

- API keys stored in environment variables (`OPENAI_API_KEY`, `DEEPSEEK_KEY`)
- Never commit keys to repo. Use `.env` or secrets manager.
- Rate-limiting on public APIs; per-user quotas for multi-tenant

## Deployment Notes

- Local dev: Streamlit app runs via `streamlit run app.py` and uses local SQLite.
- Production: Serve backend with Uvicorn + Gunicorn, use Docker, database migrations (Alembic).

## Implementation Roadmap (developer tasks)

1. Implement `score_prompt` in `src/prompt_analyzer.py` with unit tests.
2. Implement `optimize_prompt` in `src/prompt_optimizer.py` and add integration tests.
3. Add simple REST API wrappers in `src/api.py` and wire to `app.py` UI.
4. Add DB models and migrations (SQLite initial schema).
5. Build background worker tasks for batch operations.
6. Create Streamlit pages for Template Library, Prompt Editor, A/B Dashboard.

## Next Steps
- Implement core backend functions in `src/prompt_analyzer.py` and `src/prompt_optimizer.py` (I can start implementing these now).

