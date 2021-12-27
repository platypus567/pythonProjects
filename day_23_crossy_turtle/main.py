import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
player = Player()
game_is_on = True
screen.listen()
screen.onkey(player.go_up,"Up")
car_manager = CarManager()
while game_is_on:
    if player.ycor() >= 280:
        player.reset_pos()
        scoreboard.level_up()
        car_manager.speed += 5
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    car_manager.move_forward()
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()

screen.exitonclick()