import unittest
import pygame
from ship import Ship
from settings import Setting

def setUp(self):
    pygame.init()
    self.ai_settings = Setting() # 创建游戏设置实例
    self.screen = pygame.display.set_mode((self.ai_settings.screen_width, 
                                            self.ai_settings.screen_height)) # 创建窗口
    self.ship = Ship(self.ai_settings, self.screen) # 创建飞船实例

def test_move_left(self):
    initial_center_x = self.ship.rect.centerx # 记录初始中心x坐标
    self.ship.moving_left = True # 设置向左移动标志为True
    self.ship.update() # 更新飞船位置
    self.assertEqual(self.ship.rect.centerx, 
                    initial_center_x - self.ai_settings.ship_speed) # 检查飞船位置是否正确

def test_move_right(self):
    initial_center_x = self.ship.rect.centerx # 记录初始中心x坐标
    self.ship.moving_right = True # 设置向右移动标志为True
    self.ship.update() # 更新飞船位置
    self.assertEqual(self.ship.rect.centerx, 
                    initial_center_x + self.ai_settings.ship_speed) # 检查飞船位置是否正确

def tearDown(self):
    pygame.quit() # 退出pygame


if __name__ == '__main__':
    unittest.main()