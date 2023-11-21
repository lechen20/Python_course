# 《Python程序设计基础》程序设计作品说明书

题目： 外星人入侵游戏👽

学院： 21计科01

姓名： 陈乐

学号： B20190202222

指导教师： 周景

起止日期：2023.11.10-2023.12.10

## 摘要

_介绍本次设计完成的项目的概述，本文的主要内容，总结你主要完成的工作以及关键词。_

关键词：外星人入侵, pygame, alien, bullet, button, game_functions,    
        scoreboard, settings, ship, game_stats    

## 第1章 需求分析

1. 实现教材12章的功能：创建游戏窗口、添加飞船图像、驾驶飞船、飞船可以射击子弹。    
2. 实现教材13章的功能：创建一群外星人、外星人可以移动、可以射杀外星人、结束游戏。    
3. 实现教材14章的功能：添加Play按钮、可以提高等级、计分功能。     
4. 实现教材部分练习的功能：练习12-6将飞船放在屏幕左侧进行射击、练习13-2在游戏背景中随机位置绘制星星、练习14-5 将游戏中得到的最高分保存到文件中。    

## 第2章 分析与设计

### 项目设计   

#### 设计思想 

1. 在完成某一个需求前，首先确定职责 —— 要做的事情（方法）   

2. 根据职责确定不同的对象，在对象内部封装不同的方法（多个）   

3. 最后完成的代码，就是顺序地让不同的对象调用不同的方法   

    《外星人入侵》项目，是一个 飞船通过发射子弹消灭外星人来获取得分、升级的游戏。需要的对象有：飞船、子弹、外星人等等。   

#### 游戏流程   

1. 初始化游戏：pygame.init()   
2. 新建模块settings，包含Settings类，用于存储与游戏相关的所有设置    
3. 新建模块game_function，包含很多方法，用于存储与游戏相关的所有操作    
4. 新建游戏窗口对象   
5. 创建一艘飞船   
6. 创建一个子弹编组   
7. 创建一个外星人编组   
8. 创建一个游戏开始的按钮   
9. 创建一个用于存储游戏统计信息的实例   
10. 创建记分   
11. 创建外星人群   
12. 游戏的主循环   
    检测事件   
    针对不同事件，让不同的对象 调用 同的方法   



### 项目使用各类方法

#### 窗口相关操作   

1. 创建窗口   
    pygame.display.set_mode((窗口宽，窗口高))   
2. 设置窗口标题   
    pygame.display.set_caption("窗口标题")   
3. 设置窗口图标   
    pygame.display.set_icon(image)   
4. 指定坐标，将图片绘制到窗口   
    self.screen.blit(self.image,self.rect)   
    blit() ： 绘图方法   
5. 不断更新屏幕，命令pygame让最近绘制的屏幕可见   
    pygame.display.flip()   


#### 图像相关操作

1. pygame.image : 图像相关操作   
2. pygame.rect : 管理矩形区域   
3. 加载资源图片，返回图片对象（返回的就是surface）    
    image = pygame.image.load("图片路径")   
4. 获得图片矩形对象   
    get_rect()：获取相应surface的属性rect   
将游戏元素居中，可设相应rect对象的属性center,centerx或centery     
将游戏元素与屏幕边缘对齐，可使用属性top,bottom,left或right   
调整游戏元素的水平或垂直位置，可使用属性x和y，它们分别是相应矩形左上角的x和y坐标   
  rect = image.get_rect(centerx=x,centery=y)   
5. 默认情况下左上角坐标是(0,0)   
6. 绘制图形：pygame.draw()   
            blit()   
7. 在原位置基础上，移动指定的偏移量（x,y增加）   
    rect.move_ip(num1,num2)    
8. 判断两个矩形是否相交，相交返回True，否则返回False   
pygame.Rect.colliderect(rect1,rect2)    
同理，判断两个圆形是否相交，把rect改为circle    
判断两个组是否相交，改为groupcollide()    
检验任何图像是否发生碰撞，改为collideany()   

#### 事件相关操作   

1. QUIT 关闭窗口    
2. KEYDOWN 键盘按键   
3. KEYUP 松开键盘    
4. 获得所有事件的列表   
   for event in pygame.event.get()   
5. 鼠标点击关闭窗口事件   
    if event.type == pygame.QUIT   
        sys.exit()   
6. 键盘按下事件   
    if event.type == pygame.KEYDOWN   
7. 判断用户按下的键是否是a键   
    if event.key == pygame.K_q   
