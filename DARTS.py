import math
import turtle
import random
import time

points = 0
result = 0
t = turtle.Turtle()
t.width(20)
t.speed(20)
t.shape("circle")
board = turtle.Screen()
board.setup(600, 600)

t.penup()
t.setpos(-300, -280)
t.fillcolor("blue")
t.begin_fill()
t.pendown()
t.forward(580)
t.left(90)
t.forward(575)
t.left(90)
t.forward(570)
t.left(90)
t.forward(575)
t.end_fill()

t.penup()
t.setpos(0, -250)
t.fillcolor("white")
t.begin_fill()
t.left(90)
t.pendown()
t.circle(250)
t.end_fill()

t.penup()
t.setpos(0, -150)
t.fillcolor("red")
t.begin_fill()
t.pendown()
t.circle(150)
t.end_fill()

t.penup()
t.setpos(0, -50)
t.fillcolor("yellow")
t.begin_fill()
t.pendown()
t.circle(50)
t.end_fill()
t.penup()

t.color("green")
t.width(5)
for i in range(100):
    x_cord = random.randint(-550, 550)
    y_cord = random.randint(-550, 550)
    t.setpos(x_cord, y_cord)
    t.stamp()
    result = abs(math.sqrt(math.pow(abs(t.xcor()), 2)+math.pow(abs(t.ycor()), 2)))
    if result <= 60:
        points += 10
        t.write("    10")
    elif result <= 160:
        points += 5
        t.write("    5")
    elif result <= 260:
        points += 1
        t.write("    1")
    else:
        points += 0
        t.write("    0")
time.sleep(10)
t.clear()
t.penup()
t.setpos(-50, 0)
t.write(f"   You got {points} points")
t.color("white")
time .sleep(5)
