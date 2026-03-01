import pygame
import random
import time
from pygame import mixer
pygame.init()
Display = pygame.display.set_mode((1020,680))
pygame.display.set_caption("Attack on Alien")
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)
background = pygame.image.load('background.png')
mixer.music.load("background-loop-71744.wav")
mixer.music.play(-1)

player_image = pygame.image.load('spaceship.png')
playerX_pos = 478
playerY_pos = 536
playerX_pos_change = 0

enemy_image = pygame.image.load('alien.png')
enemyX_pos = random.randint(0,956)
enemyY_pos = random.randint(0,120)
enemyX_pos_change = 4
enemyYpos_change = 40

def player(playerX_pos,playerY_pos):
    Display.blit(player_image,(playerX_pos,playerY_pos))

def enemy(enemyX_pos,enemyY_pos):
    Display.blit(enemy_image,(enemyX_pos,enemyY_pos))


run = True
while run:
    Display.fill((0,0,0))
    Display.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerX_pos_change = -2
        else:
            playerX_pos_change = 0
        if keys[pygame.K_RIGHT]:
            playerX_pos_change = 2

    playerX_pos += playerX_pos_change
    if playerX_pos <= 0:
        playerX_pos = 0
    elif playerX_pos >= 956:
        playerX_pos = 956

    enemyX_pos += enemyX_pos_change
    if enemyX_pos <= 0:
        enemyX_pos_change = 4
        enemyY_pos += enemyYpos_change
    elif enemyX_pos >= 956:
        enemyX_pos_change = -4
        enemyY_pos += enemyYpos_change

    enemy(enemyX_pos,enemyY_pos)
    player(playerX_pos,playerY_pos)
    pygame.display.update()
pygame.quit()