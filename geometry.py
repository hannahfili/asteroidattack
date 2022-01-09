import math

class Point:
    
    def __init__(self, x, y, centerCoordX=0, centerCoordY=0):
        self.x=x
        self.y=y
        sum=math.pow((x-centerCoordX),2)+math.pow((y-centerCoordY),2)
        distance=math.sqrt(sum)
        self.distanceToCenter=distance
    
    def __eq__(self, other) : 
        return (self.x, self.y) == (other.x, other.y)
    
    def countDistanceBetweenTwoPoints(p1, p2):
        sum=math.pow((p1.x-p2.x),2)+math.pow((p1.y-p2.y),2)
        distance=math.sqrt(sum)
        return distance
    
    

class LineEquation:
    def __init__(self, a, b):
        self.a=a
        self.b=b


class Distance:
    def findCoordinatesByKnowingDistanceAndAngle(distance, angle, currentStartingPoint):
        Y=distance*math.sin(math.radians(angle))+currentStartingPoint.y
        X=distance*math.cos(math.radians(angle))+currentStartingPoint.x
        return Point(X, Y)