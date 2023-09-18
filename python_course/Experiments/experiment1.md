# 实验一 Git和Markdown基础

班级： 21计科1

学号： 20190202222

姓名： 陈乐

Github地址：<https://github.com/lechen20/python_course>

---

## 实验目的

1. Git基础，使用Git进行版本控制
2. Markdown基础，使用Markdown进行文档编辑

## 实验环境

1. Git
2. VSCode
3. VSCode插件

## 实验内容和步骤

### 第一部分 实验环境的安装

1. 安装git，从git官网下载后直接点击可以安装：[git官网地址](https://git-scm.com/)
2. 从Github克隆课程的仓库：[课程的仓库地址](https://github.com/zhoujing204/python_course)，运行git bash应用（该应用包含在git安装包内），在命令行输入下面的命令（命令运行成功后，课程仓库会默认存放在Windows的用户文件夹下）

```bash
git clone https://github.com/zhoujing204/python_course.git
```

如果你在使用`git clone`命令时遇到SSL错误，请运行下面的git命令(这里假设你的Git使用了默认安装目录)：

```bash
git config --global http.sslCAInfo C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt
```

该仓库的课程材料后续会有更新，如果需要更新课程材料，可以在本地课程仓库的目录下运行下面的命令：

```bash
git pull
```

3. 注册Github账号，创建一个新的仓库，用于存放实验报告和实验代码。
4. 安装VScode，下载地址：[Visual Studio Code](https://code.visualstudio.com/)
5. 安装下列VScode插件
   - GitLens
   - Git Graph
   - Git History
   - Markdown All in One
   - Markdown Preview Enhanced
   - Markdown PDF
   - Auto-Open Markdown Preview
   - Paste Image
   - markdownlint

### 第二部分 Git基础

教材《Python编程从入门到实践》P440附录D：使用Git进行版本控制，按照教材的步骤，完成Git基础的学习。

### 第三部分 learngitbranching.js.org

访问[learngitbranching.js.org](https://learngitbranching.js.org)，如下图所示完成Main部分的Introduction Sequence和Ramping Up两个小节的学习。

![Learngitbranching.js.org](/Experiments/img/2023-07-28-21-07-40.png)

上面你学习到的git命令基本上可以应付百分之九十以上的日常使用，如果你想继续深入学习git，可以：

- 继续学习[learngitbranching.js.org](https://learngitbranching.js.org)后面的几个小节（包括Main和Remote）
- 在日常的开发中使用git来管理你的代码和文档，用得越多，记得越牢
- 在git使用过程中，如果遇到任何问题，例如：错误删除了某个分支、从错误的分支拉取了内容等等，请查询[git-flight-rules](https://github.com/k88hudson/git-flight-rules)

### 第四部分 Markdown基础

查看[Markdown cheat-sheet](http://www.markdownguide.org/cheat-sheet)，学习Markdown的基础语法

使用Markdown编辑器（例如VScode）编写本次实验的实验报告，包括[实验过程与结果](#实验过程与结果)、[实验考查](#实验考查)和[实验总结](#实验总结)，并将其导出为 **PDF格式** 来提交。

## 实验过程与结果

请将实验过程中编写的代码和运行结果放在这里，注意代码需要使用markdown的代码块格式化，例如Git命令行语句应该使用下面的格式：

![Git命令](/Experiments/img/2023-07-26-22-48.png)

显示效果如下：

```bash
git init
git add .
git status
git commit -m "first commit"
```

Introduction Sequence
1.Git Commit

```bash
git commit           #创建新的提交记录
git commit
```

2.Git Branch

```bash
git branch bugFix    #创建新的分支
git checkout bugFix  #切换到这个分支
```

3.Git Merge

```bash
git branch bugFix    #创建一个新的名字叫bugFix分支
git checkout bugFix  #切换到这个分支
git commit           #提交一次
git checkout main    #切换回到main分支
git commit           #提交一次
git merge bugFix     #合并分支
```

4.Git rebase

```bash
git branch bugFix    #创建一个新的名字叫bugFix分支
git checkout bugFix  #切换到这个分支
git commit           #提交一次
git checkout main    #切换回到main分支
git commit           #提交一次
git checkout bugFix  #切换到这个分支
git rebase main      #合并分支
```

Ramping Up
1.分离HEAD

```bash
git checkout C4     #由HEAD->main->C4，变成HEAD->C4
```

2.相对引用^

```bash
git checkout C4^     #向上移动一个提交记录
```

3.相对引用2~（可强制移动分支）

```bash
git branch -f bugFix HEAD~2  #将bugFix分支强制指向HEAD的第2级父提交
git branch -f main C6        #将main分支强制指向C6
git checkout HEAD^           #切换到HEAD的上一个提交记录
```

4.撤销变更

```bash
git reset HEAD~1       #退回上一个(删去C2，保留C1)——本地分支
git checkout pushed    #切换到这个分支
git revert HEAD        #引入C2'相当于C1的状态——远程分支

```




如果是Python代码，应该使用下面代码块格式，例如：

![Python代码](/Experiments/img/2023-07-26-22-52-20.png)

显示效果如下：

```python
def add_binary(a,b):
    return bin(a+b)[2:]
```

代码运行结果的文本可以直接粘贴在这里。

**注意：不要使用截图，Markdown文档转换为Pdf格式后，截图可能会无法显示。**

## 实验考查

请使用自己的语言回答下面的问题，这些问题将在实验检查时用于提问和答辩，并要求进行实际的操作。

1. 什么是版本控制？使用Git作为版本控制软件有什么优点？
2. 如何使用Git撤销还没有Commit的修改？如何使用Git检出（Checkout）已经以前的Commit？（实际操作）
3. Git中的HEAD是什么？如何让HEAD处于detached HEAD状态？（实际操作）
4. 什么是分支（Branch）？如何创建分支？如何切换分支？（实际操作）
5. 如何合并分支？git merge和git rebase的区别在哪里？（实际操作）
6. 如何在Markdown格式的文本中使用标题、数字列表、无序列表和超链接？（实际操作）

## 实验总结

总结一下这次实验你学习和使用到的知识，例如：编程工具的使用、数据结构、程序语言的语法、算法、编程技巧、编程思想。

1.Git 基础
初步学习使用git进行版本控制，了解到版本控制是一种可以记录文件或代码在不同时间点的变化，并且能够追踪、管理和恢复这些变化的系统，还了解到Git作为一种分布式版本控制系统，具有强大的分支管理、高效的性能、完整的历史记录和强大的冲突解决功能。
通过学习和闯关：
基础：git commit、git branch、git merge、git rebase
高级：分离HEAD、相对引用^、相对引用2~（可强制移动分支）、撤销变更
实操学习，使我更加形象的理解一些基础命令，为我接下来熟练使用git和代码管理打下良好的基础。例如分支管理：Git的分支管理功能非常强大，学习Git基础命令后，您可以使用git branch命令创建和查看分支，使用git checkout命令切换分支，使用git merge命令合并分支；版本回退：可以使用git reset命令回退到之前的版本，这样可以轻松地查看代码的演变过程，比较不同版本之间的差异，并且可以回滚到之前的版本。除此之外还有git revert用于撤销某次提交的修改，它会创建一个新的提交，将之前提交的修改撤销掉，这个新的提交会保留之前提交的历史记录，因此可以避免历史记录的混乱等等还有非常多且能够提供效率的命令，是需要我接下来继续学习的。

2.Markdown基础
虽然是初次学习和使用Markdown，但已经感受到它的简洁易读易写的特点了，在初次使用过程中，因为不够熟练，还是需要查使用资料，不过我相信经过持续的使用，Markdown会成为我之后常用的文本编辑语言，我会继续探寻它的优点和功能。
