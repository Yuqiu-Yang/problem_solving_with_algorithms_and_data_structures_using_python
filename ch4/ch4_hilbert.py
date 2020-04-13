from turtle import *


def hilbert(edgeLen, degree, myTurtle, oriantation =1):
    if degree == 0:
        return None
    else:
        myTurtle.right(90 * oriantation)
        hilbert(edgeLen, degree - 1, myTurtle, -1 * oriantation)
        myTurtle.forward(edgeLen)
        myTurtle.left(90 * oriantation)
        hilbert(edgeLen, degree - 1, myTurtle, oriantation)
        myTurtle.forward(edgeLen)
        hilbert(edgeLen, degree - 1, myTurtle, oriantation)
        myTurtle.left(90 * oriantation)
        myTurtle.forward(edgeLen)
        hilbert(edgeLen, degree - 1, myTurtle, -1 * oriantation)
        myTurtle.right(90 * oriantation)

myTurtle = Turtle()
myTurtle.speed("fastest")
myWin = myTurtle.getscreen()
myTurtle.up()
myTurtle.backward(300)
myTurtle.left(90)
myTurtle.forward(200)
myTurtle.right(90)
myTurtle.down()
hilbert(5, 6, myTurtle)

myWin.exitonclick()
