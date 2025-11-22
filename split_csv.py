# -*- coding: utf-8 -*-
import pandas as pd
import os
import math

def split_csv(input_file, output_dir='split_files', rows_per_file=1000):
    """
    将大型CSV文件分割成多个小文件

    Args:
        input_file (str): 输入CSV文件路径
        output_dir (str): 输出目录名称
        rows_per_file (int): 每个文件的行数（不包括表头）
    """

    # 创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"创建输出目录: {output_dir}")

    try:
        # 读取CSV文件
        print(f"正在读取文件: {input_file}")
        df = pd.read_csv(input_file, encoding='utf-8')
        total_rows = len(df)
        print(f"文件总行数（不包括表头）: {total_rows}")

        # 计算需要分割的文件数量
        num_files = math.ceil(total_rows / rows_per_file)
        print(f"将分割成 {num_files} 个文件，每个文件最多 {rows_per_file} 条数据")

        # 获取文件名（不带扩展名）
        base_name = os.path.splitext(os.path.basename(input_file))[0]

        # 分割文件
        for i in range(num_files):
            start_idx = i * rows_per_file
            end_idx = min((i + 1) * rows_per_file, total_rows)

            # 提取数据片段
            chunk = df.iloc[start_idx:end_idx]

            # 生成输出文件名
            output_file = os.path.join(output_dir, f"{base_name}_part_{i+1:03d}.csv")

            # 保存到CSV文件
            chunk.to_csv(output_file, index=False, encoding='utf-8')

            actual_rows = len(chunk)
            print(f"已创建文件 {i+1}/{num_files}: {output_file} ({actual_rows} 条数据)")

        print(f"\n✅ 文件分割完成！")
        print(f"输出目录: {output_dir}")
        print(f"原始文件: {input_file}")
        print(f"总数据条数: {total_rows}")
        print(f"分割文件数: {num_files}")
        print(f"每个文件最多: {rows_per_file} 条数据")

    except FileNotFoundError:
        print(f"❌ 错误: 找不到文件 {input_file}")
    except Exception as e:
        print(f"❌ 错误: {str(e)}")

if __name__ == "__main__":
    # 设置文件路径
    input_csv = "doc/客服语料.csv"

    # 检查文件是否存在
    if os.path.exists(input_csv):
        # 分割文件，每个文件1000条数据
        split_csv(input_csv, rows_per_file=1000)
    else:
        print(f"❌ 错误: 找不到文件 {input_csv}")
        print("请确保文件路径正确，或者修改 input_csv 变量")