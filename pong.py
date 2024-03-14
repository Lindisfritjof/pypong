# det her er et simpelt pong spil, der virker i Pyhton 3
# lavet efter en tutorial på FreeCodeCamp.orgs youtubekanal

import turtle
import os

wn = turtle.Screen()
wn.title("pong til Alva")
wn.bgcolor("lightblue")
wn.setup(width=800, height=600)
wn.tracer(0)

# score
score_a = 0
score_b = 0

# første bat
bat_a = turtle.Turtle()
bat_a.speed(0)
bat_a.shape("square")
bat_a.color("magenta")
bat_a.shapesize(stretch_wid=5, stretch_len=1)
bat_a.penup()
bat_a.goto(-350, 0)

# andet bat
bat_b = turtle.Turtle()
bat_b.speed(0)
bat_b.shape("square")
bat_b.color("blue")
bat_b.shapesize(stretch_wid=5, stretch_len=1)
bat_b.penup()
bat_b.goto(350, 0)

# boldens egenskaber/udseende
bold = turtle.Turtle()
bold.speed(0)
bold.shape("turtle")
bold.color("green")
bold.penup()
bold.goto(0 , 0)
bold.dx = 0.3
bold.dy = 0.3

# Pen (grafisk element, ligesom skilpadden)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Alva: 0 Far: 0", align="center", font=("Courier", 24, "normal"))


# funktionerne til spillet
# først bat a op
def bat_a_op():
    y = bat_a.ycor() # Denne funktion er fra Turtle-modulet og finder y koordinatet.
    y += 20 # tilføjer 20 px til y-koordinatet
    bat_a.sety(y)
    
#så bat a ned
def bat_a_ned():
    y = bat_a.ycor() # Denne funktion er fra Turtle-modulet og finder y koordinatet.
    y -= 20 # tilføjer 20 px til y-koordinatet
    bat_a.sety(y)

# først bat b op
def bat_b_op():
    y = bat_b.ycor() # Denne funktion er fra Turtle-modulet og finder y koordinatet.
    y += 20 # tilføjer 20 px til y-koordinatet
    bat_b.sety(y)
    
#så bat b ned
def bat_b_ned():
    y = bat_b.ycor() # Denne funktion er fra Turtle-modulet og finder y koordinatet.
    y -= 20 # tilføjer 20 px til y-koordinatet
    bat_b.sety(y)


# boldens egenskaber

# tastaturbindinger
wn.listen() # Det her fortæller den at den skal "lytte" efter tastaturinput
wn.onkeypress(bat_a_ned, "e")
wn.onkeypress(bat_a_op, "w")
wn.onkeypress(bat_b_ned, "o")
wn.onkeypress(bat_b_op, "i")

# hovedloop for spillet
while True:
    wn.update()

    #flyt bolden
    bold.setx(bold.xcor() + bold.dx)
    bold.sety(bold.ycor() + bold.dy)

    # hold rammen med bolden
    if bold.ycor() > 290:
        bold.sety(290)
        bold.dy *= -1
        os.system("aplay bounce.wav&")
        
    if bold.ycor() < -290:
        bold.sety(-290)
        bold.dy *= -1
        os.system("aplay bounce.wav&")

    if bold.xcor() > 390:
        bold.goto(0, 0)
        bold.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Alva: {score_a} Far: {score_b}", align="center", font=("Courier", 24, "normal"))
        os.system("aplay powerup.wav&")


    if bold.xcor() < -390:
        bold.goto(0, 0)
        bold.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Alva: {score_a} Far: {score_b}", align="center", font=("Courier", 24, "normal"))
        os.system("aplay powerup.wav&")

    # højre bat og bold kollision
    if (bold.xcor() > 340 and bold.xcor() < 350) and (bold.ycor() < bat_b.ycor() + 40 and bold.ycor() > bat_b.ycor() - 50):
        bold.setx(340)
        bold.dx *= -1
        os.system("aplay popbat.wav&")

     # venstre bat og bold kollision
    if (bold.xcor() < -340 and bold.xcor() < -35) and (bold.ycor() < bat_a.ycor() + 40 and bold.ycor() > bat_a.ycor() - 50):
        bold.setx(-340)
        bold.dx *= -1
        os.system("aplay popbat.wav&")

