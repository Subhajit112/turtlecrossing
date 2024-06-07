from turtle import Turtle

class total_score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(-250,250)
        self.scorelist = 0  
        self.update_scoreboard()
        self.hideturtle()
    def update_scoreboard(self):
        self.write(f"SCORE: {self.scorelist}", False, font=("Arial", 20, "normal"))

    def scoring(self):
         self.scorelist +=1
         self.clear()
         self.update_scoreboard()
    def gameover(self):
        self.penup()
        self.hideturtle()
        self.goto(0,0)
        self.color("black")  
        self.write("GAME OVER!", False, "center", font=("Arial", 25, "normal"))
        
