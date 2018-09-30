import turtle
import math
t=turtle.Turtle()
t.color("red")
t.begin_fill()
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)
def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)


arc(t, 30, 180)
t.lt(45)
t.fd(45)
t.lt(90)
t.fd(45)
t.end_fill()
t.pu()
t.fd(100)
t.pd()
t.color('blue')
t.begin_fill()
polygon(t, 5, 50) 
t.end_fill()
t.pu()
t.backward(300)
t.pd()
polyline(t, 10, 100, 135)
