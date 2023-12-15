# Python script for a simple version of the Snake game using pygame

import pygame
import random
import time

# Initialize pygame
pygame.init()

# Set up display
width, height = 640, 480
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Colors
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Snake properties
snake_block = 10
snake_speed = 15
snake_list = []

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])

# Main function
def snake_game():
    game_over = False
    game_close = False

    # Starting position
    x1 = width / 2
    y1 = height / 2

    # Snake movement
    x1_change = 0
    y1_change = 0

    # Snake initial length
    snake_length = 1

    # Food location
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # Game loop
    while not game_over:

        while game_close:
            display.fill(blue)
            font_style = pygame.font.SysFont(None, 50)
            message = font_style.render('You Lost! Press Q-Quit or C-Play Again', True, red)
            display.blit(message, [width / 6, height / 3])

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        snake_game()

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

        # Check if snake is out of bounds
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # Move snake
        x1 += x1_change
        y1 += y1_change
        display.fill(blue)

        # Draw food
        pygame.draw.rect(display, red, [foodx, foody, snake_block, snake_block])

        # Snake head
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for collision with self
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Draw snake
        draw_snake(snake_block, snake_list)

        pygame.display.update()

        # Eating food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            snake_length += 1

        time.sleep(0.1 / snake_speed)

    pygame.quit()
    quit()

# Run the game
snake_game()
