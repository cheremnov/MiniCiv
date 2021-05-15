import pygame

BLACK = (0, 0, 0)


class vis_cell(pygame.sprite.Sprite):
    def __init__(self, x, y, cell_img, map):
        pygame.sprite.Sprite.__init__(self)
        self.image = cell_img
        self.image.set_colorkey(BLACK)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.map = map
        self._layer = 1
        self.count = 0
        self.unit = None

    def local_coords(self, point):
        return point[0] - self.rect.left, point[1] - self.rect.top

    def check_click(self, mouse):
        if self.rect.collidepoint(mouse) and self.mask.get_at(self.local_coords(mouse)) == 1:
            if self.unit is None:
                for line in self.map.get_cells():
                    for cell in line:
                        if cell.vis_cell.get_unit() is not None and cell.vis_cell.get_unit().moving() is True\
                                and cell.vis_cell.get_unit().is_immovable() is False:
                            self.set_unit(cell.vis_cell.get_unit())
                            self.unit.set_move(False)
                            self.unit.set_skip(True)
                            cell.vis_cell.set_unit(None)

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
        if self.unit is not None:
            self.unit.set_center(self.rect.centerx, self.rect.centery)

    def set_unit(self, unit):
        self.unit = unit
        if self.unit is not None:
            self.unit.set_center(self.rect.centerx, self.rect.centery)

    def get_unit(self):
        return self.unit

    def update_image(self, cell_img):
        self.image = cell_img
        self.image.set_colorkey(BLACK)
        self.mask = pygame.mask.from_surface(self.image)
