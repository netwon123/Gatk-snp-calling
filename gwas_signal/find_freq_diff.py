import pandas as pd
import argparse

# 读取受选择区间文件（BED格式）
def read_bed_file(bed_file):
    intervals = []
    with open(bed_file, 'r') as f:
        for line in f:
            chrom, start, end = line.strip().split()
            intervals.append((chrom, int(start), int(end)))
    return intervals

# 读取群体频率文件
def read_freq_file(freq_file):
    return pd.read_csv(freq_file, sep='\t', index_col=0)

# 筛选受选择区间内的位点
def filter_sites_in_intervals(freq_df, intervals):
    filtered_sites = []
    for site in freq_df.index:
        chrom, pos = site.split(':')  # 假设位点格式为 "chromosome:position"
        pos = int(pos)
        for interval in intervals:
            if chrom == interval[0] and interval[1] <= pos <= interval[2]:
                filtered_sites.append(site)
                break
    return freq_df.loc[filtered_sites]

# 计算频率差异并筛选差异较大的位点
def find_large_diff_sites(freq_df, group1, group2, threshold=0.5):
    freq_df['diff'] = abs(freq_df[group1] - freq_df[group2])
    large_diff_sites = freq_df[freq_df['diff'] > threshold]
    return large_diff_sites

# 主函数
def main(bed_file, freq_file, group1, group2, threshold, output_file):
    # 读取文件
    intervals = read_bed_file(bed_file)
    freq_df = read_freq_file(freq_file)
    
    # 筛选受选择区间内的位点
    filtered_freq_df = filter_sites_in_intervals(freq_df, intervals)
    
    # 计算频率差异并筛选差异较大的位点
    large_diff_sites = find_large_diff_sites(filtered_freq_df, group1, group2, threshold)
    
    # 输出结果
    large_diff_sites[[group1, group2, 'diff']].to_csv(output_file, sep='\t')
    print(f"Results saved to {output_file}")

# 命令行参数解析
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find sites with large frequency differences between two populations within selected intervals.")
    parser.add_argument("--bed", required=True, help="Path to the BED file with selected intervals.")
    parser.add_argument("--freq", required=True, help="Path to the frequency file with population allele frequencies.")
    parser.add_argument("--group1", required=True, help="Name of the first population in the frequency file.")
    parser.add_argument("--group2", required=True, help="Name of the second population in the frequency file.")
    parser.add_argument("--threshold", type=float, default=0.5, help="Threshold for frequency difference (default: 0.5).")
    parser.add_argument("--output", required=True, help="Path to the output file.")
    
    args = parser.parse_args()
    
    # 调用主函数
    main(args.bed, args.freq, args.group1, args.group2, args.threshold, args.output)
