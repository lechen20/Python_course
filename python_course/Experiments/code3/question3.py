# 第三题：括号匹配（Valid Braces）
def valid_braces(string):
    list=[]
    for n in string:
        if n=="(" or n=="[" or n=="{":
            list.append(n)
        elif n==')' and (not list or list[-1]!='(' ):  #not list不是空列表 or 最后一个元素不是'('
            return False
        elif n==']' and (not list or list[-1]!='[' ):
            return False
        elif n=='}' and (not list or list[-1]!='{'):
            return False
        else:
            list.pop()                                 #删除
    return not list                                    #非空为True
            
