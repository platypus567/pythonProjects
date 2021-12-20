from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
def move_forward():
    tim.forward(10)
def move_backward():
    tim.back(10)
def counterclock():
    tim.left(15)
def clock():
    tim.right(15)

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counterclock)
screen.onkey(key="d", fun=clock)
screen.exitonclick()
