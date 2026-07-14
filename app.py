from datetime import datetime

import pandas as pd
import streamlit as st

from src.prompt_analyzer import diagnose_prompt, score_prompt
from src.prompt_optimizer import explain_optimization, optimize_prompt
from src.prompt_templates import PROMPT_TEMPLATES


HISTORY_PATH = "data/history.csv"


st.set_page_config(
    page_title="PromptLab",
    layout="wide"
)

st.markdown(
    """
    <style>
        .stApp {
            background: #f7f8fb;
            color: #17202a;
        }

        .block-container {
            max-width: 1180px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        h1 {
            color: #111827;
            font-size: 2.35rem !important;
            font-weight: 760 !important;
            letter-spacing: 0;
            margin-bottom: 0.15rem !important;
        }

        h2, h3 {
            color: #1f2937;
            font-weight: 680 !important;
            letter-spacing: 0;
        }

        p, label, span, div {
            letter-spacing: 0;
        }

        .app-subtitle {
            color: #5b6472;
            font-size: 1rem;
            margin: 0 0 1.2rem 0;
        }

        .section-note {
            color: #657080;
            font-size: 0.95rem;
            margin-top: -0.35rem;
            margin-bottom: 1rem;
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: 0.45rem;
            border-bottom: 1px solid #d9dee8;
        }

        .stTabs [data-baseweb="tab"] {
            background: transparent;
            border-radius: 0;
            padding: 0.55rem 0.75rem;
        }

        .stTabs [aria-selected="true"] {
            border-bottom: 2px solid #2563eb;
        }

        .stTabs [data-baseweb="tab"] p {
            color: #475569;
            font-weight: 600;
        }

        .stTabs [aria-selected="true"] p {
            color: #1d4ed8;
        }

        textarea {
            background: #ffffff !important;
            color: #111827 !important;
            border: 1px solid #ccd5e1 !important;
            border-radius: 8px !important;
        }

        .stButton > button {
            background: #2563eb;
            color: #ffffff;
            border: 0;
            border-radius: 8px;
            padding: 0.55rem 1rem;
            font-weight: 650;
        }

        .stButton > button:hover {
            background: #1d4ed8;
            color: #ffffff;
        }

        [data-testid="stMetric"] {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 1rem;
        }

        [data-testid="stMetricValue"] {
            color: #111827;
            font-size: 2.5rem !important;
            font-weight: 780 !important;
        }

        [data-testid="stMetricDelta"] {
            color: #64748b !important;
            background: transparent !important;
        }

        .dim-row {
            display: flex;
            justify-content: space-between;
            gap: 1rem;
            margin-top: 0.45rem;
            margin-bottom: 0.15rem;
        }

        .dim-name {
            color: #263241;
            font-weight: 650;
            font-size: 0.94rem;
        }

        .dim-score {
            color: #64748b;
            font-size: 0.9rem;
        }

        .stProgress > div > div > div > div {
            background-color: #2563eb;
        }

        code, pre {
            border-radius: 8px !important;
        }

        .stImage img {
            object-fit: contain;
            max-height: 330px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


def save_history(original_prompt: str, score: int, optimized_prompt: str) -> None:
    history_data = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "original_prompt": original_prompt,
        "score": score,
        "optimized_prompt": optimized_prompt
    }

    try:
        old_data = pd.read_csv(HISTORY_PATH)
        new_data = pd.concat([old_data, pd.DataFrame([history_data])], ignore_index=True)
    except Exception:
        new_data = pd.DataFrame([history_data])

    new_data.to_csv(HISTORY_PATH, index=False)


def read_history() -> pd.DataFrame:
    try:
        return pd.read_csv(HISTORY_PATH)
    except Exception:
        return pd.DataFrame(columns=["time", "original_prompt", "score", "optimized_prompt"])


st.title("PromptLab")
st.markdown(
    "<p class='app-subtitle'>A focused workspace for diagnosing, improving, and reusing prompts.</p>",
    unsafe_allow_html=True
)

tab_analyzer, tab_templates, tab_history = st.tabs(
    ["Prompt Analyzer", "Template Library", "History"]
)

with tab_analyzer:
    st.subheader("Analyze a Prompt")
    st.markdown(
        "<p class='section-note'>Paste a rough prompt below. PromptLab will score it, diagnose missing parts, and produce a cleaner version.</p>",
        unsafe_allow_html=True
    )

    user_prompt = st.text_area(
        "Prompt",
        height=170,
        placeholder="Example: Help me write an article about AI."
    )

    analyze_btn = st.button("Analyze and Optimize", type="primary")

    if analyze_btn:
        if not user_prompt.strip():
            st.warning("Please enter a prompt first.")
        else:
            evaluation_result = score_prompt(user_prompt)
            total_score = evaluation_result["score"]
            metrics_dict = evaluation_result["dimension_scores"]
            problems = evaluation_result.get("problems", diagnose_prompt(user_prompt))
            optimized_prompt = optimize_prompt(user_prompt, problems)
            optimization_notes = explain_optimization(problems)

            score_col, metrics_col = st.columns([1, 1.35])

            with score_col:
                st.subheader("Overall Quality")
                if total_score >= 85:
                    score_note = "Strong prompt"
                elif total_score >= 65:
                    score_note = "Usable, with room to improve"
                else:
                    score_note = "Needs more structure"
                st.metric("Score", f"{total_score}/100", score_note)

            with metrics_col:
                st.subheader("Dimension Metrics")
                for metric_name, score_value in metrics_dict.items():
                    st.markdown(
                        f"""
                        <div class="dim-row">
                            <span class="dim-name">{metric_name}</span>
                            <span class="dim-score">{score_value}/100</span>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    st.progress(score_value / 100)

            st.divider()
            diagnosis_col, prompt_col = st.columns([1, 1.3])

            with diagnosis_col:
                st.subheader("Diagnosis")
                if problems:
                    for problem in problems:
                        st.warning(problem)
                else:
                    st.success("No major prompt problems detected.")

                st.subheader("What Changed")
                for note in optimization_notes:
                    st.write(f"- {note}")

            with prompt_col:
                st.subheader("Optimized Prompt")
                st.code(optimized_prompt, language="markdown")

            save_history(user_prompt, total_score, optimized_prompt)
            st.success("Saved to history.")

with tab_templates:
    st.subheader("Prompt Template Library")
    st.markdown(
        "<p class='section-note'>Choose a category and reuse a structured prompt template.</p>",
        unsafe_allow_html=True
    )

    category_col, template_col = st.columns(2)
    with category_col:
        selected_category = st.selectbox("Category", list(PROMPT_TEMPLATES.keys()))
    with template_col:
        selected_template_name = st.selectbox(
            "Template",
            list(PROMPT_TEMPLATES[selected_category].keys())
        )

    final_template_text = PROMPT_TEMPLATES[selected_category][selected_template_name]
    st.code(final_template_text.strip(), language="markdown")

with tab_history:
    st.subheader("Prompt History")
    st.markdown(
        "<p class='section-note'>Recent prompts saved from the analyzer workflow.</p>",
        unsafe_allow_html=True
    )

    history_df = read_history()
    if history_df.empty:
        st.info("No prompt history yet.")
    else:
        history_df = history_df.sort_values("time", ascending=False)
        st.dataframe(
            history_df[["time", "score", "original_prompt", "optimized_prompt"]],
            use_container_width=True,
            hide_index=True
        )
