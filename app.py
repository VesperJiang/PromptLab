import streamlit as st
import pandas as pd
import os
from datetime import datetime

# ==========================================
# 0. Backend & Data Module Integration
# ==========================================
from src.prompt_analyzer import diagnose_prompt, score_prompt
from src.prompt_optimizer import optimize_prompt, explain_optimization
from src.prompt_templates import PROMPT_TEMPLATES

# ==========================================
# 1. Page Configuration
# ==========================================
st.set_page_config(
    page_title="PromptLab",
    layout="wide"
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
# 4. Tab 1: Prompt Analyzer
# ==========================================
with tab1:
    st.subheader("Input Your Raw Prompt")
    st.write("Submit your unoptimized text below. Our diagnostic engine will evaluate its quality against structural engineering principles.")

    user_prompt = st.text_area(
        "Enter your prompt below to diagnose and optimize:",
        height=180,
        placeholder="Example: Help me write an article about AI..."
    )
    
    analyze_btn = st.button("Analyze and Optimize", type="primary")
    
    if analyze_btn:
        if not user_prompt.strip():
            st.warning("Boundary Check: Please enter a prompt first before initiating analysis.")
        else:
            st.success("Form submission captured successfully. Passing telemetry to the AI engine.")
            
            st.markdown("---")
            evaluation_result = score_prompt(user_prompt)
            total_score = evaluation_result["score"]
            metrics_dict = evaluation_result["dimension_scores"]

            col_score, col_progress = st.columns([1, 2])

            with col_score:
                st.subheader("Overall Quality")
                score_gap = total_score - 100
                st.metric(
                    label="Evaluation Score", 
                    value=f"{total_score} / 100", 
                    delta=f"{score_gap} pts below parity" if score_gap < 0 else "Optimal Quality"
                )

            with col_progress:
                st.subheader("Dimension Metrics")
                for metric_name, score_value in metrics_dict.items():
                    st.write(f"**{metric_name}**: {score_value} / 100")
                    st.progress(score_value / 100)

# ==========================================
# 5. Tab 2: Prompt Template Library
# ==========================================
with tab2:
    st.subheader("Enterprise Prompt Templates")
    st.write("Browse and select verified, production-ready system prompt templates across multiple domains.")
    
    template_col1, template_col2 = st.columns([1, 2])
    
    with template_col1:
        categories = list(PROMPT_TEMPLATES.keys())
        selected_category = st.selectbox("Select Template Category", categories)
        
        available_templates = PROMPT_TEMPLATES[selected_category]
        template_names = list(available_templates.keys())
        selected_template_name = st.selectbox("Select Target Template", template_names)
        
    with template_col2:
        st.subheader("Template Content Preview")
        final_template_text = available_templates[selected_template_name]
        st.code(final_template_text.strip(), language="markdown")

# ==========================================
# 6. Tab 3: Market Survey Insights 
# ==========================================
with tab3:
    st.subheader("Market Survey & Analytical Insights")
    st.write("Quantitative telemetry fetched from the team data infrastructure regarding prompt engineering pain points.")
    
    # 定义图表根目录
    image_base_path = "docs/images"
    
    # 建立多行并排网格系统布局
    grid_row1_col1, grid_row1_col2 = st.columns(2)
    grid_row2_col1, grid_row2_col2 = st.columns(2)
    
    # 1. 渲染图1：AI使用频率 (饼图)
    with grid_row1_col1:
        st.markdown("**1. AI Tool Usage Frequency**")
        img1_path = os.path.join(image_base_path, "ai_usage.png")
        if os.path.exists(img1_path):
            st.image(img1_path, use_container_width=True)
        else:
            st.caption("Telemetry stream pending initialization.")

    # 2. 渲染图2：写Prompt困难程度 (柱状图)
    with grid_row1_col2:
        st.markdown("**2. Prompt Engineering Difficulty Distribution**")
        img2_path = os.path.join(image_base_path, "difficulty.png")
        if os.path.exists(img2_path):
            st.image(img2_path, use_container_width=True)
        else:
            st.caption("Telemetry stream pending initialization.")

    # 3. 渲染图3：用户痛点分布 (柱状图)
    with grid_row2_col1:
        st.markdown("**3. Core User Pain Points Distribution**")
        img3_path = os.path.join(image_base_path, "pain_points.png")
        if os.path.exists(img3_path):
            st.image(img3_path, use_container_width=True)
        else:
            st.caption("Telemetry stream pending initialization.")

    # 4. 渲染图4：最想要的功能 (柱状图)
    with grid_row2_col2:
        st.markdown("**4. High-Demand Feature Requirements**")
        img4_path = os.path.join(image_base_path, "features.png")
        if os.path.exists(img4_path):
            st.image(img4_path, use_container_width=True)
        else:
            st.caption("Telemetry stream pending initialization.")

    st.markdown("---")
    
    # 5. 单独用居中或宽幅渲染图5：使用意愿 (饼图)
    st.markdown("**5. Target User Adoption Willingness for PromptLab**")
    img5_path = os.path.join(image_base_path, "willingness.png")
    if os.path.exists(img5_path):
        # 限制一下宽度，防止饼图被拉得太大变形
        st.image(img5_path, width=600)
    else:
        st.caption("Telemetry stream pending initialization.")
        
    st.markdown("---")
    st.info("Analytical Conclusion: The visualization metrics above validate the substantial market viability and user demand for PromptLab automation tools.")