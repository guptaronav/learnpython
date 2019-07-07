import turtle
import random
fred = turtle.Pen()

fred.speed(0)
fred.shape("turtle")
fred.width(1)

colorlist = ["red","green","blue","yellow","orange"]

def polygon(sides,size):
    for i in range(sides):
        fred.forward(size)
        fred.left(360/sides)

def square(size):
    for i in range(4):
        fred.forward(size)
        
for i in range(1000):
    x = random.randrange(-200,200)
    y = random.randrange(-200,200)
    n = random.randrange(4,10)
    s = random.randrange(10,200)
    fred.up()
    fred.goto(x,y)
    fred.down()
    col = random.choice(colorlist)
    polygon(n,s)
    fred.color(col)
    
##polygon(4,5)
##fred.forward(100)
##polygon(6,10)
##fred.forward(100)
##polygon(8,15)
