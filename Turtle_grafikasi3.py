from turtle import *
import colorsys
speed(0)
bgcolor("black")
h=0.09

#y=0.09
pensize(4)

for i in range(140):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.008
    for j in range(6):
        fd(i)
        rt(150)
        lt(60)
    rt(120*2)
    circle(60)
#    for j in range(130):
#        col=colorsys.hsv_to_rgb(y,1,1)
#        bgcolor(col)
#        y+=0.09
done()