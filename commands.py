from turtle import *

def dashed_line(number_of_dashes, dash_length):
    dashes = 0
    while dashes < number_of_dashes:
        timmy.pendown()
        timmy.forward(dash_length)
        timmy.penup()
        timmy.forward(dash_length)
        dashes += 1


def draw_triangle(length):
    timmy.forward