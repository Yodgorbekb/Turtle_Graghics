from turtle import *
import colorsys

speed(0)
h=0.8
pensize(2)
bgcolor('black')

for i in range(550):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.004
    circle(190-i,30)
    rt(220)
    lt(20)
    circle(190-i,30)
done()