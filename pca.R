library(ggplot2)
library(RColorBrewer)
setwd('G:/博士/bama_project/')
pca <- read.table("PCA.txt",sep = "\t",header = T)
pdf('pca.pdf',width = 10,height = 10)
#my_colors <- c(rgb(1,0,0), rgb(0,1,0), rgb(0,0,1), rgb(1,1,0), rgb(1,0,1), rgb(0,1,1), rgb(1,0.5,0), rgb(0.5,1,0), rgb(0,0.5,1), rgb(1,0,0.5), rgb(0.5,0,1), rgb(0.5,0.5,0.5))
#my_colors <- brewer.pal(12, "Set3")
colors <- rainbow(12)
ggplot(pca, aes(x=pca1,y=pca2)) +
  geom_point(aes(color=pop),size=5,alpha = 0.7)+
  labs(x="PC1(57.9812%)",y="PC2(13.6253%)")+theme_bw()+theme(legend.title = element_blank())+scale_color_manual(values = colors)+theme(panel.grid=element_blank())+theme(text=element_text(size=16))+ theme(panel.grid.major.x = element_line(color = "gray", linetype = "dashed"),
                                                                                                                                                                                                            panel.grid.major.y = element_line(color = "gray", linetype = "dashed"))
dev.off()
