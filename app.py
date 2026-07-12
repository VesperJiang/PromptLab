import streamlit as st
import pandas as pd
from datetime import datetime

# ==========================================
# 0. Backend Integration
# ==========================================
from src.prompt_analyzer import diagnose_prompt, score_prompt
from src.prompt_optimizer import optimize_prompt, explain_optimization

# ==========================================
# 1. Page Configuration
# ==========================================
st.set_page_config(
    page_title="PromptLab",
    layout="wide"  # Wide layout provides an optimal dual-column presentation
)

# ==========================================
# 2. Header Section
# ==========================================
st.title("PromptLab: AI Prompt Engineering Studio")
st.caption("An enterprise-grade web studio designed to diagnose, score, optimize, and manage system prompts.")
st.markdown("---") 

# ==========================================
# 3. Core Navigation Layout
# ==========================================
tab1, tab2, tab3 = st.tabs([
    "Prompt Analyzer", 
    "Template Library", 
    "Market Survey"
])

# ==========================================
# 4. Tab 1: Prompt Analyzer (Core Form Building)
# ==========================================
with tab1:
    st.subheader("Input Your Raw Prompt")
    st.write("Submit your unoptimized text below. Our diagnostic engine will evaluate its quality against structural engineering principles.")

    # A spacious text area component for users to paste complex system prompts
    user_prompt = st.text_area(
        "Enter your prompt below to diagnose and optimize:",
        height=180,
        placeholder="Example: Help me write an article about AI..."
    )
    
    # Clean and prominent action button without unnecessary emoticons
    analyze_btn = st.button("Analyze and Optimize", type="primary")
    
    # Dynamic logic control and input boundary verification
    if analyze_btn:
        if not user_prompt.strip():
            # Intercept empty input to prevent sending invalid data to the backend module
            st.warning("Boundary Check: Please enter a prompt first before initiating analysis.")
        else:
            # Valid input captured, confirming state migration
            st.success("Form submission captured successfully. Passing telemetry to the AI engine.")
            
            # ==========================================
            # 3. Third Stage: Score Visualization
            # ==========================================
            st.markdown("---")
            
            # score_prompt returns a dictionary containing "score" and "dimension_scores"
            evaluation_result = score_prompt(user_prompt)
            total_score = evaluation_result["score"]
            metrics_dict = evaluation_result["dimension_scores"]

            # Establish a dual-column layout: Left for primary score, Right for fine-grained dimensions
            col_score, col_progress = st.columns([1, 2])

            with col_score:
                st.subheader("Overall Quality")
                # Calculate the numerical gap to provide a benchmark for optimization
                score_gap = total_score - 100
                st.metric(
                    label="Evaluation Score", 
                    value=f"{total_score} / 100", 
                    delta=f"{score_gap} pts below parity" if score_gap < 0 else "Optimal Quality"
                )

            with col_progress:
                st.subheader("Dimension Metrics")
                # Dynamic iteration through backend metrics (e.g., Clarity, Context, Constraints)
                for metric_name, score_value in metrics_dict.items():
                    st.write(f"**{metric_name}**: {score_value} / 100")
                    # st.progress requires a float boundary between 0.0 and 1.0
                    st.progress(score_value / 100)

# ==========================================
# 5. Tab 2 and Tab 3: Sandbox Placeholders
# ==========================================
with tab2:
    st.header("Prompt Template Library")
    st.info("Status: Sandbox. This section will present cross-domain high-quality templates with dynamic variables.")

with tab3:
    st.header("Market Survey Insights")
    st.info("Status: Sandbox. This section will visualize user pain points and analytical questionnaire statistics.")