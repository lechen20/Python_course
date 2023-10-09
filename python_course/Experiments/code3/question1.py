# 第一题：3和5的倍数（Multiples of 3 or 5）
def solution(number):
    if number<0:
        return 0
    s=0
    for i in range(0,number):
        if i%3==0:
            s=s+i
        elif i%5==0:
            s=s+i
    return s
