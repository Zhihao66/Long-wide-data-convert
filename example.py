"""
使用示例 / Usage Examples
这个脚本演示了数据转换工具的基本用法
"""

import pandas as pd
from data_transformer import DataTransformer


def example_wide_to_long():
    """示例：宽转长"""
    print("=" * 60)
    print("示例 1: 宽格式转换为长格式")
    print("=" * 60)
    
    # 创建示例数据
    data = {
        'student_id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'Math': [85, 90, 78],
        'English': [92, 88, 95],
        'Science': [88, 92, 85],
    }
    df = pd.DataFrame(data)
    
    print("\n原始数据 (宽格式):")
    print(df)
    
    transformer = DataTransformer()
    result = transformer.wide_to_long(
        df,
        id_vars=['student_id', 'name'],
        var_name='subject',
        value_name='score'
    )
    
    print("\n转换后的数据 (长格式):")
    print(result)
    print()


def example_long_to_wide():
    """示例：长转宽"""
    print("=" * 60)
    print("示例 2: 长格式转换为宽格式")
    print("=" * 60)
    
    # 创建示例数据
    data = {
        'student_id': [1, 1, 1, 2, 2, 2, 3, 3, 3],
        'name': ['Alice', 'Alice', 'Alice', 'Bob', 'Bob', 'Bob', 'Charlie', 'Charlie', 'Charlie'],
        'subject': ['Math', 'English', 'Science', 'Math', 'English', 'Science', 'Math', 'English', 'Science'],
        'score': [85, 92, 88, 90, 88, 92, 78, 95, 85],
    }
    df = pd.DataFrame(data)
    
    print("\n原始数据 (长格式):")
    print(df)
    
    transformer = DataTransformer()
    result = transformer.long_to_wide(
        df,
        index=['student_id', 'name'],
        columns='subject',
        values='score'
    )
    
    print("\n转换后的数据 (宽格式):")
    print(result)
    print()


def example_sales_data():
    """示例：销售数据转换"""
    print("=" * 60)
    print("示例 3: 销售数据按地区和年份的转换")
    print("=" * 60)
    
    # 宽格式：每个地区每年的销售额
    data = {
        'region': ['East', 'West', 'South'],
        '2020': [100000, 150000, 120000],
        '2021': [120000, 160000, 135000],
        '2022': [140000, 180000, 155000],
    }
    df_wide = pd.DataFrame(data)
    
    print("\n原始数据 (按地区和年份):")
    print(df_wide)
    
    transformer = DataTransformer()
    
    # 转换为长格式
    df_long = transformer.wide_to_long(
        df_wide,
        id_vars='region',
        var_name='year',
        value_name='sales'
    )
    
    print("\n转换后 (按行记录):")
    print(df_long)
    
    # 再转换回宽格式（演示可逆性）
    df_wide_again = transformer.long_to_wide(
        df_long,
        index='region',
        columns='year',
        values='sales'
    )
    
    print("\n再次转换回宽格式:")
    print(df_wide_again)
    print()


if __name__ == '__main__':
    example_wide_to_long()
    example_long_to_wide()
    example_sales_data()
    
    print("=" * 60)
    print("所有示例执行完成！")
    print("=" * 60)
