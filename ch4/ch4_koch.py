from turtle import *
import math
def drawSnowflakeEdge(points,color,  myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1])
    myTurtle.goto(points[2])
    myTurtle.goto(points[3])
    myTurtle.goto(points[4])
    myTurtle.goto(points[1])
    myTurtle.goto(points[5])
    myTurtle.end_fill()

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
def getThirds(p1,p2):
    return [((2*p1[0]/3 + p2[0]/3), (2*p1[1]/3 + p2[1]/3)), \
            ((p1[0]/3 + 2*p2[0]/3), (p1[1]/3 + 2*p2[1]/3))]

def getTops(p1, p2):
    midP = ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)
    vP = (p1[0] - p2[0], p1[1]-p2[1])
    norm_vP = norm(vP)
    pVP = ((vP[1])/norm_vP, (-1 * vP[0])/norm_vP)
    dis = (math.sqrt(3))/6 * norm_vP
    top1 = (midP[0] + dis * (pVP[0]), midP[1] + dis * (pVP[1]))
    top2 = (midP[0] - dis * (pVP[0]), midP[1] - dis * (pVP[1]))
    return top1, top2


def norm(p):
    return math.sqrt((p[0])**2 + (p[1])**2)

def kochSnowflake(points, degree, myTurtle,color):
    pt = [points[0], points[1]]
    pt3th = getThirds(pt[0], pt[1])
    pttops = getTops(pt[0], pt[1])
    snowpts = [pt[0],pt3th[0],pttops[0], pt3th[1],pttops[1],pt[1]]
    drawSnowflakeEdge(snowpts, color, myTurtle)
    if degree > 0:
        kochSnowflake([pt[0], pt3th[0]], degree - 1, myTurtle, color)
        kochSnowflake([pt3th[0], pttops[0]], degree - 1, myTurtle, color)
        kochSnowflake([pttops[0], pt3th[1]], degree - 1, myTurtle, color)
        kochSnowflake([pt3th[0], pttops[1]], degree - 1, myTurtle, color)
        kochSnowflake([pttops[1], pt3th[1]], degree - 1, myTurtle, color)
        kochSnowflake([pt3th[1], pt[1]], degree - 1, myTurtle, color)


color = "purple"
degree = 3
myTurtle = Turtle()
myTurtle.pencolor(color)
myTurtle.speed(1000)
myWin = myTurtle.getscreen()

pt = [(-300,-150),(0,300*(math.sqrt(3))-150),(300,-150)]


kochSnowflake([pt[0], pt[1]], degree, myTurtle, color)
kochSnowflake([pt[1], pt[2]], degree, myTurtle, color)
kochSnowflake([pt[2], pt[0]], degree, myTurtle, color)
drawTriangle(pt, color, myTurtle)

myWin.exitonclick()
