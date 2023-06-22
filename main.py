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

window_width = 720
window_height = 480

fruit_pos = [random.randrange(1, (window_width // 10)) * 10,
             random.randrange(1, (window_height // 10)) * 10]

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

