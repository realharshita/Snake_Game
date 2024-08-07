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
white = (255, 255, 255)
blue = (50, 153, 213)

snake_block = 10
initial_snake_speed = 15

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    window.blit(value, [0, 0])

def your_level(level):
    value = score_font.render("Level: " + str(level), True, black)
    window.blit(value, [width - 100, 0])

def our_snake(snake_block, snake_list, snake_color):
    for x in snake_list:
        pygame.draw.rect(window, snake_color, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [width / 6, height / 3])

def pause_game():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        window.fill(blue)
        message("Paused. Press P to resume or Q to quit.", red)
        pygame.display.update()
        clock.tick(5)

def create_obstacles(num_obstacles, snake_block):
    obstacles = []
    for _ in range(num_obstacles):
        obx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        oby = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
        obstacles.append([obx, oby])
    return obstacles

def draw_obstacles(obstacles, color):
    for ob in obstacles:
        pygame.draw.rect(window, color, [ob[0], ob[1], snake_block, snake_block])

def choose_snake_skin():
    snake_colors = [green, red, white, black]
    color_names = ["Green", "Red", "White", "Black"]
    index = 0
    choosing = True

    while choosing:
        window.fill(blue)
        message(f"Choose your snake color: {color_names[index]}. Press Enter to select.", white)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    index = (index + 1) % len(snake_colors)
                elif event.key == pygame.K_LEFT:
                    index = (index - 1) % len(snake_colors)
                elif event.key == pygame.K_RETURN:
                    choosing = False
    return snake_colors[index]

def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    score = 0
    level = 1
    snake_speed = initial_snake_speed
    level_target = 5

    obstacles = create_obstacles(level, snake_block)
    snake_color = choose_snake_skin()

    while not game_over:

        while game_close:
            window.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            your_score(score)
            your_level(level)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_p:
                    pause_game()

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        for ob in obstacles:
            if x1 == ob[0] and y1 == ob[1]:
                game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(blue)
        pygame.draw.rect(window, white, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list, snake_color)
        draw_obstacles(obstacles, black)
        your_score(score)
        your_level(level)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            score += 1
            if score % level_target == 0:
                level += 1
                snake_speed += 5
                obstacles = create_obstacles(level, snake_block)

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
