import tkinter as tk
import random

from tkinter.messagebox import Message


from draw_on_canvas.draw_on_canvas import DrawOnCanvas
from street_models.street_map import StreetMap
from ui_model.person import Person
from ui_model.light import Light
from generators.street_generator import StreetGenerator
from tkinter import filedialog as fd
from configuration_parser.parser import parse_scenario

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

canvas = tk.Canvas(frame, width=700, height=600, borderwidth=0, highlightthickness=0,
                   bg="white")
canvas.pack()

draw_gui = DrawOnCanvas(canvas, window)
parse_scenario("./example_scenarios/scenario1.txt", draw_gui)

def move():
    draw_gui.draw_people_moving()
    draw_gui.update_lights()
    window.after(50, move)
    return

def add_person():
    point, street = draw_gui.streetmap.find_spawning_spot()
    person1 = Person(20,  point, street) #TODO : Do not refer to gui static'ish way
    draw_gui.add_person(person1)
    draw_gui.draw_person(person1)

B = tk.Button(frame2, text ="Add", command = add_person)

B.pack()

def select_file():
    filetypes = [('text files', '*.txt')]

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    parse_scenario(filename, draw_gui)
    if filename is not None:
        try:
            parse_scenario(filename, draw_gui)
        except Exception:
            tk.messagebox.showerror(title='Error', message='Invalid scenario file format')

    print('Opened ', filename)

# open button
open_button = tk.Button(
    frame2,
    text='Open scenario',
    command=select_file
)

open_button.pack(expand=True)

move()

window.mainloop()