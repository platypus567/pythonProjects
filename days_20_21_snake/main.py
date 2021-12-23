from turtle import Turtle, Screen
screen = Screen()
screen.setup(width=640,height=640)
screen.bgcolor("black")
screen.title("Snake Game")
starting_positions = [(0,0),(-20,0),(-40,0)]
segments = []
for pos in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.penup()
    new_segment.color('white')
    new_segment.goto(pos)
    segments.append(new_segment)
game_is_on = True
while game_is_on == True:
    for segment in segments:
        segment.forward(20)











screen.exitonclick()
