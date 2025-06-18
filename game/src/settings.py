import pygame
from pygame.math import Vector2 as vector
from sys import exit

WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720
TILE_SIZE = 64
ANIMATION_SPEED = 6
TILE_PER_SINGLE_COAST_IMAGE = 3

WORLD_PRIORITY_ORDER = {
    "water": 0,
    "bg": 1,
    "shadow": 2,
    "main": 3,
    "top": 4
}
