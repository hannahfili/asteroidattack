import turtle
from smallAsteroid import *
from asteroid import Asteroid
from asteroid import Point
from background import Background
from bullet import Bullet
from helper import Helper
from rocket import Rocket
from move import Move
import time
import winsound
import math

gameWindow=Background.createWindow()

winsound.PlaySound("rocket-preparing.wav", winsound.SND_ASYNC)
initialText=Background.specialText("ROCKET PREPARING...", 0, 60)
gameWindow.tracer(1)
# gameWindow.tracer(0)
rocketObject=Rocket(0.25)
rocketCoord=rocketObject.createRocket_3(rocketObject.scale, 1)

initialText.clear()
gameWindow.tracer(0)
rocketCoord2=Rocket.createRocket_2(0.3)

gameWindow.register_shape("rocket", rocketCoord)
gameWindow.register_shape("rocket2", rocketCoord2)


rocket=turtle.Turtle()
rocketObject.rocketTurtle=rocket

rocketObject.currentStartingPoint=Rocket.findCurrentStartingPoint(rocketObject)
rocketObject.rocketTop=Rocket.findRocketTop(rocketObject)


rocket.penup()
rocket.seth(135)
rocket.shape("rocket")
rocket.color("#E1D9D8", "#E1D9D8")
minSpeed=0.1
maxSpeed=2
rocket.speed=minSpeed

def setHeadingAnglePositive():
    actualHeading=rocket.heading()
    headingAngle=10
    rocket.setheading(actualHeading+headingAngle)

def setHeadingAngleNegative():
    actualHeading=rocket.heading()
    headingAngle=-10
    rocket.setheading(actualHeading+headingAngle)

def speedUp():
    rocket.speed=rocket.speed+0.1
    if rocket.speed>maxSpeed: rocket.speed=maxSpeed

def speedDown():
    rocket.speed=rocket.speed-0.1
    if rocket.speed<minSpeed: rocket.speed=minSpeed

bulletTurtle=turtle.Turtle()
bulletObject=Bullet(rocketObject, bulletTurtle, step=3)
bulletObject.bulletTurtle.penup()
bulletObject.bulletTurtle.hideturtle()



def shoot():
    if bulletObject.state=="ready":
        winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
        bulletObject.findCurrentStartingPoint()
        bulletObject.bulletTurtle.seth(bulletObject.rocketObject.rocketTurtle.heading())
        bulletObject.state = "moving"
        bulletObject.bulletTurtle.clear()

        bulletObject.setPosition()
        bulletTurtle.color("white")
        bulletTurtle.showturtle()


visibility=1
radius=50

numberOfAsteroids=10
asteroids=[]
for i in range(numberOfAsteroids):
    asteroids.append(Asteroid(radius))

asteroidTurtles=[]
for i in range(numberOfAsteroids):
    asteroidTurtles.append(turtle.Turtle())

numberOfAsteroidsInGameWindow=0
n=10
startOfGame=time.process_time()
numberOfLives=5
points=0




lives=[turtle.Turtle(), turtle.Turtle(), turtle.Turtle(),turtle.Turtle(), turtle.Turtle()]
Rocket.setLifePointers(lives)
redstart=time.process_time()
pointsLabel=turtle.Turtle()
pointsLabel.hideturtle()
Helper.setPointsLabel(pointsLabel)
bulletObject.currentStartingPoint=Point(10000,10000)
bulletObject.currentMovingPoint=Point(10000,10000)
bulletObject.bulletTurtle.setpos(bulletObject.currentStartingPoint.x, bulletObject.currentStartingPoint.y)


