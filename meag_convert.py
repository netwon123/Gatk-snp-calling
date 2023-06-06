import sys,re,os


ID_file = open("Distance.out.mdist.id","r")
arr = []
for i in ID_file:
    arr.append(i.strip().split()[0])
head = map(str,range(1,len(arr)+1))
ID_file.close()


meg=open('Distance.meg',mode='w')
dist_file =open("Distance.out.mdist","r")
dist_filedata=dist_file.readlines()
meg.write("#mega\n!Title: fasta file;\n!Format DataType=Distance DataFormat=LowerLeft NTaxa=%d;\n" % len(arr))
for i,j in enumerate(arr):
    meg.write('['+str(i+1)+']'+' #'+j)




meg.write('[    '+'    '.join(head)+' ]\n')

for l,m in enumerate(dist_filedata):
    tmp = m.strip().split()

    meg.write('['+str(l+2)+']    '+'    '.join(tmp)+'\n')


dist_file.close()
meg.close()
