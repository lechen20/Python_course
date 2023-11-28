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