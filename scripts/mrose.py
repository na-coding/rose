import turtle
from math import sin, cos, radians

screen = turtle.Screen()
screen.tracer(0)

turtle.hideturtle()
turtle.speed(0)
turtle.color('black', 'red')

n = 6
d = 71
distance = 150

turtle.penup()
turtle.begin_fill()
for i in range (361):
    # x = distance * cos(radians(n*i)) * cos(radians(i))
    # y = distance * cos(radians(n*i)) * sin(radians(i))

    k = i * d
    r = distance * sin(radians(n * k))
    x =  r * cos(radians(k))
    y = r * sin(radians(k))

    turtle.goto(x,y)
    turtle.pendown()
    turtle.dot(6)
    turtle.update()

turtle.end_fill()
turtle.exitonclick()