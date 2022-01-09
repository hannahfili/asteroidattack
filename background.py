import turtle
import time

class Background:

    def createWindow():
        gameWindow=turtle.Screen()
        gameWindow.setup(800,800)
        gameWindow._root.resizable(False, False) 
        
        gameWindow.title("Asteroid attack")
        gameWindow.bgcolor("black")

        gameBoarder=turtle.Turtle()
        gameBoarder.speed(0)
        gameBoarder.pensize(3)
        gameBoarder.pencolor("white")



        gameBoarder.penup()
        gameBoarder.setposition(-400,-400)
        gameBoarder.pendown()

        for i in range(4):
            gameBoarder.forward(800)
            gameBoarder.left(90)

        gameBoarder.hideturtle()
        
        
        return gameWindow
    
    def specialText(text, posX, posY, color="white", fontSize=30, sleep=0.1):
        initialText=turtle.Turtle()
        initialText.hideturtle()
        initialText.setposition(posX,posY)
        initialText.color(color)
        index=0
        for i in range(len(text)+1):
            initialText.clear()
            initialText.write(text[:index], False, align="center", font=("Courier New", fontSize, "normal"))
            index+=1
            time.sleep(sleep)
        
        return initialText
    
