# 第一题：3和5的倍数（Multiples of 3 or 5）
def solution(number):
    if number<0:
        return 0
    nums=[]
    for i in range(0,number):
        if i%3==0:
            nums.append(i)
        elif i%5==0:
            nums.append(i)
    s = sum(nums)
    return s
