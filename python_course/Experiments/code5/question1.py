# 第一题：停止逆转我的单词   
def spin_words(sentence):
    words = sentence.split()  
    words1 = []
    for word in words:
        if len(word) > 4: 
            word = word[::-1] 
        words1.append(word)
    return ' '.join(words1) 
