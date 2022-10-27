import random

class Person():

    def __init__(self, canvas, x, y, size, color='black'):
        self.canvas = canvas
        
        self.x = x 
        self.y = y
        
        self.start_x = x
        self.start_y = y
        
        self.size = size
        self.color = color
        
        rect = [self.x, self.y, self.x+self.size, self.y+self.size]
        self.circle = canvas.create_oval(rect, outline=color, fill=color)
        
    def move(self):
        x_vel = random.randint(-5, 5)
        y_vel = random.randint(-5, 5)
    
        self.canvas.move(self.circle, x_vel, y_vel)
        coordinates = self.canvas.coords(self.circle)
    
        self.x = coordinates[0]
        self.y = coordinates[1]

        # if outside screen move to start position
        if self.y < -self.size:
            self.x = self.start_x
            self.y = self.start_y
            self.canvas.coords(self.circle, self.x, self.y, self.x + self.size, self.y + self.size)