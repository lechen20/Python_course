# 第五题： 去掉喷子的元音（Disemvowel Trolls）  
def disemvowel(string_):
    letters = [letter for letter in string_ ]
    list=[]
    for n in letters:
        if n.lower()!='a' and n.lower()!='e' and n.lower()!='i' and n.lower()!='o' and n.lower()!='u':
            list.append(n)
    string_ = ''.join(list)
    return string_
