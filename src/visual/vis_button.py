import pygame as pg
import pygame.freetype
from src.visual.vis_object import vis_object

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class vis_button(vis_object):
    def __init__(self, x, y, text, button_img, font=None):
        vis_object.__init__(self, x, y, button_img)
        self.text = text
        self._layer = 4
        if font is None:
            font = pg.freetype.SysFont('Comic Sans MS', 16)
        self.font = font
        self.textsurface, _ = font.render(text, (1, 1, 1))
        self.image.blit(self.textsurface, (10, 25))

    def check_click(self, mouse):
        if self.rect.collidepoint(mouse) and self.mask.get_at(self.local_coords(mouse)) == 1:
            self.action()

    def action(self):
        print('NOT IMPLEMENTED YET')

    def draw_text(self):
        self.textsurface, _ = self.font.render(self.text, (0, 0, 0))
        self.image.blit(self.textsurface, (10, 25))
