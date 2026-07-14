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
# 2. Premium Light-Theme CSS Injection
# ==========================================
st.markdown("""
    <style>
        /* 1. 全局黑底白字 */
        .stApp {
            background-color: #000000 !important;
            color: #FFFFFF !important;
        }

        /* 2. 标题层级深色适配 */
        h1 {
            color: #F5F5F5 !important;
            font-weight: 800 !important;
            font-size: 2.6rem !important;
            margin-bottom: 0.2rem !important;
        }
        h2, h3 {
            color: #E0E0E0 !important;
            font-weight: 600 !important;
            margin-top: 1.5rem !important;
        }

        /* Tab深色模式样式 */
        .stTabs [data-baseweb="tab"] {
            border: 1px solid #555555 !important;
            background-color: #222222 !important;
            padding: 0 !important;
            border-radius: 4px !important;
            margin: 0 4px !important;
            overflow: hidden !important;
        }
        .stTabs [data-baseweb="tab"] div[role="tab"] button,
        .stTabs [data-baseweb="tab"] button {
            color: #FFFFFF !important;
            padding: 8px 16px !important;
            background: transparent !important;
            font-size: 1rem !important;
        }
        /* hover悬浮 */
        .stTabs [data-baseweb="tab"]:hover div[role="tab"] button,
        .stTabs [data-baseweb="tab"]:hover button {
            color: #ff3333 !important;
        }
        .stTabs [data-baseweb="tab"]:hover {
            border-color: #777777 !important;
        }
        /* 选中Tab */
        .stTabs [data-baseweb="tab"][aria-selected="true"] {
            background-color: #333333 !important;
            border: 1px solid #777777 !important;
        }
        .stTabs [data-baseweb="tab"][aria-selected="true"] div[role="tab"] button,
        .stTabs [data-baseweb="tab"][aria-selected="true"] button {
            color: #66aaff !important;
        }
        .stTabs [data-baseweb="tab-list"] {
            gap: 6px !important;
        }
        .stTabs [data-baseweb="tab-highlight"] {
            display: none !important;
        }

        /* Metric指标深色适配 */
        [data-testid="stMetricValue"] {
            color: #F5F5F5 !important;
            font-size: 4.4rem !important;
            font-weight: 800 !important;
            line-height: 1 !important;
        }
        [data-testid="stMetricDelta"] {
            color: #ff6666 !important;
            background-color: #2A1010 !important;
            padding: 2px 8px !important;
            border-radius: 4px !important;
            font-size: 0.9rem !important;
            font-weight: 600 !important;
        }

        /* 进度条深色 */
        .stProgress > div > div > div > div {
            background-color: #66aaff !important;
            height: 10px !important;
            border-radius: 8px !important;
        }

        /* 维度文字深色 */
        .dim-name {
            color: #E0E0E0 !important;
            font-weight: 600 !important;
            font-size: 0.95rem !important;
        }
        .dim-score {
            color: #BBBBBB !important;
            font-size: 0.88rem !important;
        }

        /* 输入框深色 */
        textarea {
            background-color: #1A1A1A !important;
            color: #FFFFFF !important;
            border: 1px solid #444444 !important;
        }
        .stButton>button {
            background-color: #224488 !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 4px !important;
            font-weight: 500 !important;
        }
        .stButton>button:hover {
            background-color: #112244 !important;
        }

        /* 图片保持原有逻辑 */
        .stImage>img {
            object-fit: contain !important;
            max-height: 340px !important;
            width: auto !important;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. Header Section
# ==========================================
# 使用更大的自定义主标题以提高醒目度（CSS 已同步放大）
st.markdown("<h1 style='margin:0 0 0.2rem 0;'>PromptLab: AI Prompt Engineering Studio</h1>", unsafe_allow_html=True)
# 副标题使用稍微淡一些的灰色进行视觉降噪
st.markdown("<p style='color: #4A4A4A; font-size: 1.05rem; margin-top: -0.5rem;'>An enterprise-grade web studio designed to diagnose, score, optimize, and manage system prompts.</p>", unsafe_allow_html=True)
st.markdown("---")

# ==========================================
# 4. Core Navigation Layout
# ==========================================
tab1, tab2, tab3 = st.tabs([
    "Prompt Analyzer", 
    "Template Library", 
    "Market Survey"
])

# ==========================================
# 5. Tab 1: Prompt Analyzer (评分与维度两列对齐优化)
# ==========================================
with tab1:
    st.subheader("Input Your Raw Prompt")
    st.markdown("<p style='color: #4A4A4A;'>Submit your unoptimized text below. Our diagnostic engine will evaluate its quality against structural engineering principles.</p>", unsafe_allow_html=True)

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
            
            # 调用后端核心函数
            evaluation_result = score_prompt(user_prompt)
            total_score = evaluation_result["score"]
            metrics_dict = evaluation_result["dimension_scores"]
            problems = evaluation_result.get("problems", diagnose_prompt(user_prompt))
            optimized_prompt = optimize_prompt(user_prompt, problems)
            optimization_notes = explain_optimization(problems)

            # 调整分栏比例为 [3, 2]：让 Overall 更宽、更突出，维度列表更精致紧凑
            col_score, col_progress = st.columns([3, 2])

            with col_score:
                st.subheader("Overall Quality")
                score_gap = total_score - 100
                
                # 使用 container 包裹，并留出 top margin 强行让主分数在视觉上与右侧进度条中轴对齐
                st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
                st.metric(
                    label="Evaluation Score",
                    value=f"{total_score} / 100",
                    delta=f"{score_gap} pts below parity" if score_gap < 0 else "Optimal Quality"
                )
                st.markdown("<p style='color: #6C757D; font-size: 0.85rem; margin-top: 1rem;'>The metric above integrates overall semantic structures and syntactical criteria.</p>", unsafe_allow_html=True)

            with col_progress:
                st.subheader("Dimension Metrics")
                st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
                # 动态循环遍历维度并渲染（名称与分数采用更小、更紧凑的视觉风格）
                for metric_name, score_value in metrics_dict.items():
                    # 左右小排版，使得名称和具体分数呈现在一行
                    prog_col_left, prog_col_right = st.columns([3, 1])
                    with prog_col_left:
                        st.markdown(f"<span class='dim-name'>{metric_name}</span>", unsafe_allow_html=True)
                    with prog_col_right:
                        st.markdown(f"<span class='dim-score'>{score_value} / 100</span>", unsafe_allow_html=True)
                    st.progress(score_value / 100)
                    st.markdown("<div style='margin-bottom: 0.6rem;'></div>", unsafe_allow_html=True)

            st.markdown("---")
            diag_col, opt_col = st.columns([2, 3])

            with diag_col:
                st.subheader("Diagnosis")
                if problems:
                    for problem in problems:
                        st.warning(problem)
                else:
                    st.success("No major prompt problems detected.")

                st.subheader("Optimization Notes")
                for note in optimization_notes:
                    st.write(f"- {note}")

            with opt_col:
                st.subheader("Optimized Prompt")
                st.code(optimized_prompt, language="markdown")

            history_data = {
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "original_prompt": user_prompt,
                "score": total_score,
                "optimized_prompt": optimized_prompt
            }

            try:
                old_data = pd.read_csv("data/history.csv")
                new_data = pd.concat([old_data, pd.DataFrame([history_data])], ignore_index=True)
            except Exception:
                new_data = pd.DataFrame([history_data])

            new_data.to_csv("data/history.csv", index=False)
            st.success("Prompt record saved to history.")

# ==========================================
# 6. Tab 2: Prompt Template Library
# ==========================================
with tab2:
    st.subheader("Enterprise Prompt Templates")
    st.markdown("<p style='color: #4A4A4A;'>Browse and select verified, production-ready system prompt templates across multiple domains.</p>", unsafe_allow_html=True)
    
    # 垂直布局：将选择器与预览垂直堆叠，避免横向占用空间
    with st.container():
        categories = list(PROMPT_TEMPLATES.keys())
        selected_category = st.selectbox("Select Template Category", categories)

        available_templates = PROMPT_TEMPLATES[selected_category]
        template_names = list(available_templates.keys())
        selected_template_name = st.selectbox("Select Target Template", template_names)

        st.subheader("Template Content Preview")
        final_template_text = available_templates[selected_template_name]
        st.code(final_template_text.strip(), language="markdown")

# ==========================================
# 7. Tab 3: Market Survey Insights (容器与自适应排版优化)
# ==========================================
with tab3:
    st.subheader("Market Survey & Analytical Insights")
    st.markdown("<p style='color: #4A4A4A;'>Quantitative telemetry fetched from the team data infrastructure regarding prompt engineering pain points.</p>", unsafe_allow_html=True)
    
    image_base_path = "docs/images"
    
    # 将整个大屏包裹进一个最大宽度受限的中央容器中，防止宽屏下两边图片无限横向失真拉伸
    with st.container():
        st.markdown("<div style='max-width: 1100px; margin: 0 auto;'>", unsafe_allow_html=True)
        
        # 建立优雅的两列网格布局，严格控制列的宽度和缩放
        grid_row1_col1, grid_row1_col2 = st.columns(2)
        grid_row2_col1, grid_row2_col2 = st.columns(2)
        
        # 1. 渲染图1：AI使用频率 (饼图)
        with grid_row1_col1:
            st.markdown("<p style='color: #2D3136; font-weight: 600;'>1. AI Tool Usage Frequency</p>", unsafe_allow_html=True)
            img1_path = os.path.join(image_base_path, "ai_usage.png")
            if os.path.exists(img1_path):
                # 调整第一张图宽度，使用CSS已设置的最大高度控制显示高度
                st.image(img1_path, use_container_width=False, width=650)
            else:
                st.caption("Telemetry stream pending initialization.")

        # 2. 渲染图2：写Prompt困难程度 (柱状图)
        with grid_row1_col2:
            st.markdown("<p style='color: #2D3136; font-weight: 600;'>2. Prompt Engineering Difficulty Distribution</p>", unsafe_allow_html=True)
            img2_path = os.path.join(image_base_path, "difficulty.png")
            if os.path.exists(img2_path):
                st.image(img2_path, use_container_width=True)
            else:
                st.caption("Telemetry stream pending initialization.")

        # 3. 渲染图3：用户痛点分布 (柱状图)
        with grid_row2_col1:
            st.markdown("<p style='color: #2D3136; font-weight: 600;'>3. Core User Pain Points Distribution</p>", unsafe_allow_html=True)
            img3_path = os.path.join(image_base_path, "pain_points.png")
            if os.path.exists(img3_path):
                st.image(img3_path, use_container_width=True)
            else:
                st.caption("Telemetry stream pending initialization.")

        # 4. 渲染图4：最想要的功能 (柱状图)
        with grid_row2_col2:
            st.markdown("<p style='color: #2D3136; font-weight: 600;'>4. High-Demand Feature Requirements</p>", unsafe_allow_html=True)
            img4_path = os.path.join(image_base_path, "features.png")
            if os.path.exists(img4_path):
                st.image(img4_path, use_container_width=True)
            else:
                st.caption("Telemetry stream pending initialization.")

        st.markdown("<hr style='border-top: 1px solid #E9ECEF;'>", unsafe_allow_html=True)
        
        # 5. 单独用居中或宽幅渲染图5：使用意愿 (饼图)
        st.markdown("<p style='color: #2D3136; font-weight: 600;'>5. Target User Adoption Willingness for PromptLab</p>", unsafe_allow_html=True)
        img5_path = os.path.join(image_base_path, "willingness.png")
        if os.path.exists(img5_path):
            # 将图5的展示宽度收紧，使其更加规整
            st.image(img5_path, width=450)
        else:
            st.caption("Telemetry stream pending initialization.")
            
        st.markdown("</div>", unsafe_allow_html=True)
        
    st.markdown("---")
    st.info("Analytical Conclusion: The visualization metrics above validate the substantial market viability and user demand for PromptLab automation tools.")
