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