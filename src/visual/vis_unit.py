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
        self.move = False
        self.skip = False
        self._layer = 2

    def local_coords(self, point):
        return (point[0] - self.rect.left, point[1] - self.rect.top)

    def check_click(self, mouse):
        if self.skip == True:
            self.skip = False
            return
        if self.rect.collidepoint(mouse) and self.mask.get_at(self.local_coords(mouse)) == 1:
            self.move = not self.move
        else:
            self.move = False

    def check_right_click(self, mouse):
        pass

    def check_right_release(self, mouse):
        pass

    def check_motion(self, rel):
        pass

    def set_center(self, x, y):
        self.rect.center = (x, y)

    def set_move(self, move):
        self.move = move

    def moving(self):
        return self.move

    def set_skip(self, skip):
        self.skip = skip
