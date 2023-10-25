# 第二题： 观察到的PIN（The observed PIN）

def get_pins(observed):
    PIN = {'1':['1','2','4'], '2':['1','2','3','5'], '3':['2','3','6'], '4':['1','4','5','7'], '5':['2','4','5','6','8'], '6':['3','5','6','9'], '7':['4','7','8'], '8':['5','7','8','9','0'], '9':['6','8','9'], '0':['0','8']}
    if len(observed) == 1:
        return PIN[observed]
    else:
        res = []
        first = observed[0]
        rest = get_pins(observed[1:])
        for value1 in PIN[first]:
            for value2 in rest:
                res.append(value1+value2)
        return res
