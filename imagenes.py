import pygame, sys

pygame.init()

pantalla = pygame.display.set_mode((370,442))
pygame.display.set_caption("Mario Bros")
NEGRO = (0, 0 , 0)
pantalla.fill(NEGRO)

# Cargar imagen
mario = pygame.image.load("assets/mario.png").convert()

# Ubicar imagen en la ventana
pantalla.blit(mario,(5, 5))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.display.flip()