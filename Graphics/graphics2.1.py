from tkinter import *
import random
tk = Tk()
canvas = Canvas(tk, width=500, height=400)
tk.title("Drawing")
canvas.pack()

canvas.create_polygon(400,10,380,300,500,380, fill="blue")

for i in range(100):
    x1 = random.randrange(360)
    y1 = random.randrange(180)
    x2 = random.randrange(360)
    y2 = random.randrange(180)
    canvas.create_rectangle(x1, x2, y2, y2)
     
canvas.mainloop()