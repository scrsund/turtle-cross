from turtle import Turtle

ALIGNMENT = 'center'
FONT= ('Courier', 25, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.level = 1
        self.write(f'LEVEL: {self.level}', align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f'LEVEL: {self.level}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align=ALIGNMENT, font=FONT)
