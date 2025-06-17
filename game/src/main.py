import pygame.time

from settings import *
from pytmx.util_pygame import load_pygame
from os.path import join, exists

from sprites import Sprite, AnimatedSprite
from entities import Player
from groups import AllSprites
from support import import_folder, coast_importer,all_character_import


class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Monster Bash")
        self.clock = pygame.time.Clock()
        # Groups - contains all of visible sprites
        self.all_sprites = AllSprites()

        self.import_assets()
        self.setup(self.tmx_maps["world"], "house")

    def import_assets(self):
        # print(exists("../assets/maps/world.tmx"))
        self.tmx_maps = {'world': load_pygame(join("..", "assets", "maps", "world.tmx")),
                         "hospital": load_pygame(join("..", "assets", "maps", "hospital.tmx")),
                         }

        self.overworld_frames = {
            "water": import_folder("..", "graphics", "tilesets", "water"),
            "coast": coast_importer(TILE_PER_SINGLE_COAST_IMAGE * 8, TILE_PER_SINGLE_COAST_IMAGE * 4, "..", "graphics",
                                    "tilesets", "coast"),
            "character": all_character_import("..","graphics", "characters"),
        }

    def setup(self, tmx_map, player_start_pos):
        # Terrrain tiles
        terrain_layer_tiles = tmx_map.get_layer_by_name("Terrain").tiles()
        for x, y, surf in terrain_layer_tiles:
            position = (x * TILE_SIZE, y * TILE_SIZE)
            Sprite(position, surf, self.all_sprites)

        # Terrrain top tiles
        terrain_top_layer_tiles = tmx_map.get_layer_by_name("Terrain Top").tiles()
        for x, y, surf in terrain_top_layer_tiles:
            position = (x * TILE_SIZE, y * TILE_SIZE)
            Sprite(position, surf, self.all_sprites)

        # Object layer
        object_layer = tmx_map.get_layer_by_name("Objects")
        for obj in object_layer:
            obj_pos = (obj.x, obj.y)
            Sprite(obj_pos, obj.image, self.all_sprites)

        # Entity objects
        entities_layer_tiles = tmx_map.get_layer_by_name("Entities")
        for obj in entities_layer_tiles:
            if obj.name == "Player" and obj.properties['pos'] == player_start_pos:
                player_pos = (obj.x, obj.y)
                self.player = Player(player_pos, self.all_sprites)

        # Water layer
        water_layer = tmx_map.get_layer_by_name("Water")
        for obj in water_layer:
            # range(start,end, incremental_step)
            for x in range(int(obj.x), int(obj.x + obj.width), TILE_SIZE):
                for y in range(int(obj.y), int(obj.y + obj.height), TILE_SIZE):
                    # print (x, y)
                    position = (x, y)
                    AnimatedSprite(position, self.overworld_frames["water"], self.all_sprites)

        # Coast layer
        coast_layer = tmx_map.get_layer_by_name("Coast")
        for obj in coast_layer:
            position = (obj.x, obj.y)
            terrain_type = obj.properties['terrain']
            costal_side = obj.properties['side']
            frames = self.overworld_frames["coast"][terrain_type][costal_side]
            AnimatedSprite(position, frames, self.all_sprites)

    def run(self):
        while True:
            # Delta time
            dt = self.clock.tick() / 1000
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # game logic
            self.all_sprites.update(dt)
            self.display.fill('black')
            self.all_sprites.draw(self.player.rect.center)
            # print(self.clock.get_fps())
            # print(dt)
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
