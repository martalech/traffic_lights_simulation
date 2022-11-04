from time import gmtime
from typing import List
from street_models.street_map import StreetMap
from ui_model.light import Light
from PIL import Image, ImageDraw, ImageTk

class DrawOnCanvas:

    total_light_time = 0
    temp_string = None
    def __init__(self, canvas, window) -> None:
        self.canvas = canvas
        self.streetmap = None
        self.lights= []
        self.people = []
        self.rectangles = []
        self.circles = []
        self.window = window
        self.images = []

    def draw_initial(self):
        self.draw_streets()
        self.draw_lights()
        self.draw_people()

    def draw_people_moving(self):
        self.total_light_time = 0
        self.move_people()

        for light in self.lights:
            self.total_light_time += light.light_time

        # print("Total light time: " + str((self.total_light_time * 10)) + " seconds")
        if "Total energy consumption: " + str((round(self.total_light_time * 10 * 100 / 3600, 2))) + " Watt/hours"\
                != self.temp_string and not None:
            self.temp_string = "Total energy consumption: " + str((round(self.total_light_time * 10 * 100 / 3600, 2))) + " Watt/hours"
            print("Total energy consumption: " + str((round(self.total_light_time * 10 * 100 / 3600, 2))) + " Watt/hours")

    # Street
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
        for i, l in enumerate(self.lights):
            l.adjust_light(self.people)
            rect = [l.x-l.size, l.y-l.size, l.x+l.size, l.y+l.size]
            
            alpha = int(l.power / 2 * 255)
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
            l.adjust_light(self.people)
            rect = [l.x-l.size, l.y-l.size, l.x+l.size, l.y+l.size]
            
            alpha = int(l.power / 2 * 255)
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

    # Person
    def add_people(self, people):
        self.people = people

    def add_person(self, person):
        self.people.append(person)

    def draw_people(self):
        for person in self.people:
            self.draw_person(person)
        
    def draw_person(self, person):
        rect = [person.x-person.size, person.y-person.size, person.x+person.size, person.y+person.size]
        person.circle = self.canvas.create_oval(rect, outline="black", fill="black")

    def move_people(self):
        for person in self.people:
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
