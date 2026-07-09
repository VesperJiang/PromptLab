import streamlit as st
import pandas as pd
from datetime import datetime

from src.prompt_analyzer import diagnose_prompt, score_prompt
from src.prompt_optimizer import optimize_prompt, explain_optimization
from src.prompt_templates import PROMPT_TEMPLATES


st.set_page_config(
    page_title="PromptLab",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 PromptLab: AI Prompt Engineering Studio")
st.write("Diagnose, score, optimize, and manage your prompts.")

tab1, tab2, tab3 = st.tabs([
    "Prompt Analyzer",
    "Prompt Template Library",
    "About"
])

with tab1:
    st.header("Prompt Analyzer")

    user_prompt = st.text_area(
        "Enter your prompt:",
        height=180,
        placeholder="Example: Help me write an article about AI."
    )

    if st.button("Analyze and Optimize"):
        if not user_prompt.strip():
            st.warning("Please enter a prompt first.")
        else:
            result = score_prompt(user_prompt)
            problems = result["problems"]
            score = result["score"]
            optimized = optimize_prompt(user_prompt)
            explanations = explain_optimization()

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Prompt Score")
                st.metric("Score", f"{score}/100")

                st.subheader("Diagnosis")
                if problems:
                    for problem in problems:
                        st.write(f"❌ {problem}")
                else:
                    st.success("No major problems found.")

            with col2:
                st.subheader("Optimized Prompt")
                st.code(optimized, language="markdown")

                st.subheader("What was improved?")
                for item in explanations:
                    st.write(f"✅ {item}")

            history_data = {
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "original_prompt": user_prompt,
                "score": score,
                "optimized_prompt": optimized
            }

            try:
                old_data = pd.read_csv("data/history.csv")
                new_data = pd.concat([old_data, pd.DataFrame([history_data])], ignore_index=True)
            except Exception:
                new_data = pd.DataFrame([history_data])

            new_data.to_csv("data/history.csv", index=False)

            st.success("Prompt record saved to history.")

with tab2:
    st.header("Prompt Template Library")

    category = st.selectbox(
        "Choose a category:",
        list(PROMPT_TEMPLATES.keys())
    )

    template_name = st.selectbox(
        "Choose a template:",
        list(PROMPT_TEMPLATES[category].keys())
    )

    st.subheader(template_name)
    st.code(PROMPT_TEMPLATES[category][template_name], language="markdown")

with tab3:
    st.header("About PromptLab")

    st.write("""
PromptLab is a lightweight AI prompt engineering tool.

It helps users:
- diagnose common prompt problems;
- score prompt quality;
- optimize vague prompts;
- reuse prompt templates;
- save prompt history.

This project focuses on solving a real problem: many users do not know how to write clear and effective prompts for AI tools.
""")