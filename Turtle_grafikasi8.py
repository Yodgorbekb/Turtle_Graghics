from turtle import *
import colorsys


speed(0)
bgcolor('black')
h=0.8

for i in range(300):
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h+=0.09
    fd(i)
    rt(89)
    fd(i*2)
    rt(89)
done()