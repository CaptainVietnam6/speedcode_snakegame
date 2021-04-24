'''
Copyright (©) 2021 Kiet Pham <kiet.riley2005@gmail.com>
This software/program has a copyright license, more information is in the 'LICENSE' file
IF YOU WANT TO USE/COPY/MODIFY/REPRODUCE/RE-DISTRIBUTE THIS PROGRAM, YOU MUST INCLUDE A COPY OF THE LICENSE

Author Name: Kiet Pham
Author Contact: kiet.riley2005@gmail.com
Discord: CaptainVietnam6#7932
Discord Server: https://discord.gg/3z76p8H5yj
GitHub: https://github.com/CaptainVietnam6
Instagram: @itz_kietttttttttt
Program Status: FINALISED, ABANDONED, OUTDATED
'''

import pygame
import time
import random

pygame.init()

screen_size_x = 800
screen_size_y = 450

half_screen_size_x = 400
half_screen_size_y = 225

clock = pygame.time.Clock()

dis = pygame.display.set_mode((screen_size_x, screen_size_y))
pygame.display.update()
pygame.display.set_caption("Snake game by Kiet")

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 165, 0)

snake_size = 25
snake_speed = 10

font_style = pygame.font.SysFont(None, 25)
score_font = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [225, 200])

def total_score(score):
    value = score_font.render("Score: " + str(score), True, green)
    dis.blit(value, [10, 10])

def snake_body(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, blue, [x[0], x[1], snake_size, snake_size])

def game_Loop():
    game_over = False
    close_game = False

    x1 = 450
    y1 = 225

    x1_movement_change = 0
    y1_movement_change = 0

    snake_list = []
    snake_length = 1

    spawn_food_x = round(random.randrange(0, screen_size_x - snake_size) / snake_size) * snake_size
    spawn_food_y = round(random.randrange(0, screen_size_y - snake_size) / snake_size) * snake_size

    while game_over != True:
        
        while close_game == True:
            dis.fill(orange)
            message("Your died! Press Q to quit or R to restart", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        print("quitting game")
                        game_over = True
                        close_game = False
                    if event.key == pygame.K_r:
                        print("restarting game")
                        game_Loop()
            if game_over:
                break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x1_movement_change = snake_size
                    y1_movement_change = 0
                elif event.key == pygame.K_LEFT:
                    x1_movement_change = -snake_size
                    y1_movement_change = 0
                elif event.key == pygame.K_UP:
                    x1_movement_change = 0
                    y1_movement_change = -snake_size
                elif event.key == pygame.K_DOWN:
                    x1_movement_change = 0
                    y1_movement_change = snake_size
                
                elif event.key == pygame.K_d:
                    x1_movement_change = snake_size
                    y1_movement_change = 0
                elif event.key == pygame.K_a:
                    x1_movement_change = -snake_size
                    y1_movement_change = 0
                elif event.key == pygame.K_w:
                    x1_movement_change = 0
                    y1_movement_change = -snake_size
                elif event.key -- pygame.K_s:
                    x1_movement_change = 0
                    y1_movement_change = snake_size
        
        if x1 >= screen_size_x or x1 <= 0 or y1 >= screen_size_y or y1 <= 0:
            close_game = True

        x1 += x1_movement_change
        y1 += y1_movement_change

        dis.fill(orange)
        pygame.draw.rect(dis, black, [spawn_food_x, spawn_food_y, snake_size, snake_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        
        for x in snake_list[:-1]:
            if x == snake_head:
                close_game = True

        snake_body(snake_size, snake_list)
        total_score(snake_length -1)
        pygame.display.update()

        if x1 == spawn_food_x and y1 == spawn_food_y:
            print("ate food")
            spawn_food_x = round(random.randrange(0, screen_size_x - snake_size) / snake_size) * snake_size
            spawn_food_y = round(random.randrange(0, screen_size_y - snake_size) / snake_size) * snake_size
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_Loop()
