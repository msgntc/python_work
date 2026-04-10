import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("this is not a blue background dont ever look it wont be blue. and i quote from, someperson i. humanity who has probally said theese exatr words possobly")

blue = (0, 0, 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(blue)
    pygame.display.flip()