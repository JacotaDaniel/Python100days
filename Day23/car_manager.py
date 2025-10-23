import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        # self.hideturtle()
        self.shape("square")
        self.shapesize(1,2)
        self.penup()
        self.new_y = random.randrange(-250, 250, 25)
        self.goto(310,self.new_y)
        self.all_cars = []
        self.car_spd = MOVE_INCREMENT

    def move(self):
        new_x = self.xcor() - self.car_spd

        if new_x < -310:
            self.setx(-320)
            self.hideturtle()


        else:
            # Move the car by the regular step
            self.setx(new_x)

        # Optional: Keep the print statement for debugging
        print(self.xcor())














