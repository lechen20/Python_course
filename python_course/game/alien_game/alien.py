#alien.py
#控制外星人类

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        #初始化外星人并设置起始位置
        super().__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        
        #加载外星人图片，并设置其属性
        self.image = pygame.image.load('d:/all_course/PythonC/course/alien_game/images/2.bmp')
        self.rect=self.image.get_rect()
        
        #每个外星人最初都在屏幕左上角附近
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        
        #存储外星人的准确位置
        self.x=float(self.rect.x)
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
        
    def update(self):
        self.x+=(self.ai_settings.alien_speed*
                self.ai_settings.fleet_direction)
        #将外星人的移动量设置为外星人的速度和fleet_direction值的乘积
        
        self.rect.x=self.x


    #检查外星人是否撞到了屏幕边缘
    def check_edges(self):
        #如果外星人位于屏幕边缘就返回True
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            #如果外星人的rect的right属性大于或者等于屏幕的rect的right属性
            #就说明外星人位于屏幕的右边缘
            return True
        elif self.rect.left<=0:
            return True