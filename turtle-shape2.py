import turtle as my_turtle
import random
t = my_turtle.Turtle()

colors = ['red', 'green', 'blue', 'cyan', 'lightgreen', 'turquoise', 'skyblue', 'IndianRed']

def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        t.forward(100)
        t.right(angle)

for shapa_side_n in range(3,11):
    t.color(random.choice(colors))
    draw_shape(shapa_side_n)