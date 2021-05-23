from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]        # Posiciones inicales de la serpiente. Una tupla por segmento
DISTANCIA_DE_PASO = 20                                  # Distancia que recorre la serpiente en cada movimiento
UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270


class Snake:
    """ La clase serpiente crea una serpiente formada con 3 segmentos. Dicha serpiente puede moverse por la pantalla """
    def __init__(self):
        self.cuerpo = []
        self.crear_serpiente()
        self.cabeza = self.cuerpo[0]

    def crear_serpiente(self):
        # Creamos una serpiente con 3 segmentos y los colocamos en las posiciones inicales.
        for position in STARTING_POSITION:
           self.añadir_cuadrado(position)

    def añadir_cuadrado(self, posicion):
        # Crea un nuevo cuadrado para la serpiente, blanco, con el pincel levantado y en la posicion indicada
        square = Turtle(shape="square")
        square.color("white")
        square.penup()
        square.goto(posicion)
        self.cuerpo.append(square)

    def crecer(self):
        # Añade un nuevo cuadrado a la serpiente, en la posicion de la ultima pieza
        self.añadir_cuadrado(self.cuerpo[-1].position())

    def move(self):
        """ El metodo move mueve a la serpiente, con el cuerpo siguiendo a la cabeza """
        for seg_number in range(len(self.cuerpo) - 1, 0, -1):
            new_x = self.cuerpo[seg_number - 1].xcor()
            new_y = self.cuerpo[seg_number - 1].ycor()
            self.cuerpo[seg_number].goto(new_x, new_y)

        self.cabeza.forward(DISTANCIA_DE_PASO)



    def up(self):
        if not self.cabeza.heading() == DOWN:
            self.cabeza.setheading(UP)

    def down(self):
        if not self.cabeza.heading() == UP:
            self.cabeza.setheading(DOWN)

    def left(self):
        if not self.cabeza.heading() == RIGHT:
            self.cabeza.setheading(LEFT)

    def right(self):
        if not self.cabeza.heading() == LEFT:
            self.cabeza.setheading(RIGHT)
