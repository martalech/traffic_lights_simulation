import tkinter as tk

from person import Person

# Create window

window = tk.Tk()
window.geometry("800x600")
window.minsize(800, 600)
window.maxsize(800, 600)

# Create background

canvas = tk.Canvas(window, width=800, height=600, borderwidth=0, highlightthickness=0,
                   bg="white")
canvas.grid(row=0, column=0, sticky='w')

# Add circles
people = []
person = Person(canvas, 20, 20, 20)
people.append(person)

def move():
    for person in people:
        person.move()

    window.after(33, move)

move()

window.mainloop()