8. 无论单击屏幕什么地方，Pygame将检测到一个MOUSEBUTTONDOWN事件   
    pygame.mouse.get_pos()，返回一个元组，其中包含单击时的x和y坐标 


### 项目模块

#### sprite（精灵）模块：pygame.sprite

1. 作用：一种可以在屏幕上移动的图形对象，并且可以与其他图形对象交互。使用它，只需继承它，然后按需写出自己的类。    
2. sprite模块包含类Sprite    
3. 创建一个精灵组：pygame.sprite.Group()    

#### sys 模块 

1. 作用：sys.exit()退出当前程序    
2. 函数基本使用方法为：import sys后，直接调用就可以终止程序    


### 项目功能

#### 创建游戏窗口

    pygame.init()初始化背景设置
    screen = pygame.display.set_mode((1150,800))创建一个名为screen的窗口
    对象screen是一个surface。在Pygame中，surface是屏幕的一部分，用于显示游戏元素。
    display.set_mode()返回的surface是游戏窗口
    pygame.event.get()使用此方法监听所有键盘和鼠标事件，促使for循环的进行
    pygame.QUIT和sys.exit():当玩家点击窗口的关闭按钮时，将检测到 pygame.QUIT事件，则调用sys.exit()来退出游戏
    pygame.display.flip():每次执行while循环时都会绘制一个空屏幕，并擦去旧屏幕，使得只有新绘制的屏幕可见。这样可以实现不断更新屏幕显示元素的新位置。

![Alt text](image.png)

#### 添加飞船图像

1. 将图片设置为位图bmp格式最简单，因为pygame默认加载位图
2. 创建Ship类:    
    pygame.image.load:此函数可以返回一个表示飞船的surface，参数为存放图片的地址    
self.image.get_rect():加载图像后，使用get_rect()获取对应的surface属性 rect      
rect对象:处理rect对象时可使用矩形四角和中心的x,y坐标。通过这些参数指定矩形的位置
pygame中原点(0,0)位于屏幕左上角，向右下方移动时，坐标值将增大。右下角的坐标值为最大值     
self.rect.centerx:表示飞船中心的x坐标     
self.rect.bottom:表示飞船下边缘的y坐标     
两个属性设置好的效果为飞船处于屏幕底部中央    
blitme()方法可以根据self.rect指定的位置将图像绘制到屏幕上    

![Alt text](image-1.png)

#### 驾驶飞船

    每当用户按键时，都将在Pygame中注册一个事件。
    事件都是通过方法pygame.event.get()获取的，因此需要在方法_check_events()中指定要检查哪些类型的事件。
    每次按键都被注册为一个KEYDOWN事件。      
    Pygame检测到KEYDOWN事件时，需要检查按下的是否是触发行动的键。
    例如，如果玩家按下的是右箭头键，就增大飞船的rect.centerx值，将飞船向右移动.    
    在方法_check_events()中，为事件循环添加一个elif代码块，以便在Pygame检测到KEYDOWN事件时做出相应。
    我们检查按下键(event.key)是否是右箭头键(pygame.K_RIGHT)。如果是，就将self.ship.rect.centerx的值加1，从而将飞船向右移动。   
    如果现在运行alien_invasion.py，则每按右箭头一次，飞船都将向右移动1像素

#### 飞船射击子弹

    添加射击功能，玩家按空格键时发射子弹，子弹在屏幕中向上穿行，抵达屏幕边缘时消失。   

1. 添加子弹设置：更新 settings.py
2. 创建子弹类   
    pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height):   
    子弹并非是基于图像的，所以必须使用 pygame.Rect()从空白开始创建一个矩形。   
    在创建这个实例时，必须提供矩形左上角的x,y的坐标，还有此矩形的高度和宽度。   
    子弹的初始位置取决于飞船当前的位置，所以子弹的高度和宽度是从ai_settings中获得的。
3. 将子弹储存到编组group中     
    在alien_invasion.py文件中创建一个编组，用于存储所有有效子弹。    
    bullets.update():对编组调用update()时，编组将自动对齐其中的每个精灵调用update()。     
    所以会为编组中的每颗子弹调用bullets.update()
4. 射击子弹：在game_function.py 文件中修改             
    check_keydown_events()使得可以实现在按下空格时发射一颗子弹
