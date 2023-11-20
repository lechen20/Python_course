#game_stats.py
#跟踪游戏统计信息的类
class GameStats():
    def __init__(self,ai_settings):
        self.ai_settings=ai_settings
        self.reset_stats()
        self.high_score=0
        
        #设置让游戏一开始处于非活动状态
        self.game_active=False
        
    def reset_stats(self):
        self.ship_left=self.ai_settings.ship_limit
        #当玩家重新开始时，需要重置一些统计信息，所以使用reset_stats方法来初始化统计信息
        #ship_limit存储的是一开始拥有的飞船数量
        
        self.level=1
        self.score=0
        
        #每次开始时游戏重置得分
        self.score=0
