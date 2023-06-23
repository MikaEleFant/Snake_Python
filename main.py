import pygame

from game import Game

window_width = 720
window_height = 480
colors = {
    "BLACK": pygame.Color(0, 0, 0),
    "WHITE": pygame.Color(255, 255, 255),
    "RED": pygame.Color(255, 0, 0),
    "GREEN": pygame.Color(0, 255, 0),
    "BLUE": pygame.Color(0, 0, 255)
}

# Initialize Game

game = Game(window_width, window_height, colors)

game.start()