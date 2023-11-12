import numpy as np
import pandas as pd
import sys

def calculate_statistics(file_path):
    # 读取txt文件并提取第三列数据
    data = pd.read_csv(file_path, delimiter='\t', header=None)
    column_3 = data.iloc[:, 2].values
    
    # 计算均值、标准差、众数和中位数
    mean = np.mean(column_3)
    std = np.std(column_3)
  
    median = np.median(column_3)
    
    # 计算大于0.5的百分比
    percent_gt_0_5 = (column_3 > 0.5).mean() * 100
    
    # 计算0.125-0.5的百分比
    percent_0_125_to_0_5 = ((column_3 >= 0.125) & (column_3 <= 0.5)).mean() * 100
    
    # 计算小于0.5的百分比
    percent_lt_0_5 = (column_3 < 0.125).mean() * 100
    
    results = {
        "均值": mean,
        "标准差": std,
        
        "中位数": median,
        "大于0.5的百分比": percent_gt_0_5,
        "0.125-0.5的百分比": percent_0_125_to_0_5,
        "小于0.5的百分比": percent_lt_0_5
    }
    
    return results

if __name__ == '__main__':
    file_path = sys.argv[1]  # 从命令行参数获取文件路径
    results = calculate_statistics(file_path)

    for key, value in results.items():
        print(key, ":", value)

