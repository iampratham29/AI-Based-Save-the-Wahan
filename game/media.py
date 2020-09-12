import pygame
from game.geometry import *

pygame.init()
# start_music = pygame.mixer.Sound("Hurry_Up.mp3")
pygame.mixer.music.load("../Media/music1.mp3")
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Racing")
clock = pygame.time.Clock()

spImg = pygame.image.load("../Media/rocket1.png")  # load the car image
sp2Img = pygame.image.load("../Media/obstacle.png")
bgspImg = pygame.image.load("../Media/space.png")
crash_img = pygame.image.load("../Media/crash.png")

carImg = pygame.image.load("../Media/car1.png")  # load the car image
car2Img = pygame.image.load("../Media/car2.png")
bgImg = pygame.image.load("../Media/back2.png")

boatImg = pygame.image.load("../Media/boat.png")  # load the car image
boat2Img = pygame.image.load("../Media/shark.png")
bgbtImg = pygame.image.load("../Media/water.png")
