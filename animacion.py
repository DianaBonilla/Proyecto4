## Diana Bonilla
## Movimiento de una imagen


import pygame
from pygame.locals import*
pygame.init()
v = pygame.display.set_mode((700,700)) ## crea la ventana
pygame.display.set_caption("Moviento de una imagen por teclado----->   :)") ## titulo de la ventana
my_image = pygame.image.load("tefy.jpg") ## la imagen
posX = 150 # posicion inicial en x
posY = 150 # posicion inicial en y

movimiento = 10 ## "velocidad a la que se mueve"
Morado = (165,105,189) ## color de fondo (RGB)
##derecha=True
while True:
    v.fill(Morado)
    v.blit(my_image,(posX,posY))   
    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            sys.exit()
          if event.type == pygame.KEYDOWN: ## movimientos con las flechas
              if event.key == K_LEFT: ## movimiento a la izquierda
                  posX -= movimiento
              elif event.key == K_RIGHT:  ## movimiento a la derecha
                  posX += movimiento
              elif event.key == K_UP:  ## movimiento hacia arriba
                  posY -= movimiento
              elif event.key == K_DOWN: ## movimiento hacia abajo
                  posY += movimiento

            

                
    pygame.display.update()

    
