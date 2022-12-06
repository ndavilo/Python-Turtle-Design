from turtle import Turtle, Screen
my_turtle = Turtle()
my_screen = Screen()
import colorsys

my_screen.bgcolor('black')
my_turtle.speed(0)
n=36
h=0

for i in range(460):
    c =colorsys.hsv_to_rgb(h,1,0.9)
    my_turtle.color(c)
    my_turtle.left(145)

    for i in range(5):
        my_turtle.forward(300)
        my_turtle.left(150)


my_screen.exitonclick()