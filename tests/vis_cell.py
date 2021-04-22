import pygame
import os

from src.visual.vis_cursor import vis_cursor
from src.visual.vis_cell import vis_cell

WIDTH = 800
HEIGHT = 650
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

game_folder = os.path.dirname("../")

pygame.init()
pygame.mixer.init()
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

cell_img = pygame.image.load(os.path.join(game_folder, 'res/hex1-res2.png')).convert()
cursor_img = pygame.image.load(os.path.join(game_folder, 'res/cursor1_rs2.png')).convert()
cell = vis_cell(100, 100, cell_img)
cell2 = vis_cell(148, 129, cell_img)
cursor = vis_cursor(cursor_img)

cell_group = pygame.sprite.AbstractGroup()
cell_group.add(cell)
cell_group.add(cell2)

all_sprites.add(cell)
all_sprites.add(cell2)
all_sprites.add(cursor)

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