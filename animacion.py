# importamos la libreria pygame
import pygame
import sys

# inicializamos los modulos de la librería
pygame.init()

# Establecer dimensiones de la ventana
ventana = pygame.display.set_mode((450, 400))

# establecer titulo de la ventana
pygame.display.set_caption("Rebotes rectángulo")

# definición colores
rojo = (255,0,0)
azul = (0,0,255)

# variable de movimiento
YY = 100
MOVIMIENTO_Y = 3

# Velocidad
YY = 100
MOVIMIENTO_Y = 3

# Objeto para la gestión del tiempo
clock = pygame.time.Clock()


# bucle principal del juego
while True:
    # Maximo de fotogramas por segundo
    clock.tick(70)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(azul)

    # movimiento del rectángulo horizontl
    if XX >= 320:
        XX = 320
        MOVIMIENTO = -MOVIMIENTO
    elif XX <= 0:
        XX = 0
    MOVIMIENTO = -MOVIMIENTO

    # movimiento del rectangulo vertical
    if YY >= 320:
        YY = 320
    MOVIMIENTO_Y = -MOVIMIENTO_Y
    elif YY <= 0:
    YY = 0
    MOVIMIENTO_Y = -MOVIMIENTO_Y

    # dibujar rectangulo en ventana
    pygame.draw.rect(ventana, rojo, (XX, YY, 80, 80))

    # actualizar visualización de la ventana
    pygame.display.flip()