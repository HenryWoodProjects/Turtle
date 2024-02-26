import turtle as t
import random

t.colormode(255)
timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("blue")
timmy.pensize(1)
timmy.speed(50)

turtle_colours = ["red", "blue", "green", "purple", "pink", "orange", "violet", "slateblue", "rosybrown", "seagreen"]


def dashed_line(number_of_dashes, dash_length):
    dashes = 0
    while dashes < number_of_dashes:
        timmy.pendown()
        timmy.forward(dash_length)
        timmy.penup()
        timmy.forward(dash_length)
        dashes += 1


def draw_shape(number_of_sides, length):
    sides = 0
    angle = 360 / number_of_sides
    while sides < number_of_sides:
        timmy.forward(length)
        timmy.right(angle)
        sides += 1


def draw_multiple_shapes(number_of_shapes, length_of_sides):
    shapes = 3
    while shapes <= number_of_shapes:
        colour = turtle_colours[shapes-1]
        timmy.pencolor(colour)
        draw_shape(shapes, length_of_sides)
        shapes += 1


def random_walk(steps, step_length):
    direction = 90 * random.randint(1, 4)
    steps_taken = 0
    while steps_taken <= steps:
        colour = random_colour()
        timmy.color(colour)
        timmy.right(direction)
        timmy.forward(step_length)
        steps_taken += 1
        direction = 90 * random.randint(1, 4)


def random_colour():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    rgb_tuple = (r, g, b)
    return rgb_tuple


def spirograph(circles, radius):
    angle = 0
    rotation = 360 / circles
    while angle <= 360:
        colour = random_colour()
        timmy.color(colour)
        timmy.circle(radius)
        timmy.left(rotation)
        angle += rotation


spirograph(50, 100)

screen = t.Screen()
screen.exitonclick()
