class Snake:
    def __init__(self, x, y, headTex, bodyTex):
        self.position = [x, y]
        self.body = [
            [x, y],
            [x + 1, y],
            [x + 2, y],
            [x + 3, y]
        ]
        self.headTex = headTex
        self.bodyTex = bodyTex
        self.direction = 'LEFT'
        self.dx = -1
        self.dy = 0

    def move(self):
        i = len(self.body) - 1
        while i >= 1:
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]
            i -= 1
        self.position[0] += self.dx
        self.position[1] += self.dy
        self.body[0][0] = self.position[0]
        self.body[0][1] = self.position[1]