import pygame
import time

from snake import Snake
from fruit import Fruit

class Game:
    def __init__(self, window_width, window_height, colors):
        self.window_width = window_width
        self.window_height = window_height
        self.colors = colors
        self.score = 0

        self.game_window = pygame.display.set_mode((self.window_width, self.window_height))
        self.fps = pygame.time.Clock()

        self.snake = Snake()
        self.fruit = Fruit(window_width, window_height)

    def start(self):
        pygame.init()
        pygame.display.set_caption("Snake...?")

        self.run()

    def is_game_over(self):
        if self.snake.pos[0] < 0 or self.snake.pos[0] > self.window_width - 10:
            return True
        if self.snake.pos[1] < 0 or self.snake.pos[1] > self.window_height - 10:
            return True
        for snake_body_block in self.snake.body[1:]:
            if self.snake.pos[0] == snake_body_block[0] and self.snake.pos[1] == snake_body_block[1]:
                return True
        
        return False

    def display_score(self, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render("Score : " + str(self.score), True, color)
        score_box = score_surface.get_rect()
        
        self.game_window.blit(score_surface, score_box)

    def game_over(self):
        game_font = pygame.font.SysFont("Times New Roman", 50)
        game_over_surface = game_font.render("Your final score is : " + str(self.score), True, self.colors["RED"])
        game_over_box = game_over_surface.get_rect()
        game_over_box.midtop = (self.window_width / 2, self.window_height / 4)

        self.game_window.blit(game_over_surface, game_over_box)
        pygame.display.flip()

        time.sleep(2)
        pygame.quit()
        quit()

    def run(self):
        game_is_over = self.is_game_over()

        while not game_is_over:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.turn("UP")
                    elif event.key == pygame.K_DOWN:
                        self.snake.turn("DOWN")
                    elif event.key == pygame.K_LEFT:
                        self.snake.turn("LEFT")
                    elif event.key == pygame.K_RIGHT:
                        self.snake.turn("RIGHT")

            self.snake.move()
            
            if self.snake.pos[0] == self.fruit.pos[0] and self.snake.pos[1] == self.fruit.pos[1]:
                self.score += 10
                self.fruit = Fruit(self.window_width, self.window_height)
                self.snake.grow()
                
            self.game_window.fill(self.colors["BLACK"])

            for snake_body_pos in self.snake.body:
                pygame.draw.rect(self.game_window, self.colors["GREEN"], pygame.Rect(snake_body_pos[0] + 0.5, snake_body_pos[1] + 0.5, 9, 9))
            pygame.draw.rect(self.game_window, self.colors["WHITE"], pygame.Rect(self.fruit.pos[0] + 0.5, self.fruit.pos[1] + 0.5, 9, 9))

            game_is_over = self.is_game_over()

            self.display_score(self.colors["WHITE"], "Times New Roman", 20)
            pygame.display.update()
            self.fps.tick(self.snake.speed)

        self.game_over()