# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
import turtle
from turtle import Turtle
import random


turtle.colormode(255)
color_list = [ (124, 180, 210), (234, 243, 238), (198, 174, 16), (29, 119, 167), (176, 14, 45), (235, 150, 76), (236, 204, 90), (217, 124, 163), (26, 144, 74), (215, 80, 123), (9, 171, 210), (212, 61, 27), (237, 77, 45), (245, 157, 187), (64, 21, 53), (12, 183, 150), (13, 31, 75), (161, 57, 106), (76, 27, 22), (129, 209, 233), (161, 192, 164), (15, 48, 132), (102, 116, 181), (250, 159, 152), (168, 24, 19), (121, 216, 209), (3, 
88, 57)]

jim = Turtle()
jim.penup()
jim.hideturtle()
jim.speed("fastest")

jim.setheading(225)
jim.forward(300)
jim.setheading(0)

number_of_dots = 101

for dots_count in range(1, number_of_dots):
    jim.dot(20, random.choice(color_list))
    
    jim.forward(50)
    if dots_count % 10 == 0:
        jim.setheading(90)
        jim.forward(50)
        jim.setheading(180)
        jim.forward(500)
        jim.setheading(0)






screen = turtle.Screen()
screen.exitonclick()