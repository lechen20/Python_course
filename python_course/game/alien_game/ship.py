#ship.py
#管理飞船行为的类
import pygame 
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_settings,screen): 
        super().__init__()
        self.screen=screen  #screen 用来指定绘制飞船的位置
        self.ai_settings=ai_settings  #ai_settings让飞船获取到速度设置
        self.image=pygame.image.load('d:/all_course/PythonC/course/alien_game/images/1.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=self.screen.get_rect()
        
        #将每艘新飞船放在屏幕中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        
        #在飞船的属性centerx中存储小数值
        self.center=float(self.rect.centerx)
        
        #移动标志,玩家按下右键时，将标志设为true，
        #松开重设为false
        self.moving_right=False
        self.moving_left=False
    
    #方法update()检查标志状态，标志为true时调整飞船位置
    def update(self):
        
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center += self.ai_settings.ship_speed
        if self.moving_left and self.rect.left>0:
            self.center -= self.ai_settings.ship_speed
        
        #根据self.center更新rect对象
        self.rect.centerx=self.center
        
        
    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)
        
    def center_ship(self):
        #让飞船在屏幕上居中
        self.center=self.screen_rect.centerx