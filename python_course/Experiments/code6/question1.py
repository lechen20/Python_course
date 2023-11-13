# 第一题：编码聚会1
def count_developers(lst):
    count=0
    for lsts in lst:
        if lsts['continent']=='Europe' and lsts['language']=='JavaScript':
            count+=1
    return count
