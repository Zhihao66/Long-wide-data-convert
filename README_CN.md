# 宽数据和长数据格式转换工具

[English](README.md) | 中文

一个强大的 Python 工具，用于在宽数据格式（Wide Format）和长数据格式（Long Format）之间进行无缝转换。

## ✨ 主要特性

- 🔄 **双向转换**：宽 ↔ 长格式相互转换
- 📁 **多格式支持**：CSV、Excel、JSON 文件
- 🎯 **易于使用**：简洁的 Python API 和 CLI 界面
- ⚡ **高效处理**：基于 pandas，性能优异
- 📝 **类型提示**：完整的类型注解，IDE 友好
- ✅ **充分测试**：单元测试覆盖率高
- 🚀 **持续集成**：GitHub Actions 自动测试

## 🎓 理论基础

### 宽格式 (Wide Format)
每一行代表一个观测单位，多个变量作为不同的列：

```
| 学生ID | 姓名 | 2020数学 | 2021数学 | 2020英语 | 2021英语 |
|--------|------|---------|---------|---------|---------|
| 1      | Alice | 85      | 90      | 92      | 95      |
| 2      | Bob   | 78      | 82      | 88      | 90      |
```

### 长格式 (Long Format)
每一行代表一个观测值，通过多列组合标识观测单位：

```
| 学生ID | 姓名  | 年份 | 科目 | 成绩 |
|--------|-------|------|------|------|
| 1      | Alice | 2020 | 数学 | 85   |
| 1      | Alice | 2020 | 英语 | 92   |
| 1      | Alice | 2021 | 数学 | 90   |
| 1      | Alice | 2021 | 英语 | 95   |
| 2      | Bob   | 2020 | 数学 | 78   |
| 2      | Bob   | 2020 | 英语 | 88   |
| 2      | Bob   | 2021 | 数学 | 82   |
| 2      | Bob   | 2021 | 英语 | 90   |
```

**何时使用**：
- **宽格式**：数据可视化、统计测试、比较不同列
- **长格式**：数据分析、建立模型、时间序列分析

## 📦 安装

### 从 PyPI 安装（推荐）
```bash
pip install data-transformer
```

### 从源代码安装
```bash
git clone https://github.com/yourusername/data-transformer.git
cd data-transformer
pip install -e .
```

### 开发环境安装
```bash
git clone https://github.com/yourusername/data-transformer.git
cd data-transformer
pip install -e ".[dev]"
```

## 🚀 快速开始

### Python API

#### 示例 1：学生成绩转换

```python
from data_transformer import DataTransformer
import pandas as pd

# 创建宽格式数据
df_wide = pd.DataFrame({
    'student_id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'Math': [85, 90, 78],
    'English': [92, 88, 95],
    'Science': [88, 92, 85]
})

transformer = DataTransformer()

# 转换为长格式
df_long = transformer.wide_to_long(
    df_wide,
    id_vars=['student_id', 'name'],
    var_name='subject',
    value_name='score'
)

print(df_long)
# 输出:
#    student_id     name  subject  score
# 0           1    Alice     Math     85
# 1           2      Bob     Math     90
# 2           3  Charlie     Math     78
# 3           1    Alice  English     92
# ...
```

#### 示例 2：长格式转换为宽格式

```python
# 转换回宽格式
df_wide_again = transformer.long_to_wide(
    df_long,
    index=['student_id', 'name'],
    columns='subject',
    values='score'
)

print(df_wide_again)
# 输出: 与原始数据相同
```

#### 示例 3：时间序列销售数据

```python
# 销售数据 - 每年每个地区的销售额
df = pd.DataFrame({
    'region': ['East', 'West', 'South'],
    '2020': [100000, 150000, 120000],
    '2021': [120000, 160000, 135000],
    '2022': [140000, 180000, 155000]
})

# 转换为长格式便于时间序列分析
df_long = transformer.wide_to_long(
    df,
    id_vars='region',
    var_name='year',
    value_name='sales'
)

# 现在可以轻松分析每个地区的增长趋势
print(df_long)
```

### 命令行工具

#### 查看帮助
```bash
data-transformer --help
```

#### 宽转长
```bash
data-transformer wide-to-long input.csv output.csv \
    --id-vars student_id,name \
    --var-name subject \
    --value-name score
```

#### 长转宽
```bash
data-transformer long-to-wide input.csv output.csv \
    --index student_id,name \
    --columns subject \
    --values score
```

## 📚 详细文档

- [快速开始指南](docs/QUICKSTART.md) - 10分钟入门
- [API 文档](docs/API.md) - 完整的 API 参考
- [部署指南](DEPLOYMENT.md) - GitHub 部署步骤
- [贡献指南](CONTRIBUTING.md) - 参与项目开发

## 🔧 高级用法

### 保存和加载数据

```python
# 从不同格式加载数据
df_csv = transformer.load_data('data.csv')
df_excel = transformer.load_data('data.xlsx')
df_json = transformer.load_data('data.json')

# 保存为不同格式
transformer.save_data(df_long, 'output.csv', format='csv')
transformer.save_data(df_long, 'output.xlsx', format='excel')
transformer.save_data(df_long, 'output.json', format='json')
```

