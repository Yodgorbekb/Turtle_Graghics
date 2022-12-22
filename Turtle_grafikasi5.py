from turtle import *
import colorsys

speed(0)
bgcolor('black')
h=0.1

for i in range(200):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=0.1
    fillcolor(c)
    begin_fill()
    for j in range(4):
        fd(0.2*i*j)
        lt(91)
    lt(73*15/100+15)
    end_fill()
done()