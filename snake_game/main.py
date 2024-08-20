from turtle import Screen
from snake_1 import Snake
from food_1 import Food
from board import Board
import time


sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("green")
sc.title("Snake Game")
sc.tracer(0)

s = Snake()
f = Food()
b = Board()

sc.listen()
sc.onkey(s.right, "d")
sc.onkey(s.left, "a")
sc.onkey(s.up, "w")
sc.onkey(s.down, "s")

game_is_on = True
while game_is_on:
    sc.update()
    time.sleep(0.1)
    s.move()

    if s.head.distance(f) < 15:
        f.refresh()
        b.update_score()
        s.extend()

    if s.head.xcor() > 280 or s.head.xcor() < -280 or s.head.ycor() > 280 or s.head.ycor() < -280:
        game_is_on = False
        b.game_over()

    for segment in s.segments:
        if segment == s.head:
            pass
        elif s.head.distance(segment) < 10:
            game_is_on = False
            b.game_over()

sc.exitonclick()