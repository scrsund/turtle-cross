from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)


player = Player()
car = Car()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")


game_is_on = True

while game_is_on:
    time.sleep(car.move_speed)
    screen.update()

    car.generate_car()
    car.move_cars()

    for i in car.cars:
        if player.distance(i) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        scoreboard.increase_level()
        player.go_to_start()
        car.increase_level()





screen.exitonclick()


#cars moving
#levels with increasing speed of cars
