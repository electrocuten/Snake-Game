from turtle import Turtle

CENTRADO = "center"
FUENTE = ("Courier", 24, "normal")

class Marcador(Turtle):

    def __init__(self):
        super().__init__()
        self.puntos = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.actualizar_marcador()

    def actualizar_marcador(self):
        self.write(f"PUNTOS: {self.puntos}", move=False, align=CENTRADO, font=FUENTE)

    def sumar_puntos(self):

        self.puntos += 1
        self.clear()
        self.actualizar_marcador()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align=CENTRADO, font=FUENTE)