from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Board(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        self.write(f" Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER!", align="center", font=FONT)
        self.goto(0, -30)
        self.write(f" Your score is {self.score}", align="center", font=FONT)
