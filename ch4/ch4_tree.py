import random
from turtle import *


def tree(branchLen, t):
    if branchLen > 5:
        t.pensize(branchLen/10)
        t.pendown()
        if branchLen > 20:
            t.pencolor("brown")
        else:
            t.pencolor("green")
        t.forward(branchLen)
        subLen = random.uniform(3,8)
        rAngle = random.uniform(10,20)
        t.right(rAngle)
        tree(branchLen - subLen, t)
        lAngle = random.uniform(1.5 * rAngle, 2.5*rAngle)
        t.left(lAngle)
        tree(branchLen - subLen, t)
        t.right(lAngle - rAngle)
        t.penup()
        t.backward(branchLen)



t = Turtle()
t.speed(500)
myWin = t.getscreen()
t.left(90)
t.up()
t.backward(300)
t.down()
tree(50, t)
myWin.exitonclick()
