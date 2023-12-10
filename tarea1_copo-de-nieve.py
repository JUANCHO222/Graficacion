import turtle

# Función para dibujar un segmento de la curva de Koch
def segmento_koch(longitud, nivel):
    if nivel == 0:
        turtle.forward(longitud)
    else:
        longitud /= 3.0
        segmento_koch(longitud, nivel - 1)
        turtle.left(60)
        segmento_koch(longitud, nivel - 1)
        turtle.right(120)
        segmento_koch(longitud, nivel - 1)
        turtle.left(60)
        segmento_koch(longitud, nivel - 1)

# Función para dibujar un copo de nieve de Koch completo
def copo_nieve_koch(longitud, nivel):
    for _ in range(3):
        segmento_koch(longitud, nivel)
        turtle.right(120)

# Configuración inicial de Turtle
turtle.speed(70)  # Velocidad máxima (ajusta el número según desees)
turtle.penup()
turtle.goto(-150, 90)  # Posición inicial
turtle.pendown()

# Llama a la función para dibujar el copo de nieve de Koch
copo_nieve_koch(300, 4)

# Cierra la ventana haciendo clic
turtle.exitonclick()