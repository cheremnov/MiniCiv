import pygame
from src.visual.vis_object import vis_object

BLACK = (0, 0, 0)

WIDTH = 800
HEIGHT = 650


class vis_cursor(vis_object):
    def __init__(self, cursor_img):
        vis_object.__init__(self, WIDTH / 2, HEIGHT / 2, cursor_img)
        self._layer = 4

    def update(self):
        x, y = pygame.mouse.get_pos()
        self.rect.topleft = (x, y)
