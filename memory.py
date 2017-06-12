import random
from tkinter import *

master = Tk()
master.title('Memory')

def restart():
    TurnsLabel.configure(text="Turns: 0")
    deck = random.sample(range(10), 10)*2
    random.shuffle(deck)
    print(deck)
    exposed=[False]*len(deck)
    print(exposed)

def click(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))


MemoryFrame = Frame(master, width=100, height=100, bg="black")
MemoryFrame.grid(row=0, column = 0)

TurnsLabel = Label(MemoryFrame, text="Turns: 0", font=("Calibri", 32), width=10, fg="green", bg="black")
TurnsLabel.grid(row=1, column = 0)

RestartButton = Button(MemoryFrame, text="Restart", width=10, command=restart, font=("Calibri", 32))
RestartButton.grid(row=0, column=0)

MemoryCanvas = Canvas(master, width=200, height=150)
MemoryCanvas.grid(row=0, column = 1, rowspan=2)

MemoryCanvas.create_rectangle(0, 0, 100, 151, fill="blue")
MemoryCanvas.create_rectangle(100, 0, 200, 151, fill="blue")

master.bind('<Button-1>', click)
mainloop()
