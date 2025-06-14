from settings import *


class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        # frect() => floating point rectangle
        self.rect = self.image.get_frect(topleft=pos)
