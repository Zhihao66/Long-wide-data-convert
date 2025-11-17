# 🚀 启动指南 / Getting Started Guide

## ⏱️ 5分钟快速启动

### 第1步：验证安装（1分钟）

```powershell
# 进入项目目录
cd e:\数据转换

# 检查项目结构
dir
```

你应该看到类似的结构：
```
data_transformer/    (项目包)
tests/              (测试)
docs/               (文档)
.github/            (GitHub Actions)
README.md, README_CN.md, ...  (文档文件)
```

### 第2步：本地测试（2分钟）

```powershell
# 安装项目（开发模式）
pip install -e .

# 验证安装成功
data-transformer --help

# 运行示例
python example.py
```

### 第3步：更新信息（1分钟）

编辑 `pyproject.toml`，找到并修改：

```toml
# 第 9-10 行
authors = [
    {name = "你的名字", email = "你的邮箱@example.com"}
]

# 第 32-34 行
[project.urls]
Homepage = "https://github.com/你的用户名/data-transformer"
Repository = "https://github.com/你的用户名/data-transformer.git"
"Bug Tracker" = "https://github.com/你的用户名/data-transformer/issues"
```

### 第4步：推送到 GitHub（1分钟）

```powershell
# 初始化 Git
git init
git add .
git commit -m "feat: initial project setup with wide-long format converter"

# 添加远程仓库（用你的用户名替换）
git remote add origin https://github.com/你的用户名/data-transformer.git
git branch -M main
git push -u origin main
```

**Done! 🎉** 你的项目现在在 GitHub 上了！

---

## 📖 详细文档导航

根据你的需要选择阅读：

### 👤 我是新手用户
→ 阅读 [README_CN.md](README_CN.md) 了解项目是什么

### 💻 我想立即使用
→ 阅读 [docs/QUICKSTART.md](docs/QUICKSTART.md) 快速上手

### 🔌 我想调用 API
→ 阅读 [docs/API.md](docs/API.md) 查看完整接口

### 📋 我想快速参考
→ 使用 [QUICK_REFERENCE.md](QUICK_REFERENCE.md) 查询

### 🚀 我想部署到 GitHub
→ 按照 [DEPLOYMENT.md](DEPLOYMENT.md) 逐步操作

### 🤝 我想贡献代码
→ 阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 参与开发

### ✅ 我想检查完成度
→ 查看 [PROJECT_CHECKLIST.md](PROJECT_CHECKLIST.md) 交付清单

### 📊 我想了解整体情况
→ 阅读 [SUMMARY.md](SUMMARY.md) 项目总结

---

## 🎯 常见任务

### 运行代码

```powershell
# 安装项目
pip install -e .

# 运行示例
python example.py

# 运行 CLI
data-transformer wide-to-long input.csv output.csv --id-vars id,name
```

### 测试代码

```powershell
# 运行所有测试
pytest tests/ -v

# 运行特定测试
pytest tests/test_converter.py::TestDataTransformer::test_wide_to_long -v

# 生成覆盖率报告
pytest tests/ --cov=data_transformer --cov-report=html
```

### 开发代码

```powershell
# 格式化代码
black data_transformer/ tests/

# 检查代码风格
flake8 data_transformer/ tests/

# 整理 import
isort data_transformer/ tests/
```

### 推送代码

```powershell
# 查看改动
git status

# 添加改动
git add .

# 创建提交
git commit -m "feat: description of your changes"

# 推送到 GitHub
git push
```

---

## 🆘 遇到问题？

### 问题 1: 找不到命令 `data-transformer`

**解决**：确保已安装项目
```powershell
pip install -e .
```

### 问题 2: pytest 找不到模块

**解决**：运行以下命令
```powershell
pip install pytest pandas openpyxl
```

### 问题 3: 推送时认证失败

**解决**：使用 Personal Access Token
1. 访问 https://github.com/settings/tokens
2. 创建 `repo` 权限的 token
3. 推送时用 token 代替密码

### 问题 4: 想要修改项目名

**解决**：需要修改以下文件：
```
pyproject.toml       - name 字段
README.md           - 所有 data-transformer 引用
DEPLOYMENT.md       - GitHub URLs
GitHub 仓库名称      - 重命名仓库
```

---

## 🎓 学习路径

### 初级（了解基础）
1. 阅读 README_CN.md
2. 看理论基础部分
3. 查看使用示例

### 中级（学会使用）
1. 跟随 QUICKSTART.md 操作
2. 运行 example.py
3. 自己编写转换代码

### 高级（参与开发）
1. 阅读源代码 (converter.py)
2. 运行测试 (test_converter.py)
3. 按 CONTRIBUTING.md 贡献新功能

---

## 📊 项目统计

```
📦 项目类型：        Python 数据处理工具
🎯 主要功能：        宽/长格式数据转换
📝 代码行数：        ~450 行
📚 文档行数：        ~3000 行
🧪 测试覆盖：        主要功能全覆盖
📋 文件数：          25+ 文件
🏷️ 许可证：          MIT
🌍 语言：           中文/英文
```

---

## ⚡ 快速命令

```powershell
# 安装
pip install -e .

# 测试
pytest tests/ -v

# 示例
python example.py

# CLI 帮助
data-transformer --help

# 初始化 Git
.\init_github.bat

# 推送代码
git push
```

---

## 📞 获取帮助

- 📖 [完整文档](README_CN.md)
- 🚀 [部署指南](DEPLOYMENT.md)
- 💬 [提交 Issue](https://github.com/你的用户名/data-transformer/issues)
- ✨ [查看示例](example.py)

---

## 🎉 下一步

完成以上步骤后，你可以：

1. ✅ 在本地使用这个工具
2. ✅ 在 GitHub 上发布项目
3. ✅ 邀请他人使用和贡献
4. ✅ 发布到 PyPI（可选）
5. ✅ 建立一个开源项目社区

---

**祝你使用愉快！有问题可以查看相关文档。** 📚

**让数据转换变得简单！** 🚀
