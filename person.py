import random

class Person():

    def __init__(self, canvas, size, color='black'):
        self.canvas = canvas
        self.rand = random.Random()

        self.x = self.rand.randint(size, 750) 
        self.y = self.rand.randint(size, 600)
        
        self.size = size
        self.color = color

        self.move_x = self.rand.randint(-5, 6)
        self.move_y = self.rand.randint(-5, 6)
        
        rect = [self.x-self.size, self.y-self.size, self.x+self.size, self.y+self.size]
        self.circle = canvas.create_oval(rect, outline=color, fill=color)

    def move(self):
        self.canvas.move(self.circle, self.move_x, self.move_y)
    
        self.x = self.x + self.move_x
        self.y = self.y + self.move_y

        # if outside screen give a new direction
        if self.y < self.size:
            self.move_y = 5
            self.move_x = self.rand.randint(-5, 6)
            # self.canvas.coords(self.circle, self.x, self.y, self.x + self.size, self.y + self.size)    
            # self.x = self.x + self.size
            # self.y = self.y + self.size
        if self.x < self.size:
            self.move_x = 5
            self.move_y = self.rand.randint(-5, 6)
            # self.canvas.coords(self.circle, self.x, self.y, self.x + self.size, self.y + self.size)
            # self.x = self.x + self.size
            # self.y = self.y + self.size
        if self.x >= -self.size + self.canvas.winfo_width():
            self.move_x = -5
            self.move_y = self.rand.randint(-5, 6)
            # self.canvas.coords(self.circle, self.x, self.y, self.x + self.size, self.y + self.size)
            # self.x = self.x + self.size
            # self.y = self.y + self.size
        if self.y >= self.canvas.winfo_height() - self.size:
            self.move_y = -5
            self.move_x = self.rand.randint(-5, 6)
            # self.canvas.coords(self.circle, self.x, self.y, self.x + self.size, self.y + self.size)
            # self.x = self.x + self.size
            # self.y = self.y + self.size
