import pygame
import sys
from random import randint
from star import Star

class StarSky:
    def __init__(self):
        #初始化 
        pygame.init()

        # 创建一个显示窗口，并设置窗口尺寸
        self.screen = pygame.display.set_mode((1000, 800))
        #  设置背景色
        self.bg_color = (20, 20, 20)

        self.stars = pygame.sprite.Group()
        self._create_starry()

        pygame.display.set_caption("Star Sky")

    def _create_starry(self):
        # 创建星群 
        # 创建一个星星并计算一行可容纳多少个星星
        star = Star(self)
        star_width, star_height = star.rect.size
        # 屏幕x方向左右各预留一个星星宽度
        self.availiable_space_x = self.screen.get_rect().width - (2 * star_width)
        # 星星的间距为星星宽度的3倍
        number_stars_x = self.availiable_space_x // (4 * star_width) + 1

        # 计算屏幕可容纳多少行星星
        # 屏幕y方向上下各预留一个星星宽度
        self.availiable_space_y = self.screen.get_rect().height - (2 * star_height)
        # 星星的间距为星星高度的3倍
        number_rows = self.availiable_space_y // (4 * star_height) + 1

        # 创建星群
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        # 创建一个星星并将其加入到当前行
        star = Star(self)
        star.rect.x = randint(0, self.availiable_space_x)
        star.rect.y = randint(0, self.availiable_space_y)
        self.stars.add(star)

    def starry(self):
        # 开始星空展示 
        while True:
            # 屏幕展示
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # 每次循环时都重绘屏幕
            self.screen.fill(self.bg_color)

            self.stars.draw(self.screen)

            # 让最近绘制的屏幕可见
            pygame.display.flip()


if __name__ == '__main__':
    # 创建实例并运行
    sky = StarSky()
    sky.starry()