5. 删除已消失的子弹：alien_invasion.py文件中添加检查条件     
    运行程序后发现，子弹到达屏幕顶端时会消失，但这是因为pygame无法在屏幕外面绘制子弹，但子弹仍然存在，只是y坐标为负数。      
    所以要真正删除已经在屏幕外的子弹，需要检查条件：子弹的rect的bottom属性为0，这代表子弹已经到达屏幕顶端。
6. 限制子弹数量：在settings.py文件中存储允许的最大子弹数    
7. 重构代码：将子弹管理代码重构至模块game_functins中，重构代码可以使主程序更简洁。

#### 创建一群外星人


1. 确定屏幕上一行可以容纳多少个外星人     
    一行可容纳的外星人个数当然是个设置的游戏屏幕宽度有关。     
    在放外星人时也不想让外星人占满屏幕，需要实现在一行外星人的两端空出一点空白。    
    我们把两边留白的宽度设置为外星人的宽度，现在可以确定屏幕上一行可用于放置外星人的空间宽度为：    
    screen_width-(2*alien_width)     
    两个外星人之间也需要留白，否则出来的效果会是一个紧贴另一个。        
    我们将两个外星人之间的留白宽度也设置为外星人的宽度。      
    这样显示一个外星人所需宽度就为实际外星人图片宽度的两倍:      
    一个宽度放置外星人图片，另一个宽度为外星人图片右边的留白     
    现在确定了一行实际可容纳的外星人个数为:上面用于放置外星人的空间宽度/(2*alien_width)
2. 创建多行外星人   
    在alien_invasion.py中编写新函数create_fleet()
3. 添加行     
    要创建外星人群，需要计算游戏屏幕可容纳多少行外星人。并对创建一行外星人的代码循环重复对应行数。      
    计算可用垂直空间的方法：    
    将屏幕高度减去第一行外星人的上边距（设置为外星人高度）、飞船的高度以及最初外星人群与飞船的距离（设置为外星人高度的两倍）：    
    al_settings.screen_height-3*alien_height-ship_height     
    运行效果为在飞船上方留出一定空白区域，给玩家留出射击外星人的时间    
    每行外星人的下方也需要留白，设置为外星人的高度。和计算一行容纳的外星人数量逻辑一样。    
    我们用可用垂直空间除以外星人高度的两倍: number_rows=available_space_y / (2* alien_height)    
    我们在game_functions中添加相应代码
![Alt text](image-2.png)

#### 外星人可以移动

    我们先实现让外星人群在屏幕上向右移动，撞到屏幕边缘后下移一定距离，再沿反方向移动。
    不断移动所有外星人，直到所有外星人都被消灭

1. 向右移动外星人：修改alien.py中的update方法
2. 创建表示外星人移动方向的设置:在settings.py中实现    
    需要实现的效果为:外星人撞到屏幕右边缘后向下移动，再向左移动。  
3. 检查外星人是否撞到了屏幕边缘:在alien.py中添加check_edges()函数来实现
4. 向下移动外星人群并改变移动方向:对game_functions.py作出修改     
    当有外星人到达屏幕边缘时，需要将外星人下移并改变移动方向.    
    编写函数 check_fleet_edges和函数change_fleet_direction

#### 射杀外星人

    本节我们将编写飞船子弹射击外星人代码。
    在子弹击中外星人时需要检查碰撞。在游戏编程中，碰撞是指游戏元素重叠在一起。

1. 要让子弹能够击落外星人，我们就需要使用sprite.groupcollide()方法检测两个编组的成员之间的碰撞     
    在game_functions.py中修改函数update_bullets()的代码    
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True):    
    sprite.groupcollide方法将每颗子弹的rect和每个外星人的rect进行比较，并返回一个字典，
    其中包含了发生了碰撞的子弹和外星人。    
    在这个字典中，每一个键是一颗子弹，对应的值是被击中的外星人    
    这行代码表示遍历编组bullets中的每颗子弹，再遍历编组aliens中的每个外星人。    
    每当有子弹和外星人的rect重叠时，groupcollide就在它返回的字典中添加一个键值对。     
    两个实参True告诉pygame删除发生碰撞的子弹和外星人
2. 生成新的外星人群    
    要实现在外星人群被消灭后又显示一群外星人，首先要检查编组aliens是否为空。
    如果为空，就调用creat_fleet()。我们在game_functions.py中的 update_bullets函数中编写检查代码
3. 重构update_bullets()    
    我们将处理子弹和外星人碰撞的代码移动到一个独立的函数中: check_bullet_alien_collisions()函数

