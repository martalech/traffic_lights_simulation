import tkinter as tk

from draw_on_canvas.draw_on_canvas import DrawOnCanvas
from tkinter import filedialog as fd
from configuration_parser.parser import parse_scenario_to_draw_gui

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
parse_scenario_to_draw_gui("./example_scenarios/powerlight_gui.txt", draw_gui)

def move():
    draw_gui.tick()
    window.after(50, move)
    return

def select_file():
    filetypes = [('text files', '*.txt')]

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='./example_scenarios',
        filetypes=filetypes)
    parse_scenario_to_draw_gui(filename, draw_gui)
    if filename is not None:
        try:
            parse_scenario_to_draw_gui(filename, draw_gui)
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