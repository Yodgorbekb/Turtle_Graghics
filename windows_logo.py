import turtle
import colorsys

turtle.title("Windows Logo")
turtle.bgcolor("black")
turtle.speed(0)

y=0.009

def kub1():
    #Kubning  1-tarafi
    turtle.fillcolor("#1b0cc2")
    turtle.begin_fill()
    turtle.lt(90)
    turtle.fd(200)
    #2-taraf
    turtle.lt(90)
    turtle.fd(200)
    #3-taraf
    turtle.lt(90)
    turtle.fd(200)
    #4-taraf
    turtle.lt(90)
    turtle.fd(200)
    turtle.end_fill()

def kub2():
    #oraliq
    turtle.fillcolor('#1b0cc2')
    turtle.begin_fill()
    turtle.fd(237)
    #1-taraf
    turtle.lt(90)
    turtle.fd(200)
    #2-taraf
    turtle.lt(90)
    turtle.fd(200)
    #3-taraf
    turtle.lt(90)
    turtle.fd(200)
    #4-taraf
    turtle.lt(90)
    turtle.fd(200)
    
    turtle.end_fill()

def kub3():
    turtle.fillcolor('#1b0cc2')
    turtle.begin_fill()
    #oraliq
    turtle.rt(90)
    turtle.fd(237)
    #1-taraf
    turtle.rt(90)
    turtle.fd(200)
    #2-taraf
    turtle.rt(90)
    turtle.fd(200)
    #3-taraf
    turtle.rt(90)
    turtle.fd(200)
    #4-taraf
    turtle.rt(90)
    turtle.fd(200)

    turtle.end_fill()

def kub4():
    turtle.fillcolor('#1b0cc2')
    turtle.begin_fill()
    #oraliq
    turtle.rt(90)
    turtle.fd(237)
    #1-taraf
    turtle.fd(200)
    #2-taraf
    turtle.rt(90)
    turtle.fd(200)
    #3-taraf
    turtle.rt(90)
    turtle.fd(200)
    #4-taraf
    turtle.rt(90)
    turtle.fd(200)

    turtle.end_fill()

def text():
    turtle.rt(90)
    turtle.fd(120)

#    turtle.rt(90)
#    turtle.fd(200)

#    turtle.lt(90)
#    turtle.fd(40)
#   turtle.rt(90)
#    turtle.fd(20)
    turtle.color('red')
    turtle.write("Windows  10", font=("Verdana",70,"bold"))
    turtle.hideturtle()

def rang():
    for j in range(130):
        v=colorsys.hsv_to_rgb(y,1,1)
        turtle.bgcolor(v)
        y+=0.009
        turtle.hideturtle()




kub1()
kub2()
kub3()
kub4()
text()
#rang()

turtle.mainloop()