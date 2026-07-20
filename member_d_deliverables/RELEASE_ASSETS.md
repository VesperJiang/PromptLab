# Release Assets — PromptLab (Member D Deliverables)

## Final Submission Inventory

| Asset | Source Location | Destination | Status |
|---|---|---|---|
| Project Background | `docs/project_background.md` | Repository root | ✅ Done |
| Product Story | `docs/product_story.md` | Repository root | ✅ Done |
| User Personas | `docs/user_personas.md` | Repository root | ✅ Done |
| System Design | `docs/system_design.md` | Repository root | ✅ Done |
| Marketing Plan | `docs/marketing_plan.md` | Repository root | ✅ Done |
| Git Contribution Guide | `docs/git_contribution.md` | Repository root | ✅ Done |
| Final Report (QMD) | `report.qmd` | Repository root | ✅ Done |
| Final Report (PDF) | Generated from `report.qmd` | Repository root | ✅ Done |
| Pitch Outline | `docs/pitch_outline.md` | Repository root | ✅ Done |
| Survey Results | `data/survey_results.csv` | Repository root | ✅ Done |
| Test Prompts | `data/test_prompts.csv` | Repository root | ✅ Done |
| README | `README.md` | Repository root | ✅ Done |
| .gitignore | `.gitignore` | Repository root | ✅ Done |

## Notes

- The **primary report source** is `report.qmd` (Quarto format) at the repository root.
- The **PDF report** is generated from `report.qmd` using Quarto + TinyTeX.
- Supporting documentation is maintained under `docs/`.
- Survey data and test prompts are in `data/`.

## Regeneration Commands

```bash
# Generate PDF report
quarto render report.qmd --to pdf

# Clean generated files
quarto clean report.qmd
```
