# 读取IBD结果文件

library(ggplot2)
library(reshape2)

# 读取数据
df <- read.table('IBD_result.genome', header=TRUE)

# 将数据转换为长格式
df_melt <- melt(df, id.vars=c('IID1', 'IID2'))

# 对数据进行排序
df_melt <- arrange(df_melt, IID1, IID2)

# 绘制heatmap
ggplot(df_melt, aes(x=IID1, y=IID2, fill=value)) +
  geom_tile() +
  scale_fill_gradient(low='white', high='red') +
  theme(axis.text.x = element_text(angle = 90, hjust = 1, size=4),
        axis.text.y = element_text(size=4))

