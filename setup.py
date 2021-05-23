from distutils.core import setup


setup(
    name="snake_game",
    version="1.0",
    description="Una version simple del juego de la serpiente",
    author="Daniel R",
    author_email="daniel94ramos@gmail.com",
    scripts=["main.py", "comida.py", "snake.py", "marcador.py"],
    options={"py2exe": {"bundle_files": 1}},
    zipfile=None
)
