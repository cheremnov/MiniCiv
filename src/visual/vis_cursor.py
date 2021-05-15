import pygame

BLACK = (0, 0, 0)

WIDTH = 800
HEIGHT = 650


class vis_cursor(pygame.sprite.Sprite):
    def __init__(self, cursor_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = cursor_img
        self.image.set_colorkey(BLACK)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self._layer = 4

    def update(self):
        x, y = pygame.mouse.get_pos()
        self.rect.topleft = (x, y)

    def check_click(self, mouse):
        pass

    def check_right_click(self, mouse):
        pass

    def check_right_release(self, mouse):
        pass

    def check_motion(self, rel):
        pass