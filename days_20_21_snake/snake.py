from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)
    def add_segment(self,pos):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(pos)
        self.segments.append(new_segment)


    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x,y=new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def hit_wall(self):
        if self.head.xcor() > 307 or self.head.xcor() < -307 or self.head.ycor() > 309 or self.head.ycor() < -309:
            return True
