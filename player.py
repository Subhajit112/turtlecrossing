from turtle import Turtle

class players(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(0,-280)

    def forward(self):
        newy=self.ycor()+10
        self.goto(0,newy)
    
