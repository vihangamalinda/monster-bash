from  settings import *
from os.path import join,exists

def import_image(*path,alph=True,format="png"):
    full_path = join(*path) +f".{format}"
    print(full_path)
    print(exists(full_path))
    if alph:
        surface =pygame.image.load(full_path).convert_alpha()
    else:
        surface =pygame.image.load(full_path).convert()
    return surface