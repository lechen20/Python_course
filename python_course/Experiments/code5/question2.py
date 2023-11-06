# 第二题： 发现离群的数(Find The Parity Outlier)    
def find_outlier(integers):
    even_num=0
    odd_num=0
    even=None
    odd=None
    for i in integers:
        if(i%2==0):
            odd_num+=1
            odd=i
        else:
            even_num+=1
            even=i
    if(odd_num>even_num):
        return even
    else:
        return odd
