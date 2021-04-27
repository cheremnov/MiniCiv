import pygame

BLACK = (0, 0, 0)

class vis_cell(pygame.sprite.Sprite):
    def __init__(self, x, y, cell_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = cell_img
        self.image.set_colorkey(BLACK)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self._layer = 1
        self.count = 0

    def local_coords(self, point):
        return (point[0] - self.rect.left, point[1] - self.rect.top)

    def check_click(self, mouse):
        if self.rect.collidepoint(mouse) and self.mask.get_at(self.local_coords(mouse)) == 1:
            print("HOLA" + str(self.count))
            self.count = self.count + 1

    def check_right_click(self, mouse):
        pass

    def check_right_release(self, mouse):
        pass

    def check_motion(self, rel):
        pass

    def x_size(self):
        return self.rect.right - self.rect.left

    def y_size(self):
        return self.rect.bottom - self.rect.top

    def move(self, move):
        self.rect.center = (self.rect.center[0] + move[0], self.rect.center[1] + move[1])