library(ggplot2)
library(RColorBrewer)
setwd('G:/博士/bama_project/BMA100+/')
pca <- read.table("testacc_qc.eigenvec",sep = "\t",header = T)
pdf('pca.pdf',width = 10,height = 10)
#my_colors <- c(rgb(1,0,0), rgb(0,1,0), rgb(0,0,1), rgb(1,1,0), rgb(1,0,1), rgb(0,1,1), rgb(1,0.5,0), rgb(0.5,1,0), rgb(0,0.5,1), rgb(1,0,0.5), rgb(0.5,0,1), rgb(0.5,0.5,0.5))
#my_colors <- brewer.pal(12, "Set3")
colors <- rainbow(12)
ggplot(pca, aes(x=pca1,y=pca2)) +
  geom_point(aes(color=pop),size=5,alpha = 0.5)+
  labs(x="PC1(56.6314%)",y="PC2(21.9888%)")+theme_bw()+theme(legend.title = element_blank())+scale_color_manual(values = colors)+theme(panel.grid=element_blank())+theme(text=element_text(size=20,face ='bold'))+ theme_bw()+
  stat_ellipse(aes(fill=pop),type="norm",geom="polygon",alpha=0.3,color=NA,level = 0.95) +
  theme(axis.title = element_text(
    
    face='bold', ##字体外形（粗斜体等）
    size=20, ##字体大小
    lineheight = 1),##标签行间距的倍数
    axis.text = element_text(
     
      face="bold", ##字体外形（粗斜体等）
      size=10))
                                                                                                                                                                                                          
dev.off()


