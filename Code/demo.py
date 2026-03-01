import pygame
import random
from pygame import mixer

#Coded by Ali Ahmad Khan


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
bullet_image = pygame.image.load('bullet.png')
bulletX = 0
bulletY = playerY_pos
bulletY_change = 10
bullet_state = "ready"  
enemy_image = pygame.image.load('alien.png')
enemies = []  
enemy_spawn_time = 1000  
last_enemy_spawn = pygame.time.get_ticks()

score = 0
font = pygame.font.Font(None, 40)

game_over_font = pygame.font.Font(None, 80)

def show_score():
    score_text = font.render("Score: " + str(score), True, (255,255,255))
    Display.blit(score_text, (10,10))

def game_over_text():
    over_text = game_over_font.render("GAME OVER", True, (255,0,0))
    Display.blit(over_text, (350,300))

def player(x,y):
    Display.blit(player_image, (x,y))

def enemy(x,y):
    Display.blit(enemy_image, (x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    Display.blit(bullet_image, (x+16,y+10))

def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = ((enemyX - bulletX)**2 + (enemyY - bulletY)**2)**0.5
    return distance < 27

run = True
while run:
    Display.fill((0,0,0))
    Display.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerX_pos_change = -5
    elif keys[pygame.K_RIGHT]:
        playerX_pos_change = 5
    else:
        playerX_pos_change = 0

    if keys[pygame.K_SPACE]:
        if bullet_state == "ready":
            bullet_sound = mixer.Sound("laser-312360.wav")
            bullet_sound.play()
            bulletX = playerX_pos
            fire_bullet(bulletX, bulletY)

    playerX_pos += playerX_pos_change
    playerX_pos = max(0, min(playerX_pos, 956))

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        if bulletY <= 0:
            bulletY = playerY_pos
            bullet_state = "ready"

    current_time = pygame.time.get_ticks()
    if current_time - last_enemy_spawn > enemy_spawn_time:
        enemyX_pos = random.randint(0, 956)
        enemyY_pos = random.randint(0, 120)
        enemyX_change = random.choice([6, -6])
        enemies.append({'x': enemyX_pos, 'y': enemyY_pos, 'x_change': enemyX_change, 'y_change': 40})
        last_enemy_spawn = current_time

    for enemy_obj in enemies[:]:
        enemy_obj['x'] += enemy_obj['x_change']
        if enemy_obj['x'] <= 0:
            enemy_obj['x_change'] = abs(enemy_obj['x_change'])
            enemy_obj['y'] += enemy_obj['y_change']
        elif enemy_obj['x'] >= 956:
            enemy_obj['x_change'] = -abs(enemy_obj['x_change'])
            enemy_obj['y'] += enemy_obj['y_change']

        if is_collision(enemy_obj['x'], enemy_obj['y'], bulletX, bulletY):
            col_sound = mixer.Sound("car-crash-sound-376882.wav")
            col_sound.play()
            bulletY = playerY_pos
            bullet_state = "ready"
            enemies.remove(enemy_obj)
            score += 1

        if enemy_obj['y'] > playerY_pos - 64:
            for e in enemies:
                e['y'] = 2000 
            game_over_text()
            pygame.display.update()
            pygame.time.delay(300)

            run = False

        enemy(enemy_obj['x'], enemy_obj['y'])

    player(playerX_pos, playerY_pos)
    show_score()
    pygame.display.update()

pygame.quit()