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

    def move(self, direction):
        self.turn = direction

        if self.turn == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        if self.turn == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
        if self.turn == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        if self.turn == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"

        if self.direction == "UP":
            self.pos[0] -= 10
        if self.direction == "DOWN":
            self.pos[0] += 10
        if self.direction == "LEFT":
            self.pos[1] -= 10
        if self.direction == "RIGHT":
            self.pos[1] += 10

        self.body.insert(0, list(self.pos))
        self.body.pop()

    def grow(self):
        self.body.insert(0, list(self.pos))