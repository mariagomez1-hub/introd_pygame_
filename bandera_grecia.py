# importamos la libreria pygames
import pygame

# inicializamos los modulos de la libreria
pygame.init()

# establecer dimensiones de la ventana
ventana = pygame.display.set_mode((450,300))

# establecer titulo de la ventana
pygame.display.set_caption("Bandera de Grecia")

# definir colores
azul = (0, 0, 255)
blanco = (255, 255, 255)

# fondo blanco
ventana.fill(blanco)

# dibujar franjas (9)
alto_franja = 300 // 9

for i in range(9):
    if i % 2 == 0:
        pygame.draw.rect(ventana, azul, (0, i * alto_franja, 450, alto_franja))

# cuadrao azul(esquina superior izquierda
pygame.draw.rect(ventana, azul, (0, 0, 150, 150))

# cruz blanca
# vertical
pygame.draw.rect (ventana, blanco, (60, 0, 150, 150))
#horizontal
pygame.draw.rect(ventana, blanco,(0, 60, 150, 30))

# actualizar pantalla
pygame.display.flip()

# blucle del juego
ejecutando = True
while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            ejecutando = False

pygame.quit()
