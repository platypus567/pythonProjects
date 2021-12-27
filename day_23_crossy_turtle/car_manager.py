COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random
from turtle import Turtle


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.speed = STARTING_MOVE_DISTANCE
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1,stretch_len=random.randint(2,3))
            new_car.goto(x=300, y=random.randint(-250,250))
            new_car.setheading(180)
            self.all_cars.append(new_car)
    def move_forward(self):
        for car in self.all_cars:
            car.forward(self.speed)




