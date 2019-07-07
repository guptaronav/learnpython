from tkinter import *
import time
import random


tk = Tk()
canvas = Canvas(tk, width=2000, height=2000)
tk.title("Drawing")
canvas.pack()

class Ball:
    def __init__(self, color, size):
        self.shape = canvas.create_oval(10, 10, size, size, fill=color)
        self.xspeed = random.randrange(10,100)
        self.yspeed = random.randrange(10,100)

    def move(self):
        canvas.move(self.shape, self.xspeed, self.yspeed)
        pos = canvas.coords(self.shape)
        if pos[3] >= 2000 or pos[1] <= 0:
            self.yspeed = -self.yspeed
        if pos[2] >= 2000 or pos[0] <= 0:
            self.xspeed = -self.xspeed

colors = ['red','green','blue','orange','yellow','purple','cyan','magenta','dodgerblue','lightgreen','turquoise','grey','gold','pink','darkgreen']

balls = []
for i in range(1000):
    balls.append(Ball(random.choice(colors),random.randrange(1,100)))

while True:
    for ball in balls:
        ball.move()
    tk.update()
    time.sleep(0.01)

tk.mainloop()
