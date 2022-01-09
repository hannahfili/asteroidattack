import turtle
from geometry import Point
import math


class Helper:
    def CheckOppositeSign(a, b):
        if a*b>0: return False
        else: return True
    
    def CheckIfAnyCoordIsInsideGameWindow(coordinates):
        resX = True in (coord.x >=-400 and coord.x<= 400 for coord in coordinates)
        resY= True in (coord.y >=-400 and coord.y<= 400 for coord in coordinates)
        if resX and resY:
            return True
        else:
            return False
    
    def checkIfAsteroidCentreIsInsideGameWindow(asteroid):
        if asteroid.currentStartingPoint.x>=-400 and asteroid.currentStartingPoint.x<=400 and asteroid.currentStartingPoint.y>=-400 and asteroid.currentStartingPoint.y<=400:
            return True
        return False
    
    def checkCollision(object1, object2, minDistance):
        if Point.countDistanceBetweenTwoPoints(object1, object2)<=minDistance:
            return True
        return False
    
    def checkIfBulletIsOutsideGameWindow(bulletPoint):
        if bulletPoint.currentMovingPoint.x>=-400 and bulletPoint.currentMovingPoint.x<=400 and bulletPoint.currentMovingPoint.y>=-400 and bulletPoint.currentMovingPoint.y<=400:
            return False
        return True
    
    def setPointsLabel(pointsLabel):
        pointsLabel.penup()
        pointsLabel.setposition(-390,360)
        pointsLabel.color("white")
        text="POINTS: 0"
        pointsLabel.write(text, False, align="left", font=("Courier New", 15, "normal"))
        pointsLabel.hideturtle()
        

    
    def drawPoints(points, pointsLabel):
        pointsLabel.clear()
        text="POINTS: {}".format(points)
        pointsLabel.write(text, False, align="left", font=("Courier New", 15, "normal"))
        pointsLabel.hideturtle()

        