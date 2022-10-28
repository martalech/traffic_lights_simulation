import math

from person import Person

class Light():

    def __init__(self, canvas, x, y, light_number, color='yellow'):
        self.canvas = canvas

        self.x = x  
        self.y = y
        self.size = 120
        self.canvas = canvas
        self.light_no = light_number
        
        rect = [self.x-self.size, self.y-self.size, self.x+self.size, self.y+self.size]
        self.circle = self.canvas.create_oval(rect, outline=color, fill=color, tags=self.light_no)
        self.canvas.itemconfig(self.light_no, state="hidden")

    def turn_off_the_light(self):
        self.canvas.itemconfig(self.light_no, state="hidden")

    def turn_on_the_light(self):
        self.canvas.itemconfig(self.light_no, state="normal")

    def check_light(self, people):
        turn_on = False
        for person in people:
            if self.check_intersection(person.x, person.y, person.size, self.x, self.y, self.size):
                turn_on = True
        if turn_on:
            self.turn_on_the_light()
            print("turn on")
        else:
            self.turn_off_the_light()
            print("turn off")

    def check_intersection(self, x1, y1, r1, x2, y2, r2):
        d = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
        if(d <= r1 - r2):
            return False
        elif(d <= r2 - r1):
            return True
        elif(d < r1 + r2):
            return True
        elif(d == r1 + r2):
            return True
        else:
            return False
