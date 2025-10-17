import pygame
import constantes
from personaje import Personaje

pygame.init()

window= pygame.display.set_mode((constantes.ANCHO_SCREEN,
                                 constantes.ALTO_SCREEN))
pygame.display.set_caption("Juego GOD")

jugador= Personaje(250,350)

mover_arriba = False
mover_abajo= False
mover_izquierda= False
mover_derecha= False

 
reloj= pygame.time.Clock()

run = True 
while run == True: 
    
    reloj.tick(constantes.FPS)

    window.fill(constantes.COLOR_BG)
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda == True:
        delta_x = -constantes.VELOCIDAD
    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD
    if mover_arriba== True:
        delta_y = -constantes.VELOCIDAD

    jugador.movimiento(delta_x, delta_y)

    jugador.draw(window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            mover_izquierda=True
        if event.key == pygame.K_RIGHT:
            mover_derecha=True
        if event.key == pygame.K_UP:
            mover_arriba=True
        if event.key == pygame.K_DOWN:
            mover_abajo=True

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            mover_izquierda=False
        if event.key == pygame.K_RIGHT:
            mover_derecha=False
        if event.key == pygame.K_UP:
            mover_arriba=False
        if event.key == pygame.K_DOWN:
            mover_abajo=False

    pygame.display.update()
pygame.quit