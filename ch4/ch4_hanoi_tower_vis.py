from turtle import *

class hanoi_tower:
    def __init__(self,n, baseTurtle, baseWin,palette = []):
        if palette == []:
            palette.append("blue")
        self.palette = palette
        self.num_disks = n
        self.t = baseTurtle
        self.wn = baseWin
        self.wn.setworldcoordinates(-800, 0, 800, 800)
        self.t_list = [Turtle() for i in range(n)]
        for i in range(n):
            (self.t_list[i]).up()
            (self.t_list[i]).shape("square")
            (self.t_list[i]).shapesize(stretch_wid = 1, stretch_len = (i+1))
            (self.t_list[i]).color(self.palette[i%(len(self.palette))])
        for i in range(n):
            self.t_list[i].goto(-400,55 + 400 - (400/n)*(i+1))

    def drawTower(self):
        self.t.speed("fastest")
        self.drawCenteredBox(-800,50,800,0,"silver")
        self.drawCenteredBox(-410,800,-390,50,"silver")
        self.drawCenteredBox(-10,800,10,50,"silver")
        self.drawCenteredBox(390,800,410,50,"silver")
        self.t.hideturtle()
        self.wn.update()
    def drawCenteredBox(self,tlx,tly,brx, bry, color):
        self.t.up()
        self.t.goto(tlx, tly)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.down()
        self.t.begin_fill()
        self.t.forward(brx-tlx)
        self.t.right(90)
        self.t.forward(tly-bry)
        self.t.right(90)
        self.t.forward(brx-tlx)
        self.t.right(90)
        self.t.forward(tly-bry)
        self.t.right(90)
        self.t.end_fill()

def moveTowerVis(n, fromPole, toPole, withPole, tower):
    if n >= 1:
        moveTowerVis(n - 1, fromPole, withPole, toPole, tower)
        moveDiskVis(fromPole, toPole, tower)
        moveTowerVis(n - 1, withPole, toPole, fromPole, tower)

def moveDiskVis(fp, tp, tower):
    target_disk = -1
    fp_h = 0
    tp_h = 0
    for i in range(tower.num_disks):
        current_pos = (tower.t_list[i]).pos()
        if current_pos[0] == fp:
            if target_disk == -1:
                target_disk = i
            if current_pos[1] > fp_h:
                fp_h = current_pos[1]
        elif current_pos[0] == tp:
            if current_pos[1] > tp_h:
                tp_h = current_pos[1]
        else:
            continue
    (tower.t_list[target_disk]).goto(tp,tp_h + 400/(tower.num_disks))


myTurtle = Turtle()
myWin = myTurtle.getscreen()
n = 10
tower = hanoi_tower(n,myTurtle, myWin)
tower.drawTower()
moveTowerVis(n, -400, 400, 0, tower)

myWin.exitonclick()
