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

def setUp(self):
    pygame.init()
    self.screen = pygame.display.set_mode((1150, 800)) # 创建窗口
    self.ai_settings = Setting() # 创建游戏设置实例
    self.ship=Ship(self.ai_settings,self.screen) # 创建飞船实例
    self.bullets = pygame.sprite.Group() # 创建子弹组
    self.aliens = pygame.sprite.Group() # 创建外星人组
    self.stats=GameStats(self.ai_settings) # 创建游戏状态实例
    self.sb=Scoreboard(self.ai_settings,self.screen,self.stats) # 创建记分牌实例

def test_fire_bullets(self):
    initial_bullet_count = len(self.bullets) # 记录初始子弹数
    fire_bullets(self.ai_settings, self.screen, self.ship, self.bullets) # 发射子弹
    self.assertEqual(len(self.bullets), initial_bullet_count + 1) # 检查子弹数是否增加

def test_check_bullet_alien_collisions(self):
    bullet = Bullet(self.ai_settings, self.screen, self.ship) # 创建子弹实例
    self.bullets.add(bullet) # 将子弹加入子弹组
    alien = Alien(self.ai_settings, self.screen) # 创建外星人实例
    self.aliens.add(alien) # 将外星人加入外星人组
    initial_alien_count = len(self.aliens) # 记录初始外星人数
    check_bullet_alien_collisions(self.ai_settings, self.screen, self.stats, 
                                    self.sb, self.ship, self.aliens, self.bullets) # 检查子弹和外星人的碰撞
    self.assertEqual(len(self.aliens), initial_alien_count ) # 检查外星人数是否减少

def test_update_bullets(self):
    bullet = Bullet(self.ai_settings, self.screen, self.ship) # 创建子弹实例
    self.bullets.add(bullet) # 将子弹加入子弹组
    update_bullets(self.ai_settings, self.screen, self.stats, self.sb, 
                    self.ship, self.aliens, self.bullets) # 更新子弹位置
    self.assertEqual(len(self.bullets), 0) # 检查子弹数是否减少

def tearDown(self):
    pygame.quit() # 退出pygame


if __name__ == '__main__':
    unittest.main()
