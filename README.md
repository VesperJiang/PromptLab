# PromptLab: AI Prompt Engineering Studio

PromptLab is a web-based prompt engineering toolkit designed to help users diagnose, score, optimize, and manage prompts for large language models. The project aims to make prompt writing more structured, more explainable, and easier for non-experts to improve.

## Problem Statement

Many users receive unsatisfactory AI responses because their prompts are vague, incomplete, or lack clear requirements. Common issues include:
- Task descriptions that are too vague or ambiguous
- No specification of output format (table, code, markdown, etc.)
- Missing role definitions ("you are a teacher", "you are a programmer")
- No constraints (length, tone, style, deadline)
- No way to compare or reuse successful prompting patterns

PromptLab addresses these problems by providing a structured workflow for prompt diagnosis, scoring, optimization, and template reuse.

## Project Objectives

- Help users write higher-quality prompts with less trial and error.
- Provide a simple and explainable scoring system for prompt quality.
- Support prompt optimization, template reuse, and version history management.
- Encourage better prompt engineering habits among students, creators, and professionals.

## Core Features

1. **Prompt Diagnosis**: Checks whether a prompt includes essential elements such as role, task, context, constraints, and output format.

2. **Prompt Scoring**: Evaluates prompt quality across multiple dimensions, including clarity, completeness, context, constraints, and output format.

3. **Prompt Optimization**: Generates an improved version of the original prompt and explains the main changes.

4. **Prompt Template Library**: Provides reusable templates for learning, programming, office work, writing, and content creation.

5. **Prompt History and Versioning**: Saves prompt records so users can compare earlier and later versions.

## Technology Stack

- Python
- Streamlit (frontend)
- Quarto (report generation)
- Git (version control)
- CSV and SQLite (lightweight data storage)

## Lessons Learned

Throughout this project, we encountered several key challenges that taught us important lessons:

1. **API integration trade-offs**: We initially planned to use real LLM APIs for scoring and optimization, but switched to a rule-based approach due to cost, security, and network constraints. This turned out to make the system more explainable and demo-friendly.

2. **Survey limitations**: With only 30 survey responses, we learned to focus on qualitative trends rather than statistical significance. The clear patterns in the data validated our approach despite the small sample.

3. **Integration complexity**: Building a real-time interactive demo required careful attention to state management and data flow. Simplifying the architecture early saved us significant debugging time later.

4. **Team coordination**: A structured Git workflow with clear role assignments and documented conventions was essential for smooth collaboration across four members with different technical backgrounds.

## Team Members

| Member | Name | Student ID | College | Role | Primary Responsibilities |
|---|---|---|---|---|---|
| A | 姜姗 (Jiang Shan) | 202420119007 | 信息科学技术学院 | Technical Lead / Backend | Prompt analysis, scoring, and optimization logic |
| B | 杨琦彧 (Yang Qiyu) | 202420119020 | 信息科学技术学院 | Frontend / Demo Lead | Streamlit interface and live demonstration |
| C | (TBD) | (TBD) | (TBD) | Data & Evaluation Lead | Surveys, prompt testing, and evaluation analysis |
| D | 刘璟暄 (Liu Jingxuan) | 202520105002 | 法语语言文化学院 | Product & Report Lead | Documentation, final report, marketing, and integration |

## Repository Contents

| File | Description |
|---|---|
| `report.qmd` | Quarto source file for the final PDF report |
| `final_report.pdf` | Generated PDF version of the final report |
| `references.bib` | BibTeX reference entries |
| `.gitignore` | Git ignore rules (includes Quarto and Python artifacts) |
| `app.py` | Streamlit application entry point |
| `src/` | Core Python modules (analyzer, optimizer, templates) |
| `data/` | Survey results and test prompt data |
| `docs/` | Supporting documentation and deliverables |
| `tests/` | Test suite |

## Quick Links

- **Report Source (QMD)**: [report.qmd](./report.qmd)
- **Final Report (PDF)**: [final_report.pdf](./final_report.pdf)
- **Survey Results**: [data/survey_results.csv](./data/survey_results.csv)
- **Test Prompts**: [data/test_prompts.csv](./data/test_prompts.csv)
- **Project Documentation**: [docs/](./docs/)

## How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

## How to Generate the PDF Report

```bash
# Render the Quarto report to PDF
quarto render report.qmd --to pdf
```

## Submission

This repository is submitted as the final project for SUM26001 — International Summer School, Beijing Foreign Studies University.  
Submitted to: [https://classproject-iss-bfsu.azurewebsites.net/report/](https://classproject-iss-bfsu.azurewebsites.net/report/)  
Submission deadline: July 25, 2026