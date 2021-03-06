# Importamos las clases Screen y Turtle
from turtle import Screen
import time
from snake import Snake
from comida import Comida
from marcador import Marcador
# Creamos una pantalla
pantalla = Screen()

# Configuramos la pantalla, medidas, color de fondo y titulo
pantalla.setup(width=600, height=600)
pantalla.bgcolor("black")
pantalla.title("Snake Game. Developed by Daniel R")
pantalla.tracer(0)                          # Apagamos la animacion de la pantalla

game_on = True

# Esta funcion indica que hay que cerrar el juego. Se activa con la tecla Escape


def fin_juego():
    global game_on
    game_on = False


serpiente = Snake()
bocadito = Comida()
marcador = Marcador()

pantalla.listen()
pantalla.onkey(key="Up", fun=serpiente.up)
pantalla.onkey(key="Down", fun=serpiente.down)
pantalla.onkey(key="Left", fun=serpiente.left)
pantalla.onkey(key="Right", fun=serpiente.right)
pantalla.onkey(key="Escape", fun=fin_juego)


while game_on:
    pantalla.update()                   # Al desactivar la animación de los cuadrados, debemos actualizar la pantalla
    time.sleep(0.1)                     # Hacemos que cada ciclo tenga un retraso de 0.1 s
    serpiente.move()

    # Detectamos si la cabeza toca la comida. Si es asi, debemos sumar un punto y hacer que aparezca en otro lugar
    if serpiente.cabeza.distance(bocadito) < 15:
        bocadito.actualizar()
        marcador.sumar_puntos()
        serpiente.crecer()

    # Detectamos si hay colision con la pared
    if serpiente.cabeza.xcor() > 280 or serpiente.cabeza.xcor() < -290 \
            or serpiente.cabeza.ycor() > 270 or serpiente.cabeza.ycor() < -290:
        marcador.reset()
        serpiente.reset()

    # Detectamos choque con nuestro cuerpo
    for square in serpiente.cuerpo[1:]:
        if serpiente.cabeza.distance(square) < 10:
            marcador.reset()
            serpiente.reset()


# No cerramos la ventana hasta hacer click
# pantalla.exitonclick()
# Cerramos la pantalla al salir del bucle
pantalla.bye()