#### 计分功能

    本节我们来实现一个游戏记分系统，实时跟踪玩家得分，并显示最高得分、当前等级、和余下的飞船数
    在game_stats.py中添加一个score属性

1. 显示得分:创建一个新类:Scoreboard来实现在屏幕上显示得分
2. 创建记分牌:在alien_invasion.py中创建一个Scoreboard实例
3. 在外星人被消灭时更新得分:更新score的值，再调用prep_score()更新得分图像
4. 将消灭的每个外星人的点数都计入得分:    
    当前的代码在记分时略有瑕疵。    
    例如:如果在一次循环中有两颗子弹击中了外星人，或者因子弹设置的更宽而同时击中了多个外星人，    
    玩家只能得到一个被消灭外星人的得分。
5. 提高点数:    
    玩家每提高一个等级，游戏都会变得更难，在处于更高等级时，击落外星人的得分应更高
6. 设置分数格式:    
    round(self.stats.score，-1):   
    函数round()可以让小数精确到小数点后多少位，其中小数位数是由第二个参数指定的。    
    但当第二个参数为负数时，round()函数将整数调整到10、100、1000等整数倍    
    score_str = "{:,}".format(rounded_score):    
    此处使用了一个字符串格式设置指令，它让python将数值转换为字符串时，在其中插入逗号    
    运行效果为:玩家得分1000000,则屏幕上显示1.000.000
7. 最高得分:实现跟踪并显示最高得分   
8. 显示玩家等级:在game_stats.py中添加一个表示当前等级的属性
9. 示余下的飞船数:   
    实现显示玩家还有多少飞船，在屏幕左上角绘制飞船图像来显示还余下多少艘飞船

![Alt text](image-3.png)

#### 提高等级

    当整群外星人被消灭完后，玩家将提高一个等级，并且加快游戏节奏

1. 修改速度设置:   
    重新组织settings.py,将游戏设置分为静态和动态的两组。
2. 重置速度:   
    每当玩家开始新游戏时，我们都需要将发生了变化的设置重置为初试值。
    否则新游戏开始时，新游戏设置将是前一次游戏增加了的值

![Alt text](image-5.png)

#### 添加Play按钮

    本节我们将添加一个play按钮，它在游戏开始前出现，并在游戏结束后再次出现，
    使玩家能够开始新游戏现在主程序是alien_invasion.py，所以在运行主程序时游戏开始。
    我们需要让游戏一开始处于非活动状态，并提示玩家点击play按钮开始游戏。
    现在主程序是alien_invasion.py，所以在运行主程序时游戏开始。
    我们需要让游戏一开始处于非活动状态，并提示玩家点击play按钮开始游戏。
    在game_stats.py中修改代码

1. 创建button类:    
    pygame没有内置的创建按钮的方法，需要我们创建一个Button类，用于创建带标签的实心矩形。
2. 在屏幕上绘制按钮:在alien_invasion.py中创建play按钮
3. 开始游戏:    
    要实现单击play按钮开始游戏，我们在game_invasion.py中添加监视与这个按钮相关的鼠标事件代码来实现此功能
4. 重置：game_functions	文件中修改相关代码    
    前面代码只编写了处理玩家第一次单击play按钮的情况，而没有处理游戏结束的情况。   
    因为我们没有重置导致游戏结束的条件   
    为了实现在玩家每次单击play按钮时都重置游戏，   
    需要重新重置统计信息、删除现有的外星人和子弹、创建一群新的外星人、让飞船居中
5. 将play按钮切换到非活动状态    
    当前有一个问题，即使play按钮不可见，在单击原来所在区域时，游戏依然会做出响应重置。    
    为修复这个问题，我们设置让游戏仅在game_active为 false时才开始
6. 隐藏光标      
    在开始游戏时，我们要让光标可见玩家才能点击play按钮。     
    在游戏开始以后，我们在游戏处于活动状态时设置让光标不可见


![Alt text](image-4.png)

#### 结束 游戏

    本节我们将给这个小游戏设置游戏结束的条件:比如:
    玩家没有在足够短的时间内将外星人群消灭干净，并且有外星人碰到了飞船，飞船将被摧毁。
    同时，限制可供玩家使用的飞船数量，当有外星人触碰到游戏屏幕底端时，飞船也会被摧毁。当玩家用光了所有飞船，游戏结束。

