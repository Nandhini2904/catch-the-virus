# catch the virus
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
