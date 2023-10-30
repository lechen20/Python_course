# 实验四 Python字典和while循环

班级： 21计科1

学号： 20190202222

姓名： 陈乐

Github地址：<https://github.com/lechen20/python_course>

CodeWars地址：<https://www.codewars.com/users/lechen20>

---

## 实验目的

1. 学习Python字典
2. 学习Python用户输入和while循环

## 实验环境

1. Git
2. Python 3.10
3. VSCode
4. VSCode插件

## 实验内容和步骤

### 第一部分

Python列表操作

完成教材《Python编程从入门到实践》下列章节的练习：

- 第6章 字典
- 第7章 用户输入和while循环

---

### 第二部分

在[Codewars网站](https://www.codewars.com)注册账号，完成下列Kata挑战：

---

#### 第一题：淘气还是乖孩子（Naughty or Nice）

难度： 7kyu

圣诞老人要来镇上了，他需要你帮助找出谁是淘气的或善良的。你将会得到一整年的JSON数据，按照这个格式：

```python
{
    January: {
        '1': 'Naughty','2': 'Naughty', ..., '31': 'Nice'
    },
    February: {
        '1': 'Nice','2': 'Naughty', ..., '28': 'Nice'
    },
    ...
    December: {
        '1': 'Nice','2': 'Nice', ..., '31': 'Naughty'
    }
}
```

你的函数应该返回 "Naughty!"或 "Nice!"，这取决于在某一年发生的总次数（以较大者为准）。如果两者相等，则返回 "Nice！"。
代码提交地址：
<https://www.codewars.com/kata/5662b14e0a1fb8320a00005c>

---

#### 第二题： 观察到的PIN（The observed PIN）

难度：4kyu

好了，侦探，我们的一个同事成功地观察到了我们的目标人物，抢劫犯罗比。我们跟踪他到了一个秘密仓库，我们认为在那里可以找到所有被盗的东西。这个仓库的门被一个电子密码锁所保护。不幸的是，我们的间谍不确定他看到的密码，当罗比进入它时。

键盘的布局如下：

```python
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
```

他注意到密码1357，但他也说，他看到的每个数字都有可能是另一个相邻的数字（水平或垂直，但不是对角线）。例如，代替1的也可能是2或4。而不是5，也可能是2、4、6或8。

他还提到，他知道这种锁。你可以无限制地输入错误的密码，但它们最终不会锁定系统或发出警报。这就是为什么我们可以尝试所有可能的（*）变化。

*可能的意义是：观察到的PIN码本身和考虑到相邻数字的所有变化。

你能帮助我们找到所有这些变化吗？如果有一个函数，能够返回一个列表，其中包含一个长度为1到8位的观察到的PIN的所有变化，那就更好了。我们可以把这个函数命名为getPINs（在python中为get_pins，在C#中为GetPINs）。

但请注意，所有的PINs，包括观察到的PINs和结果，都必须是字符串，因为有可能会有领先的 "0"。我们已经为你准备了一些测试案例。
侦探，我们就靠你了!
代码提交地址：
<https://www.codewars.com/kata/5263c6999e0f40dee200059d>

---

#### 第三题： RNA到蛋白质序列的翻译（RNA to Protein Sequence Translation）

难度：6kyu

蛋白质是由DNA转录成RNA，然后转译成蛋白质的中心法则。RNA和DNA一样，是由糖骨架（在这种情况下是核糖）连接在一起的长链核酸。每个由三个碱基组成的片段被称为密码子。称为核糖体的分子机器将RNA密码子转译成氨基酸链，称为多肽链，然后将其折叠成蛋白质。

蛋白质序列可以像DNA和RNA一样很容易地可视化，作为大字符串。重要的是要注意，“停止”密码子不编码特定的氨基酸。它们的唯一功能是停止蛋白质的转译，因此它们不会被纳入多肽链中。“停止”密码子不应出现在最终的蛋白质序列中。为了节省您许多不必要（和乏味）的键入，已为您的氨基酸字典提供了键和值。

给定一个RNA字符串，创建一个将RNA转译为蛋白质序列的函数。注意：测试用例将始终生成有效的字符串。

```python
protein（'UGCGAUGAAUGGGCUCGCUCC'）
```

将返回`CDEWARS`

作为测试用例的一部分是一个真实世界的例子！最后一个示例测试用例对应着一种叫做绿色荧光蛋白的蛋白质，一旦被剪切到另一个生物体的基因组中，像GFP这样的蛋白质可以让生物学家可视化细胞过程！

Amino Acid Dictionary

```python
   # Your dictionary is provided as PROTEIN_DICT
   PROTEIN_DICT = {
    # Phenylalanine
    'UUC': 'F', 'UUU': 'F',
    # Leucine
    'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    # Isoleucine
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
    # Methionine
    'AUG': 'M',
    # Valine
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    # Serine
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'AGU': 'S', 'AGC': 'S',
    # Proline
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    # Threonine
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    # Alanine
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    # Tyrosine
    'UAU': 'Y', 'UAC': 'Y',
    # Histidine
    'CAU': 'H', 'CAC': 'H',
    # Glutamine
    'CAA': 'Q', 'CAG': 'Q',
    # Asparagine
    'AAU': 'N', 'AAC': 'N',
    # Lysine
    'AAA': 'K', 'AAG': 'K',
    # Aspartic Acid
    'GAU': 'D', 'GAC': 'D',
    # Glutamic Acid
    'GAA': 'E', 'GAG': 'E',
    # Cystine
    'UGU': 'C', 'UGC': 'C',
    # Tryptophan
    'UGG': 'W',
    # Arginine
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',
    # Glycine
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    # Stop codon
    'UAA': 'Stop', 'UGA': 'Stop', 'UAG': 'Stop'
}
```

代码提交地址：
<https://www.codewars.com/kata/555a03f259e2d1788c000077>

---

#### 第四题： 填写订单（Thinkful - Dictionary drills: Order filler）

难度：8kyu

您正在经营一家在线业务，您的一天中很大一部分时间都在处理订单。随着您的销量增加，这项工作占用了更多的时间，不幸的是最近您遇到了一个情况，您接受了一个订单，但无法履行。

您决定写一个名为`fillable()`的函数，它接受三个参数：一个表示您库存的字典`stock`，一个表示客户想要购买的商品的字符串`merch`，以及一个表示他们想购买的商品数量的整数n。如果您有足够的商品库存来完成销售，则函数应返回`True`，否则应返回`False`。

有效的数据将始终被传入，并且n将始终大于等于1。

代码提交地址：
<https://www.codewars.com/kata/586ee462d0982081bf001f07/python>

---

#### 第五题： 莫尔斯码解码器（Decode the Morse code, advanced）

难度： 4kyu

在这个作业中，你需要为有线电报编写一个莫尔斯码解码器。
有线电报通过一个有按键的双线路运行，当按下按键时，会连接线路，可以在远程站点上检测到。莫尔斯码将每个字符的传输编码为"点"（按下按键的短按）和"划"（按下按键的长按）的序列。

在传输莫尔斯码时，国际标准规定：

- "点" - 1个时间单位长。
- "划" - 3个时间单位长。
- 字符内点和划之间的暂停 - 1个时间单位长。
- 单词内字符之间的暂停 - 3个时间单位长。
- 单词间的暂停 - 7个时间单位长。

但是，该标准没有规定"时间单位"有多长。实际上，不同的操作员会以不同的速度进行传输。一个业余人士可能需要几秒钟才能传输一个字符，一位熟练的专业人士可以每分钟传输60个单词，而机器人发射器可能会快得多。

在这个作业中，我们假设消息的接收是由硬件自动执行的，硬件会定期检查线路，如果线路连接（远程站点的按键按下），则记录为1，如果线路未连接（远程按键弹起），则记录为0。消息完全接收后，它会以一个只包含0和1的字符串的形式传递给你进行解码。

例如，消息`HEYJUDE`，即`·····−·−−··−−−··−−··`可以如下接收：

```python
1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011
```

如您所见，根据标准，这个传输完全准确，硬件每个"点"采样了两次。

因此，你的任务是实现两个函数：

函数decodeBits(bits)，应该找出消息的传输速率，正确解码消息为点（.）、划（-）和空格（字符之间有一个空格，单词之间有三个空格），并将它们作为一个字符串返回。请注意，在消息的开头和结尾可能会出现一些额外的0，确保忽略它们。另外，如果你无法分辨特定的1序列是点还是划，请假设它是一个点。

函数decodeMorse(morseCode)，它将接收上一个函数的输出，并返回一个可读的字符串。

注意：出于编码目的，你必须使用ASCII字符.和-，而不是Unicode字符。

莫尔斯码表已经预加载给你了（请查看解决方案设置，以获取在你的语言中使用它的标识符）。

```python
morseCodes(".--")  #to access the morse translation of ".--"
```

下面是Morse码支持的完整字符列表：

```javascript
A    ·–
B    –···
C    –·–·
D    –··
E    ·
F    ··–·
G    ––·
H    ····
I    ··
J    ·–––
K    –·–
L    ·–··
M    ––
N    –·
O    –––
P    ·––·
Q    ––·–
R    ·–·
S    ···
T    –
U    ··–
V    ···–
W    ·––
X    –··–
Y    –·––
Z    ––··
0    –––––
1    ·––––
2    ··–––
3    ···––
4    ····–
5    ·····
6    –····
7    ––···
8    –––··
9    ––––·
.    ·–·–·–
,    ––··––
?    ··––··
'    ·––––·
!    –·–·––
/    –··–·
(    –·––·
)    –·––·–
&    ·–···
:    –––···
;    –·–·–·
=    –···–
+    ·–·–·
-    –····–
_    ··––·–
"    ·–··–·
$    ···–··–
@    ·––·–·
```

代码提交地址：
<https://www.codewars.com/kata/decode-the-morse-code-advanced>

---

### 第三部分

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

- [第一部分 Python列表操作和if语句](#第一部分)
  

- [第二部分 Codewars Kata挑战](#第二部分)

#### 第一题：淘气还是乖孩子（Naughty or Nice）
```python   
def naughty_or_nice(data):
    nau=0
    nic=0
    for mouth ,keys in data.items():
        for key , value in keys.items():
            if value=='Naughty':
                nau+=1
            elif value=='Nice':
                nic+=1
    if nic >= nau:
        return "Nice!"
    else:
        return "Naughty!"

```   
![Alt text](image-17.png)   


#### 第二题： 观察到的PIN（The observed PIN）
```python   
def get_pins(observed):
    PIN = {'1':['1','2','4'], '2':['1','2','3','5'], '3':['2','3','6'], '4':['1','4','5','7'], '5':['2','4','5','6','8'], '6':['3','5','6','9'], '7':['4','7','8'], '8':['5','7','8','9','0'], '9':['6','8','9'], '0':['0','8']}
    if len(observed) == 1:
        return PIN[observed]
    else:
        res = []
        first = observed[0]
        rest = get_pins(observed[1:])
        for value1 in PIN[first]:
            for value2 in rest:
                res.append(value1+value2)
        return res

```     
![Alt text](image-20.png)

#### 第三题： RNA到蛋白质序列的翻译（RNA to Protein Sequence Translation）  

```python   
def protein(rna):
    CDEWARS = ""
    for i in range(0, len(rna), 3):
        m = rna[i:i+3]
        n = PROTEIN_DICT[m]
        if n == "Stop":
            break
        CDEWARS += n
    return CDEWARS

```     
![Alt text](image-19.png)

#### 第四题： 填写订单（Thinkful - Dictionary drills: Order filler）  

```python   
def fillable(stock, merch, n):
    if merch in stock and stock[merch]>=n:
        return True
    else:
        return False

```      
![Alt text](image-18.png)

#### 第五题： 莫尔斯码解码器（Decode the Morse code, advanced）

```python   
def decode_bits(bits):
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
            


def decode_morse(morseCode):
    morseCode.strip()     #从莫尔斯码字符串中去除前导和尾随的空格
    result = ""
    characters = morseCode.split(" ")   #空格作为分隔符将字符串分割成单个字符
    for character in characters:
        if character != "":
            result += MORSE_CODE[character]
        else:
            result += " "
    return ' '.join(result.split())

```
![Alt text](image-21.png)



- [第三部分 使用Mermaid绘制程序流程图](#第三部分)

#### 题一   

```mermaid
flowchart LR   
A[Start] -->B[nau=0,nic=0]
B --> C[遍历 字典data]
C --> D[遍历 嵌套字典]
D --> E{判断 嵌套字典中 value='Naughty'?}
E -->|Yes| F[nau+=1]
F --> D
E -->|No| G{判断 嵌套字典中 value='Nice'?}
G -->|Yes| H[nic+=1]
H --> D
G -->|No| D
D -->|结束遍历| C
C -->|结束遍历| I{判断 nic >= nau ?}
I -->|Yes| J[返回 'Nice!']
I -->|No| K[返回 'Naughty!']
J --> L[End]
K --> L[End] 

```    

#### 题二   

```mermaid
flowchart LR  
A[Start] --> B{判断 数字长度是否是1}
B -->|Yes| C[返回 数字对应的可能数字列表]
B -->|No| D[初始化空列表 res]
D --> E[获取观察到的数字的第一个数字]
E --> F[递归调用'get_pins'函数]
F --> G[遍历第一个数字对应的可能数字列表]
G --> H[遍历其余数字的所有可能组合]
H --> I[组合连接所有可能形成新的密码组合]
I --> H
H -->|遍历结束| G
G -->|遍历结束| J[返回 列表 res]
J --> K[End]
C --> K[End]
```   

#### 题三   

```mermaid
flowchart LR  
A[Start] --> B[CDEWARS初始化为空字符串]
B --> C[在字符串 rna 中每次遍历长度为3 ]
C --> D[以3为单位 将rna中的字符放入m ]
D --> E[在字典PROTEIN_DICT 中找到关键字m的值]
E --> F{判断 n == 'Stop'?}
F -->|Yes| G[返回 CDEWARS ]
F -->|No| H[CDEWARS += n]
H --> C
C -->|遍历结束| G
G --> I[End]

```    

#### 题四  

```mermaid
flowchart LR   
A[Start] -->B{判断 merch在stock中并且 数量>=n}
B -->|Yes| C[返回 True]
B -->|No| D[返回 False]
C --> E[End]
D --> E[End]

```    








#### 题五   

```mermaid
flowchart LR
    A[start] --> B["bits.strip('0')"]
    B --> C[unit = 0]
    C --> D[for bit in bits]
    D --> E{"if bit != '0'"}
    E -->|Yes| F[unit += 1]
    E -->|No| G[break]
    G --> H[unit now might be 1 unit or 3 units]
    D -->|结束遍历| I[count = 1]
    H --> I
    I --> J["for i in range(1,len(bits))"]
    J --> K{"if bits[i] == bits[i-1]"}
    K -->|Yea| L[count += 1]
    K -->|No| M{if count < unit}
    L --> J
    M -->|Yes| N[unit = count]
    N --> O[count = 1]
    O -->J
    M -->|No| P[count = 1]
    P --> J
    J -->|结束遍历| Q[morse_code = ""]
    Q --> R["words = bits.split('0'*7*unit)"]

    R --> S[for word in words]
    S --> T["characters = word.split('0'*3*unit)"]
    T --> U[for character in characters]
    U --> V["signs = character.split('0'*unit)"]
    V --> W[for sign in signs]
    W --> X{"if sign == '1'*3*unit"}
    X -->|Yes| Y[morse_code += '-']
    X -->|No| Z[morse_code += '.']
    Y --> W
    Z --> W
    W -->|结束遍历| AA[morse_code += ' ']
    AA --> U
    U -->|结束遍历| AB[morse_code += '   ']
    AB --> S
    S -->|结束遍历| AC[return morse_code]
 
```    




## 实验考查

请使用自己的语言并使用尽量简短代码示例回答下面的问题，这些问题将在实验检查时用于提问和答辩以及实际的操作。

1. 字典的键和值有什么区别？    
   字典的键和值是成对出现的，键是字典中的唯一标识符，而值是与键相关联的数据。键必须是不可变的，例如字符串、数字或元组，而值可以是任意类型的数据。    
    区别如下：    
        唯一性：字典中的键是唯一的，每个键只能出现一次，而值可以重复。   
        可变性：字典的键必须是不可变的，而值可以是可变的。    
        访问方式：可以通过键来访问字典中的值，但不能通过值来访问字典中的键。     
        顺序：字典是无序的，键和值的存储顺序是不固定的，而列表是有序的。     
        用途：键通常用于查找和索引数据，而值用于存储和表示实际的数据。     

2. 在读取和写入字典时，需要使用默认值可以使用什么方法？     
   在读取和写入字典时，可以使用get()方法来设置默认值。   
   get()方法接受两个参数：键和默认值。    
   如果键存在于字典中，则返回对应的值；如果键不存在，则返回默认值。   

3. Python中的while循环和for循环有什么区别？     
    循环次数：for循环通常用于循环遍历一个序列或集合中的元素，循环次数是固定的，而while循环则可以根据条件来控制循环次数，循环次数是不确定的。   
    循环变量：for循环需要提供一个循环变量，用于在每次循环中获取序列或集合中的下一个元素，而while循环则需要在循环体内手动更新循环变量。    
    循环变量：for循环需要提供一个循环变量，用于在每次循环中获取序列或集合中的下一个元素，而while循环则需要在循环体内手动更新循环变量。    
    适用场景：for循环适用于在已知序列或集合中循环遍历元素的情况，而while循环适用于在未知条件下循环执行一段代码的情况。   


4. 阅读[PEP 636 – Structural Pattern Matching: Tutorial](https://peps.python.org/pep-0636/), 总结Python 3.10中新出现的match语句的使用方法。    
    (1) 基本语法：
    match value:
    pattern_1:
        # 执行代码块1
    ...
    pattern_n:
        # 执行代码块n
    (2)匹配顺序：   
    match语句按照从上到下的顺序进行模式匹配，只会执行第一个匹配成功的代码块，后续的模式不再匹配。    
    可以使用|操作符将多个模式组合在一起，表示匹配任意一个模式。     
    (3)模式匹配：   
    常量模式：匹配特定的常量值，例如42、"hello"。    
    变量模式：将匹配的值绑定到一个变量，例如x、name。     
    占位符模式：使用下划线_表示不关心的部分，不会绑定任何值。    
    类型模式：匹配指定的类型，使用type(...)进行匹配。     
    结构模式：匹配复杂的数据结构，例如元组、列表、字典等。    
    (4)条件匹配：     
    可以在模式中使用if语句进行条件匹配，例如pattern if condition。   
    只有当条件为真时，才会进行模式匹配     


## 实验总结

总结一下这次实验你学习和使用到的知识，例如：编程工具的使用、数据结构、程序语言的语法、算法、编程技巧、编程思想。
1. 字典是Python中非常重要的数据结构之一，它用于存储键值对，并且可以根据键快速查找对应的值。字典可以通过循环遍历来访问所有的键、值或键值对    
2. 字典的键必须是唯一的，而值可以重复    
3. 字典的键可以是任意不可变的数据类型，如整数、浮点数、字符串、元组等，但不能是可变的数据类型，如列表、字典。字典的值可以是任意的数据类型，甚至可以是另一个字典     
4. 字典提供了一些常用的方法，如keys()、values()、items()等，可以用于获取字典中的键、值或键值对。字典的复制可以使用copy()方法来实现，但是，复制的是字典的引用，而不是创建一个新的字典。    
5. 通过学习Python字典，我们可以更灵活地处理数据，提高代码的效率和可读性     
6. 通过学习Python的while循环，我们可以实现更加灵活和动态的代码逻辑，可以根据不同的条件来控制程序的执行流程。while循环在处理需要重复执行的任务时非常有用，可以提高代码的效率和可维护性。同时，需要注意循环条件的设置，以避免出现死循环的情况