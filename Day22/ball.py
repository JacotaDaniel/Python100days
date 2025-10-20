from turtle import Turtle, Screen

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x , new_y)

    def bounce(self, wall_bounce, paddle_bounce):
        if wall_bounce == 1 and paddle_bounce == 0 :
            new_y_move = self.y_move * -1
            self.y_move = new_y_move
            wall_bounce = new_y_move

        elif wall_bounce == 0 and paddle_bounce == 1:
            new_x_move = self.x_move * -1
            self.x_move = new_x_move
            paddle_bounce = new_x_move

        else:
            print("Chose one!")