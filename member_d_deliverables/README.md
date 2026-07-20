# Member D Deliverables for PromptLab

This folder contains the final submission package for the project.

## Source of Truth

The **primary report source** is maintained at the repository root:
- **`report.qmd`**: Quarto source file for the final PDF report (root directory)
- **`README.md`**: Project description, team info, and submission links (root directory)
- **`docs/`**: Supporting documentation (project background, user personas, system design, marketing plan, git contribution, pitch outline)

This `member_d_deliverables/` directory is a **packaged copy** for submission convenience.

## Contents

| File | Description |
|---|---|
| `README.md` | This file — deliverables overview |
| `RELEASE_ASSETS.md` | Asset inventory and generation notes |
| `final_report.md` | Report markdown source (copy from docs/) |

## Related Files (in Repository Root)

| File | Description |
|---|---|
| `report.qmd` | **Quarto source** for generating final_report.pdf |
| `final_report.pdf` | **Generated PDF** of the final report |
| `references.bib` | BibTeX references |
| `.gitignore` | Git ignore rules |

## Quick Links for Submission

- **GitHub Repository**: [https://github.com/VesperJiang/PromptLab](https://github.com/VesperJiang/PromptLab)
- **Report QMD Source**: [`report.qmd`](../report.qmd)
- **Final Report PDF**: [`final_report.pdf`](../final_report.pdf)
- **README**: [`README.md`](../README.md)

## PDF Generation (if regenerating)

```bash
# Requires Quarto + TinyTeX installed
quarto install tinytex   # One-time setup
quarto render report.qmd --to pdf
```

## Submission Notes

This package supports the SUM26001 final project submission.  
Submitted to: [https://classproject-iss-bfsu.azurewebsites.net/report/](https://classproject-iss-bfsu.azurewebsites.net/report/)  
Also submitted to BSFU Blackboard.
