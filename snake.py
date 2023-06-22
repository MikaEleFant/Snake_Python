class Snake:
    def __init__(self):
        self.speed = 15
        self.pos = [100, 50]
        self.body = [[100, 50],
                    [90, 50],
                    [80, 50],
                    [70, 50]]
        self.direction = "RIGHT"
        self.turn_direction = self.direction

    def turn(self, direction):
        self.turn_direction = direction

        if self.turn_direction == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        if self.turn_direction == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
        if self.turn_direction == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        if self.turn_direction == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"


    def move(self):
        if self.direction == "UP":
            self.pos[1] -= 10
        if self.direction == "DOWN":
            self.pos[1] += 10
        if self.direction == "LEFT":
            self.pos[0] -= 10
        if self.direction == "RIGHT":
            self.pos[0] += 10

        self.body.insert(0, list(self.pos))
        self.body.pop()

    def grow(self):
        diff_in_x = self.body[-1][0] - self.body[-2][0]
        x = self.body[-1][0] + diff_in_x

        diff_in_y = self.body[-1][1] - self.body[-2][1]
        y = self.body[-1][1] + diff_in_y
        self.body.append([x, y])