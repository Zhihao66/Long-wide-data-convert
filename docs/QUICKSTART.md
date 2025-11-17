# 快速开始 / Quick Start

## 10分钟快速入门

### 1. 安装

```bash
pip install data-transformer
```

### 2. 使用 Python API

```python
from data_transformer import DataTransformer
import pandas as pd

# 创建样例数据
data = {
    'student_id': [1, 2, 3],
    'student_name': ['Alice', 'Bob', 'Charlie'],
    'Math': [85, 90, 78],
    'English': [92, 88, 95],
    'Science': [88, 92, 85]
}
df = pd.DataFrame(data)

transformer = DataTransformer()

# 宽转长：每个学生的成绩
result = transformer.wide_to_long(
    df,
    id_vars=['student_id', 'student_name'],
    var_name='subject',
    value_name='score'
)

print(result)
```

### 3. 使用命令行

```bash
# 创建示例CSV文件
# wide_data.csv:
# student_id,student_name,Math,English,Science
# 1,Alice,85,92,88
# 2,Bob,90,88,92
# 3,Charlie,78,95,85

# 转换宽格式为长格式
data-transformer wide-to-long wide_data.csv long_data.csv \
    --id-vars student_id,student_name \
    --var-name subject \
    --value-name score

# 查看结果
cat long_data.csv
```

## 常见场景

### 场景1: 销售数据按年份展开

**原始数据（长格式）:**
```
| product | 2020  | 2021  | 2022  |
|---------|-------|-------|-------|
| 产品A  | 10000 | 12000 | 15000 |
| 产品B  | 8000  | 9500  | 11000 |
```

**转换后（长格式）:**
```
| product | year | sales |
|---------|------|-------|
| 产品A  | 2020 | 10000 |
| 产品A  | 2021 | 12000 |
| 产品A  | 2022 | 15000 |
| 产品B  | 2020 | 8000  |
| 产品B  | 2021 | 9500  |
| 产品B  | 2022 | 11000 |
```

### 场景2: 患者医疗数据整理

**原始数据（长格式）:**
```
| patient_id | visit_date | blood_pressure | heart_rate | temperature |
|------------|------------|----------------|------------|-------------|
| P001       | 2025-01-01 | 120/80         | 72         | 36.5        |
| P001       | 2025-01-08 | 122/81         | 74         | 36.4        |
```

**可转换为宽格式便于分析**

## 更多信息

查看 [API 文档](./API.md) 了解更多详情。
