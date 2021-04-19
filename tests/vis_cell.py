# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
import time
import os

WIDTH = 800
HEIGHT = 650
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

game_folder = os.path.dirname(".")

class vis_cursor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = cursor_img
        self.image.set_colorkey(BLACK)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        x, y = pygame.mouse.get_pos()
        self.rect.topleft = (x, y)

    def check_click(self, mouse):
        pass


class vis_cell(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = cell_img
        self.image.set_colorkey(BLACK)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        if x == 0 and y == 0:
            self.rect.center = (WIDTH / 2, HEIGHT / 2)
        else:
            self.rect.center = (x, y)
        self.count = 0

    def local_coords(self, point):
        return (point[0] - self.rect.left, point[1] - self.rect.top)

    def check_click(self, mouse):
        if self.rect.collidepoint(mouse) and self.mask.get_at(self.local_coords(mouse)) == 1:
            print("HOLA" + str(self.count))
            self.count = self.count + 1

    # def update(self):
    #     ms = pygame.mouse.get_pos()
    #     if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(ms):
    #         print("HOLA")

    # def update(self):
    #     self.rect.x += 5
    #     if self.rect.left > WIDTH:
    #         self.rect.right = 0


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

cell_img = pygame.image.load(os.path.join(game_folder, 'hex1-res2.png')).convert()
cursor_img = pygame.image.load(os.path.join(game_folder, 'cursor1_rs2.png')).convert()
cell = vis_cell(100, 100)
cell2 = vis_cell(148, 129)
cursor = vis_cursor()

cell_group = pygame.sprite.AbstractGroup()
cell_group.add(cell)
cell_group.add(cell2)

all_sprites.add(cell)
all_sprites.add(cell2)
all_sprites.add(cursor)

# Цикл игры
running = True
it = 0
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)

    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

        # in event handling:
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos

            for sprite in all_sprites:
                sprite.check_click(event.pos)
            # for box in all_sprites:
            #     print(box.)
            #     if box.rect.collidepoint(x, y):
            #         it += 1
            #         print("H {}".format(it))

    # Обновление
    all_sprites.update()

    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()