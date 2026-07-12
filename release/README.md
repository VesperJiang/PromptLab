Final release files for PromptLab.

To generate the PDF report locally (requires `pandoc` and a LaTeX engine such as `xelatex`):

```bash
# Install pandoc (macOS with Homebrew):
brew install pandoc
# Install a TeX distribution if needed (MacTeX recommended):
# https://www.tug.org/mactex/

# Convert markdown to PDF:
pandoc docs/final_report.md -o release/final_report.pdf --pdf-engine=xelatex
```

If you'd like, I can attempt alternative PDF generation methods here, but they may require additional system packages. If you want me to proceed, confirm and I'll try creating a simple PDF fallback.
