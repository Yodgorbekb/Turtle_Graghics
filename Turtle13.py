from turtle import *
import colorsys

speed(0)
bgcolor('black')
pensize(4)
h=0.2

for i in range(40):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.008
    lt(20)
    for j in range(5):
        fd(250)
        rt(144)
done()