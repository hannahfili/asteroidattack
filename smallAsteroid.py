import turtle
from asteroid import Asteroid
from geometry import Point
import math
import copy

def generateSmallAsteroid(bigAsteroid, bulletObject, radius, opposite=False):
        newAsteroid=Asteroid(radius)
        newAsteroid.initialStartingPoint=copy.copy(bigAsteroid.currentStartingPoint)
        newAsteroid.initialCoordinates=Asteroid.generateAsteroidCoordinates(newAsteroid.initialStartingPoint, radius)

        bulletVector=turtle.Turtle()
        bulletVector.hideturtle()
        bulletVector.setpos(newAsteroid.initialStartingPoint.x, newAsteroid.initialStartingPoint.y)
        
        
        
        bulletVector.seth(bulletObject.bulletTurtle.heading())
        bulletVector.forward(bulletObject.step)

        

        headingFromLineEquation=math.degrees(math.atan(bigAsteroid.lineEquation.a))

        bulletVector.seth(headingFromLineEquation)
        bulletVector.forward(bigAsteroid.step)
        finalCoor=bulletVector.pos()
        finalCoor=Point(bulletVector.xcor(), bulletVector.ycor())

        bulletVector.setpos(newAsteroid.initialStartingPoint.x, newAsteroid.initialStartingPoint.y)
        bulletVector.goto(finalCoor.x, finalCoor.y)

        newAsteroid.lineEquation.a=math.tan(math.radians(bulletVector.heading()))
        

        if opposite:
                newAsteroid.lineEquation.a=newAsteroid.lineEquation.a*(-1)
        
        newAsteroid.lineEquation.b=finalCoor.y-newAsteroid.lineEquation.a*finalCoor.x

        if bulletVector.heading()>-90 and bulletVector.heading()<=90:
            newAsteroid.xDirection=1
        elif bulletVector.heading()>90 and bulletVector.heading()<=270:
            newAsteroid.xDirection=-1


        newAsteroid.currentStartingPoint=newAsteroid.initialStartingPoint
        newAsteroid.initialCoordinates=Asteroid.generateAsteroidCoordinates(newAsteroid.initialStartingPoint, newAsteroid.radius)

        newAsteroid.heading=bulletVector.heading()
        newAsteroid.step=bigAsteroid.step

        return newAsteroid


