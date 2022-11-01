import tkinter as tk

from tkinter.messagebox import Message
from draw_on_canvas.draw_on_canvas import DrawOnCanvas
from street_models.street_map import StreetMap
from ui_model.person import Person
from ui_model.light import Light
from generators.street_generator import StreetGenerator

# Create window

window = tk.Tk()
window.geometry("800x600")
window.minsize(800, 600)
window.maxsize(800, 600)

frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
frame.grid(row=0, column=0)

frame2 = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
frame2.grid(row=0, column=1)

# Create background

canvas = tk.Canvas(frame, width=750, height=600, borderwidth=0, highlightthickness=0,
                   bg="white")
canvas.pack()

draw_gui = DrawOnCanvas(canvas)

# Add lights
draw_gui.add_lights([Light(100, 200), Light(200, 300), Light(300, 400)])

#Add streets
map = StreetMap()
map.add_street(StreetGenerator.generate_horizontal_street(0,0,750))
map.add_street(StreetGenerator.generate_vertical_street(0,0,600))

# draw gui
draw_gui.add_streets(map)

# Add circles
people = []
person1 = Person(20)
person2 = Person(20)
people = [person1, person2]
draw_gui.add_people(people)
draw_gui.draw_initial()

def move():
    draw_gui.draw_people_moving()
    window.after(50, move)

def helloCallBack():
    person1 = Person(20)
    draw_gui.add_person(person1)
    draw_gui.draw_person(person1)

B = tk.Button(frame2, text ="Add", command = helloCallBack)

B.pack()

move()

window.mainloop()