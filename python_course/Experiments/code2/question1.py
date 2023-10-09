# 第1题：求离整数n最近的平方数（Find Nearest square number） 
def nearest_sq(n):
    num= int(n ** 0.5)
    num1 = num ** 2
    num2 = (num + 1) ** 2

    if num2 - n < n - num1:
        return num2
    else:
        return num1
