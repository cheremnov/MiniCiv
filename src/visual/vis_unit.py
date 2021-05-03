import pygame

BLACK = (0, 0, 0)

class vis_unit(pygame.sprite.Sprite):
    def __init__(self, unit_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = unit_img
        self.image.set_colorkey(BLACK)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self._layer = 2

    def check_click(self, mouse):
        pass

    def check_right_click(self, mouse):
        pass

    def check_right_release(self, mouse):
        pass

    def check_motion(self, rel):
        pass

    def set_center(self, x, y):
        self.rect.center = (x, y)