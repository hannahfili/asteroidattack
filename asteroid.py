import turtle
import random
import math
from helper import Helper
from geometry import Point
from geometry import LineEquation

class Asteroid:

    def __init__(self, radius, finished=False):
        self.initialStartingPoint=Asteroid.generateInitialStartingPoint()
        self.radius=radius
        self.initialCoordinates=Asteroid.generateAsteroidCoordinates(self.initialStartingPoint, self.radius)
        self.lineEquation=Asteroid.generateLineEquation(self)
        if self.initialStartingPoint.x>0:
            self.xDirection=-1
        else:
            self.xDirection=1
        self.currentStartingPoint=self.initialStartingPoint
        self.currentCoordinates=self.initialCoordinates
        self.finished=finished
        self.step=random.random()     
        if(radius>=50):
            kind="big"
        else:
            kind="small"
        self.kind=kind
        self.heading=None    
  
    def generateLineEquation(self):
        x=self.initialStartingPoint.x
        y=self.initialStartingPoint.y
        distancesToScreenTops=[Point(400,400,x, y), Point(-400, 400, x, y), Point(400, -400, x, y), Point(-400, -400, x, y)]
        
        distancesToScreenTops.sort(key=lambda point: point.distanceToCenter, reverse=True)
        furthestPoint=distancesToScreenTops[0]


        pointForLineEquation=Asteroid.findPointForLineEquation(furthestPoint)
        
        a=(y-pointForLineEquation.y)/(x-pointForLineEquation.x)
        b=y-a*x

        lineEquation=LineEquation(a,b)

        return lineEquation
    
    def findPointForLineEquation(furthestPoint):
        pointMinus400_400=Point(-400, 400)
        point400_400=Point(400,400)
        point400_Minus400=Point(400,-400)
        pointMinus400_Minus400=Point(-400,-400)

        pointForLine=Point(0,0)

        if furthestPoint==pointMinus400_400:
            pointForLine=Asteroid.chooseBetweenTwoLines(furthestPoint, Point(0, 400), Point(-400, 0))
        elif furthestPoint==point400_400:
            pointForLine=Asteroid.chooseBetweenTwoLines(furthestPoint, Point(0, 400), Point(400, 0))
        elif furthestPoint==point400_Minus400:
            pointForLine=Asteroid.chooseBetweenTwoLines(furthestPoint, Point(0, -400), Point(400, 0))
        elif furthestPoint==pointMinus400_Minus400:
            pointForLine=Asteroid.chooseBetweenTwoLines(furthestPoint, Point(-400, 0), Point(0, -400))
        

        
        return pointForLine
    

    def chooseBetweenTwoLines(furthestPoint, point1, point2):
        pointChosen=random.choice([point1, point2])

        pointForLine=Point(0,0)

        x1forRange=furthestPoint.x
        x2forRange=pointChosen.x

        y1forRange=furthestPoint.y
        y2forRange=pointChosen.y

        if x1forRange>x2forRange:
            pointForLine.x=random.randint(x2forRange, x1forRange)
        else:
            pointForLine.x=random.randint(x1forRange, x2forRange)
        if y1forRange>y2forRange:
            pointForLine.y=random.randint(y2forRange, y1forRange)
        else:
            pointForLine.y=random.randint(y1forRange, y2forRange)

        return pointForLine
    
    
    def generateAsteroidCoordinates(startingPoint, radius):

        coordinates=[]
        p0=Point(startingPoint.x, startingPoint.y+radius)
        p1=Point(startingPoint.x+0.5*radius, startingPoint.y+radius*math.sqrt(3)/2)
        p2=Point(startingPoint.x+radius*math.sqrt(3)/2, startingPoint.y+0.5*radius)
        p3=Point(startingPoint.x+radius, startingPoint.y)
        p4=Point(startingPoint.x+radius*math.sqrt(3)/2, startingPoint.y+(-0.5)*radius)
        p5=Point(startingPoint.x+0.5*radius, startingPoint.y+(radius*math.sqrt(3)/2)*(-1))
        p6=Point(startingPoint.x, startingPoint.y-radius)
        p7=Point(startingPoint.x-0.5*radius, startingPoint.y+(radius*math.sqrt(3)/2)*(-1))
        p8=Point(startingPoint.x+(radius*math.sqrt(3)/2)*(-1), startingPoint.y-0.5*radius)
        p9=Point(startingPoint.x-radius, startingPoint.y)
        p10=Point(startingPoint.x+(radius*math.sqrt(3)/2)*(-1), startingPoint.y+0.5*radius)
        p11=Point(startingPoint.x-0.5*radius, startingPoint.y+radius*math.sqrt(3)/2)

        coordinates.append(p0)
        coordinates.append(p1)
        coordinates.append(p2)
        coordinates.append(p3)
        coordinates.append(p4)
        coordinates.append(p5)
        coordinates.append(p6)
        coordinates.append(p7)
        coordinates.append(p8)
        coordinates.append(p9)
        coordinates.append(p10)
        coordinates.append(p11)
        coordinates.append(p0)

        return coordinates
    
    def generateInitialStartingPoint():
        xCoordOption1=random.randint(-1000, -410)
        xCoordOption2=random.randint(410, 1000)
        xChosen=random.choice([xCoordOption1, xCoordOption2])

        yCoordOption1=random.randint(-1000, -410)
        yCoordOption2=random.randint(410, 1000)
        yChosen=random.choice([yCoordOption1, yCoordOption2])

        startingPoint=Point(xChosen, yChosen)
        return startingPoint


    def drawAsteroid(self, asteroidTurtle, visibility, step=0, moving=False):
                
        # tops=12
        if moving:
            self.currentStartingPoint.x=self.currentStartingPoint.x+self.xDirection*step
            self.currentStartingPoint.y=self.lineEquation.a*self.currentStartingPoint.x+self.lineEquation.b
        
        self.currentCoordinates=Asteroid.generateAsteroidCoordinates(self.currentStartingPoint, self.radius)
        coordinates=self.currentCoordinates
        coordinatesLength=len(coordinates)

        allTopsOutOfScreen=False
        if self.currentStartingPoint.x+self.radius>=500 or self.currentStartingPoint.x-self.radius<=-500 or self.currentStartingPoint.y+self.radius>=500 or self.currentStartingPoint.y-self.radius<=-500:
            allTopsOutOfScreen=True
        
        # allTopsOutOfScreen = all(abs(coord.x)>=400 and abs(coord.y)>=400 for coord in coordinates)

        if self.kind=="big":
            if allTopsOutOfScreen and Helper.CheckOppositeSign(coordinates[0].x, self.initialCoordinates[0].x) and Helper.CheckOppositeSign(coordinates[0].y, self.initialCoordinates[0].y):
                asteroidTurtle.clear()
                self.finished=True
                return coordinates
        else:
            if allTopsOutOfScreen:
                asteroidTurtle.clear()
                self.finished=True
                return coordinates
        
        
        if allTopsOutOfScreen:
            asteroidTurtle.clear()
            return coordinates
        

        if visibility==1:
            asteroidTurtle.color("white")
        else:
            asteroidTurtle.color("black")
        asteroidTurtle.penup()
        asteroidTurtle.setpos(coordinates[0].x, coordinates[0].y)
        asteroidTurtle.pendown()

        for i in range(coordinatesLength):
            asteroidTurtle.goto(coordinates[i].x, coordinates[i].y)
        asteroidTurtle.penup()
        asteroidTurtle.setpos(self.initialStartingPoint.x, self.initialStartingPoint.y)
        asteroidTurtle.hideturtle()
        return coordinates


