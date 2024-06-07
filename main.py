from turtle import Screen
from player import players
from carmanager import cars
from scoreboard import total_score
import time
screen=Screen()
screen.title("turtle vs car")
screen.bgcolor("white")
screen.setup(600,600)
screen.tracer(0)
obj=players()
car=cars()
score = total_score()

screen.listen()
screen.onkey(obj.forward,"Up")

game=True
while game:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()
    for m in car.allcar:
        if obj.distance(m)<20:
            score.gameover()
            game = False
    if obj.ycor() > 280:
        obj.goto(0,-280)
        car.move_faster()
        score.scoring()

screen.exitonclick()
