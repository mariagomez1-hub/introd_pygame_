# importamos la libreria pygame

import pygame
import sys

# Inicializar pygame
pygame.init()

# Ventana
ANCHO = 400
ALTO = 400

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Rebotes en todas las esquinas")

# Colores
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

# Posición inicial
x = 100
y = 100

# Tamaño del rectángulo
ancho_rect = 80
alto_rect = 80

# Velocidad
mov_x = 5
mov_y = 8

# Reloj
clock = pygame.time.Clock()

# Bucle principal
while True:

    clock.tick(60)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fondo
    ventana.fill(AZUL)

    # Movimiento
    x += mov_x
    y += mov_y

    # Rebote izquierda/derecha
    if x <= 0 or x >= ANCHO - ancho_rect:
        mov_x *= -1

    # Rebote arriba/abajo
    if y <= 0 or y >= ALTO - alto_rect:
        mov_y *= -1

    # Dibujar rectángulo
    pygame.draw.rect(
        ventana,
        ROJO,
        (x, y, ancho_rect, alto_rect)
    )

    # Actualizar pantalla
    pygame.display.flip()