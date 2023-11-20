#game_functions.py
#存储让游戏运行的函数
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep #导入函数sleep()，暂停游戏


#响应按键函数
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right=True  #玩家按下右键时，将标志设为true
    elif event.key == pygame.K_LEFT:
        ship.moving_left=True   #玩家按下左键时，将标志设为true
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q: #玩家按下q键时,游戏结束
        sys.exit()

#响应松开函数
def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right=False   #松开重设为false
    elif event.key == pygame.K_LEFT:
        ship.moving_left=False

def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets): #玩家按右键时，飞船向右移动
    for event in pygame.event.get():
            #监视鼠标和键盘事件
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                check_keydown_events(event,ai_settings,screen,ship,bullets)
            elif event.type==pygame.KEYUP:
                check_keyup_events(event,ship)
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y=pygame.mouse.get_pos()
                check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)  
                
def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    #玩家单击play时开始新游戏
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        
        #重置游戏设置
        ai_settings.initialize_dynamic_settings()
        
        #隐藏光标
        pygame.mouse.set_visible(False)
        
        #重置游戏统计信息
        stats.reset_stats()
        stats.game_active=True
        
        #重置计分图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        
        #清空现有外星人和子弹列表
        aliens.empty()
        bullets.empty()
        
        #创建一群新外星人，让子弹居中
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
                    
def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    screen.fill(ai_settings.bg_color) #每次循环时都重新绘制屏幕
    #重新绘制所有子弹
    for bullet in bullets.sprites(): #遍历编组中的所有子弹，每个子弹都调用draw_bullet()
        bullet.draw_bullet()
    ship.blitme()  #每次循环时重新绘制飞船
    #先绘制飞船和子弹，在绘制外星人
    aliens.draw(screen) #在屏幕上绘制编组中的每个外星人
    sb.show_score()  #显示得分
    #如果游戏处于非活动状态，就绘制play按钮
    if not stats.game_active:
        play_button.draw_button()
    
    pygame.display.flip() #让绘制的屏幕可见
    
def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    
    bullets.update()
        #删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
            
    #检查是否有子弹击中
    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)
        
            

def fire_bullets(ai_settings,screen,ship,bullets):
    #发射子弹
    if len(bullets)< ai_settings.bullets_allowed:
            
        #创建一个子弹
        new_bullet=Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)  #像编组中添加新子弹，用法类似列表
        
#检查子弹和外星人的碰撞
def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
    collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        for aliens in collisions.values():
            stats.score+=ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)
    if len(aliens) ==0:
        #删除现有的子弹并创建一群新的外星人
        bullets.empty()
        ai_settings.increase_speed()
        
        #提高玩家等级
        stats.level+=1
        sb.prep_level
        create_fleet(ai_settings,screen,ship,aliens)
        
        
        
#创建外星人群
def create_fleet(ai_settings,screen,ship,aliens):
    alien=Alien(ai_settings,screen)
    number_aliens_x=get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows=get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    
    #创建外星人群
    for row_number in range(number_rows):
        #创建一行外星人
        for alien_number in range(number_aliens_x):
            #创建一个外星人并加入当前行
            create_alien(ai_settings,screen,aliens,alien_number,row_number)
    

def get_number_aliens_x(ai_settings,alien_width):
    #计算一行可用于放置外星人的宽度
    available_space_x=ai_settings.screen_width-2*alien_width
    #计算一行可用于放置外星人图片个数
    number_aliens_x=int(available_space_x/(2*alien_width))
    return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    alien=Alien(ai_settings,screen)
    alien_width=alien.rect.width
    alien.x=alien_width+2*alien_width*alien_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height+2*alien.rect.height * row_number
    aliens.add(alien)
    
#计算可用于放置多少行外星人
def get_number_rows(ai_settings,ship_height,alien_height):
    available_space_y=ai_settings.screen_height-(3*alien_height)-ship_height
    number_rows=int(available_space_y/ (2*alien_height))
    return number_rows

def update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets):
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    
    #检查外星人和飞船的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
    check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets)
    
def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break
    
def change_fleet_direction(ai_settings,aliens):
    #外星人下移并改变方向
    for alien in aliens.sprites():
        alien.rect.y+=ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    
def ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets):
    #响应被外星人撞到的飞船
    if stats.ship_left>0:
        stats.ship_left -=1
        #更新记分牌
        sb.prep_ships()
        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
    
        #创建一群新的外星人，并将飞船放到底部中央
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
    
        #暂停游戏
        sleep(0.5)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)
        
        
    
    
def check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets):
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
            break
        
def check_high_score(stats, sb):
    #检查是否诞生了新的最高得分
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()    