from turtle import *

def kochSnowflake(edgeLen,degree, myTurtle):
    if degree == 0:
        myTurtle.forward(edgeLen)
        return None
    else:
        edgeLen /= 3
        kochSnowflake(edgeLen, degree - 1, myTurtle)
        myTurtle.left(60)
        kochSnowflake(edgeLen, degree - 1, myTurtle)
        myTurtle.right(120)
        kochSnowflake(edgeLen, degree - 1, myTurtle)
        myTurtle.left(60)
        kochSnowflake(edgeLen, degree - 1, myTurtle)


myTurtle = Turtle()
myTurtle.speed(1000)
myWin = myTurtle.getscreen()
myTurtle.fillcolor("purple")
myTurtle.up()
myTurtle.backward(200)
myTurtle.left(90)
myTurtle.forward(100)
myTurtle.right(90)
myTurtle.down()
myTurtle.begin_fill()
for i in range(3):
    kochSnowflake(500, 4, myTurtle)
    myTurtle.right(120)
myTurtle.end_fill()
myWin.exitonclick()
