from settings import *
from pytmx.util_pygame import load_pygame
from  os.path import join,exists

from  sprites import Sprite

class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Monster Bash")
        # Groups - contains all of visible sprites
        self.all_sprites = pygame.sprite.Group()

        self.import_assets()
        self.setup(self.tmx_maps["world"],"house")

    def import_assets(self):
        print(exists("../assets/maps/world.tmx"))
        self.tmx_maps = {'world': load_pygame(join("..", "assets", "maps", "world.tmx"))}
        print(self.tmx_maps)

    def setup(self,tmx_map,player_start_pos):
        terrain_layer_tiles = tmx_map.get_layer_by_name("Terrain").tiles()
        for x,y,surf in terrain_layer_tiles:
            position = (x * TILE_SIZE, y * TILE_SIZE)
            Sprite(position, surf,self.all_sprites)

    def run(self):
        while True:
            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # game logic
            self.all_sprites.draw(self.display)
            pygame.display.update()

if __name__=="__main__":
    game = Game()
    game.run()