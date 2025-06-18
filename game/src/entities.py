import pygame

from settings import *


class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, frames, facing_direction, groups):
        super().__init__(groups)
        self.drawing_priority=WORLD_PRIORITY_ORDER["main"]

        # graphic
        self.frame_index = 0
        self.frames = frames
        self.facing_direction = facing_direction

        # movement
        self.direction = vector()
        self.speed = 250

        # sprite setup
        self.image = self.frames[self.get_state()][self.frame_index]
        self.rect = self.image.get_frect(center=pos)
        self.y_sort =self.rect.centery

    def animate(self, dt):
        self.frame_index += ANIMATION_SPEED * dt
        player_state = self.get_state()
        current_frame = int(self.frame_index % len(self.frames[player_state]))
        self.image = self.frames[player_state][current_frame]

    def update(self, dt):
        self.animate(dt)

    def get_state(self):
        moving = bool(self.direction)
        if moving:
            is_moving_x_axis = self.direction.x != 0
            if is_moving_x_axis:
                self.facing_direction = "right" if self.direction.x > 0 else "left"

            is_moving_y_axis = self.direction.y != 0
            if is_moving_y_axis:
                self.facing_direction = "down" if self.direction.y > 0 else "up"
        return f'{self.facing_direction}{"" if moving else "_idle"}'


class Player(Entity):
    def __init__(self, pos, frames, facing_direction, groups):
        super().__init__(pos, frames, facing_direction, groups)

    def input(self):
        keys = pygame.key.get_pressed()
        input_vector = vector()

        if keys[pygame.K_a]:
            input_vector.x -= 1
        if keys[pygame.K_d]:
            input_vector.x += 1
        if keys[pygame.K_w]:
            input_vector.y -= 1
        if keys[pygame.K_s]:
            input_vector.y += 1
        self.direction = input_vector

    def move(self, dt):
        self.rect.center += self.direction * self.speed * dt

    def update(self, dt):
        super().update(dt)
        self.input()
        self.move(dt)


class Character(Entity):
    def __init__(self, pos, frames, facing_direction, groups):
        super().__init__(pos, frames, facing_direction, groups)

    def update(self, dt):
        super().update(dt)
