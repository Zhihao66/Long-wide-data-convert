# 贡献指南 / Contributing Guide

感谢您对本项目的兴趣！我们欢迎所有形式的贡献。

## 开始之前

1. Fork 本仓库
2. Clone 您的 fork：`git clone https://github.com/yourusername/data-transformer.git`
3. 创建新分支：`git checkout -b feature/your-feature-name`

## 设置开发环境

```bash
cd data-transformer
pip install -e ".[dev]"
```

## 代码规范

本项目遵循 PEP 8 规范。

### 代码格式化

```bash
# 自动格式化代码
black data_transformer/ tests/

# 整理 import
isort data_transformer/ tests/

# 代码检查
flake8 data_transformer/ tests/
```

### 提交 PR 前

```bash
# 运行测试
pytest tests/ -v

# 检查覆盖率
pytest tests/ --cov=data_transformer
```

## 提交规范

提交信息应遵循以下格式：

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type（必须）
- `feat`: 新功能
- `fix`: bug 修复
- `docs`: 文档更新
- `style`: 代码风格调整
- `refactor`: 代码重构
- `perf`: 性能优化
- `test`: 测试相关
- `chore`: 构建、依赖等

### 示例

```
feat(converter): add support for XML format

- Added load_data() support for XML files
- Added save_data() support for XML format
- Updated documentation

Closes #123
```

## 创建 Pull Request

1. 确保代码通过所有测试
2. 添加或更新相关测试
3. 更新 README.md 和文档
4. 提交 PR 前运行完整的测试套件
5. 在 PR 描述中清楚地说明变更内容

## 报告 Bug

使用 GitHub Issues 报告 bug。请包括：

- 清晰的描述
- 复现步骤
- 预期行为
- 实际行为
- Python 版本和操作系统

## 功能建议

使用 GitHub Issues 提出功能建议。请说明：

- 功能的使用场景
- 期望的行为
- 可能的实现方式

## 问题和讨论

使用 GitHub Discussions 进行一般问题和讨论。

## 许可证

通过贡献，您同意您的代码将在 MIT License 下发布。

谢谢您的贡献！🎉
