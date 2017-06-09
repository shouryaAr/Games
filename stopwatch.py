import random
from tkinter import *

master = Tk()
master.title('Stopwatch')

timer = [0, 0, 0]
TimePattern = '{0:01d}:{1:02d}:{2:01d}'

score = [0, 0]
ScorePattern = '{0:01d}/{1:01d}'

state = False

def start():
    global state
    state = True
    time_update()

def stop():
    global state
    state = False
    if timer[2] == 0:
        score[0] += 1
    score[1] += 1
    ScoreText = ScorePattern.format(score[0], score[1])
    ScoreLabel.configure(text="Score: " + ScoreText)

def reset():
    global state
    state = False
    score[0] = 0
    score[1] = 0
    timer[0] = 0
    timer[1] = 0
    timer[2] = 0
    TimeLabel.configure(text="0:00:0")
    ScoreText = ScorePattern.format(score[0], score[1])
    ScoreLabel.configure(text="Score: " + ScoreText)

StopwatchFrame = Frame(master, width=200, height=100)
StopwatchFrame.pack()

StartButton = Button(StopwatchFrame, text="Start", height=2, width=5, command=start, font=("Calibri", 32))
StartButton.grid(row=0, column=0)

StopButton = Button(StopwatchFrame, text="Stop", height=2, width=5, command=stop, font=("Calibri", 32))
StopButton.grid(row=0, column=1)

ResetButton = Button(StopwatchFrame, text="Reset", height=2, width=5, command=reset, font=("Calibri", 32))
ResetButton.grid(row=0, column=2)

TimeLabel = Label(StopwatchFrame, text="0:00:0", font=("Calibri", 72))
TimeLabel.grid(row=2, column = 0, columnspan=3)

ScoreLabel = Label(StopwatchFrame, text="Score: 0/0", font=("Calibri", 32), fg="green")
ScoreLabel.grid(row=1, column = 0, columnspan=3)

def time_update():
    if state:
        timer[2] += 1

        if timer[2] == 10:
            timer[1] += 1
            timer[2] = 0

        if timer[1] == 60:
            timer[0] += 1
            timer[1] = 0

        TimeText = TimePattern.format(timer[0], timer[1], timer[2])
        TimeLabel.configure(text=TimeText)

        master.after(100, time_update)

mainloop()
