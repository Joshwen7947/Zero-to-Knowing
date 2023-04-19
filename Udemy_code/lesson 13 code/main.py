from turtle import *

t = Turtle()
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
t.forward(100)
t.left(60)
exitonclick()

########################################################

t = Turtle()
t.width(5)
t.color("orange")

for i in range(6):
    t.forward(100)
    t.left(60)
exitonclick()

########################################################

t1 = Turtle()
t2 = Turtle()
t3 = Turtle()

t1.width(4)
t2.width(4)
t3.width(4)

t1.color("purple")
t2.color("lime green")
t3.color("red")

t1.penup()
t2.penup()
t3.penup()

t1.goto(-150,150)
t2.goto(-150,50)
t3.goto(-150,-50)

t1.pendown()
t2.pendown()
t3.pendown()

t1.begin_fill()
t2.begin_fill()
t3.begin_fill()

for i in range(3):
    t1.forward(100)
    t1.left(120)
    t2.forward(100)
    t2.left(120)
    t3.forward(100)
    t3.left(120)

t1.end_fill()
t2.end_fill()
t3.end_fill()
exitonclick()

########################################################

def square(t,size):
    for i in range(4):
        t.forward(size)
        t.left(90)
        
def triangle(t,size):
    for i in range(3):
        t.forward(size)
        t.left(120)

t = Turtle()
square(t,75)
triangle(t,60)

########################################################

def square(t,size):
    for i in range(4):
        t.forward(size)
        t.left(90)
        
def triangle(t,size):
    for i in range(3):
        t.forward(size)
        t.left(120)
        
ask = input("Square or Triangle: ").lower()
t = Turtle()
while ask != 'quit':
    if ask == 'square':
        size = int(input("Enter the size: "))
        square(t,size)
    elif ask == 'triangle':
        size = int(input("Enter the size: "))
        triangle(t,size)
    else:
        print("We don't have that shape!")
    ask = input("Square or Triangle: ").lower()







