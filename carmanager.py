from turtle import Turtle
import random
Colors=["red","blue","orange","yellow","green","purple"]
Move_cars=5
class cars(Turtle):
    def __init__(self):
        self.allcar=[]
        self.movingcars=Move_cars

    def create_car(self):  
        randomnumeber= random.randint(1,8)
        if randomnumeber ==1:
            new_car=Turtle()  
            new_car.shape("square")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random.choice(Colors))
            random_y=random.randint(-250, 250)
            new_car.goto(280,random_y)
            self.allcar.append(new_car)
    
    def move_car(self):
        for i in self.allcar:
            i.backward(self.movingcars)

    def move_faster(self):
        self.movingcars= self.movingcars+Move_cars

           


