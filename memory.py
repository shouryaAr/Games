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
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all", 0 , 0, wscale, hscale)

def new_game():
    global exposed, state, deck, turns
    turns = 0
    TurnsLabel.configure(text="Turns: " + str(turns))
    deck = random.sample(range(10), 10)*2
    random.shuffle(deck)
    exposed=[False]*len(deck)
    state = 0
    draw_cards()
    print(deck)
    print(exposed)

def click(event):
    global state, turns, cardone, cardtwo, rect1, rect2, text1, text2
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))
    #card=(x // 100)+(y // 150)*5
    #print("Card is " + str(card))
    currentw = MemoryCanvas.winfo_width()
    currenth = MemoryCanvas.winfo_height()
    print(str(currentw)+ " " + str(currenth))
    cardw = currentw / 5
    cardh = currenth / 4
    print(str(cardw)+ " " + str(cardh))
    card=int((x // cardw)+(y // cardh)*5)
    print("Card is " + str(card))
    
    '''
    if exposed[card] == False:
        if state == 0:
            rect1 = MemoryCanvas.create_rectangle(x // 100 * 100, y // 150 * 150, x // 100 * 100 + 100,
                                                  y // 150 * 150 + 150, fill="blue")
            text1 = MemoryCanvas.create_text(x // 100 * 100 + 50, y // 150 * 150 + 75, text=deck[card], fill="white",
                                             font=("Calibri", 72))
            print("card is " + str(card) + " and is true")
            cardone = card
            exposed[cardone] = True
            state = 1
            print(state)
        elif state == 1:
            rect2 = MemoryCanvas.create_rectangle(x // 100 * 100, y // 150 * 150, x // 100 * 100 + 100,
                                                  y // 150 * 150 + 150, fill="blue")
            text2 = MemoryCanvas.create_text(x // 100 * 100 + 50, y // 150 * 150 + 75, text=deck[card], fill="white",
                                             font=("Calibri", 72))
            print("card is " + str(card) + " and is true")
            cardtwo = card
            exposed[cardtwo] = True
            state = 2
            print(state)
            turns += 1
            TurnsLabel.configure(text="Turns: " + str(turns))
        else:
            if deck[cardone] != deck[cardtwo]:
                exposed[cardone] = False
                exposed[cardtwo] = False
                MemoryCanvas.itemconfig(rect1, fill="Green")
                MemoryCanvas.itemconfig(text1, fill="Green")
                MemoryCanvas.itemconfig(rect2, fill="Green")
                MemoryCanvas.itemconfig(text2, fill="Green")
            cardone = card
            exposed[cardone] = True
            rect1 = MemoryCanvas.create_rectangle(x // 100 * 100, y // 150 * 150, x // 100 * 100 + 100,
                                                  y // 150 * 150 + 150, fill="blue")
            text1 = MemoryCanvas.create_text(x // 100 * 100 + 50, y // 150 * 150 + 75, text=deck[card], fill="white",
                                             font=("Calibri", 72))
            state = 1
            print(state)
     '''
    
#MemoryFrame = Frame(master, width=100, height=100, bg="black")
#MemoryFrame.grid(row=0, column = 0)

MemoryFrame = Frame(master)
MemoryFrame.pack(fill=BOTH, expand=YES)

TurnsLabel = Label(MemoryFrame, text="Turns: 0", font=("Calibri", 32), width=10, fg="green", bg="black")
TurnsLabel.grid(row=1, column = 0)

RestartButton = Button(MemoryFrame, text="Restart", width=10, command=new_game, font=("Calibri", 32))
RestartButton.grid(row=0, column=0)

#MemoryCanvas = Canvas(master, width=500, height=600)
#MemoryCanvas.grid(row=1, column = 0, columnspan=5)

MemoryCanvas = ResizingCanvas(master, width=500, height=600, bg="red", highlightthickness=0)
MemoryCanvas.pack(fill=BOTH, expand=YES)

'''
MemoryCanvas.create_rectangle(0, 0, 101, 151, fill="blue")
MemoryCanvas.create_rectangle(100, 0, 201, 151, fill="blue")
MemoryCanvas.create_rectangle(200, 0, 301, 151, fill="blue")
MemoryCanvas.create_rectangle(300, 0, 401, 151, fill="blue")
MemoryCanvas.create_rectangle(400, 0, 501, 151, fill="blue")
'''

def draw_cards():
    x=0
    y=0
    xe=101
    ye=151
    rows=list(range(0, 4))
    columns=list(range(0, 5))
    for row in rows:
        for column in columns:
            MemoryCanvas.create_rectangle(x, y, xe, ye, fill="green")
            x+=100
            xe+=100
            column+=1
        xe=101
        ye+=150
        x=0
        y+=150

new_game()
draw_cards()
MemoryCanvas.addtag_all("all")
master.bind('<Button-1>', click)
mainloop()
