from settings import *
from os.path import join, exists
from os import walk


def import_image(*path, alph=True, format="png"):
    full_path = join(*path) + f".{format}"
    print(full_path)
    print(exists(full_path))
    if alph:
        surface = pygame.image.load(full_path).convert_alpha()
    else:
        surface = pygame.image.load(full_path).convert()
    return surface


def import_folder(*path):
    frames = []
    for folder_path, sub_folders, image_names in walk(join(*path)):
        for img_name_with_extension in sorted(image_names,
                                              key=lambda name_with_extension: name_with_extension.split('.')[0]):
            full_path = join(folder_path, img_name_with_extension)
            surface = pygame.image.load(full_path).convert_alpha()
            frames.append(surface)
    return frames


def import_folder_dic(*path):
    frames = {}
    for folder_path, sub_folders, image_names in walk(join(*path)):
        for img_name_with_extension in image_names:
            full_path = join(folder_path, img_name_with_extension)
            surface = pygame.image.load(full_path).convert_alpha()
            image_name = img_name_with_extension.split(".")[0]
            frames[image_name] = surface
    return frames
