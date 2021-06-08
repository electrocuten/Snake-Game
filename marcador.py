from turtle import Turtle

CENTRADO = "center"
FUENTE = ("Courier", 24, "normal")

class Marcador(Turtle):

    def __init__(self):
        super().__init__()
        self.puntos = 0
        # De esta forma podemos abrir un fichero externo
        with open("memoria.txt") as memoria:
            puntos_fichero = memoria.read()
        if str(puntos_fichero) == "":
            self.puntuacion_alta = 0
        else:
            self.puntuacion_alta = int(puntos_fichero)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.actualizar_marcador()

    def actualizar_marcador(self):
        self.clear()
        self.write(f"PUNTOS: {self.puntos} RECORD: {self.puntuacion_alta}", move=False, align=CENTRADO, font=FUENTE)

    def sumar_puntos(self):

        self.puntos += 1
        self.actualizar_marcador()

    def reset(self):
        if self.puntos > self.puntuacion_alta:
            self.puntuacion_alta = self.puntos
            # El fichero podemos abrirlo como lectura (r), escritura (w) (se sobreescribe el texto por el nuevo)
            # o para añadir (a), donde se añade a lo anterior lo nuevo.
            with open("memoria.txt", mode="w") as memoria:
                memoria.write(str(self.puntuacion_alta))

        self.puntos = 0
        self.actualizar_marcador()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", move=False, align=CENTRADO, font=FUENTE)