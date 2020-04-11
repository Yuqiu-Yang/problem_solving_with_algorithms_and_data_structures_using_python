from turtle import *
import random

def drawTriangle(points, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1])
    myTurtle.goto(points[2])
    myTurtle.goto(points[0])
    myTurtle.end_fill()


def getRandomMid(p1, p2, p3):
    r_x = random.uniform(-(p1[0] + p2[0] + p3[0])/3, \
                        (p1[0] + p2[0] + p3[0])/3)
    r_y = random.uniform(-(p1[1] + p2[1] + p3[0])/3,\
                        (p1[1] + p2[1] + p3[0])/3)

    return ((p1[0] + p2[0] + p3[0])/3 + r_x, (p1[1] + p2[1] + p3[1])/3 + r_y)

def fractalMountain3d(points, degree, myTurtle):
    colorMap = ["blue","red","green","white",\
                "yellow","violet","orange"]
    drawTriangle(points,colorMap[random.randint(0,len(colorMap)-1)], \
                myTurtle)
    if degree > 0:
        midPt = getRandomMid(points[0], points[1], points[2])
        fractalMountain3d([points[0],points[1], midPt],degree - 1,myTurtle)
        fractalMountain3d([midPt, points[1],points[2]],degree - 1,myTurtle)
        fractalMountain3d([points[0],midPt,points[2]],degree - 1,myTurtle)






myTurtle = Turtle()
myTurtle.speed(1000)
myWin = myTurtle.getscreen()
fractalMountain3d([(-300,-150),(0,300),(300,-150)], \
4, myTurtle)

myWin.exitonclick()
