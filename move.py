import turtle
from geometry import *

class Move:
    def moveRocket(rocketObject, maxCor):
        scale=rocketObject.scale
        rocketTop=rocketObject.rocketTop

        initialTopCoordinates=Point(0.374*scale, 105.456*scale)
        distanceBetweenStartingPointAndRocketTop=Point.countDistanceBetweenTwoPoints(Point(0,0), initialTopCoordinates)
        angle=rocketObject.rocketTurtle.heading()


        outside=False


        if rocketTop.x >= maxCor:
            rocketTop.x=maxCor
            outside=True
            
        if rocketTop.x <= -maxCor:
            rocketTop.x=-maxCor
            outside=True            

        if rocketTop.y >= maxCor:
            rocketTop.y=maxCor
            outside=True
        if rocketTop.y <= -maxCor:
            rocketTop.y=-maxCor
            outside=True
        
        if outside:
            newCoords=Distance.findCoordinatesByKnowingDistanceAndAngle(distanceBetweenStartingPointAndRocketTop, angle+180, rocketTop)
            rocketObject.rocketTurtle.setpos(newCoords.x, newCoords.y)
        
        rocketObject.rocketTurtle.forward(rocketObject.rocketTurtle.speed)

        

