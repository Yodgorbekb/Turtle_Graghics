from turtle import *
import colorsys

speed(0)
bgcolor('black')
pensize(3)
h=0.1

for i in range(600):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.004
    if i%8==0:
        lt(5)
    fd(100)
    rt(360/8)


speed(0)
bgcolor("black")
u=0.0
pensize(4)

for i in range(130):
    c=colorsys.hsv_to_rgb(u,1,1)
    color(c)
    u+=0.005
    for j in range(6):
        fd(i)
        rt(150)
        lt(60)
    rt(120*2)
    circle(60)


done()