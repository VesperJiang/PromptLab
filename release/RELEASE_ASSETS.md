# Release Assets — PromptLab

已收集到的发布资产：

- docs/project_background.md -> release/project_background.md
- docs/user_personas.md -> release/user_personas.md
- docs/marketing_plan.md -> release/marketing_plan.md
- docs/git_contribution.md -> release/git_contribution.md
- docs/final_report.md -> release/final_report.md
- docs/pitch_outline.md -> release/pitch_outline.md
- slides/simple_slides.md -> release/simple_slides.md

说明：
- 我已将源 Markdown 文件的拷贝放在 `release/` 中，供打包提交或制作演示使用。
- 系统上未安装 `pandoc`，因此我未能在此环境中生成 `release/final_report.pdf` 或 `release/promptlab_pitch.pptx`。

本地生成建议命令（需安装 pandoc 与 LaTeX 或 pandoc + PowerPoint 支持）：

```bash
# 生成 PDF 报告（需要 xelatex）
pandoc docs/final_report.md -o release/final_report.pdf --pdf-engine=xelatex

# 生成幻灯片 PPTX
pandoc slides/simple_slides.md -t pptx -o release/promptlab_pitch.pptx
```

需要我尝试使用其他简单方法生成 PDF（例如将 Markdown 转为 HTML 再打印为 PDF，或用 headless Chromium 渲染）吗？这些方法也可能不在当前环境可用。
