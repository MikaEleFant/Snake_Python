import pygame
import time

from snake import Snake
from fruit import Fruit

# Variables

window_width = 720
window_height = 480

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

snake = Snake()
fruit = Fruit(window_width, window_height)

# Game Score

def display_score(color, font, size):
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
    snake.move()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.turn("UP")
            elif event.key == pygame.K_DOWN:
                snake.turn("DOWN")
            elif event.key == pygame.K_LEFT:
                snake.turn("LEFT")
            elif event.key == pygame.K_RIGHT:
                snake.turn("RIGHT")

    # Snake Body Growth
    
    if snake.pos[0] == fruit.pos[0] and snake.pos[1] == fruit.pos[1]:
        score += 10
        fruit = Fruit(window_width, window_height)
        snake.grow()
        
    game_window.fill(BLACK)

    for snake_body_pos in snake.body:
        pygame.draw.rect(game_window, GREEN, pygame.Rect(snake_body_pos[0] + 0.5, snake_body_pos[1] + 0.5, 9, 9))
    pygame.draw.rect(game_window, WHITE, pygame.Rect(fruit.pos[0] + 0.5, fruit.pos[1] + 0.5, 9, 9))

    # Game Over Conditions

    if snake.pos[0] < 0 or snake.pos[0] > window_width - 10:
        game_over()
    if snake.pos[1] < 0 or snake.pos[1] > window_height - 10:
        game_over()
    for snake_body_block in snake.body[1:]:
        if snake.pos[0] == snake_body_block[0] and snake.pos[1] == snake_body_block[1]:
            game_over()

    display_score(WHITE, "Times New Roman", 20)
    pygame.display.update()
    fps.tick(snake.speed)