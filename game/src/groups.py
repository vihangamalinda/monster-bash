from settings import *


class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = vector()

    def draw(self, player_center):
        self.offset.x = -(player_center[0] - WINDOW_WIDTH / 2)
        self.offset.y = -(player_center[1] - WINDOW_HEIGHT / 2)

        background_sprites = [sprite for sprite in self if sprite.drawing_priority < WORLD_PRIORITY_ORDER["main"]]
        main_sprites = sorted([sprite for sprite in self if sprite.drawing_priority == WORLD_PRIORITY_ORDER["main"]],
                              key=lambda sprite: sprite.y_sort)
        foreground_sprites = [sprite for sprite in self if sprite.drawing_priority > WORLD_PRIORITY_ORDER["main"]]

        for layer in (background_sprites, main_sprites, foreground_sprites):
            for sprite in layer:
                self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset)
