# WE ARE USING THIS JUST TO IMPORT COLOUR DETAILS FROM AN IMAGE ONCE WE GET THAT WE WILL SAVE IT TO ANOTHER
# LIST AND USE THAT
# import colorgram
#
# rgb_values = []
# colors = colorgram.extract('practice.png',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     col_tupl = (r, g, b)
#     rgb_values.append(col_tupl)
#
# print(rgb_values)
import random
import turtle as t
from itertools import count

color_list = [(68, 13, 60), (30, 22, 68), (134, 20, 94), (48, 42, 121), (143, 85, 48), (55, 84, 149),
              (243, 37, 117), (164, 45, 102), (229, 151, 65), (249, 229, 53), (188, 148, 40), (232, 83, 61),
              (69, 36, 22), (88, 107, 202), (102, 158, 210), (110, 44, 35), (171, 139, 167), (91, 72, 23),
              (89, 104, 94), (231, 224, 179), (67, 147, 179), (228, 211, 16), (97, 228, 252), (134, 158, 142),
              (110, 140, 124), (34, 39, 36), (205, 174, 208), (205, 185, 181), (43, 70, 81), (211, 202, 207)]

ninja_tle = t.Turtle()
ninja_tle.speed("fastest")
ninja_tle.hideturtle()
t.colormode(255)
for i in range(0,10):
    count = 0
    while count != 10:
        ninja_tle.penup()
        ninja_tle.dot(20,random.choice(color_list))
        ninja_tle.fd(50)
        count +=1
    ninja_tle.home()
    ninja_tle.lt(90)
    ninja_tle.fd(25+(25*i))
    ninja_tle.rt(90)


ninja_tleScreen = t.Screen()
ninja_tleScreen.exitonclick()
