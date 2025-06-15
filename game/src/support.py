from  settings import *
from os.path import join,exists
from os import walk

def import_image(*path,alph=True,format="png"):
    full_path = join(*path) +f".{format}"
    print(full_path)
    print(exists(full_path))
    if alph:
        surface =pygame.image.load(full_path).convert_alpha()
    else:
        surface =pygame.image.load(full_path).convert()
    return surface

def import_folder(*path):
    frames =[]
    for folder_path,sub_folders,image_names in walk(join(*path)):
        for image_name in sorted(image_names,key=lambda name:name.split('.')[0]):
            full_path = join(folder_path,image_name)
            surface = pygame.image.load(full_path).convert_alpha()
            frames.append(surface)
    return frames