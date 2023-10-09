# 第二题： 重复字符的编码器（Duplicate Encoder）
def duplicate_encode(word):
    word = word.lower()  # 将所有字母转换为小写，以忽略大小写
    words=[]
    for n in word:
        count=0
        for m in word:
            if n==m:
                count+=1
        if count>=2 :
            words.append(')')
        else:
            words.append('(')
    return ''.join(words) #将列表的字符合并成字符串
