import pygame, random
pygame.init()
white = (255,255,255)
class Ball():
    def __init__(self,x,y,w):
        self.x,self.y = x,y
        self.w = w
        self.velx = random.randint(8,12)*-1
        self.vely = random.randint(4,6)*-1
    def Generate(self,surf):
        pygame.draw.rect(surf,white,(self.x,self.y,self.w,self.w))
    def Out(self,p1_scr,bt_scr,width,height):
        if self.x + self.w >= width or self.x <= 0:
            if self.velx > 0:
                p1_scr += 1
                self.velx = random.randint(8,12)*-1
            else:
                bt_scr += 1
                self.velx = random.randint(8,12)
            self.x,self.y = width//2,height//2
            if random.randint(0,1):
                self.vely = random.randint(4, 6) * -1
            else:
                self.vely = random.randint(4, 6)
        return p1_scr, bt_scr
    def Bounce(self,surf,height,width,player,bot):
        if self.y <= 0 or self.y+self.w >= height:
            self.vely *= -1
        if self.y >= player.y and self.y <= player.y+player.h:
            if self.x >= player.x and self.x <= player.x+player.w:
                self.velx = random.randint(8,12)
                self.vely = random.randint(4,6)*(self.vely)/abs(self.vely)
        elif self.y+self.w >= player.y and self.y+self.w <= player.y+player.h:
            if self.x >= player.x and self.x <= player.x+player.w:
                self.velx = random.randint(8,12)
                self.vely = random.randint(4,6)*(self.vely)/abs(self.vely)
        if self.y >= bot.y and self.y <= bot.y+bot.h:
            if self.x+self.w >= bot.x:
                self.velx = random.randint(8, 12)*-1
                self.vely = random.randint(4, 6)*(self.vely)/abs(self.vely)
        self.x += self.velx
        self.y += self.vely
def Algorithm(ball, width, height):
    delta_x = ball.x
    initial_vely = ball.vely
    if initial_vely < 0:
        if (width-delta_x) < abs(ball.y*ball.velx/ball.vely):
            return ball.y - (width-delta_x)*abs(ball.vely/ball.velx)
        delta_x += abs(ball.y*ball.velx/ball.vely)
    else:
        if (width-delta_x) < abs((height-ball.y)*ball.velx/ball.vely):
            return ball.y + (width-delta_x)*abs(ball.vely/ball.velx)
        delta_x += abs((height-ball.y)*ball.velx/ball.vely)
    count = 1
    while width - delta_x >= height * abs(ball.velx / ball.vely):
        delta_x += height * abs(ball.velx / ball.vely)
        count += 1
    if initial_vely > 0:
        if count%2:
            return height - (width-delta_x)*abs(ball.vely/ball.velx)
        else:
            return (width-delta_x)*abs(ball.vely/ball.velx)
    else:
        if count%2:
            return (width-delta_x)*abs(ball.vely/ball.velx)
        else:
            return height - (width-delta_x)*abs(ball.vely/ball.velx)
class Bots():
    def __init__(self,x,y,w,h):
        self.x,self.y = x,y
        self.w,self.h = w,h
        self.update,self.ready = False,True
        self.target_y = 200
        self.vel = 5
    def Generate(self,surf):
        pygame.draw.rect(surf, white, (self.x,self.y,self.w,self.h))
    def Automate(self, ball,width,height):
        if ball.velx > 0 and self.ready:
            self.update = True
            self.ready = False
        elif ball.velx < 0:
            self.ready = True
        if self.update:
            self.target_y = Algorithm(ball,width,height)
            self.update = False
        if self.y + self.h*2//3 < self.target_y and self.y + self.h < height:
            self.y += self.vel
        elif self.y + self.h//3 > self.target_y and self.y > 0:
            self.y -= self.vel