# 第三题： 缩短数值的过滤器(Number Shortening Filter)

def shorten_number(suffixes,base):
    def my_filter(data):
        try:
            number = int(data)
        except (TypeError, ValueError):
            return str(data)
        else:
            i = 0
            while number//base > 0 and i < len(suffixes)-1:
                number //= base
                i += 1
            return str(number) + suffixes[i] 
    
    return my_filter

