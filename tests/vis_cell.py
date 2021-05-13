import pygame
import os
import sys

from src.visual.vis_cursor import vis_cursor
from src.visual.vis_cell import vis_cell
from src.visual.vis_map import vis_map

WIDTH = 800
HEIGHT = 650
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

game_folder = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))

pygame.init()
pygame.mixer.init()
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.LayeredUpdates()

cell_img = pygame.image.load(os.path.join(game_folder, 'res/hex1-res2.png')).convert()
cursor_img = pygame.image.load(os.path.join(game_folder, 'res/cursor1_rs2.png')).convert()

map = vis_map()
map.set_size(20, 8, cell_img)

cursor = vis_cursor(cursor_img)

all_sprites.add(cursor)
for line in map.get_cells():
    for cell in line:
        all_sprites.add(cell)

running = True
it = 0
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos

            for sprite in all_sprites:
                sprite.check_click(event.pos)

    all_sprites.update()

    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
