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

        self.game_window.fill(self.colors["BLACK"])

        self.display(self.colors["WHITE"], "Times New Roman", 25, "Snake...?", 314.5, 100)
        self.display(self.colors["WHITE"], "Times New Roman", 25, "Start", 336.5, 200)
        self.display(self.colors["WHITE"], "Times New Roman", 25, "Quit", 337.5, 250)
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 336.5 <= mouse_pos[0] <= 383.5 and 200 <= mouse_pos[1] <= 228:
                        self.run()
                    if 337.5 <= mouse_pos[0] <= 382.5 and 250 <= mouse_pos[1] <= 278:
                        pygame.quit()
                        quit()

            mouse_pos = pygame.mouse.get_pos()

    def is_game_over(self):
        if self.snake.pos[0] < 0 or self.snake.pos[0] > self.window_width - 10:
            return True
        if self.snake.pos[1] < 0 or self.snake.pos[1] > self.window_height - 10:
            return True
        for snake_body_block in self.snake.body[1:]:
            if self.snake.pos[0] == snake_body_block[0] and self.snake.pos[1] == snake_body_block[1]:
                return True
        
        return False

    def display(self, color, font, size, text, x=0, y=0):
        text_font = pygame.font.SysFont(font, size)
        text_surface = text_font.render(text, True, color)
        text_box = text_surface.get_rect(topleft = (x, y))
        
        self.game_window.blit(text_surface, text_box)

    def game_over(self):
        self.display(self.colors["RED"], "Times New Roman", 50, "Your final score is : " + str(self.score), 144.5, 100)

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

            self.display(self.colors["WHITE"], "Times New Roman", 20, "Score : " + str(self.score))
            pygame.display.update()
            self.fps.tick(self.snake.speed)

        self.game_over()