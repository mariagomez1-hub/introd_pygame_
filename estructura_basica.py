# importamos la libreria pygames
import pygame

# inicializamos los modulos de la libreria
pygame.init()

# establecer dimensiones de la ventana
ventana = pygame.display.set_mode((400,400))

# establecer titulo de la ventana
pygame.display.set_caption("Pygame Guanenta")

# definir colores
azul = (0,0,255)
rojo = (255, 0, 0)
verde = (0,255,0)
amarillo = (255,255,0)
blanco = (255,255,255)

# creamos una superficie
superficie_1 = pygame.surface((200,200))
superficie_2 = pygame.surface((200,200))
superficie_3 = pygame.surface((200,200))
superficie_4 = pygame.surface((200,200))
superficie_5 = pygame.surface((200,200))

# rellenamos la superficie de color
superficie_1.fill(azul)
superficie_2.fill(rojo)
superficie_3.fill(verde)
superficie_4.fill(amarillo)
superficie_5.fill(blanco)

# agregar o mover la superficie de la ventana
ventana.blit(Superficie_1, (0,0))
ventana.blit(Superficie_2, (200,0))
ventana.blit(Superficie_3, (0,200))
ventana.blit(Superficie_4, (200,200))
ventana.blit(Superficie_5, (100,100))
# actualizar visualizacion de la ventana
pygame.display.flip()

# bucle del juego
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()

