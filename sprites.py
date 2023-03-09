# File created by: Liam Newberry

import pygame as pg
from pygame.sprite import Sprite
from settings import *
from random import choice
from random import randint
from time import sleep

vec = pg.math.Vector2

# create a player

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.confric = 0.1
        self.canjump = False
    def input(self):
        keystate = pg.key.get_pressed()
        
        if keystate[pg.K_w] and PUP == True:
            self.acc.y = -PLAYER_ACC
        if keystate[pg.K_a] and PLEFT == True:
            self.acc.x = -PLAYER_ACC
        if keystate[pg.K_s] and PDOWN == True:
            self.acc.y = PLAYER_ACC
        if keystate[pg.K_d] and PRIGHT == True:
            self.acc.x = PLAYER_ACC
    def update(self):
        self.acc = self.vel * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos
        if self.rect.x > WIDTH:
            print("I'm off the right screen...")
            # self.pos = vec(WIDTH/2, HEIGHT/2)
            PRIGHT = False
        if self.rect.x < 0:
            print("I'm off the left screen...")
            # self.pos = vec(WIDTH/2, HEIGHT/2)
            PLEFT = False
        if self.rect.y < 0:
            print("I'm off the top screen...")
            # self.pos = vec(WIDTH/2, HEIGHT/2)
            PUP = False
        if self.rect.y > HEIGHT:
            print("I'm off the bottom screen...")
            # self.pos = vec(WIDTH/2, HEIGHT/2)
            PDOWN = False
        
class Mob(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.cofric = 0.1
        self.canjump = False
    def behavior(self):
        direction = None
        directions = ['u','l','d','r']
        if randint(1,2) == 1:
            direction = choice(directions)
        keystate = pg.key.get_pressed()
        if direction == 'u':
            self.acc.y = -MOB_ACC
        if direction == 'l':
            self.acc.x = -MOB_ACC
        if direction == 'd':
            self.acc.y = MOB_ACC
        if direction == 'r':
            self.acc.x = MOB_ACC
    def update(self):
        self.acc = self.vel * PLAYER_FRICTION
        self.behavior()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos
        if self.rect.x > WIDTH:
            print("I'm off the right screen...")
            self.pos = vec(WIDTH/2, HEIGHT/2)
            PRIGHT = False
        if self.rect.x < 0:
            print("I'm off the left screen...")
            self.pos = vec(WIDTH/2, HEIGHT/2)
            PLEFT = False
        if self.rect.y < 0:
            print("I'm off the top screen...")
            self.pos = vec(WIDTH/2, HEIGHT/2)
            PUP = False
        if self.rect.y > HEIGHT:
            print("I'm off the bottom screen...")
            self.pos = vec(WIDTH/2, HEIGHT/2)
            PDOWN = False