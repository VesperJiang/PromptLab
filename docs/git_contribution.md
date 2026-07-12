# Git Contribution & Release Guide — PromptLab

## 目标
提供清晰的分支策略、提交规范、Pull Request 流程，以及如何在本项目中本地运行、测试和发布小版本，以便团队成员（尤其是非技术成员）也能参与协作。

## 基本约定
- 主分支：`main` — 可部署的稳定分支
- 开发分支：`dev`（可选） — 用于集成中期工作
- 功能分支：`feature/{short-description}` — 每个新功能或文档在独立分支上实现
- 修复分支：`fix/{issue-id-or-desc}`
- 发布分支：`release/{version}` — 用于准备发布
- 标签格式：`vMAJOR.MINOR.PATCH`（例如 `v1.0.01`）

## 提交信息规范
使用简洁的一行 header，加可选详细 body。
格式举例：

- Header：`type(scope): short summary`
  - `type`：`feat`、`fix`、`docs`、`chore`、`test`、`refactor`
  - `scope`：可选模块或文件名，比如 `docs`、`app`、`api`

示例：
- `docs: add project background`
- `feat(api): add /api/score endpoint`

## Pull Request 流程
1. 从 `main` 或 `dev` 创建功能分支：

```bash
git checkout -b feature/add-marketing-plan main
```

2. 完成工作后提交并推送分支：

```bash
git add .
git commit -m "docs: add marketing plan"
git push -u origin feature/add-marketing-plan
```

3. 在 GitHub 上创建 PR，选择 reviewers（至少 1 人），并在 PR 描述中列出变更点与测试方法。
4. 通过 CI 检查（如有），获得批准后合并到 `main` 或 `dev`。

## 本地运行项目（快速开始）
1. 建议使用 Python 3.10+ 虚拟环境：

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. 运行 Streamlit UI（开发）：

```bash
streamlit run app.py
```

3. 运行测试：

```bash
pytest -q
```

## 发布新版本（示例流程）
1. 从 `main` 创建发布分支并更新版本号（例如 `v1.0.02`）：

```bash
git checkout -b release/v1.0.02 main
# 更新版本号（README 或其他需要的地方）
git commit -am "chore(release): bump version to v1.0.02"
```

2. 合并到 `main` 并打标签：

```bash
git checkout main
git merge --no-ff release/v1.0.02
git tag -a v1.0.02 -m "Release v1.0.02"
git push origin main --tags
```

3. 可选：在 GitHub Releases 页面发布 release notes。

## 如何处理远程冲突（常见场景）
- 在推送前先 fetch & rebase：

```bash
git fetch origin
git rebase origin/main
```

- 若遇不可自动解决的冲突，手动解决冲突后 `git rebase --continue`，然后 `git push --force-with-lease`。

## 非技术成员快速贡献（文档/营销）
- 文档变更可直接使用 `docs/` 下的文件。
- 推荐工作流：
  1. 在 GitHub 上直接编辑文件并提交分支。
  2. 创建 PR 并在描述中注明目的与要点。

## CI / 测试建议（可选）
- 建议添加 GitHub Actions：
  - `lint`（flake8/isort/black）
  - `test`（pytest）
  - `build`（如果需要构建部署镜像）

## 安全与敏感信息
- 不要将 API keys 或凭证提交到仓库。使用 `.env` 或 GitHub Secrets。
- 添加 `.env.example` 以示例形式展示所需环境变量。


## 常见命令速查
```bash
# 更新本地 main
git checkout main
git pull origin main

# 创建并推送分支
git checkout -b feature/your-feature
git push -u origin feature/your-feature

# 合并 release
git checkout main
git merge --no-ff release/vX.Y.Z
git tag -a vX.Y.Z -m "Release vX.Y.Z"
git push origin main --tags
```

