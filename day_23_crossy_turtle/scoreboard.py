FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(x=-230,y=260)
        self.write_score()
    def write_score(self):
        self.write(f"Level:{self.level}",False,"center", FONT)
    def level_up(self):
        self.level += 1
        self.clear()
        self.write_score()
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over.",False,"center",FONT)


