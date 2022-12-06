import turtle as my_turtle
import random
my_turtle.colormode(255)
t = my_turtle.Turtle()
screen = my_turtle.Screen()
#screen.tracer(False)

directions = [0, 90, 180, 270]
thickness = [i for i in range(10)]
move = [i for i in range(30, 70, 10)]
t.speed(0)
t.hideturtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r, g, b)
    return random_color

def draw():
    t.color(random_color())
    t.width(random.choice(thickness))
    t.forward(random.choice(move))
    t.setheading(random.choice(directions))
    return None

for _ in range(2000):
    draw()


