from time import gmtime
from typing import List

from model.time import Time
from street_models.street_map import StreetMap
from ui_model.light import Light
from PIL import Image, ImageDraw, ImageTk

class DrawOnCanvas:

    def __init__(self, canvas, window) -> None:
        self.canvas = canvas
        self.streetmap: StreetMap = None
        self.lights= []
        self.rectangles = []
        self.circles = []
        self.window = window
        self.images = []
        self.time = Time()

    def draw_initial(self):
        self.draw_streets()
        self.draw_lights()
        self.draw_people()

    def tick(self):
        self.time.tick()
        shift_factor = self.time.get_shift_factor()
        if shift_factor != 1:
            self.remove_people()
            self.streetmap.adjust_traffic(shift_factor)
            self.draw_people()
        self.draw_people_moving()
        self.update_lights()

    def draw_people_moving(self):
        self.move_people()

    # street
    def add_streets(self, streetmap: StreetMap):
        self.streetmap = streetmap

    def draw_streets(self):
        for s in self.streetmap.streets:
            rectangle = self.canvas.create_rectangle(s.start_point.x, s.start_point.y, s.end_point.x, s.end_point.y, fill='gray', outline="gray")
            self.canvas.tag_lower(rectangle)
            self.rectangles.append(rectangle)

    # light
    def add_lights(self, lights: List[Light]):
        self.lights = lights

    def draw_lights(self):
        for l in self.lights:
            l.adjust_light(self.streetmap.people)
            rect = [l.x-l.size, l.y-l.size, l.x+l.size, l.y+l.size]
            
            alpha = l.calculate_light_gui()
            fill = self.window.winfo_rgb("yellow") + (alpha,)
            image = Image.new('RGBA', (700, 600))
            ImageDraw.Draw(image).ellipse(rect, fill=fill)
            tk_image = ImageTk.PhotoImage(image)
            self.images.append(tk_image)

            circle = self.canvas.create_image(0, 0, image=tk_image, anchor='nw', tags=l.light_no)
            self.circles.append(circle)

            if l.power == 0:
                self.turn_off_the_light(l)
            else:
                self.turn_on_the_light(l)

    def update_lights(self):
        for i, l in enumerate(self.lights):
            l.adjust_light(self.streetmap.people)
            rect = [l.x-l.size, l.y-l.size, l.x+l.size, l.y+l.size]
            
            alpha = l.calculate_light_gui()
            fill = self.window.winfo_rgb("yellow") + (alpha,)
            image = Image.new('RGBA', (700, 600))
            ImageDraw.Draw(image).ellipse(rect, fill=fill)
            self.images[i] = ImageTk.PhotoImage(image)

            self.canvas.itemconfig(l.light_no, image=self.images[i])

            if l.power == 0:
                self.turn_off_the_light(l)
            else:
                self.turn_on_the_light(l)
    
    def turn_off_the_light(self, light):
        self.canvas.itemconfig(light.light_no, state="hidden")

    def turn_on_the_light(self, light):
        self.canvas.itemconfig(light.light_no, state="normal")

    def draw_people(self):
        for person in self.streetmap.people:
            self.draw_person(person)
        
    def draw_person(self, person):
        rect = [person.x-person.size, person.y-person.size, person.x+person.size, person.y+person.size]
        person.circle = self.canvas.create_oval(rect, outline="black", fill="black")

    def move_people(self):
        for person in self.streetmap.people:
            person.move(self.canvas.winfo_width(), self.canvas.winfo_height())
            self.canvas.move(person.circle, person.move_x, person.move_y)
    
    def remove_strets(self):
        for rectangle in self.rectangles:
            self.canvas.delete(rectangle)
        self.rectangles = []
    
    def remove_lights(self):
        for circle in self.circles:
            self.canvas.delete(circle)
        self.circles = []
        self.images = []

    def remove_people(self):
        if self.streetmap is not None:
            for person in self.streetmap.people:
                self.canvas.delete(person.circle)