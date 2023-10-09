# 第2题：弹跳的球（Bouncing Balls）  
def bouncing_ball(h, bounce, window):  
    if(h<=0 or bounce<=0 or bounce>=1 or window>=h):
        return -1
    count=1
    m=h*bounce
    while m>window :
        m*=bounce
        count+=2
    return count
