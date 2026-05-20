import pygame
import sys

# Iniciar modulos
pygame.init()
pygame.mixer.init()

# Colores
BLANCO = pygame.color(255,255,255)

# Ventana
pantalla = pygame.display.set_mode((400,400))
pantalla.fill(BLANCO)
pygame.display.set_caption("Sonidos en Pygame")

# Variables auxiliares
continuar = True

# Sonido de fondo
GALLO = pygame.mixer.music.load("introd_pygame_/assets/sounds/gallo.ogg")
CUERVO = pygame.mixer.music.load("introd_pygame_/assets/sounds/cuervo.ogg")
BICI = pygame.mixer.music.load("introd_pygame_/assets/sounds/silbato.ogg")

# --------------------
# Bucle del juego
# --------------------

while continuar:
    for event in pygame.event.get():
        # cerrar ventana si hace click en el boton de cerrar
        if event.type == pygame.QUIT:
            continuar = False
            # detectar si se oprime una tecla
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                continuar = False
        elif event.key == pygame.K_o:
            GALLO.play()
        elif event.key == pygame.K_c:
            CUERVO.play()
        elif event.key == pygame.K_v:
            BICI.play()

pygame.display.flip()
