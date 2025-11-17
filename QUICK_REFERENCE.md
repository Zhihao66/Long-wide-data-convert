# 快速参考卡 / Quick Reference Card

## 🎯 最常用的命令

### Python API

```python
from data_transformer import DataTransformer
import pandas as pd

transformer = DataTransformer()

# 1️⃣ 宽 → 长
df_long = transformer.wide_to_long(df, id_vars=['id', 'name'])

# 2️⃣ 长 → 宽
df_wide = transformer.long_to_wide(df, index=['id'], columns='year', values='value')

# 3️⃣ 加载数据
df = transformer.load_data('file.csv')      # CSV
df = transformer.load_data('file.xlsx')     # Excel
df = transformer.load_data('file.json')     # JSON

# 4️⃣ 保存数据
transformer.save_data(df, 'output.csv')
transformer.save_data(df, 'output.xlsx')
transformer.save_data(df, 'output.json')
```

### 命令行

```bash
# 宽转长
data-transformer wide-to-long input.csv output.csv \
    --id-vars id,name \
    --var-name year \
    --value-name value

# 长转宽
data-transformer long-to-wide input.csv output.csv \
    --index id,name \
    --columns year \
    --values value

# 帮助
data-transformer --help
```

## 📊 数据格式对比

| 方面 | 宽格式 | 长格式 |
|------|--------|--------|
| 行数 | 少 | 多 |
| 列数 | 多 | 少 |
| 易读性 | 高 | 中 |
| 分析易度 | 中 | 高 |
| 时间序列 | 不易 | 容易 |
| 统计测试 | 容易 | 需转换 |

## 🔄 转换决策树

```
你的数据格式是？
│
├─→ 每行一个观测单位，多列放不同变量 → 这是宽格式 → 用 wide_to_long()
│
└─→ 每行一个值，多行同一观测单位 → 这是长格式 → 用 long_to_wide()
```

## ⚙️ 参数速查

### wide_to_long()
- `id_vars`: 保持不变的列 ✓ 必需
- `value_vars`: 要转换的列 (默认：除 id_vars 外全部)
- `var_name`: 新变量列名 (默认："variable")
- `value_name`: 新值列名 (默认："value")

### long_to_wide()
- `index`: 行索引列 ✓ 必需
- `columns`: 用作新列名的列 ✓ 必需
- `values`: 用作值的列 ✓ 必需
- `aggfunc`: 重复值聚合方式 (默认："first")

## 💡 常见问题速答

**Q: 多少列才算宽格式？**
A: 没有固定标准。如果列代表同一变量的不同时期/类别，就是宽格式。

**Q: 转换会丢失数据吗？**
A: 不会。两种格式只是组织方式不同，内容相同。

**Q: 转换后数据顺序变了？**
A: 正常。可用 `.sort_values().reset_index(drop=True)` 重新排序。

**Q: 能处理大文件吗？**
A: 可以。pandas 支持较大数据集。超大文件可分批处理。

## 🚀 一行代码解决

```python
# 5行代码完成转换和保存
from data_transformer import DataTransformer

t = DataTransformer()
df = t.load_data('input.csv')
result = t.wide_to_long(df, id_vars='id')
t.save_data(result, 'output.csv')
```

---

**💬 更多帮助：** 查看完整文档 [README_CN.md](README_CN.md)
