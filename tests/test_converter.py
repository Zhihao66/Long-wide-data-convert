"""
单元测试 / Unit Tests
"""

import unittest
import pandas as pd
import tempfile
import os
from data_transformer import DataTransformer


class TestDataTransformer(unittest.TestCase):
    """数据转换器测试类 / Data Transformer Test Class"""

    def setUp(self):
        """设置测试数据 / Setup test data"""
        self.transformer = DataTransformer()
        
        # 宽格式示例 / Wide format example
        self.wide_df = pd.DataFrame({
            'id': [1, 2, 3],
            'name': ['Alice', 'Bob', 'Charlie'],
            '2020': [100, 200, 300],
            '2021': [110, 210, 310],
            '2022': [120, 220, 320],
        })
        
        # 长格式示例 / Long format example
        self.long_df = pd.DataFrame({
            'id': [1, 1, 1, 2, 2, 2, 3, 3, 3],
            'name': ['Alice', 'Alice', 'Alice', 'Bob', 'Bob', 'Bob', 'Charlie', 'Charlie', 'Charlie'],
            'year': ['2020', '2021', '2022', '2020', '2021', '2022', '2020', '2021', '2022'],
            'value': [100, 110, 120, 200, 210, 220, 300, 310, 320],
        })

    def test_wide_to_long(self):
        """测试宽转长 / Test wide to long conversion"""
        result = self.transformer.wide_to_long(
            self.wide_df,
            id_vars=['id', 'name'],
            var_name='year',
            value_name='value'
        )
        
        self.assertEqual(len(result), 9)  # 3行 × 3年
        self.assertEqual(list(result.columns), ['id', 'name', 'year', 'value'])
        self.assertEqual(result['value'].tolist(), [100, 110, 120, 200, 210, 220, 300, 310, 320])

    def test_long_to_wide(self):
        """测试长转宽 / Test long to wide conversion"""
        result = self.transformer.long_to_wide(
            self.long_df,
            index=['id', 'name'],
            columns='year',
            values='value'
        )
        
        self.assertEqual(len(result), 3)  # 3行
        self.assertIn('2020', result.columns)
        self.assertIn('2021', result.columns)
        self.assertIn('2022', result.columns)

    def test_load_save_csv(self):
        """测试CSV文件读写 / Test CSV file I/O"""
        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = os.path.join(tmpdir, 'test.csv')
            
            # 保存
            self.transformer.save_data(self.wide_df, filepath, format='csv')
            self.assertTrue(os.path.exists(filepath))
            
            # 加载
            loaded_df = self.transformer.load_data(filepath)
            pd.testing.assert_frame_equal(loaded_df, self.wide_df)

    def test_load_save_json(self):
        """测试JSON文件读写 / Test JSON file I/O"""
        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = os.path.join(tmpdir, 'test.json')
            
            # 保存
            self.transformer.save_data(self.wide_df, filepath, format='json')
            self.assertTrue(os.path.exists(filepath))
            
            # 加载
            loaded_df = self.transformer.load_data(filepath)
            pd.testing.assert_frame_equal(loaded_df, self.wide_df)


if __name__ == '__main__':
    unittest.main()
