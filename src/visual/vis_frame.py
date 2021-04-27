import pygame as pg
from src.visual.vis_map import vis_map

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class vis_frame(pg.sprite.Sprite):
    def __init__(self, x, y, frame_img, game_map):
        pg.sprite.Sprite.__init__(self)
        self.image = frame_img
        self.image.set_colorkey(BLACK)
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.map = game_map
        self._layer = 1

    def local_coords(self, point):
        return (point[0] - self.rect.left, point[1] - self.rect.top)

    def check_click(self, mouse):
        if self.rect.collidepoint(mouse) and self.mask.get_at(self.local_coords(mouse)) == 1:
            pass

    def check_right_click(self, mouse):
        self.map.set_moving(True)

    def check_right_release(self, mouse):
        self.map.set_moving(False)

    def check_motion(self, rel):
        self.map.move(rel)
