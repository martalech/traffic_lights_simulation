from typing import List
from street_models.street_map import StreetMap
from ui_model.light import Light



class DrawOnCanvas:
    def __init__(self, canvas) -> None:
        self.canvas = canvas
        self.streetmap = None
        self.lights= []
        self.people = []
        self.rectangles = []
        self.circles = []

    def draw_initial(self):
        self.draw_streets()
        self.draw_lights()
        self.draw_people()

    def draw_people_moving(self):
        self.move_people()

        for light in self.lights:
            if light.should_turn_on_the_light(self.people):
                self.turn_on_the_light(light)
            else:
                self.turn_off_the_light(light)


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
        for l in self.lights:
            rect = [l.x-l.size, l.y-l.size, l.x+l.size, l.y+l.size]
            circle = self.canvas.create_oval(rect, outline="yellow", fill="yellow", tags=l.light_no)
            self.canvas.itemconfig(l.light_no, state="hidden")
            self.circles.append(circle)
    
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
