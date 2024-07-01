import pygame
import time
import random

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

snake_block = 10
snake_speed = 15

x1 = width // 2
y1 = height // 2
x1_change = 0
y1_change = 0

snake_list = []
snake_length = 1

clock = pygame.time.Clock()

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    font_style = pygame.font.SysFont(None, 50)
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [width // 6, height // 3])

foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

running = True
game_close = False

while running:
    while game_close:
        window.fill(black)
        message("You Lost! Press Q-Quit or C-Play Again", red)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                    game_close = False
                if event.key == pygame.K_c:
                    x1 = width // 2
                    y1 = height // 2
                    x1_change = 0
                    y1_change = 0
                    snake_list = []
                    snake_length = 1
                    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
                    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
                    game_close = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -snake_block
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = snake_block

    if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
        game_close = True

    x1 += x1_change
    y1 += y1_change
    window.fill(black)
    pygame.draw.rect(window, red, [foodx, foody, snake_block, snake_block])
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    for x in snake_list[:-1]:
        if x == snake_head:
            game_close = True

    our_snake(snake_block, snake_list)
    pygame.display.update()

    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
        snake_length += 1

    clock.tick(snake_speed)

pygame.quit()
