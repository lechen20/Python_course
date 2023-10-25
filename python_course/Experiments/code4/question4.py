# 第四题： 填写订单（Thinkful - Dictionary drills: Order filler）  

def fillable(stock, merch, n):
    if merch in stock and stock[merch]>=n:
        return True
    else:
        return False
