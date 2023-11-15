# 第五题： Currying versus partial application
from inspect import signature  # 导入signature模块
from functools import partial  # 导入partial模块

def curry_partial(main_func, *args):  # 定义函数curry_partial，参数为main_func和不定长参数args
    
    if not(callable(main_func)):  # 判断main_func是否可调用
        return main_func  # 若不可调用则返回main_func
    
    p = len(signature(main_func).parameters)  # 获取main_func的参数个数
    func = partial(main_func)  # 创建main_func的偏函数
    
    for a in args:  # 遍历不定长参数args
        if len(func.args) == p:  # 判断偏函数的参数个数是否等于p
            break  # 若相等则跳出循环
        func = partial(func, a)  # 将a作为func的参数之一
    
    if len(func.args) < p:  # 判断偏函数的参数个数是否小于p
        return partial(curry_partial, main_func, *func.args)  # 若小于p则返回curry_partial的偏函数
    
    return func()  # 返回偏函数func
```