### 处理缺失值

```python
# 转换时自动处理 NaN
df_with_nan = df_wide.fillna(0)
df_long = transformer.wide_to_long(df_with_nan, id_vars='id')
```

### 多列转换

```python
# 只转换特定列
df_long = transformer.wide_to_long(
    df_wide,
    id_vars=['id', 'name'],
    value_vars=['2020', '2021', '2022'],  # 指定要转换的列
    var_name='year',
    value_name='value'
)
```

### 自定义聚合函数

```python
# 当存在重复值时，自定义聚合方式
df_wide = transformer.long_to_wide(
    df_long,
    index='id',
    columns='subject',
    values='score',
    aggfunc='mean'  # 使用平均值而不是 'first'
)
```

## 🧪 测试

运行所有测试：
```bash
pytest tests/ -v
```

生成覆盖率报告：
```bash
pytest tests/ --cov=data_transformer --cov-report=html
```

## 📊 实际应用场景

### 场景 1：医疗健康数据

**原始数据（宽格式）**：患者体检报告
```
| 患者ID | 姓名 | 血压_2025年1月 | 血压_2025年2月 | 心率_2025年1月 | 心率_2025年2月 |
|--------|------|----------------|----------------|----------------|----------------|
| P001   | 张三 | 120/80         | 118/78         | 72             | 70             |
```

**转换后（长格式）**：便于分析指标变化
```
| 患者ID | 姓名 | 月份    | 指标 | 值    |
|--------|------|---------|------|-------|
| P001   | 张三 | 1月     | 血压 | 120/80|
| P001   | 张三 | 1月     | 心率 | 72    |
| P001   | 张三 | 2月     | 血压 | 118/78|
| P001   | 张三 | 2月     | 心率 | 70    |
```

### 场景 2：调查问卷数据

**原始数据（宽格式）**：每个受访者一行
```
| ID | Q1_满意度 | Q2_推荐度 | Q3_再购率 |
|----|----------|----------|----------|
| 1  | 5        | 4        | 5        |
| 2  | 4        | 5        | 4        |
```

**转换后（长格式）**：便于画图和统计
```
| ID | 问题 | 答案 |
|----|------|------|
| 1  | Q1   | 5    |
| 1  | Q2   | 4    |
| 1  | Q3   | 5    |
```

### 场景 3：电商销售数据

**原始数据（宽格式）**：每个产品每个月的销量
```
| 产品    | 1月 | 2月 | 3月 |
|---------|-----|-----|-----|
| 产品A   | 100 | 150 | 200 |
| 产品B   | 80  | 120 | 160 |
```

**转换后（长格式）**：构建时间序列模型
```
| 产品  | 月份 | 销量 |
|-------|------|------|
| 产品A | 1月  | 100  |
| 产品A | 2月  | 150  |
| 产品A | 3月  | 200  |
```

## 🐛 故障排除

### Q: 转换后数据顺序改变了？
A: 这是正常的。使用 `sort_values()` 或 `reset_index()` 重新排序：
```python
df_sorted = df_long.sort_values(['id', 'year']).reset_index(drop=True)
```

### Q: 如何处理含有重复值的长转宽？
A: 使用 `aggfunc` 参数指定聚合方式：
```python
df_wide = transformer.long_to_wide(
    df_long,
    index='id',
    columns='subject',
    values='score',
    aggfunc='mean'  # 可以是 'sum', 'max', 'min' 等
)
```

### Q: 支持大文件吗？
A: 支持！但超大文件可能需要更多内存。建议：
```python
# 分批处理
df_chunk = pd.read_csv('large_file.csv', chunksize=10000)
for chunk in df_chunk:
    result = transformer.wide_to_long(chunk, id_vars='id')
    # 处理结果
```

## 📈 性能指标

在标准配置（Intel i5, 8GB RAM）上的测试结果：

| 数据量 | 操作 | 耗时 |
|--------|------|------|
| 10,000 行 × 5 列 | 宽转长 | ~50ms |
| 50,000 行 × 3 列 | 长转宽 | ~200ms |
| 100,000 行 × 10 列 | 宽转长 | ~500ms |

## 🤝 贡献

欢迎任何形式的贡献！

1. Fork 项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

详见 [贡献指南](CONTRIBUTING.md)

## 📄 许可证

本项目采用 MIT License - 详见 [LICENSE](LICENSE) 文件

## 🙋 获取帮助

- 📖 查看 [文档](docs/)
- 🐛 报告 bug：[GitHub Issues](https://github.com/yourusername/data-transformer/issues)
- 💬 讨论功能建议：[GitHub Discussions](https://github.com/yourusername/data-transformer/discussions)

## 🎉 致谢

感谢所有贡献者和用户的支持！

---

**让数据转换变得简单！** 🚀

如果本项目对您有帮助，请给个 ⭐ Star 吧！
