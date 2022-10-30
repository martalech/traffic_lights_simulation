from ui_model.person import Person

class Light():

    def __init__(self, canvas, x, y, light_number, color='yellow'):
        self.canvas = canvas

        self.x = x  
        self.y = y
        self.size = 120
        self.canvas = canvas
        self.light_no = light_number
        
        rect = [self.x, self.y, self.x+self.size, self.y+self.size]
        self.circle = self.canvas.create_oval(rect, outline=color, fill=color, tags=self.light_no)

    def turn_off_the_light(self):
        self.canvas.itemconfig(self.light_no, state="hidden")

    def turn_on_the_light(self):
        self.canvas.itemconfig(self.light_no, state="normal")

    def check_light(self, person):
        if abs((person.x + person.size/2) - (self.x + self.size/2)) <= (self.size + person.size) /2 or \
            abs((person.y + person.size/2)-(self.y+ self.size/2)) <= (self.size + person.size) /2:
            self.turn_on_the_light()
        else:
            self.turn_off_the_light()
