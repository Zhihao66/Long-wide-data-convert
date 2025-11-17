"""
命令行界面 / Command Line Interface
"""

import argparse
import sys
from .converter import DataTransformer


def main():
    """命令行主函数 / Main CLI function"""
    parser = argparse.ArgumentParser(
        description="宽数据和长数据格式转换工具 / Wide and Long Data Format Converter",
        prog="data-transformer",
    )

    subparsers = parser.add_subparsers(dest="command", help="可用命令 / Available commands")

    # 宽转长命令
    wide_to_long_parser = subparsers.add_parser(
        "wide-to-long",
        help="将宽格式数据转换为长格式数据 / Convert wide format to long format",
    )
    wide_to_long_parser.add_argument("input", help="输入文件 / Input file")
    wide_to_long_parser.add_argument("output", help="输出文件 / Output file")
    wide_to_long_parser.add_argument(
        "--id-vars", required=True, help="识别变量，用逗号分隔 / ID variables (comma-separated)"
    )
    wide_to_long_parser.add_argument(
        "--var-name", default="variable", help="变量列名 / Variable column name"
    )
    wide_to_long_parser.add_argument(
        "--value-name", default="value", help="值列名 / Value column name"
    )

    # 长转宽命令
    long_to_wide_parser = subparsers.add_parser(
        "long-to-wide",
        help="将长格式数据转换为宽格式数据 / Convert long format to wide format",
    )
    long_to_wide_parser.add_argument("input", help="输入文件 / Input file")
    long_to_wide_parser.add_argument("output", help="输出文件 / Output file")
    long_to_wide_parser.add_argument(
        "--index", required=True, help="索引列，用逗号分隔 / Index columns (comma-separated)"
    )
    long_to_wide_parser.add_argument(
        "--columns", required=True, help="列列，用逗号分隔 / Column columns (comma-separated)"
    )
    long_to_wide_parser.add_argument(
        "--values", required=True, help="值列，用逗号分隔 / Value columns (comma-separated)"
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    try:
        transformer = DataTransformer()

        if args.command == "wide-to-long":
            df = transformer.load_data(args.input)
            id_vars = [v.strip() for v in args.id_vars.split(",")]
            result = transformer.wide_to_long(
                df,
                id_vars=id_vars,
                var_name=args.var_name,
                value_name=args.value_name,
            )
            transformer.save_data(result, args.output, format="csv")
            print(f"✓ 转换成功！输出文件: {args.output}")

        elif args.command == "long-to-wide":
            df = transformer.load_data(args.input)
            index = [v.strip() for v in args.index.split(",")]
            columns = [v.strip() for v in args.columns.split(",")]
            values = [v.strip() for v in args.values.split(",")]
            result = transformer.long_to_wide(
                df,
                index=index,
                columns=columns,
                values=values,
            )
            transformer.save_data(result, args.output, format="csv")
            print(f"✓ 转换成功！输出文件: {args.output}")

    except Exception as e:
        print(f"✗ 错误: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
