from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def next_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_ended(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)