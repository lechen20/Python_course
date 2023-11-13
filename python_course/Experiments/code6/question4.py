# 第四题： 编码聚会7 
def find_senior(lst):
    max=0
    lis=[]
    for lsts in lst:
        if lsts['age']>max:
            lis.clear()
            lis.append(lsts)
            max=lsts['age']
        elif lsts['age']==max:
            lis.append(lsts)
    return lis
