# 第五题： 莫尔斯码解码器（Decode the Morse code, advanced）

def decodeBits(bits):
    bits = bits.strip("0")  #从二进制字符串中去除前导和尾随的零
    unit = 0
    for bit in bits:       #通过计算连续的1的数量来确定单位长度
        if bit != "0":
            unit += 1
        else:
            break
    count = 1
    for i in range(1,len(bits)):
        if bits[i] == bits[i-1]:
            count += 1
        else:
            if count < unit:              #刷新unit的值
                unit = count
                count = 1
            else:
                count = 1
    morse_code = ""
    
    words = bits.split("0"*7*unit)  #使用 7 个单位的零作为分隔符将二进制字符串分割成单词
    for word in words:
        characters = word.split("0"*3*unit)  #使用 3 个单位的零作为分隔符将二进制字符串分割成字符
        for character in characters:
            signs = character.split("0"*unit)  #使用 1 个单位的零作为分隔符将每个字符分割成莫尔斯码符号
            for sign in signs:
                if sign == "1"*3*unit:
                    morse_code += "-"
                else:
                    morse_code += "."
            morse_code += " "
        morse_code += "   "
    return morse_code
            


def decodeMorse(morse_code):
    morse_code.strip()     #从莫尔斯码字符串中去除前导和尾随的空格
    result = ""
    characters = morse_code.split(" ")   #空格作为分隔符将字符串分割成单个字符
    for character in characters:
        if character != "":
            result += MORSE_CODE[character]
        else:
            result += " "
    return ' '.join(result.split())
