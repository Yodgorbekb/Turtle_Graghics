from turtle import *

speed(0)
bgcolor('black')
pencolor('blue')

i =1
while True:
    i += 1
    circle(3,i)
    forward(i)
    if i == 220:
        break
done()