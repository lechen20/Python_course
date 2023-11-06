
第三题： 检测Pangram    

def is_pangram(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    s = ''.join(filter(str.isalpha, s))
    for letter in alphabet:
        if letter not in s:
            return False
    return True
