# 项目部署指南 / GitHub Deployment Guide

## 项目结构

```
data-transformer/
├── data_transformer/           # 主包
│   ├── __init__.py            # 包初始化
│   ├── converter.py           # 核心转换模块
│   └── cli.py                 # 命令行界面
├── tests/                      # 测试目录
│   ├── __init__.py
│   └── test_converter.py      # 单元测试
├── docs/                       # 文档目录
│   ├── API.md                 # API 文档
│   └── QUICKSTART.md          # 快速开始指南
├── .github/workflows/          # GitHub Actions
│   └── tests.yml              # CI/CD 工作流
├── example.py                  # 使用示例
├── pyproject.toml             # 项目配置
├── README.md                   # 项目说明
├── LICENSE                     # MIT 许可证
├── CONTRIBUTING.md            # 贡献指南
├── .gitignore                 # Git 忽略文件
└── DEPLOYMENT.md              # 本文件
```

## GitHub 部署步骤

### 第一步：创建 GitHub 仓库

1. 访问 https://github.com/new
2. 填写仓库信息：
   - Repository name: `data-transformer`
   - Description: "A tool for converting between wide and long format data"
   - 选择 "Public" (如果希望其他人使用)
   - 不要初始化任何文件（因为我们已经有本地文件）
3. 点击 "Create repository"

### 第二步：初始化 Git 并推送代码

在本地项目目录执行：

```powershell
# 初始化 Git 仓库
git init

# 添加所有文件
git add .

# 首次提交
git commit -m "feat: initial project setup with wide-long format converter"

# 添加远程仓库
git remote add origin https://github.com/yourusername/data-transformer.git

# 推送到 GitHub
git branch -M main
git push -u origin main
```

### 第三步：配置 GitHub 设置

1. 进入仓库的 "Settings" → "General"
   - 勾选 "Automatically delete head branches"
   - 勾选 "Allow squash merging"

2. 进入 "Settings" → "Branches"
   - 设置 main 分支为受保护分支
   - 要求代码审查
   - 要求检查通过

3. 进入 "Settings" → "Actions"
   - 允许所有 Actions

### 第四步：发布到 PyPI（可选）

#### 准备步骤

1. 在 pyproject.toml 中更新作者信息
2. 创建 `__version__.py`：

```python
# data_transformer/__version__.py
__version__ = "1.0.0"
```

3. 更新 `__init__.py`：

```python
from .__version__ import __version__
```

#### 发布步骤

1. 创建 GitHub Release：
   - 访问 https://github.com/yourusername/data-transformer/releases
   - 点击 "Create a new release"
   - Tag version: `v1.0.0`
   - Release title: `Version 1.0.0`
   - 点击 "Publish release"

2. 安装 build 工具：
```bash
pip install build twine
```

3. 构建包：
```bash
python -m build
```

4. 上传到 PyPI：
```bash
python -m twine upload dist/*
```

5. 验证发布：
```bash
pip install data-transformer
```

### 第五步：启用 GitHub Pages（可选）

1. 进入 "Settings" → "Pages"
2. Source 选择 "Deploy from a branch"
3. 选择 "main" 分支和 "/docs" 文件夹
4. 保存

## CI/CD 工作流说明

`.github/workflows/tests.yml` 会在以下情况自动执行：

- 推送到 main 或 develop 分支
- 创建 Pull Request

工作流包括：
- 在 Python 3.8, 3.9, 3.10, 3.11 上运行测试
- 代码风格检查 (flake8)
- 代码覆盖率报告

## 常用命令

### 本地开发

```powershell
# 安装依赖
pip install -e ".[dev]"

# 运行测试
pytest tests/ -v

# 运行示例
python example.py

# 命令行工具测试
data-transformer --help
```

### Git 常用命令

```powershell
# 查看状态
git status

# 查看日志
git log --oneline

# 创建新分支
git checkout -b feature/new-feature

# 切换分支
git checkout main

# 合并分支
git merge feature/new-feature

# 删除分支
git branch -d feature/new-feature
```

## 添加其他 GitHub 功能

### 添加 Badge（徽章）

在 README.md 中添加：

```markdown
[![CI Status](https://github.com/yourusername/data-transformer/workflows/Tests/badge.svg)](https://github.com/yourusername/data-transformer/actions)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PyPI Version](https://img.shields.io/pypi/v/data-transformer.svg)](https://pypi.org/project/data-transformer/)
```

### 添加代码覆盖率

1. 注册 [Codecov](https://codecov.io)
2. 连接 GitHub 账户
3. Codecov 会自动从 CI 中收集覆盖率数据

## 项目维护清单

- [ ] 更新 pyproject.toml 中的作者信息
- [ ] 创建 GitHub 仓库
- [ ] 推送代码到 GitHub
- [ ] 配置分支保护规则
- [ ] 验证 CI/CD 工作流运行成功
- [ ] 发布到 PyPI（可选）
- [ ] 添加 README badges
- [ ] 设置 GitHub Pages（可选）

## 故障排除

### 推送时出错

```powershell
# 如果远程仓库有历史记录，使用：
git pull origin main --allow-unrelated-histories
git push -u origin main
```

### 测试失败

检查：
1. Python 版本是否符合要求（3.8+）
2. 依赖是否已安装：`pip list`
3. 运行 `pytest tests/ -v` 查看详细错误

### PyPI 上传失败

1. 检查 pyproject.toml 配置
2. 确保使用了正确的 PyPI token
3. 检查版本号未被使用过

## 后续改进

- [ ] 添加更多数据格式支持（XML, Parquet 等）
- [ ] 性能优化（处理大文件）
- [ ] 添加 Web 界面
- [ ] 国际化支持
- [ ] 更完善的错误处理和日志

---

祝您的项目成功！🚀
