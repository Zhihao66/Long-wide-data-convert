"""
核心转换模块 - 实现宽数据和长数据的转换
Core conversion module for wide and long format data transformation
"""

import pandas as pd
from typing import List, Optional, Union


class DataTransformer:
    """
    数据格式转换器 - 支持宽数据和长数据的互转
    Data format converter supporting wide and long format transformation
    """

    @staticmethod
    def wide_to_long(
        df: pd.DataFrame,
        id_vars: Union[str, List[str]],
        value_vars: Optional[Union[str, List[str]]] = None,
        var_name: str = "variable",
        value_name: str = "value",
    ) -> pd.DataFrame:
        """
        将宽格式数据转换为长格式数据
        Convert wide format data to long format data
        
        Parameters:
        -----------
        df : pd.DataFrame
            输入数据框 / Input DataFrame
        id_vars : str or list of str
            识别变量，保持不变 / ID columns that remain unchanged
        value_vars : str or list of str, optional
            要转换的列，如不指定则转换除id_vars外的所有列 / Columns to convert
        var_name : str
            新的变量列名 / Name for the variable column
        value_name : str
            新的值列名 / Name for the value column
            
        Returns:
        --------
        pd.DataFrame
            长格式数据框 / Long format DataFrame
            
        Example:
        --------
        >>> df = pd.DataFrame({'id': [1, 2], 'A': [10, 20], 'B': [30, 40]})
        >>> result = DataTransformer.wide_to_long(df, id_vars='id')
        """
        try:
            result = pd.melt(
                df,
                id_vars=id_vars,
                value_vars=value_vars,
                var_name=var_name,
                value_name=value_name,
            )
            return result
        except Exception as e:
            raise ValueError(f"Error converting wide to long format: {str(e)}")

    @staticmethod
    def long_to_wide(
        df: pd.DataFrame,
        index: Union[str, List[str]],
        columns: Union[str, List[str]],
        values: Union[str, List[str]],
        aggfunc: Union[str, callable] = "first",
    ) -> pd.DataFrame:
        """
        将长格式数据转换为宽格式数据
        Convert long format data to wide format data
        
        Parameters:
        -----------
        df : pd.DataFrame
            输入数据框 / Input DataFrame
        index : str or list of str
            用作新索引的列 / Column(s) to use as row indices
        columns : str or list of str
            用作新列的列 / Column(s) to use as column headers
        values : str or list of str
            用作新值的列 / Column(s) to use as values
        aggfunc : str or callable
            当存在重复值时的聚合函数 / Aggregation function for duplicate values
            
        Returns:
        --------
        pd.DataFrame
            宽格式数据框 / Wide format DataFrame
            
        Example:
        --------
        >>> df = pd.DataFrame({
        ...     'id': [1, 1, 2, 2],
        ...     'variable': ['A', 'B', 'A', 'B'],
        ...     'value': [10, 20, 30, 40]
        ... })
        >>> result = DataTransformer.long_to_wide(df, index='id', columns='variable', values='value')
        """
        try:
            result = df.pivot_table(
                index=index,
                columns=columns,
                values=values,
                aggfunc=aggfunc,
            )
            result.columns.name = None
            result = result.reset_index()
            return result
        except Exception as e:
            raise ValueError(f"Error converting long to wide format: {str(e)}")

    @staticmethod
    def load_data(filepath: str) -> pd.DataFrame:
        """
        从文件加载数据 / Load data from file
        
        支持格式 / Supported formats: CSV, Excel, JSON
        
        Parameters:
        -----------
        filepath : str
            文件路径 / File path
            
        Returns:
        --------
        pd.DataFrame
            加载的数据框 / Loaded DataFrame
        """
        if filepath.endswith(".csv"):
            return pd.read_csv(filepath)
        elif filepath.endswith((".xlsx", ".xls")):
            return pd.read_excel(filepath)
        elif filepath.endswith(".json"):
            return pd.read_json(filepath)
        else:
            raise ValueError(f"Unsupported file format: {filepath}")

    @staticmethod
    def save_data(df: pd.DataFrame, filepath: str, format: str = "csv") -> None:
        """
        保存数据到文件 / Save data to file
        
        Parameters:
        -----------
        df : pd.DataFrame
            数据框 / DataFrame to save
        filepath : str
            输出文件路径 / Output file path
        format : str
            输出格式 / Output format: 'csv', 'excel', 'json'
        """
        if format == "csv":
            df.to_csv(filepath, index=False, encoding="utf-8-sig")
        elif format == "excel":
            df.to_excel(filepath, index=False)
        elif format == "json":
            df.to_json(filepath, orient="records", force_ascii=False)
        else:
            raise ValueError(f"Unsupported format: {format}")
