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


MemoryFrame = Frame(master, width=500, height=100, bg="black")
MemoryFrame.pack()

TurnsLabel = Label(MemoryFrame, text="Turns: 0", font=("Calibri", 32), fg="green", bg="black")
TurnsLabel.grid(row=1, column = 0, columnspan=1)

RestartButton = Button(MemoryFrame, text="Restart", height=1, width=7, command=restart, font=("Calibri", 32))
RestartButton.grid(row=0, column=0)

mainloop()