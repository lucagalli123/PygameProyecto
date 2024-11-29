import pygame
import time

####################################################################################################################################
#                   GENERAL
####################################################################################################################################

# Configuraciones generales
ANCHO_VENTANA = 650  # Ancho de la ventana principal
ALTO_VENTANA = 750  # Alto de la ventana principal
ALTO_BARRA_SUPERIOR = 60  # Alto de la barra superior
TAMAÑO_CELDA = 540 // 9
PUNTO_DE_INICIO_TABLERO_SUDOKU_X = 55
PUNTO_DE_INICIO_TABLERO_SUDOKU_Y = 55

# Colores
COLOR_GRIS = (130, 130, 130)
COLOR_ROJO = (255, 0, 0)
COLOR_VERDE = (34, 139, 34)
COLOR_NEGRO = (0, 0, 0)
COLOR_BLANCO = (255, 255, 255)
COLOR_CELESTE = (135, 206, 250)
COLOR_CELESTE_OSCURO = (99, 176, 224)
COLOR_GRIS_OSCURO = (65, 65, 65)
COLOR_AMARILLENTO = (215, 215, 155)
COLOR_AZUL_OSCURO = (0, 0, 128)
COLOR_ROJO_OSCURO = (255, 99, 71)
COLOR_VERDE_CLARO = (50, 200, 50)
COLOR_VERDE_OSCURO = (10, 74, 10)
COLOR_CELESTE_CLARO = (182, 224, 250)
COLOR_VIOLETA_CLARO = (190, 190, 255)
COLOR_NARANJA_CLARO = (255, 151, 31)
COLOR_NARANJA_OSCURO = (158, 71, 36)
COLOR_AMARILLO_CLARO = (255, 239, 213)
COLOR_AMARILLO_FUERTE = (255, 255, 120)

# Puntajes
MULTIPLICADOR_PENA_SEGUN_DIFICULTAD = [2.0, 1.5, 1.0]  # multiplicadores segun la dificultad: facil, intermedia, dificil

# Archivo para guardar los puntajes
ARCHIVO_PUNTAJES = "PROYECTO PYGAME PRINCIPAL/puntajes.json"

# Rutas
RUTA_MUSICA_DERROTA = "PROYECTO PYGAME PRINCIPAL/musica_derrota.mp3"
RUTA_MUSICA_VICTORIA = "PROYECTO PYGAME PRINCIPAL/musica_victoria.mp3"
RUTA_MUSICA_SUDOKU = "PROYECTO PYGAME PRINCIPAL/Music_Sudoku.mp3"

####################################################################################################################################
#                   MULTIMEDIA
####################################################################################################################################


pygame.mixer.init()

pygame.mixer.music.load(RUTA_MUSICA_SUDOKU)
pygame.mixer.music.play(-1)  # Reproduce la musica en bucle

tiempo_inicio = time.time() # Tiempo inicial para calcular duracion de la partida

# Cargar las imagenes de fondo del menu y puntajes
imagen_menu = pygame.image.load("C:/Users/Luca/Documents/Programacion_1/PRACTICAS/PROYECTO PYGAME PRINCIPAL/menu_sudoku.jpg")
imagen_menu = pygame.transform.scale(imagen_menu, (540, 600 - ALTO_BARRA_SUPERIOR))  # Escalar imagen al tamaño de la ventana

imagen_puntajes = pygame.image.load("C:/Users/Luca/Documents/Programacion_1/PRACTICAS/PROYECTO PYGAME PRINCIPAL/imagen_puntajes.jpg")
imagen_puntajes = pygame.transform.scale(imagen_puntajes, (540, 600))

imagen_nombres = pygame.image.load("C:/Users/Luca/Documents/Programacion_1/PRACTICAS/PROYECTO PYGAME PRINCIPAL/imagen_fondo.jpg")
imagen_nombres = pygame.transform.scale(imagen_nombres, (540, 600))

imagen_fondo_sudoku = pygame.image.load("C:/Users/Luca/Documents/Programacion_1/PRACTICAS/PROYECTO PYGAME PRINCIPAL/imagen_fondo.jpg")
imagen_fondo_sudoku = pygame.transform.scale(imagen_fondo_sudoku, (ANCHO_VENTANA, ALTO_VENTANA))
