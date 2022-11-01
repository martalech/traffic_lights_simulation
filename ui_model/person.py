import random

class Person():

    def __init__(self, size, color='black'):
        self.rand = random.Random()

        self.x = self.rand.randint(size, 750) 
        self.y = self.rand.randint(size, 600)
        
        self.size = size
        self.color = color

        self.move_x = self.rand.randint(-5, 6)
        self.move_y = self.rand.randint(-5, 6)
        self.circle = None

    def move(self, canvas_width, canvas_heigh):
        self.x = self.x + self.move_x
        self.y = self.y + self.move_y

        # if outside screen give a new direction
        if self.y < self.size:
            self.move_y = 5
            self.move_x = self.rand.randint(-5, 6)
        if self.x < self.size:
            self.move_x = 5
            self.move_y = self.rand.randint(-5, 6)
        if self.x >= -self.size + canvas_width:
            self.move_x = -5
            self.move_y = self.rand.randint(-5, 6)
        if self.y >= canvas_heigh - self.size:
            self.move_y = -5
            self.move_x = self.rand.randint(-5, 6)
