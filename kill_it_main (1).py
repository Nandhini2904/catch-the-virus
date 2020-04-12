import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import time
import random
from pygame.locals import*


pygame.init()
pygame.font.init()


black = (0, 0, 0)
white = (255, 255, 255)
dark_blue = (0, 0, 200)
dark_red = (200, 0, 0)
dark_green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)


window_width=500
window_height=750
window=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("KILL IT")


syringe_img=pygame.image.load('syringe.png')
syringe_img=pygame.transform.scale(syringe_img,(100,100))
bg=pygame.image.load('background.jpeg')
bomb_img = pygame.image.load('bomb.png')


pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1)

clock=pygame.time.Clock()

class Syringe(object):
     def __init__(self,x,y):
        self.x=x
        self.y=y
        self.speed=10
        self.hitbox=(self.x,self.y+20,150,80)
     def draw(self,window):
        window.blit(syringe_img,(self.x,self.y))
        self.hitbox=(self.x,self.y+20,150,80)

class C_Virus(object):
     def __init__(self,x,y,c_type):
        self.x=x
        self.y=y
        self.c_type=c_type
        self.hitbox=(self.x,self.y,100,100)
     def draw(self,window):
        if self.c_type==0:
           c_virus=pygame.image.load('corona_virus.png')
           self.speed=10
        window.blit(c_virus,(self.x,self.y))
        self.hitbox=(self.x,self.y,100,100)

class H_Virus(object):
     def __init__(self,x,y,h_type):
        self.x=x
        self.y=y
        self.h_type=h_type
        self.hitbox=(self.x,self.y,100,100)
     def draw(self,window):
        if self.h_type==0:
             h_virus=pygame.image.load('hunta_virus.png')
             self.speed=10
        window.blit(h_virus,(self.x,self.y))
        self.hitbox=(self.x,self.y,100,100)

class Bombs(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10
        self.hitbox = (self.x, self.y, 100, 100)
    def draw(self, window):
        window.blit(bomb_img, (self.x, self.y))
        self.hitbox = (self.x, self.y, 100, 100)

def texts(text,font):
     textSurface=font.render(text,True,black)
     return textSurface,textSurface.get_rect()

def message(msg,x,y,size):
     regText = pygame.font.Font("C:/WINDOWS/Fonts/TAHOMABD.ttf",size)
     textSurf,textRect=texts(msg,regText)
     textRect.center=(x,y, 20)
     message("Hunta Virus: 2 point",250, 450, 20)
     button("Back", 100, 600, 75, 50, dark_blue, bright_blue, "back")
     pygame.display.update()
     clock.tick(15)

def game_intro():
     intro = True
     while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        window.blit(bg, (0,0))
        message("KILL IT",window_width/2,window_height/2, 50)
        button("Start", 100, 450, 75, 50, dark_green, bright_green, "play")
        button("Quit", 300, 450, 75, 50, dark_red, bright_red, "quit")
        button("Help", 200, 450, 75, 50, dark_blue, bright_blue, "instructions")
        pygame.display.update()
        clock.tick(15)

def main():
     score=0
     c_viruses=[]
     h_viruses=[]
     bombs=[]
     count_c_virus=0
     count_h_virus=0
     count_bombs=0
     c_virus_rate=30
     h_virus_rate=30
     bombs_rate=20
     syringe=Syringe(window_width*0.35, window_height-160)
     play=True
     while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and syringe.x > syringe.speed-5:
            syringe.x -= syringe.speed
        elif keys[pygame.K_RIGHT] and syringe.x < 500-100-syringe.speed:
            syringe.x += syringe.speed
        window.blit(bg,(0,0))
        count_c_virus+=1
        count_h_virus+=1
        count_bombs+=1
        if count_c_virus == c_virus_rate:
            count_c_virus=0
            c_startx = random.randrange(100, window_width - 100)
            c_starty = 0
            c_type = 0
            new_c_virus = C_Virus(c_startx, c_starty, c_type)
            c_viruses.append(new_c_virus)
        if count_h_virus == h_virus_rate:
            count_h_virus = 0
            h_startx = random.randrange(100, window_width - 100)
            h_starty = 0
            h_type = 0
            new_h_virus = H_Virus(h_startx, h_starty, h_type)
            h_viruses.append(new_h_virus)
        if count_bombs== bombs_rate:
            count_bombs = 0
            b_startx = random.randrange(100, window_width - 100)
            b_starty = 0
            new_bomb = Bombs(b_startx, b_starty)
            bombs.append(new_bomb)
        for item in c_viruses:
            item.draw(window)
            item.y += item.speed
        for item in c_viruses[:]:
            if (item.hitbox[0] >= syringe.hitbox[0] - 20) and (item.hitbox[0] <= syringe.hitbox[0] + 70):
                 if syringe.hitbox[1] - 120<=item.hitbox[1] <= syringe.hitbox[1] - 40:
                   c_viruses.remove(item)
                   score += 1
                   if item.c_type==0:
                       score+=0
                   print("Score:",score)

        for item in h_viruses:
            item.draw(window)
            item.y += item.speed
        for item in h_viruses[:]:
            if (item.hitbox[0] >= syringe.hitbox[0] - 20) and (item.hitbox[0] <= syringe.hitbox[0] + 70):
                if syringe.hitbox[1] - 120<=item.hitbox[1] <= syringe.hitbox[1] - 40:
                    h_viruses.remove(item)
                    score += 2
                    if item.h_type==0:
                        score += 0
                    print("Score:",score)
        for item in bombs:
            item.draw(window)
            item.y += item.speed
        for item in bombs[:]:
            if (item.hitbox[0] >= syringe.hitbox[0]) and (item.hitbox[0] <= syringe.hitbox[0] + 50):
                if syringe.hitbox[1] - 120 <= item.hitbox[1] <= syringe.hitbox[1] - 40:
                    play = False

        message("Score:" + str(score), 50, 30, 30)
        syringe.draw(window)
        pygame.display.update()
        clock.tick(60)
     pygame.quit()
     
game_intro()
main()
