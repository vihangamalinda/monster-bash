import pygame

from settings import *

class Entity(pygame.sprite.Sprite):
    def __init__(self,pos,frames,groups):
        super().__init__(groups)

        # graphic
        self.frame_index=0
        self.frames = frames
        self.facing_direction = "down"


        # movement
        self.direction = vector()
        self.speed =250

        # sprite setup
        self.image =self.frames[self.facing_direction][self.frame_index]
        self.rect =self.image.get_frect(center=pos)

    def animate(self,dt):
        self.frame_index+= ANIMATION_SPEED*dt
        player_state =self.facing_direction
        current_frame = int(self.frame_index % len(self.frames[player_state]))
        self.image = self.frames[player_state][current_frame]

    def update(self,dt):
        self.animate(dt)

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
