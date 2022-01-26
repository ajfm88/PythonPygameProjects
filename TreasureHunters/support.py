from os import listdir
from os.path import join
# using os.path's join is actually better because i've heard it is better for support on other OSes (e.g. linux, mac os)
import pygame


def import_folder(path):
    surface_list = []

    for image in listdir(path):
        full_path = join(path, f"{image}")
        image_surf = pygame.image.load(full_path).convert_alpha()
        surface_list.append(image_surf)

    return surface_list
