# 第四题： 从随机三元组中恢复秘密字符串(Recover a secret string from random triplets)
def recoverSecret(triplets):
    lis=[]
    lis = [i for triplet in triplets for i in triplet]
    lis=set(lis)                        #去重
    lis=list(lis)
    
    while True:
        count=0
        for i in range(len(triplets)):
            for j in range(len(triplets[i])-1):
                m=triplets[i][j]
                n=triplets[i][j+1]
                in_m=lis.index(m)
                in_n=lis.index(n)
                if in_m>in_n:            #m在前应该交换n
                    temp=lis[in_m]
                    lis[in_m]=lis[in_n]
                    lis[in_n]=temp
                    count+=1
        if count==0:
            return ''.join(lis)
