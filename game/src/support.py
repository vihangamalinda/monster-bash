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

def import_sub_folders(*path):
    frames ={}
    for folder_path,sub_folders,image_names in walk(join(*path)):
        if sub_folders:
            for sub_folder in sub_folders:
                frames[sub_folder] =import_folder(*path,sub_folder)
    return frames

def import_tilemap(cols,rows,*path):
    frames={}
    surf=import_image(*path)
    cell_width=surf.get_width()/cols
    cell_height=surf.get_height()/rows

    for col in range(cols):
        for row in range(rows):
            cutout_rect = pygame.Rect(col*cell_width,row*cell_height,cell_width,cell_height)
            cutout_surf =pygame.Surface((cell_width,cell_height))

            # Assigning green colour if the cutout object can't cover the whole area on the surface
            # And asking to ignore the green colour then it won't affect the appearance of the original image
            cutout_surf.fill("green")
            cutout_surf.set_colorkey("green")

            cutout_surf.blit(surf,(0,0),cutout_rect)
            frames[(col,row)] =cutout_surf
