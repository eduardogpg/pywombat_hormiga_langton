import sys
import pygame

from ant import Ant

from cell import Cell
from cell import generate_cells

WIDTH = 800
HEIGHT = 600

FPS = 60

current_time = 0

pygame.init()

fps = pygame.time.Clock()

surface = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('La hormiga de Langton')

cells = generate_cells(WIDTH, HEIGHT, 10, 10)

ant = Ant( len(cells) // 2, len(cells[0]) // 2 )

sprites = pygame.sprite.Group()
sprites.add(cells)

while True:

    time  = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            sys.exit()

    seconds = time // 50
    if current_time != seconds:
        ant.check(cells)
        current_time = seconds

    sprites.draw(surface)
    pygame.display.update()

    fps.tick(FPS)
