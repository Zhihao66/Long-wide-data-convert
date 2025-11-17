# 数据格式转换工具 / Data Format Transformer

宽数据和长数据格式相互转换的Python工具。

## 功能特性 / Features

- 🔄 **宽转长**: 将宽格式数据转换为长格式数据
- 🔄 **长转宽**: 将长格式数据转换为宽格式数据
- 📁 **多格式支持**: 支持 CSV、Excel、JSON 文件格式
- 🚀 **命令行工具**: 简单易用的 CLI 界面
- 📦 **Python API**: 灵活的 Python 库接口

## 安装 / Installation

### 从 PyPI 安装 / Install from PyPI
```bash
pip install data-transformer
```

### 从源代码安装 / Install from source
```bash
git clone https://github.com/yourusername/data-transformer.git
cd data-transformer
pip install -e .
```

## 使用示例 / Usage Examples

### Python API

#### 宽转长 / Wide to Long
```python
from data_transformer import DataTransformer
import pandas as pd

# 创建示例数据
df = pd.DataFrame({
    'id': [1, 2],
    'name': ['Alice', 'Bob'],
    '2020': [100, 200],
    '2021': [110, 210],
})

# 转换
transformer = DataTransformer()
result = transformer.wide_to_long(
    df,
    id_vars=['id', 'name'],
    var_name='year',
    value_name='sales'
)

print(result)
```

输出:
```
  id     name  year  sales
0  1    Alice  2020    100
1  2      Bob  2020    200
2  1    Alice  2021    110
3  2      Bob  2021    210
```

#### 长转宽 / Long to Wide
```python
# 转换回宽格式
wide_result = transformer.long_to_wide(
    result,
    index=['id', 'name'],
    columns='year',
    values='sales'
)

print(wide_result)
```

#### 文件操作 / File Operations
```python
# 加载数据
df = transformer.load_data('data.csv')

# 处理...

# 保存数据
transformer.save_data(result, 'output.csv', format='csv')
transformer.save_data(result, 'output.xlsx', format='excel')
transformer.save_data(result, 'output.json', format='json')
```

### 命令行工具 / CLI

#### 宽转长
```bash
data-transformer wide-to-long input.csv output.csv --id-vars id,name --var-name year --value-name value
```

#### 长转宽
```bash
data-transformer long-to-wide input.csv output.csv --index id,name --columns year --values value
```

## 数据格式说明 / Data Format Description

### 宽格式 (Wide Format)
又称为"行式"数据，每一行代表一个观测单位，多个变量分别作为不同的列。

示例:
```
| id | name    | 2020 | 2021 | 2022 |
|----|---------|------|------|------|
| 1  | Alice   | 100  | 110  | 120  |
| 2  | Bob     | 200  | 210  | 220  |
```

### 长格式 (Long Format)
又称为"列式"数据，每一行代表一个观测值的组合，包含识别变量、变量名和变量值。

示例:
```
| id | name  | year | value |
|----|-------|------|-------|
| 1  | Alice | 2020 | 100   |
| 1  | Alice | 2021 | 110   |
| 1  | Alice | 2022 | 120   |
| 2  | Bob   | 2020 | 200   |
| 2  | Bob   | 2021 | 210   |
| 2  | Bob   | 2022 | 220   |
```

## 开发指南 / Development Guide

### 设置开发环境 / Setup Development Environment
```bash
git clone https://github.com/yourusername/data-transformer.git
cd data-transformer
pip install -e ".[dev]"
```

### 运行测试 / Run Tests
```bash
pytest tests/ -v
```

### 代码检查 / Code Quality
```bash
flake8 data_transformer/
black data_transformer/
isort data_transformer/
```

## 许可证 / License

MIT License - 详见 [LICENSE](LICENSE) 文件

## 贡献 / Contributing

欢迎提交 Issue 和 Pull Request！

## 变更日志 / Changelog

### 1.0.0 (2025-11-15)
- 初始版本发布
- 支持宽长格式相互转换
- 支持多种文件格式
- 提供 CLI 和 Python API