1. 检查外星人和飞船之间的碰撞:     
    在更新每个外星人的位置后立即检查外星人和飞船之间的碰撞。    
    spritecollideany(ship, aliens):    
    此方法接受两个实参:一个精灵和一个编组。     
    它检查编组是否有成员与精灵发生了碰撞，并在找到与精灵发生碰撞了的编组成员后就停止遍历编组。    
    当没有发生碰撞时，此方法就返回None
2. 响应外星人和飞船的碰撞:     
    在确定了外星人和飞船发生碰撞后，需要做出响应。    
    我们创建一个新的ship实例，通过跟踪游戏的统计信息来记录飞船被碰撞了多少次。    
    创建一个用于统计游戏信息的新类GameStats
3. 响应外星人到达屏幕底端:     
    在game_functions中创建新函数check_aliens_bottom
4. 游戏结束:    
    在game_stats.py中添加一个标志属性game_active


## 第3章 软件测试

_本章的内容主要包括以类和函数作为单元进行单元测试，编写的对系统的主要功能的测试用例，以及测试用例执行的测试报告。_


### 飞船移动

    我们使用unittest模块编写了一个TestShipMovement类，其中包含了两个测试方法test_move_left和test_move_right。在每个测试方法中，我们首先初始化pygame和创建一个屏幕实例，然后创建一个飞船实例。接着我们设置飞船的移动标志为True，并调用飞船的update方法来模拟飞船的移动。最后使用断言来验证飞船的位置是否正确地发生了变化。

```python
import unittest
import pygame
from ship import Ship
from settings import Setting

class TestShipMovement(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.ai_settings = Setting()
        self.screen = pygame.display.set_mode((self.ai_settings.screen_width, 
                                                self.ai_settings.screen_height))
        self.ship = Ship(self.ai_settings, self.screen)

    def test_move_left(self):
        initial_center_x = self.ship.rect.centerx
        self.ship.moving_left = True
        self.ship.update()
        self.assertEqual(self.ship.rect.centerx, 
                        initial_center_x - self.ai_settings.ship_speed)

    def test_move_right(self):
        initial_center_x = self.ship.rect.centerx
        self.ship.moving_right = True
        self.ship.update()
        self.assertEqual(self.ship.rect.centerx, 
                        initial_center_x + self.ai_settings.ship_speed)

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()


```

测试结果：
![Img](./FILES/project_report.md/img-20231121154142.png)


### 外星人移动

    我们首先创建了一个 Alien 对象，并使用 MockScreen 和 MockSettings 来模拟屏幕和设置。然后我们编写了一个测试用例 test_update() 来测试外星人的 update() 方法。在测试用例中，我们首先获取外星人的初始 x 坐标，然后调用 update() 方法，最后再获取外星人的新 x 坐标，并使用 assertNotEqual() 函数来检查新位置是否与旧位置不同。

```python

import unittest
from alien import Alien

class TestAlien(unittest.TestCase):
    def setUp(self):
        # 创建一个屏幕对象，这里可以使用模拟的屏幕对象
        self.screen = MockScreen()
        self.ai_settings = MockSettings()
        self.alien = Alien(self.ai_settings, self.screen)

    def test_update(self):
        initial_x = self.alien.x
        self.alien.update()
        new_x = self.alien.x
        self.assertNotEqual(initial_x, new_x)

class MockScreen:
    def get_rect(self):
        return MockRect()

class MockSettings:
    alien_speed = 1
    fleet_direction = 1

class MockRect:
    right = 100
    left = 0

```
测试结果：
![Alt text](image-6.png)

### 飞船射击

    我们使用unittest模块编写了一个TestShooting类，其中包含了三个测试方法test_fire_bullets、test_check_bullet_alien_collisions和test_update_bullets。在每个测试方法中，我们首先初始化pygame和创建屏幕、飞船、子弹和外星人实例。然后我们调用相应的方法来模拟射击动作、子弹和外星人的碰撞以及子弹的更新。最后使用断言来验证相应的功能是否正确地发生了变化。


