import turtle
from geometry import Point
import math

class Rocket:
    def __init__(self, scale, rocketTurtle=None, initX=0, initY=0):
        self.initialStartingPoint=Point(initX, initY)
        self.radius=70*scale
        self.scale=scale
        self.rocketTurtle=rocketTurtle
        
        self.currentStartingPoint=Rocket.findCurrentStartingPoint(self)
        
        self.rocketTop=Rocket.findRocketTop(self)
        self.currentCenterPoint=Rocket.findCurrentCenterPoint(self)
    
    def drawLifePointers(lives, numberOfLives):
        if numberOfLives==0:
            for life in lives: life.hideturtle()

        if numberOfLives==5:
            for life in lives: life.showturtle()
        elif numberOfLives==4:
            lives[3].showturtle()
            lives[2].showturtle()
            lives[1].showturtle()
            lives[0].showturtle()
        elif numberOfLives==3:
            lives[2].showturtle()
            lives[1].showturtle()
            lives[0].showturtle()
        elif numberOfLives==2:
            lives[1].showturtle()
            lives[0].showturtle()
        elif numberOfLives==1:
            lives[0].showturtle()
    
    def setLifePointers(lives):
        for life in lives:
            life.color("green")
            life.shape("rocket2")
            life.hideturtle()
            life.penup()
            life.seth(90)
        lives[0].setpos(360,360)
        lives[1].setpos(330,360)
        lives[2].setpos(300,360)
        lives[3].setpos(270,360)
        lives[4].setpos(240,360)
      
   
    def findCurrentStartingPoint(self):
        if self.rocketTurtle!=None:
            return Point(self.rocketTurtle.xcor(), self.rocketTurtle.ycor())
        else: return None       


    def findRocketTop(self):
        if self.rocketTurtle!=None:
            initialTopCoordinates=Point(0.374*self.scale, 105.456*self.scale)
            distanceBetweenStartingPointAndRocketTop=Point.countDistanceBetweenTwoPoints(Point(0,0), initialTopCoordinates)
            angle=self.rocketTurtle.heading()
            topY=distanceBetweenStartingPointAndRocketTop*math.sin(math.radians(angle))+self.currentStartingPoint.y
            topX=distanceBetweenStartingPointAndRocketTop*math.cos(math.radians(angle))+self.currentStartingPoint.x
            return Point(topX, topY)
        else: return None
    
    def findCurrentCenterPoint(self):
        if self.rocketTurtle!=None:
            initialCenterCoordinates=Point(0.374*self.scale, 0.5*105.456*self.scale)
            distanceBetweenStartingPointAndRocketTop=Point.countDistanceBetweenTwoPoints(Point(0,0), initialCenterCoordinates)
            angle=self.rocketTurtle.heading()
            topY=distanceBetweenStartingPointAndRocketTop*math.sin(math.radians(angle))+self.currentStartingPoint.y
            topX=distanceBetweenStartingPointAndRocketTop*math.cos(math.radians(angle))+self.currentStartingPoint.x
            return Point(topX, topY)
        else: return None
    
    def createRocket(scale):
        pencil=turtle.Turtle()
        
        pencil.begin_poly()

        pencil.speed(0)

        pencil.forward(40*scale)
        pencil.left(90)
        pencil.forward(60*scale)
        pencil.penup()
        pencil.left(90)
        pencil.forward(40*scale)
        pencil.left(90)
        pencil.pendown()
        pencil.forward(60*scale)

        
        pencil.penup()
        pencil.setposition(0*scale,60*scale)
        pencil.setheading(90)
        pencil.pendown()
        pencil.circle(-45*scale, 57)
        pencil.penup()
        pencil.setpos(40*scale, 60*scale)
        pencil.pendown()
        pencil.setheading(90)
        
        pencil.circle(45*scale, 57)
        pencil.penup()

        pencil.setpos(20*scale,60*scale)
        pencil.pendown()
        pencil.setheading(0)
        pencil.circle(-10*scale)

        pencil.penup()
        pencil.setpos(0, 0)
        pencil.pendown()
        pencil.right(45)
        pencil.forward(14.1*scale)
        pencil.left(45)
        pencil.forward(20*scale)
        pencil.left(45)
        pencil.forward(14.1*scale)

        pencil.penup()
        pencil.setpos(0*scale, 40*scale)
        pencil.pendown()
        pencil.seth(0)
        pencil.right(117)
        pencil.forward(44.72*scale)
        pencil.seth(270)
        pencil.forward(20*scale)

        pencil.seth(0)
        pencil.left(57.5)
        pencil.forward(38.06*scale)

        pencil.penup()
        pencil.setpos(40*scale,40*scale)

        pencil.pendown()
        pencil.seth(0)
        pencil.right(90-27)
        pencil.forward(44.72*scale)
        pencil.seth(270)
        pencil.forward(20*scale)

        pencil.seth(180)
        pencil.right(57.5)
        pencil.forward(38.06*scale)

        pencil.end_poly()

        coord=pencil.get_poly()

        coord = (*coord, *coord[::-1])
        
        return coord
    
    def createRocket_2(scale):
        pencil=turtle.Turtle()

        # pencil.setposition(0,2000)
        pencil.speed(0)
        pencil.hideturtle()
        pencil.begin_poly()

        
        pencil.pencolor("white")
        

        
        pencil.setheading(-90)
        pencil.forward(20*scale)
        pencil.setheading(0)
        pencil.right(63)
        pencil.forward(44.72*scale)
        pencil.setheading(-90)
        pencil.forward(20*scale)
        pencil.seth(180)
        pencil.right(57.5)
        pencil.forward(38.06*scale)

        pencil.seth(-90)
        pencil.forward(10*scale)
        pencil.right(45)
        pencil.forward(14.1*scale)
        pencil.seth(180)
        pencil.forward(20*scale)
        pencil.right(45)
        pencil.forward(14.1*scale)
        pencil.seth(90)
        pencil.forward(10*scale)

        pencil.seth(180)
        pencil.left(57.5)
        pencil.forward(38.06*scale)
        pencil.seth(90)
        pencil.forward(20*scale)
        pencil.right(27)
        pencil.forward(44.72*scale)
        pencil.seth(90)
        pencil.forward(20*scale)

        pencil.setheading(90)
        pencil.circle(-45*scale, 57)
        pencil.setheading(-34.1)
        pencil.circle(-45*scale, 57)
        
        # pencil.penup()
        # pencil.seth(180)
        # pencil.forward(20*scale)
        # pencil.seth(-90)
        # pencil.forward(20*scale)
        # pencil.seth(0)
        # pencil.pendown()
        # pencil.circle(10*scale)

        



        pencil.end_poly()

        coord=pencil.get_poly()

        pencil.clear()
        return coord

    def createRocket_3(self, scale, visibility, initX=0, initY=0):
        pencil=turtle.Turtle()

        pencil.setposition(initX, initY)
        # pencil.speed(0)
        pencil.hideturtle()
        pencil.begin_poly()


        if visibility:
            pencil.pencolor("white")
        pencil.begin_fill()
        

        
        
        pencil.seth(180)
        pencil.forward(10*scale)
        pencil.right(45)
        pencil.forward(14.1*scale)
        pencil.seth(90)
        pencil.forward(10*scale)

        pencil.seth(180)
        pencil.left(57.5)
        pencil.forward(38.06*scale)
        pencil.seth(90)
        pencil.forward(20*scale)
        pencil.right(27)
        pencil.forward(44.72*scale)
        pencil.seth(90)
        pencil.forward(20*scale)

        pencil.setheading(90)
        pencil.circle(-45*scale, 57)
        # print("wspolrzedne wierzcholka:")
        # print(pencil.position())
        pencil.setheading(-34.1)
        pencil.circle(-45*scale, 57)
        
        pencil.setheading(-90)
        pencil.forward(20*scale)
        pencil.setheading(0)
        pencil.right(63)
        pencil.forward(44.72*scale)
        pencil.setheading(-90)
        pencil.forward(20*scale)
        pencil.seth(180)
        pencil.right(57.5)
        pencil.forward(38.06*scale)

        pencil.seth(-90)
        pencil.forward(10*scale)
        pencil.right(45)
        pencil.forward(13.6*scale)
        pencil.seth(180)
        pencil.forward(12*scale)


        pencil.end_poly()
        pencil.end_fill()

        

        coord=pencil.get_poly()
        coord = (*coord, *coord[::-1])

        pencil.clear()
        return coord