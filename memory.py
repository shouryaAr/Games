import random
from tkinter import *

master = Tk()
master.title('Memory')

class ResizingCanvas(Canvas):
    def __init__(self, parent, **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self, event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas 
        self.config(width = self.width, height = self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all", 0 , 0, wscale, hscale)

def draw_cards(cardw = 100, cardh = 150):
    global drawing, numbers
    x = 0
    y = 0
    xe = cardw+1
    ye = cardh+1
    rows = list(range(0, 4))
    columns = list(range(0, 5))
    i = 0
    drawing = [0] * 20
    numbers = [0] * 20
    for row in rows:
        for column in columns:
            drawing[i] = MemoryCanvas.create_rectangle(x, y, xe, ye, fill="green")
            numbers[i] = MemoryCanvas.create_text(x+cardw/2, y+cardh/2, text=deck[i], fill="green", font=("Calibri", 72))
            x += cardw
            xe += cardw
            i += 1
        xe = cardw+1
        ye += cardh
        x = 0
        y += cardh

def new_game():
    global exposed, state, deck, turns
    turns = 0
    TurnsLabel.configure(text="Turns: " + str(turns))
    deck = random.sample(range(10), 10)*2
    random.shuffle(deck)
    exposed = [False]*len(deck)
    state = 0
    currentw = MemoryCanvas.winfo_width()
    currenth = MemoryCanvas.winfo_height()
    cardw = currentw / 5
    cardh = currenth / 4
    draw_cards(cardw, cardh)

def click(event):
    global state, turns, cardone, cardtwo, rect1, rect2, text1, text2
    x, y = event.x, event.y
    #print('{}, {}'.format(x, y))
    currentw = MemoryCanvas.winfo_width()
    currenth = MemoryCanvas.winfo_height()
    cardw = currentw / 5
    cardh = currenth / 4
    card = int((x // cardw)+(y // cardh)*5)
    if exposed[card] == False:
        if state == 0:
            cardone = card
            exposed[cardone] = True
            MemoryCanvas.itemconfig(drawing[cardone], fill="Blue")
            MemoryCanvas.itemconfig(numbers[cardone], fill="White")
            state = 1
        elif state == 1:
            cardtwo = card
            exposed[cardtwo] = True
            MemoryCanvas.itemconfig(drawing[cardtwo], fill="Blue")
            MemoryCanvas.itemconfig(numbers[cardtwo], fill="White")
            state = 2
            turns += 1
            TurnsLabel.configure(text="Turns: " + str(turns))
        else:
            if deck[cardone] != deck[cardtwo]:
                exposed[cardone] = False
                exposed[cardtwo] = False
                MemoryCanvas.itemconfig(drawing[cardone], fill="Green")
                MemoryCanvas.itemconfig(numbers[cardone], fill="Green")
                MemoryCanvas.itemconfig(drawing[cardtwo], fill="Green")
                MemoryCanvas.itemconfig(numbers[cardtwo], fill="Green")
            cardone = card
            exposed[cardone] = True
            MemoryCanvas.itemconfig(drawing[cardone], fill="Blue")
            MemoryCanvas.itemconfig(numbers[cardone], fill="White")
            state = 1

MemoryFrame = Frame(master, bg="black")
MemoryFrame.pack(fill=BOTH, expand=YES)

TurnsLabel = Label(MemoryFrame, text="Turns: 0", font=("Calibri", 32), width=10, bg="black", fg="green")
TurnsLabel.grid(row=0, column=1)

RestartButton = Button(MemoryFrame, text="Restart", width=10, command=new_game, font=("Calibri", 32))
RestartButton.grid(row=0, column=0)

MemoryCanvas = ResizingCanvas(master, width=500, height=600, bg="red", highlightthickness=0)
MemoryCanvas.pack(fill=BOTH, expand=YES)

new_game()
draw_cards(100, 150)
#MemoryCanvas.addtag_all("all")
MemoryCanvas.bind('<Button-1>', click)
mainloop()
