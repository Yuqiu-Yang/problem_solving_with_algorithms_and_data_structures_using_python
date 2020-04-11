from turtle import *
import random
def drawTriangle(points, color, myTurtle, draw = True):
    if draw:
        myTurtle.fillcolor(color)
        myTurtle.up()
        myTurtle.goto(points[0])
        myTurtle.down()
        myTurtle.begin_fill()
        myTurtle.goto(points[1])
        myTurtle.goto(points[2])
        myTurtle.goto(points[0])
        myTurtle.end_fill()
    else:
        myTurtle.up()
        myTurtle.goto(points[0])
        myTurtle.goto(points[1])
        myTurtle.goto(points[2])
        myTurtle.goto(points[0])


def getRandomMid(p1, p2):
    r_x = random.uniform(-(p1[0] + p2[0])/20, (p1[0] + p2[0])/20)
    r_y = random.uniform(-(p1[1] + p2[1])/20, (p1[1] + p2[1])/20)
    return ((p1[0] + p2[0])/2 + r_x, (p1[1] + p2[1])/2 + r_y)


def fractalMountain2d(points, degree, myTurtle):
    colorMap = ["blue","red","green","white",\
                "yellow","violet","orange"]
    if degree <= 2:
        drawTriangle(points,colorMap[random.randint(0,len(colorMap)-1)], \
                    myTurtle, draw = (random.random() >= 0.3))
    else:
        drawTriangle(points,colorMap[degree % len(colorMap)], \
                    myTurtle, draw = False)

    if degree > 0:
        newPoints = [getRandomMid(points[0], points[1]),\
                        getRandomMid(points[1], points[2]),\
                        getRandomMid(points[2], points[0])]
        fractalMountain2d([points[0],\
                            newPoints[0],\
                            newPoints[2]],\
                            degree - 1,\
                            myTurtle)
        fractalMountain2d([newPoints[0],\
                            points[1],\
                            newPoints[1]],\
                            degree - 1,\
                            myTurtle)
        fractalMountain2d([newPoints[2],\
                            newPoints[1],\
                            points[2]],\
                            degree - 1,\
                            myTurtle)
        fractalMountain2d([newPoints[0],\
                            newPoints[1],\
                            newPoints[2]],\
                            degree - 1,
                            myTurtle)




myTurtle = Turtle()
myTurtle.speed(1000)
myWin = myTurtle.getscreen()
fractalMountain2d([(-300,-150),(0,300),(300,-150)], \
4, myTurtle)

myWin.exitonclick()
