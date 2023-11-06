# 实验五 Python数据结构与数据模型

班级： 21计科1

学号： 20190202222

姓名： 陈乐

Github地址：<https://github.com/lechen20/python_course>

CodeWars地址：<https://www.codewars.com/users/lechen20>

---

## 实验目的

1. 学习Python数据结构的高级用法
2. 学习Python的数据模型

## 实验环境

1. Git
2. Python 3.10
3. VSCode
4. VSCode插件

## 实验内容和步骤

### 第一部分

在[Codewars网站](https://www.codewars.com)注册账号，完成下列Kata挑战：

---

#### 第一题：停止逆转我的单词

难度： 6kyu

编写一个函数，接收一个或多个单词的字符串，并返回相同的字符串，但所有5个或更多的字母单词都是相反的（就像这个Kata的名字一样）。传入的字符串将只由字母和空格组成。只有当出现一个以上的单词时，才会包括空格。
例如：

```python
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"
```

代码提交地址：
<https://www.codewars.com/kata/5264d2b162488dc400000001>

提示：

- 利用str的split方法可以将字符串分为单词列表
例如：

```python
words = "hey fellow warrior".split()
# words should be ['hey', 'fellow', 'warrior']
```

- 利用列表推导将长度大于等于5的单词反转(利用切片word[::-1])
- 最后使用str的join方法连结列表中的单词。

---

#### 第二题： 发现离群的数(Find The Parity Outlier)

难度：6kyu

给你一个包含整数的数组（其长度至少为3，但可能非常大）。该数组要么完全由奇数组成，要么完全由偶数组成，除了一个整数N。请写一个方法，以该数组为参数，返回这个 "离群 "的N。

例如：

```python
[2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)
```

代码提交地址：
<https://www.codewars.com/kata/5526fc09a1bbd946250002dc>

---

#### 第三题： 检测Pangram

难度：6kyu

pangram是一个至少包含每个字母一次的句子。例如，"The quick brown fox jumps over the lazy dog "这个句子就是一个pangram，因为它至少使用了一次字母A-Z（大小写不相关）。

给定一个字符串，检测它是否是一个pangram。如果是则返回`True`，如果不是则返回`False`。忽略数字和标点符号。
代码提交地址：
<https://www.codewars.com/kata/545cedaa9943f7fe7b000048>

---

#### 第四题： 数独解决方案验证

难度：6kyu

数独背景

数独是一种在 9x9 网格上进行的游戏。游戏的目标是用 1 到 9 的数字填充网格的所有单元格，以便每一列、每一行和九个 3x3 子网格（也称为块）中的都包含数字 1 到 9。更多信息请访问：<http://en.wikipedia.org/wiki/Sudoku>

编写一个函数接受一个代表数独板的二维数组，如果它是一个有效的解决方案则返回 true，否则返回 false。数独板的单元格也可能包含 0，这将代表空单元格。包含一个或多个零的棋盘被认为是无效的解决方案。棋盘总是 9 x 9 格，每个格只包含 0 到 9 之间的整数。

代码提交地址：
<https://www.codewars.com/kata/63d1bac72de941033dbf87ae>

---

#### 第五题： 疯狂的彩色三角形

难度： 2kyu

一个彩色的三角形是由一排颜色组成的，每一排都是红色、绿色或蓝色。连续的几行，每一行都比上一行少一种颜色，是通过考虑前一行中的两个相接触的颜色而产生的。如果这些颜色是相同的，那么新的一行就使用相同的颜色。如果它们不同，则在新的一行中使用缺失的颜色。这个过程一直持续到最后一行，只有一种颜色被生成。

例如：
```python
Colour here:            G G        B G        R G        B R
Becomes colour here:     G          R          B          G
```


一个更大的三角形例子：

```python
R R G B R G B B
 R B R G B R B
  G G B R G G
   G R G B G
    B B R R
     B G R
      R B
       G
```

你将得到三角形的第一行字符串，你的工作是返回最后的颜色，这将出现在最下面一行的字符串。在上面的例子中，你将得到 "RRGBRGBB"，你应该返回 "G"。
限制条件： 1 <= length(row) <= 10 ** 5
输入的字符串将只包含大写字母'B'、'G'或'R'。

例如：

```python
triangle('B') == 'B'
triangle('GB') == 'R'
triangle('RRR') == 'R'
triangle('RGBG') == 'B'
triangle('RBRGBRB') == 'G'
triangle('RBRGBRBGGRRRBGBBBGG') == 'G'
```

代码提交地址：
<https://www.codewars.com/kata/5a331ea7ee1aae8f24000175>

提示：请参考下面的链接，利用三进制的特点来进行计算。
<https://stackoverflow.com/questions/53585022/three-colors-triangles>

---

### 第二部分

使用Mermaid绘制程序流程图

安装VSCode插件：

- Markdown Preview Mermaid Support
- Mermaid Markdown Syntax Highlighting

使用Markdown语法绘制你的程序绘制程序流程图（至少一个），Markdown代码如下：

![程序流程图](/Experiments/img/2023-08-05-22-00-00.png)

显示效果如下：

```mermaid
flowchart LR
    A[Start] --> B{Is it?}
    B -->|Yes| C[OK]
    C --> D[Rethink]
    D --> B
    B ---->|No| E[End]
```

查看Mermaid流程图语法-->[点击这里](https://mermaid.js.org/syntax/flowchart.html)

使用Markdown编辑器（例如VScode）编写本次实验的实验报告，包括[实验过程与结果](#实验过程与结果)、[实验考查](#实验考查)和[实验总结](#实验总结)，并将其导出为 **PDF格式** 来提交。

## 实验过程与结果

请将实验过程与结果放在这里，包括：

- [第一部分 Codewars Kata挑战](#第一部分)    

#### 第一题：停止逆转我的单词    


```python
def spin_words(sentence):
    words = sentence.split()  
    words1 = []
    for word in words:
        if len(word) > 4: 
            word = word[::-1] 
        words1.append(word)
    return ' '.join(words1) 

```

![Alt text](image-22.png)


#### 第二题： 发现离群的数(Find The Parity Outlier)    


```python

def find_outlier(integers):
    even_num=0
    odd_num=0
    even=None
    odd=None
    for i in integers:
        if(i%2==0):
            odd_num+=1
            odd=i
        else:
            even_num+=1
            even=i
    if(odd_num>even_num):
        return even
    else:
        return odd

```      

![Alt text](image-23.png)



#### 第三题： 检测Pangram    


```python
def is_pangram(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    s = ''.join(filter(str.isalpha, s))
    for letter in alphabet:
        if letter not in s:
            return False
    return True

```      
![Alt text](image-24.png)

#### 第四题： 数独解决方案验证    


```python

def validate_sudoku(board):
    elements = set(range(1, 10))

    for b in board:
        if set(b) != elements: 
            return False
    for b in zip(*board):  
        if set(b) != elements: 
            return False

    for i in range(3, 10, 3):
        for j in range(3, 10, 3):
            elements_set = set()
            for w in range(j-3, j):
                for q in range(i-3, i):
                    elements_set.add(board[q][w])
            if elements != elements_set:
                return False
            
    return True

```    
![Alt text](image-25.png)

#### 第五题： 疯狂的彩色三角形    


```python

def triangle(row):
    reduce=[3**i+1 for i in range(10) if 3**i<=100000][::-1]
    
    COLOR = {'GG':'G', 'BB':'B', 'RR':'R', 'BR':'G', 
            'BG':'R', 'GB':'R', 'GR':'B', 'RG':'B', 'RB':'G'}

    for length in reduce:
        while len(row)>=length:
            row=[ COLOR[row[i] + row[i+length-1]] for i in range(len(row)-length+1)]
    return row[0]

```



- [第二部分 使用Mermaid绘制程序流程图](#第二部分)
  
#### 第一题：停止逆转我的单词    

```mermaid
flowchart LR   
A[Start] -->B[将字符串分割成子字符串列表words]
B --> C[新建列表words1]
C --> D[遍历列表words]
D --> E{"判断  len(word) > 4 ?"}
E -->|Yes| F[word反序]
E -->|No| G[word插入 words1列表]
F --> G
G -->D
D -->|遍历结束| H[返回 空格连接列表words1中的元素]
H -->  I[End]
```    

#### 第二题： 发现离群的数(Find The Parity Outlier)    

```mermaid
flowchart LR   
A[Start] --> B[even_num=0]
B --> C[odd_num=0]
C --> D[even=None]
D --> E[odd=None]
E --> F[遍历integers中的i]
F --> G{判断i%2==0?}
G -->|Yes| H[odd_num+=1]
H --> I[odd=i]
G -->|No| J[even_num+=1]
J --> K[even=i]
I --> F
K --> F
F -->|结束遍历| L{判断 odd_num>even_num}
L -->|Yes| M[返回 even]
L -->|No| N[返回 odd]
M --> O[End]
N --> O[End]
```    

#### 第三题： 检测Pangram   

```mermaid
flowchart LR   
A[Start] --> B["alphabet = 'abcdefghijklmnopqrstuvwxyz'"]
B --> C[将字符串S小写化]
C --> D[从字符串s中提取所有字母并组成一个新的字符串] 
D --> E[遍历alphabet的每一个letter]
E --> F{判断letter字符是否在S中}
F -->|Yes| G[返回 False]
F -->|No| E
E -->|遍历结束| H[返回 True]
H --> I[End]
G --> I[End]
```    



#### 第四题： 数独解决方案验证   
 
```mermaid
flowchart LR   
A[Start] --> B[定义一个包含1到9的集合elements]
B --> C[遍历board每一行]
C --> D{" 判断 set(b) != elements"}
D -->|Yes| E[返回False]
D -->|No| C
C -->|遍历结束| F[遍历board每一列]
F --> G{"判断 set(b) != elements"}
G -->|Yes| H[返回False]
H --> F
G -->|No| F
F -->|遍历结束| I[遍历每个3x3的小方格的行]
I --> J[遍历每个3x3的小方格的列]
J --> K[定义一个空集合elements_set]
K --> L[遍历小方格内的每一列]
L --> M[遍历小方格内的每一行]
M --> N[将小方格内的元素添加到集合中]
N --> M
M -->|遍历结束| L
L -->|遍历结束| O{判断elements != elements_set}
O -->|Yes| P[返回False]
O -->|No| J 
J -->|遍历结束| I
I -->|遍历结束| Q[返回True]
Q --> R[end]

``` 

#### 第五题： 疯狂的彩色三角形  

```mermaid
flowchart LR   
A[Start] --> B[初始化reduce列表]
B --> C[定义COLOR字典表示颜色转换规则]
C --> D[遍历reduce列表中的每个长度length]
D --> E{判断row的长度是否大于等于length}
E -->|No| G["返回row[0]"]
E -->|Yes| F[根据颜色转换规则更新row]
F --> D
G --> H[End]


```   


代码运行结果的文本可以直接粘贴在这里。

**注意：不要使用截图，因为Markdown文档转换为Pdf格式后，截图会无法显示。**

## 实验考查

请使用自己的语言并使用尽量简短代码示例回答下面的问题，这些问题将在实验检查时用于提问和答辩以及实际的操作。

1. 集合（set）类型有什么特点？它和列表（list）类型有什么区别？    
   集合（set）类型的特点：集合是无序的，元素没有索引;集合中的元素是唯一的，不允许重复;集合中的元素是不可变的，不能修改，但可以添加或删除元素.    
   集合和列表的区别：列表是有序的，元素有索引;列表中的元素可以重复;列表中的元素是可变的，可以修改、添加或删除元素.   
2. 集合（set）类型主要有那些操作？   
   创建集合：使用大括号 {} 或 set() 函数。   
   添加元素：使用 add() 方法或 update() 方法     
   删除元素：使用 remove() 方法    
   判断元素是否存在：使用 in 关键字    
   获取集合长度：使用 len() 函数    
3. 使用`*`操作符作用到列表上会产生什么效果？为什么不能使用`*`操作符作用到嵌套的列表上？使用简单的代码示例说明。    
   使用 * 操作符作用到列表上会产生重复元素的效果。例如，[1, 2, 3]*3 的结果是 [1, 2, 3, 1, 2, 3, 1, 2, 3]。这是因为*操作符会将列表重复指定的次数。     
   不能使用*操作符作用到嵌套的列表上，因为*操作符只会复制列表的引用，而不会复制嵌套列表的内容。    
   ```python
   list = [[1, 2, 3]] * 3
   list[0][0] = 0
   print(list)  # 输出 [[0, 2, 3], [0, 2, 3], [0, 2, 3]]
   ```   

4. 总结列表,集合，字典的解析（comprehension）的使用方法。使用简单的代码示例说明。   
    
    列表
    ```python
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = [x**2 for x in numbers]
    print(squared_numbers)  # 输出 [1, 4, 9, 16, 25]
    ```       
    集合
    ```python
    numbers = [1, 2, 2, 3, 3, 4, 5]
    unique_numbers = {x for x in numbers}
    print(unique_numbers)  # 输出 {1, 2, 3, 4, 5}

    ```   
    字典
    ```python
    numbers = [1, 2, 3, 4, 5]
    squared_dict = {x: x**2 for x in numbers}
    print(squared_dict)  # 输出 {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    ```

## 实验总结

总结一下这次实验你学习和使用到的知识，例如：编程工具的使用、数据结构、程序语言的语法、算法、编程技巧、编程思想。
1. 利用str的split方法可以将字符串分为单词列表    
2. 使用str的join方法连结列表中的单词    
3. zip() 它可以用于将一个二维列表（或矩阵）进行转置。zip() 将会返回一个新的迭代器，其中每个元素都是原始二维列表中相应位置的元素组成的元组    
4. 列表,集合，字典不同的用法和区别   