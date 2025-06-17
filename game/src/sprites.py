from settings import *


class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        # frect() => floating point rectangle
        self.rect = self.image.get_frect(topleft=pos)


class AnimatedSprite(Sprite):
    def __init__(self, pos, frames, groups):
        self.frame_index = 0
        self.frames = frames
        super().__init__(pos, frames[0], groups)

    def animate(self, dt):
        self.frame_index += ANIMATION_SPEED * dt
        current_frame_index = int(self.frame_index % len(self.frames))
        self.image = self.frames[current_frame_index]

    def update(self, dt):
        self.animate(dt)
