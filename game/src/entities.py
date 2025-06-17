import pygame

from settings import *

class Entity(pygame.sprite.Sprite):
    def __init__(self,pos,frames,groups):
        super().__init__(groups)

        self.direction = vector()
        self.speed =250

class Player(Entity):
    def __init__(self, pos,frames, groups):
        super().__init__(pos,frames,groups)

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
        self.input()
        self.move(dt)
