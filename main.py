import pygame
import time
import random

# Variables

snake_speed = 15
snake_pos = [100, 50]
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]]
snake_direction = "RIGHT"
snake_turning_direction = snake_direction

window_width = 720
window_height = 480

fruit_pos = [random.randrange(1, (window_width // 10)) * 10,
             random.randrange(1, (window_height // 10)) * 10]
is_fruit_spawned = True

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)

score = 0

# Initialize Game

pygame.init()
pygame.display.set_caption("Snake...?")
game_window = pygame.display.set_mode((window_width, window_height))
fps = pygame.time.Clock()

# Game Score

def display_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render("Score : " + str(score), True, color)
    score_box = score_surface.get_rect()
    
    game_window.blit(score_surface, score_box)

# Game Over

def game_over():
    game_font = pygame.font.SysFont("Times New Roman", 50)
    game_over_surface = game_font.render("Your final score is : " + str(score), True, RED)
    game_over_box = game_over_surface.get_rect()
    game_over_box.midtop = (window_width / 2, window_height / 4)

    game_window.blit(game_over_surface, game_over_box)
    pygame.display.flip()

    time.sleep(2)
    pygame.quit()
    quit()

# Snake Movement

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_turning_direction = "UP"
            if event.key == pygame.K_DOWN:
                snake_turning_direction = "DOWN"
            if event.key == pygame.K_LEFT:
                snake_turning_direction = "LEFT"
            if event.key == pygame.K_RIGHT:
                snake_turning_direction = "RIGHT"

    if snake_turning_direction == "UP" and snake_direction != "DOWN":
        snake_direction = "UP"
    if snake_turning_direction == "DOWN" and snake_direction != "UP":
        snake_direction = "DOWN"
    if snake_turning_direction == "LEFT" and snake_direction != "RIGHT":
        snake_direction = "LEFT"
    if snake_turning_direction == "RIGHT" and snake_direction != "LEFT":
        snake_direction = "RIGHT"

    if snake_direction == "UP":
        snake_pos[1] -= 10
    if snake_direction == "DOWN":
        snake_pos[1] += 10
    if snake_direction == "LEFT":
        snake_pos[0] -= 10
    if snake_direction == "RIGHT":
        snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))

    # Snake Body Growth
    
    if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
        score += 10
        is_fruit_spawned = False
    else:
        snake_body.pop()

    # Fruit Respawn

    if not is_fruit_spawned:
        fruit_pos = [random.randrange(1, (window_width // 10)) * 10,
                    random.randrange(1, (window_height // 10)) * 10]
        
    is_fruit_spawned = True
    game_window.fill(BLACK)

    for snake_body_pos in snake_body:
        pygame.draw.rect(game_window, GREEN, pygame.Rect(snake_body_pos[0], snake_body_pos[1], 10, 10))
    pygame.draw.rect(game_window, WHITE, pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10))

    # Game Over Conditions

    if snake_pos[0] < 0 or snake_pos[0] > window_width - 10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > window_height - 10:
        game_over()
    for snake_body_block in snake_body[1:]:
        if snake_pos[0] == snake_body_block[0] and snake_pos[1] == snake_body_block[1]:
            game_over()

    display_score(1, WHITE, "Times New Roman", 20)
    pygame.display.update()
    fps.tick(snake_speed)