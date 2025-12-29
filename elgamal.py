import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '100,100'
import random
import pgzrun
import pygame
import socket

pygame.mixer.music.load("song.ogg") #MintoDog
pygame.mixer.music.play(-1)

level=-1
message=""

def draw():
    global level, url,message
    screen.clear()
    if level == -1:
        screen.blit("title", (0, 0))
    elif level == 0:
        screen.blit("intro", (0, 0))
    elif level == 1:
        screen.blit("page1",(0,0))
    elif level == 2:
        screen.blit("page2",(0,0))
    elif level == 3:
        screen.blit("page3",(0,0))
    elif level == 4:
        screen.blit("page4",(0,0))
   
def on_key_down(key, unicode=None):
    global level, url
    if key==keys.ESCAPE:
        pygame.quit()
    elif key == keys.SPACE and level >0 :
        level +=1

def update():
    global level,checker,gemacht,url
    if (level == 0 or level==-2) and keyboard.RETURN:
        level +=1
    elif level == -1 and keyboard.space:
        level = 0
    if level==5 and keyboard.space:
        level=0

pgzrun.go()
