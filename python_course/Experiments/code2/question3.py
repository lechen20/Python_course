# 第3题： 元音统计(Vowel Count)
def get_count(sentence):
    count=0
    for n in sentence:
        if n=='a' or n=='e' or n=='i' or n=='o' or n=='u':
            count+=1
    return count
