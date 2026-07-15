# Git Contribution & Release Guide — PromptLab

## 1. Project Collaboration Goal
This guide defines a simple and practical workflow for collaborating on PromptLab. It is designed for a student team where technical and non-technical members both contribute, and where documentation, data, and product thinking are as important as implementation.

## 2. Repository Structure
- app.py: main application entry point
- src/: core Python modules for analysis, optimization, templates, and evaluation
- docs/: project reports, planning documents, and submission materials
- data/: survey results and prompt history data
- tests/: basic testing files for the project

## 3. Branch Strategy
- main: stable branch for completed work
- feature/{short-name}: new features or documentation work
- fix/{short-name}: bug fixes or small corrections
- release/{version}: preparation for a release milestone

## 4. Commit Message Style
Use short, clear commit messages that describe the change clearly.

Examples:
- docs: add project background
- feat: implement prompt scoring workflow
- fix: resolve prompt parsing issue
- chore: update submission materials

## 5. Typical Workflow
1. Start from the current main branch.
2. Create a feature branch for the work.
3. Make changes, test locally, and review content.
4. Commit with a clear message.
5. Push the branch and open a pull request.
6. Review, merge, and keep the main branch clean.

Example:

```bash
git checkout main
git pull origin main
git checkout -b feature/add-marketing-plan
git add .
git commit -m "docs: add marketing plan"
git push -u origin feature/add-marketing-plan
```

## 6. Pull Request Checklist
Before opening a pull request, confirm that:
- the content is complete and logically organized
- the relevant documentation is updated
- any generated artifacts are in the expected folder
- the change is suitable for review by the rest of the team

## 7. Local Development Workflow

### Install dependencies
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run the app
```bash
streamlit run app.py
```

### Run tests
```bash
pytest -q
```

## 8. Release and Submission Process
For assignment or project milestone submission:
1. Make sure the main report source is complete.
2. Ensure the PDF report and supporting docs are generated.
3. Review the repository state and summarize the latest deliverables.
4. Push the final state to GitHub.

## 9. Contribution Roles in Practice
- Technical members: implement analysis and optimization logic.
- Data members: prepare survey data and evaluation results.
- Product and report members: maintain docs, presentation materials, and final submission package.
- All members: contribute to review, testing, and final polishing.

## 10. Notes for Non-Technical Contributors
- Documentation and presentation work can be done directly in the docs folder.
- When editing content, keep the writing clear, concise, and aligned with the overall project story.
- Use pull requests so the whole team can review changes before they are merged.

## 11. Practical Git Commands
```bash
# Update local main
git checkout main
git pull origin main

# Create a new branch
git checkout -b feature/your-feature

# Push branch
git push -u origin feature/your-feature

# Merge after review
git checkout main
git merge --no-ff feature/your-feature
```

