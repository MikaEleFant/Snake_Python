import random

class Fruit:
    def __init__(self, window_width, window_height):
        self.pos = [random.randrange(1, (window_width // 10)) * 10,
                    random.randrange(1, (window_height // 10)) * 10]