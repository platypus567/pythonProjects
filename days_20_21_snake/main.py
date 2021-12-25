from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=640,height=640)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

food = Food()
scoreboard = Scoreboard()
game_over = Turtle()
game_over.hideturtle()
game_over.penup()
game_over.color("white")
game_is_on = True

def hit_food():
    if snake.head.distance(food) < 15:
        food.move()
        scoreboard.increase_score()
        snake.extend()
while game_is_on == True:

    if snake.hit_wall() == True:
        game_over.write("Game Over.", align="center", font=("Arial",20,"normal"))
        game_is_on = False
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            game_over.write("Game Over.", align="center", font=("Arial", 20, "normal"))
    hit_food()
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
