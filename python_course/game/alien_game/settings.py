#settings.py
#存储游戏的所有设置类
class Setting():
    def __init__(self):   
        #初始化游戏的静态设置
        #屏幕设置
        self.screen_width=1150
        self.screen_height=800
        self.bg_color=(100, 150, 200)    #设置背景颜色为蓝色
        self.ship_limit=3
        
        
        #子弹设置(宽3 像素，高15像素的深灰色子弹)
        self.bullet_width=5
        self.bullet_height=20
        self.bullet_color=250,0,0
        self.bullets_allowed=3
        
        #外星人设置
        self.fleet_drop_speed=10
        
        #以什么样的速度加快游戏节奏
        self.speedup_scale=1.1
        self.initialize_dynamic_settings()
        
        #击落外星人得分的提高速度
        self.score_scale=1.5
        
    def initialize_dynamic_settings(self):
        #初始化游戏的动态设置
        self.ship_speed=1.5  #飞船速度（每次移动1.5像素）
        self.bullet_speed=1
        self.alien_speed=1
        self.fleet_direction=1
        self.alien_points=5 #击落一个外星人得5分
        
    def increase_speed(self):
        #提高速度设置
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)