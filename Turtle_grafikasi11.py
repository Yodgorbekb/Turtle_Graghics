import turtle

qalam = turtle.Turtle()
wn= turtle.Screen()
wn.title("Yodgorbek")
wn.bgcolor("white")
def egri():
    for i in range(200):
        qalam.right(1)
        qalam.forward(1)
def yur():
    qalam.fillcolor("blue")
    qalam.begin_fill()
    qalam.left(100)
    qalam.forward(113)
    egri()
    qalam.left(120)
    egri()
    qalam.forward(112)
    qalam.end_fill()
def tex():
    qalam.up()
    qalam.setpos(-72, 95)
    qalam.down()
    qalam.color("red")
    qalam.write("YODGORBEK",font=("Verdana",16,"bold"))
    qalam.hideturtle()
yur()
tex()
wn.mainloop()
