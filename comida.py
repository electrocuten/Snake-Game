from turtle import Turtle
import random


class Comida(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.color("blue")
        self.actualizar()

    def actualizar(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 250)
        self.goto(random_x, random_y)
