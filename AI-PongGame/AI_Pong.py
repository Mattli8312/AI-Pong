import pygame
from AI_PongGame import Pong_Bot
pygame.init()
white = (255,255,255)
class Fonts():
    def __init__(self,x,y,size,name,txt):
        self.x,self.y = x,y
        self.f = pygame.font.SysFont(name,size,True)
        self.txt = self.f.render(txt, False, white)
    def Write(self,surf):
        surf.blit(self.txt, (self.x,self.y))
class Paddle():
    def __init__(self,x,y,w,h):
        self.x,self.y = x,y
        self.w,self.h = w,h
        self.vel = 8
    def Generate(self,surf):
        pygame.draw.rect(surf, white, (self.x,self.y,self.w,self.h))
    def Manual(self, height):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.y > 0: self.y -= self.vel
        elif keys[pygame.K_DOWN] and self.y + self.h < height: self.y += self.vel
def DrawGrid(surf,height,width,Player1_scr,Bot_scr):
    # Scoreboard for player and bot respectively
    Score_1 = Fonts(width//2-80,10,100,"Ariel",str(Player1_scr))
    Score_2 = Fonts(width//2+30,10,100,"Ariel",str(Bot_scr))
    # Generate the division line
    for i in range(height//20):
        pygame.draw.rect(surf, white, (width//2-5, i*20, 5, 15))
    Score_1.Write(surf)
    Score_2.Write(surf)
def main():
    width, height = 600,400
    pygame.display.set_caption("AI_Pong")
    p1_scr = bt_scr = 0
    #Players
    p1_paddle = Paddle(10,height//2-30,15,60)
    ball = Pong_Bot.Ball(width//2,height//2,15)
    bot_paddle = Pong_Bot.Bots(width-25,height//2-30,15,60)
    #UI
    win = pygame.display.set_mode((width,height))
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(30)
        win.fill((0,0,0))
        DrawGrid(win, height, width, p1_scr, bt_scr)
        p1_paddle.Generate(win)
        p1_paddle.Manual(height)
        ball.Generate(win)
        ball.Bounce(win,height,width,p1_paddle,bot_paddle)
        bot_paddle.Generate(win)
        bot_paddle.Automate(ball,width,height)
        p1_scr, bt_scr = ball.Out(p1_scr, bt_scr, width,height)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()
main()