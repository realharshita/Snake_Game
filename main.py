import pygame
import time

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width,height))
pygame.display.set_caption('Snake Game')

black = (0, 0, 0)
green = (0, 255, 0)

snake_block = 10
snake_speed = 15
snake_list = []
snake_length = 1

x1 = width //2
y1 = height // 2
x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

running = True
while running:
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

    x1 += x1_change
    y1 += y1_change
    window.fill(black)
    pygame.draw.rect(window, green, [x1, y1, snake_block, snake_block])
    pygame.display.update()
    clock.tick(snake_speed)

pygame.quit()
