class Snake:
    def __init__(self):
        self.speed = 15
        self.pos = [100, 50]
        self.body = [[100, 50],
                    [90, 50],
                    [80, 50],
                    [70, 50]]
        self.direction = "RIGHT"
        self.turn = self.direction