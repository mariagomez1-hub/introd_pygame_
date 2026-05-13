# Crear una ciudad de hierro o parque de atraaciones usando los elementos graficos vistos con pygame (lineas, rectangulos, cuadrados, poligonos, circulos, elipses, arcos y textos) en donde los personajes son pacmans.
import pygame
import math

# Inicializar pygame
pygame.init()

# Tamaño de ventana
ANCHO = 1000
ALTO = 700
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ciudad de Hierro con Pacmans")

# Colores
negro = (0,0,0)
blanco = (255,255,255)
gris = (120,120,120)
gris_oscuro = (70,70,70)
azul = (80,180,255)
verde = (0,200,0)
amarillo = (255,255,0)
rojo = (255,0,0)
morado = (180,0,255)
naranja = (255,140,0)

# Fuente
fuente = pygame.font.SysFont("Arial", 30)

# Funcion para dibujar Pacman
def dibujar_pacman(x, y, radio, direccion):
    pygame.draw.circle(pantalla, amarillo, (x, y), radio)

    # Boca
    if direccion == "derecha":
        puntos = [(x, y),
    (x + radio, y - radio//2),
    (x + radio, y + radio//2)]
    elif direccion == "izquierda":
        puntos = [(x, y),
    (x - radio, y - radio//2),
    (x - radio, y + radio//2)]
    elif direccion == "arriba":
        puntos = [(x, y),
    (x - radio//2, y - radio),
    (x + radio//2, y - radio)]
    else:
        puntos = [(x, y),
    (x - radio//2, y + radio),
    (x + radio//2, y + radio)]

    pygame.draw.polygon(pantalla, negro, puntos)

    # circulo de la pantalla
    pygame.draw.circle(pantalla, negro, (x, y - radio//2), 5)


# Bucle principal
ejecutando = True

while ejecutando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Fondo cielo
    pantalla.fill(azul)

    # Suelo
    pygame.draw.rect(pantalla, verde, (0, 500, ANCHO, 200))

    # -----------------------------
    # EDIFICIOS (Rectángulos)
    # -----------------------------
    pygame.draw.rect(pantalla, gris, (80, 220, 140, 280))
    pygame.draw.rect(pantalla, gris_oscuro, (270, 170, 180, 330))
    pygame.draw.rect(pantalla, gris, (500, 250, 160, 250))


    # -----------------------------
    # NORIA (Círculos)
    # -----------------------------
    pygame.draw.circle(pantalla, blanco, (780, 250), 90, 4)

    # Radios
    for angulo in range(0, 360, 45):
        x = 780 + int(90 * math.cos(math.radians(angulo)))
        y = 250 + int(90 * math.sin(math.radians(angulo)))
        pygame.draw.line(pantalla, blanco, (780, 250), (x, y), 2)

        # Cabinas
        pygame.draw.circle(pantalla, naranja, (x, y), 12)

    # Base de la noria
    pygame.draw.line(pantalla, blanco, (740, 500), (780, 340), 5)
    pygame.draw.line(pantalla, blanco, (780, 340), (820, 500), 5)

    # -----------------------------
    # CARPA DE CIRCO (Polígono)
    # -----------------------------
    pygame.draw.polygon(
        pantalla,
        rojo,
        [(350, 500), (450, 350), (550, 500)]
    )

    pygame.draw.rect(pantalla, blanco, (390, 500, 120, 80))

    # -----------------------------
    # GLOBOS (Elipses)
    # -----------------------------
    pygame.draw.ellipse(pantalla, rojo, (120, 80, 50, 70))
    pygame.draw.ellipse(pantalla, verde, (180, 90, 50, 70))
    pygame.draw.ellipse(pantalla, morado, (250, 80, 50, 70))

    pygame.draw.line(pantalla, negro, (145, 150), (145, 220), 2)
    pygame.draw.line(pantalla, negro, (205, 160), (205, 220), 2)
    pygame.draw.line(pantalla, negro, (270, 150), (290, 200), 2)

    # -----------------------------
    # PACMANS
    # -----------------------------
    dibujar_pacman(150, 560, 30, "derecha")
    dibujar_pacman(300, 600, 25, "izquierda")
    dibujar_pacman(700, 580, 35, "arriba")

    # -----------------------------
    # TEXTO
    # -----------------------------
    titulo = fuente.render("PARQUE PACMAN CITY", True, negro)
    pantalla.blit(titulo, (280, 30))
    texto = fuente.render("Maria Kamila", True, blanco)
    pantalla.blit(texto,(0,50))

    # Actualizar pantalla
    pygame.display.update()

# Salir
pygame.quit()