while True:
    if numberOfLives==0:
        gameWindow.update()
        Rocket.drawLifePointers(lives, numberOfLives)
        winsound.PlaySound(None, winsound.SND_PURGE)
        winsound.PlaySound("game-over.wav", winsound.SND_ASYNC)
        Background.specialText("GAME OVER", 0, 35, "red", 50, 0.2)
        break
    
    
    Rocket.drawLifePointers(lives, numberOfLives)
    
    

    if bulletObject.state=="moving":
        bulletObject.bulletTurtle.forward(bulletObject.step)

    bulletObject.findCurrentStartingPoint()
    bulletObject.findCurrentMovingPoint()

    rocketObject.currentStartingPoint=Rocket.findCurrentStartingPoint(rocketObject)
    rocketObject.rocketTop=Rocket.findRocketTop(rocketObject)
    rocketObject.currentCenterPoint=Rocket.findCurrentCenterPoint(rocketObject)

    if Helper.checkIfBulletIsOutsideGameWindow(bulletObject):
        bulletObject.bulletTurtle.clear()
        bulletObject.state="ready"

    
    numberOfAsteroidsInGameWindow=0
    for i in asteroidTurtles:
        i.clear()
    
    for i in range(numberOfAsteroids):
        
        
        
        # check collision between rocket and asteroid
        if Helper.checkCollision(rocketObject.currentCenterPoint, asteroids[i].currentStartingPoint, 70*rocketObject.scale+asteroids[i].radius):
            winsound.PlaySound("collision.wav", winsound.SND_ASYNC)
            rocket.color("red")
            asteroids[i].finished=True
            numberOfLives-=1
            redstart=time.process_time()
            
        
        
        # check collision between bullet and asteroid

        if Helper.checkCollision(bulletObject.currentMovingPoint, asteroids[i].currentStartingPoint, asteroids[i].radius):
            
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            bulletObject.bulletTurtle.hideturtle()
            bulletObject.state="ready"
            bulletObject.bulletTurtle.setpos(1000000, 1000000)
            asteroids[i].finished=True
            
            if asteroids[i].kind=="big":
                newAsteroid=generateSmallAsteroid(asteroids[i], bulletObject, 20)
                asteroids.append(newAsteroid)                
                asteroidTurtles.append(turtle.Turtle())
                numberOfAsteroids+=1

                newAsteroid2=generateSmallAsteroid(asteroids[i], bulletObject, 20, True)
                asteroids.append(newAsteroid2)                
                asteroidTurtles.append(turtle.Turtle())
                numberOfAsteroids+=1
            else:
                points+=10
                Helper.drawPoints(points, pointsLabel)
                
            
    for i in range(numberOfAsteroids):
        if Helper.checkIfAsteroidCentreIsInsideGameWindow(asteroids[i]):
            numberOfAsteroidsInGameWindow+=1
    
    if (time.process_time()-startOfGame)>=n:
        n+=3
        if numberOfAsteroidsInGameWindow<8:
            
            asteroidTurtles.append(turtle.Turtle())
            asteroids.append(Asteroid(radius))
            numberOfAsteroids+=1
            


    for asteroid, asteroidTurtle in zip(list(asteroids), list(asteroidTurtles)):
        if asteroid.finished:            
            asteroids.remove(asteroid)
            asteroidTurtles.remove(asteroidTurtle)
            numberOfAsteroids-=1
            
        else:
            step=asteroid.step
            asteroid.drawAsteroid(visibility=1, asteroidTurtle=asteroidTurtle, step=step, moving=True)

    

    gameWindow.update()
    gameWindow.onkeypress(setHeadingAnglePositive, "Left")
    gameWindow.onkeypress(setHeadingAngleNegative, "Right")
    gameWindow.onkeypress(speedUp, "Up")
    gameWindow.onkeypress(speedDown, "z")

    if rocket.pencolor()=="red" and time.process_time()-redstart>1:
        rocket.color("white")
    bulletObject.bulletTurtle.color("white")
    
    Move.moveRocket(rocketObject, 390)
    
    gameWindow.listen()
    gameWindow.onkeypress(shoot,"space")
    for life in lives: life.hideturtle()  
    
    
    
    



gameWindow.mainloop()