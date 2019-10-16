import turtle
from math import sin, cos, pi

screen = turtle.Screen()
screen.tracer(0)

turtle.hideturtle()
turtle.speed(0)

n = 5
distance = 100

for i in range (0, 361, 1):
    x = distance * cos(n*i) * cos(i)
    y = distance * cos(n*i) * sin(i)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.dot(6)
    turtle.update()

turtle.exitonclick()