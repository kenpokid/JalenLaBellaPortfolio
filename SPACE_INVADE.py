import turtle
import os
import math
import random


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.tracer(0)

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 250) 
scorestring = "Score: {}".format(score)
score_pen.write(scorestring, False, align="left", font=("Roman", 20, "normal"))
score_pen.hideturtle()

player = turtle.Turtle()
player.color("green")
player.shape("square")
player.penup()
player.speed(0)
player.setposition(0 , -250)
player.setheading(90)

player.speed = 0

number_of_enemies = 30

enemies = []

for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

enemy_start_x = -225
enemy_start_y = 250
enemy_number = 0

for enemy in enemies:

    enemy.color("red")
    enemy.shape("triangle")
    enemy.penup()
    enemy.speed(0)
    x = enemy_start_x + (50 * enemy_number)
    y = enemy_start_y
    enemy.setposition(x, y)
    enemy.setheading(90)
    enemy_number += 1
    if enemy_number == 10:
        enemy_start_y -= 50
        enemy_number = 0

enemyspeed = .2

bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("circle")
bullet.penup()
bullet.speed()
bullet.setheading(90)
bullet.shapesize (1, 1)
bullet.hideturtle()

bulletspeed= 5

bulletstate = "ready"

def move_left():
    player.speed = -1

def move_right():
    player.speed = 1

def move_player():
    x = player.xcor()
    x += player.speed
    if x < -280:
        x = -280
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"

        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()

def isCollsion(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 25:
        return True
    else:
        return False

turtle.listen()
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(fire_bullet, "space")

while True:

    wn.update()
    move_player()

    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if isCollsion(bullet, enemy):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)

            enemy.setposition(0, 5000)

            score += 50
            scorestring = "Score: {}".format(score)
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Roman", 20, "normal"))

            

        if isCollsion(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break
    
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if bullet .ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"