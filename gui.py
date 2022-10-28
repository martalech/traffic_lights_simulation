import tkinter as tk

from tkinter.messagebox import Message
from person import Person
from light import Light

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

lights = [Light(canvas, 100, 200, "1"), Light(canvas, 200, 300, "2"), Light(canvas, 300, 400, "3")]

# Add circles

people = []
person1 = Person(canvas, 20)
person2 = Person(canvas, 20)
people = [person1, person2]

def move():
    for person in people:
        person.move()
    for light in lights:
        light.check_light(people)

    window.after(50, move)

def helloCallBack():
    person1 = Person(canvas, 20)
    people.append(person1)

B = tk.Button(frame2, text ="Add", command = helloCallBack)

B.pack()

move()

window.mainloop()