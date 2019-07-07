# The PolyGuess Game
import os 
import turtle
import random

fred = turtle.Pen()
fred.speed(0)
fred.shape("turtle")
fred.width(1)

colorlist = ["red","green","blue","yellow","orange","magenta","purple","pink"]

def polygon(sides,size):
    for i in range(sides):
        fred.forward(size)
        fred.left(360/sides)

def square(size):
    for i in range(4):
        fred.forward(size)

blacksides = 0
a = random.randrange(1,50)
for i in range(a):
    x = random.randrange(-200,200)
    y = random.randrange(-200,200)
    n = random.randrange(4,10)
    if i == 0:
        blacksides = n
    s = random.randrange(10,200)
    fred.up()
    fred.goto(x,y)
    fred.down()
    col = random.choice(colorlist)
    polygon(n,s)
    fred.color(col)

name = input("What's your name? ").capitalize()
guessblacksides = int(input("Guess how many sides the black polygon has? "))
if blacksides == guessblacksides:
    # play
    maxretries = 5
    for retry in range(maxretries):
        guess = int(input("Guess how many polygons are there? "))

        if guess > a:
            if retry == maxretries - 1:
                print(name, ", You guessed too high, YOU LOST") 
                print("Correct number of polygons were: ", a) 
            else:
                print("You guessed too high, retry")                 
        elif guess == a:
            print(name, ", YOU WON! Total tries = ", retry + 1)
            os.system("figlet YOU WON!") 
            break
        else:
            if retry == maxretries - 1:
                print(name, ", You guessed too low, YOU LOST") 
                print("Correct number of polygons were: ", a) 
            else:
                print("You guessed too low, retry")      
else:
    print("You guessed wrong, YOU CANNOT PLAY") 
    