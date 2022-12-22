from turtle import *
import colorsys

speed(0)
h=0.1
bgcolor('black')
pensize(2)

for i in range(600):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.004
    if i%5==0:
        lt(3)
    fd(100)
    lt(360/5)
done()