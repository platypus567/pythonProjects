from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.update_score()
    def update_score(self):
        self.clear()
        self.goto(-50, 200)
        self.write(self.l_score, False, "center", ("Courier", 80, "normal"))
        self.goto(50, 200)
        self.write(self.r_score, False, "center", ("Courier", 80, "normal"))
    def l_point(self):
        self.l_score += 1
        self.update_score()
    def r_point(self):
        self.r_score += 1
        self.update_score()


