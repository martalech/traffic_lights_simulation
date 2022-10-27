class Light():

    def __init__(self, canvas, x, y, color='yellow'):
        self.canvas = canvas

        self.x = x  
        self.y = y
        self.size = 120
        self.color = color
        
        rect = [self.x, self.y, self.x+self.size, self.y+self.size]
        self.circle = canvas.create_oval(rect, outline=color, fill=color)