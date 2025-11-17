# API 文档 / API Documentation

## DataTransformer 类

### 方法概览

#### `wide_to_long()`

将宽格式数据转换为长格式数据。

**参数 / Parameters:**
- `df` (DataFrame): 输入的宽格式数据框
- `id_vars` (str or list): 保持不变的列（识别变量）
- `value_vars` (str or list, optional): 要转换的列，默认为除 id_vars 外的所有列
- `var_name` (str): 新的变量列名，默认为 "variable"
- `value_name` (str): 新的值列名，默认为 "value"

**返回 / Returns:**
- DataFrame: 转换后的长格式数据框

**示例 / Example:**
```python
transformer = DataTransformer()
result = transformer.wide_to_long(
    df,
    id_vars=['id', 'name'],
    var_name='year',
    value_name='value'
)
```

---

#### `long_to_wide()`

将长格式数据转换为宽格式数据。

**参数 / Parameters:**
- `df` (DataFrame): 输入的长格式数据框
- `index` (str or list): 用作行索引的列
- `columns` (str or list): 用作列名的列
- `values` (str or list): 用作单元格值的列
- `aggfunc` (str or callable): 聚合函数，默认为 "first"

**返回 / Returns:**
- DataFrame: 转换后的宽格式数据框

**示例 / Example:**
```python
result = transformer.long_to_wide(
    df,
    index=['id', 'name'],
    columns='year',
    values='value'
)
```

---

#### `load_data()`

从文件加载数据。

**参数 / Parameters:**
- `filepath` (str): 文件路径

**支持格式 / Supported Formats:**
- `.csv` - 逗号分隔值
- `.xlsx`, `.xls` - Excel 工作簿
- `.json` - JSON 格式

**返回 / Returns:**
- DataFrame: 加载的数据框

**示例 / Example:**
```python
df = transformer.load_data('data.csv')
df = transformer.load_data('data.xlsx')
df = transformer.load_data('data.json')
```

---

#### `save_data()`

保存数据到文件。

**参数 / Parameters:**
- `df` (DataFrame): 要保存的数据框
- `filepath` (str): 输出文件路径
- `format` (str): 输出格式 ('csv', 'excel', 'json')，默认为 'csv'

**示例 / Example:**
```python
transformer.save_data(df, 'output.csv', format='csv')
transformer.save_data(df, 'output.xlsx', format='excel')
transformer.save_data(df, 'output.json', format='json')
```

---

## 异常处理 / Exception Handling

所有方法在出错时会抛出 `ValueError` 异常。

```python
try:
    result = transformer.wide_to_long(df, id_vars='invalid_column')
except ValueError as e:
    print(f"转换失败: {e}")
```

## 类型提示 / Type Hints

本库充分使用 Python 类型提示，支持 IDE 自动补全和类型检查。

```python
from typing import List, Union
from data_transformer import DataTransformer
import pandas as pd

transformer: DataTransformer = DataTransformer()
result: pd.DataFrame = transformer.wide_to_long(
    df,
    id_vars=['id', 'name']
)
```
