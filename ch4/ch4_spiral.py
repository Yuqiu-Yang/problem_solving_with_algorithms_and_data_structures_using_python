from turtle import *
myTurtle = Turtle()
myTurtle.speed(200)
myWin = myTurtle.getscreen()
myWin.screensize(2000,1500)
def drawSprial(myTurtle, linelen):
    if linelen < 10:
        if (linelen//10)%2 == 0:
            myTurtle.forward(linelen)
            myTurtle.right(5)
            drawSprial(myTurtle, linelen + 0.01)
        else:
            myTurtle.backward(linelen)
            myTurtle.left(5)
            drawSprial(myTurtle, linelen + 0.01)


drawSprial(myTurtle, 0.01)
myWin.exitonclick()
