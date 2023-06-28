import random
import time
import pygame

pygame.init()

# Defining colors
black = (0, 0, 0)
red = (204, 0, 0)
green = (0, 102, 0)
blue = (0, 0, 153)
yellow = (255, 204, 0)

# Width and height of the screen
width, height = 1000, 500

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("SNAKE GAME")

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15

# Setting fonts
score_font = pygame.font.SysFont('Arial', 30)
game_over_font = pygame.font.SysFont('Arial', 60)
button_font = pygame.font.SysFont('Arial', 25)
credit_font = pygame.font.SysFont('Arial', 20)

# Function to print score
def print_score(score):
    text = score_font.render("Score: " + str(score), True, yellow)
    game_display.blit(text, [20, 20])

# Function to draw snake
def draw_snake(snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, green, [pixel[0], pixel[1], snake_size, snake_size])

# Function to display game over message and buttons
def game_over_screen(score):
    game_display.fill(black)
    game_over_message = game_over_font.render("GAME OVER!", True, red)
    final_score = score_font.render("Final Score: " + str(score), True, yellow)
    quit_message = button_font.render("To quit, press Q", True, yellow)
    play_again_message = button_font.render("To play again, press R", True, yellow)
    credit_message = credit_font.render("by @sarthakkulkarni__", True, yellow)

    game_display.blit(game_over_message, (width / 2 - 160, height / 2 - 80))
    game_display.blit(final_score, (width / 2 - 100, height / 2 - 10))
    game_display.blit(quit_message, (width / 2 - 90, height / 2 + 30))
    game_display.blit(play_again_message, (width / 2 - 125, height / 2 + 70))
    game_display.blit(credit_message, (width / 2 - 90, height - 30))

    pygame.display.update()

# Function to run the game
def run_game():
    game_over = False
    x, y = width / 2, height / 2
    x_speed, y_speed = 0, 0
    snake_pixels = []
    snake_length = 1
    target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size

        if x >= width or x < 0 or y >= height or y < 0:
            game_over = True

        x += x_speed
        y += y_speed

        game_display.fill(black)
        pygame.draw.rect(game_display, yellow, [target_x, target_y, snake_size, snake_size])

        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == [x, y]:
                game_over = True

        draw_snake(snake_pixels)
        print_score(snake_length - 1)

        pygame.display.update()

        if x == target_x and y == target_y:
            target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    game_over_screen(snake_length - 1)
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = False
                    pygame.quit()
                    quit()
                if event.key == pygame.K_r:
                    run_game()

run_game()
