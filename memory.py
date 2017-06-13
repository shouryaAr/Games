import random
from tkinter import *

master = Tk()
master.title('Memory')

deck = random.sample(range(10), 10)*2
random.shuffle(deck)
print(deck)

exposed=[False]*len(deck)

def restart():
    TurnsLabel.configure(text="Turns: 0")
    deck = random.sample(range(10), 10)*2
    random.shuffle(deck)
    print(deck)
    print(exposed)

def click(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))
    MemoryCanvas.create_rectangle(0, 0, 101, 151, fill="blue")
    if exposed[x // 100] == False:
        print(str(x // 100) + " is false")
        

MemoryFrame = Frame(master, width=100, height=100, bg="black")
MemoryFrame.grid(row=0, column = 0)

TurnsLabel = Label(MemoryFrame, text="Turns: 0", font=("Calibri", 32), width=10, fg="green", bg="black")
TurnsLabel.grid(row=1, column = 0)

RestartButton = Button(MemoryFrame, text="Restart", width=10, command=restart, font=("Calibri", 32))
RestartButton.grid(row=0, column=0)

MemoryCanvas = Canvas(master, width=500, height=600)
MemoryCanvas.grid(row=1, column = 0, columnspan=5)

'''
MemoryCanvas.create_rectangle(0, 0, 101, 151, fill="blue")
MemoryCanvas.create_rectangle(100, 0, 201, 151, fill="blue")
MemoryCanvas.create_rectangle(200, 0, 301, 151, fill="blue")
MemoryCanvas.create_rectangle(300, 0, 401, 151, fill="blue")
MemoryCanvas.create_rectangle(400, 0, 501, 151, fill="blue")
'''

xr=0
yr=0
xre=101
yre=151
rows=list(range(0, 4))
columns=list(range(0, 5))
i=0
xt=50
yt=75

clicked = False

for row in rows:
    for column in columns:
        if clicked:
            MemoryCanvas.create_rectangle(xr, yr, xre, yre, fill="blue")
            MemoryCanvas.create_text(xt, yt, text=deck[i], fill="white", font=("Calibri", 72))
        else:
            MemoryCanvas.create_rectangle(xr, yr, xre, yre, fill="green")
        xr+=100
        xre+=100
        column+=1
        i+=1
        xt+=100
    xre=101
    yre+=150
    xr=0
    yr+=150
    xt=50
    yt+=150

master.bind('<Button-1>', click)
mainloop()
