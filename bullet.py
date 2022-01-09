import turtle
from geometry import *

class Bullet:

    def __init__(self, rocketObject, bulletTurtle, step, state="ready"):
        self.initialStartingPoint=Point(rocketObject.rocketTop.x, rocketObject.rocketTop.y)
        self.bulletTurtle=bulletTurtle
        self.bulletTurtle.seth(rocketObject.rocketTurtle.heading())
        self.currentStartingPoint=Point(rocketObject.rocketTop.x, rocketObject.rocketTop.y)
        self.step=step
        self.state=state
        self.rocketObject=rocketObject
        self.currentMovingPoint=Bullet.findCurrentMovingPoint(self)
    
    def setPosition(self):
        self.bulletTurtle.setpos(self.currentStartingPoint.x, self.currentStartingPoint.y)
    
    def showTurtle(self):
        self.bulletTurtle.showTurtle()
    
    def findCurrentStartingPoint(self):
        self.currentStartingPoint=Point(self.rocketObject.rocketTop.x, self.rocketObject.rocketTop.y)
    
    def findCurrentMovingPoint(self):
        self.currentMovingPoint=Point(self.bulletTurtle.xcor(), self.bulletTurtle.ycor())
     
