from turtle import Turtle
import random

COLORS = ["red", "blue", "brown", "orange", "green", "purple", "green"]
MOVING_DISTANCE = 5


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.move_speed = .075

    def move_cars(self):
        for car in self.cars:
            car.backward(MOVING_DISTANCE)

    def generate_car(self):
        random_chance = random.randint(1, 10)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-180, 200)
            new_car.goto(310, random_y)
            self.cars.append(new_car)

    def increase_level(self):
        for car in self.cars:
            car.goto(1000, 1000)
        self.cars.clear()
        self.move_speed *= .7

