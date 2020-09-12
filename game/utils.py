import pygame
from game.geometry import *
from game.media import gameDisplay

def highscore(count):
    font = pygame.font.SysFont(None, 20)
    text = font.render("Score : " + str(count), True, white)
    gameDisplay.blit(text, (0, 0))


def draw_things(thingx, thingy, thing):
    gameDisplay.blit(thing, (thingx, thingy))


def vehicle(x, y, vehimage):
    gameDisplay.blit(vehimage, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()


def message_display(text, size, x, y):
    font = pygame.font.Font("freesansbold.ttf", size)
    text_surface, text_rectangle = text_objects(text, font)
    text_rectangle.center = (x, y)
    gameDisplay.blit(text_surface, text_rectangle)
