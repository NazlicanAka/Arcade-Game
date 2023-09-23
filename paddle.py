from turtle import Turtle

STARTING_POS = (350, 0)
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
STRETCH_WID = 5
STRETCH_LEN = 1


class Paddle(Turtle):

    def __init__(self, starting_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=STRETCH_WID, stretch_len=STRETCH_LEN)
        self.speed("fastest")
        self.penup()
        self.goto(starting_pos)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


