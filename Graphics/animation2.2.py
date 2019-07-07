from tkinter import *
import time
import random

tk = Tk()
canvas = Canvas(tk, width=500, height=400)
tk.title("Drawing")
canvas.pack()

ball = canvas.create_oval(10, 10, 60, 60, fill="orange")
ball2 = canvas.create_oval(10, 10, 60, 60, fill="red")

xspeed = 7
yspeed = 8
xspeed2 = 6
yspeed2 = 9

while True:
    canvas.move(ball, xspeed, yspeed)
    pos = canvas.coords(ball)
    if pos[3] >= 400 or pos[1] <= 0:
        yspeed = -yspeed
    if pos[2] >= 500 or pos[0] <= 0:
        xspeed = -xspeed
    canvas.move(ball2, xspeed2, yspeed2)
    pos = canvas.coords(ball2)
    if pos[3] >= 400 or pos[1] <= 0:
        yspeed2 = -yspeed2
    if pos[2] >= 500 or pos[0] <= 0:
        xspeed2 = -xspeed2
    tk.update()
    time.sleep(0.01)

tk.mainloop()
#red = you, orange = me