```python

import unittest
import pygame
from ship import Ship
from bullet import Bullet
from alien import Alien
from settings import Setting 
from game_stats import GameStats
from scoreboard import Scoreboard
from game_functions import update_bullets, fire_bullets, 
                            check_bullet_alien_collisions

class TestShooting(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1150, 800))
        self.ai_settings = Setting()
        self.ship=Ship(self.ai_settings,self.screen) 
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stats=GameStats(self.ai_settings)
        self.sb=Scoreboard(self.ai_settings,self.screen,self.stats)

    def test_fire_bullets(self):
        initial_bullet_count = len(self.bullets)
        fire_bullets(self.ai_settings, self.screen, self.ship, self.bullets)
        self.assertEqual(len(self.bullets), initial_bullet_count + 1)

    def test_check_bullet_alien_collisions(self):
        bullet = Bullet(self.ai_settings, self.screen, self.ship)
        self.bullets.add(bullet)
        alien = Alien(self.ai_settings, self.screen)
        self.aliens.add(alien)
        initial_alien_count = len(self.aliens)
        check_bullet_alien_collisions(self.ai_settings, self.screen, self.stats, 
                                        self.sb, self.ship, self.aliens, self.bullets)
        self.assertEqual(len(self.aliens), initial_alien_count )

    def test_update_bullets(self):
        bullet = Bullet(self.ai_settings, self.screen, self.ship)
        self.bullets.add(bullet)
        update_bullets(self.ai_settings, self.screen, self.stats, self.sb, 
                        self.ship, self.aliens, self.bullets)
        self.assertEqual(len(self.bullets), 0)

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()

```
测试结果：
![Img](./FILES/project_report.md/img-20231121161818.png)

### 得分等级计算功能

    编写了三个测试方法来测试得分计算功能。第一个测试方法 test_defeat_alien_score_calculation() 模拟了击败外星人事件，检查得分是否增加。第二个测试方法 test_level_calculation() 模拟了得分达到一定值时，等级是否增加。第三个测试方法 test_high_score_calculation() 模拟了得分超过历史最高得分时，最高得分是否会更新。

```python

import pygame
import pygame.font
import unittest
from ship import Ship
from bullet import Bullet
from alien import Alien
from scoreboard import Scoreboard
from settings import Setting
from game_stats import GameStats
from game_functions import check_bullet_alien_collisions,check_high_score

class TestScoreboard(unittest.TestCase):
    def setUp(self):
        # 创建一个屏幕对象，这里可以使用模拟的屏幕对象
        pygame.init()
        pygame.font.init()
        #self.font = pygame.font.SysFont("comicsansms", 50)
        self.screen = pygame.display.set_mode((1150, 800))
        self.ai_settings = Setting()
        self.stats = GameStats(self.ai_settings)
        self.scoreboard = Scoreboard(self.ai_settings, self.screen, self.stats)
        self.ship=Ship(self.ai_settings,self.screen)  #绘制一艘飞船
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
    

    def test_defeat_alien_score_calculation(self):
        # 模拟击败外星人事件，得分应该增加
        self.stats.score = 1500    #设置当前得分为1500
        collisions=pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        check_bullet_alien_collisions(self.ai_settings,self.screen,self.stats,
                                    self.scoreboard,self.ship,self.aliens,self.bullets)  # 模拟击败外星人事件
        if len(self.aliens) ==0:               #没有外星人时，得分不变
            self.assertTrue(self.stats.score == 1500 )
        if collisions:                         #发生碰撞时
            self.assertTrue(self.stats.score > 1500 )

    def test_level_calculation(self):
        # 模拟得分达到一定值时，等级应该增加
        self.stats.score = 1500  # 设置当前得分为1500
        check_bullet_alien_collisions(self.ai_settings,self.screen,self.stats,
                                    self.scoreboard,self.ship,self.aliens,self.bullets)  # 重新计算等级
        self.assertEqual(self.stats.level, 2)  # 预期等级为2

    def test_high_score_calculation(self):
        # 模拟得分超过历史最高得分时，最高得分应该更新
        self.stats.high_score = 1000 # 设置历史最高得分为1000
        self.stats.score = 1500 # 设置当前得分为1500
        check_high_score(self.stats,self.scoreboard)
        self.assertEqual(self.stats.high_score, 1500)  # 预期最高得分更新为1500

```
测试结果：
![Img](./FILES/project_report.md/img-20231121183124.png)



## 结论

_本章的内容主要是对项目的总结，项目主要实现了哪些功能，达到了哪些目标，哪些不足之处，可以如何改进。_

在本篇学习了：游戏开发计划的指定，以及使用Pygame编写的游戏的基本结构；如何设置背景色，以及如何将设置存储在独立的类中，以便轻松调整；如何在屏幕上绘制图像，以及如何让玩家控制游戏元素和移动；创建自动移动的元素，如在屏幕中向上飞行的子弹，以及删除不再需要的对象；如何定期重构项目的代码，为后续开发提供便利。

## 参考文献
