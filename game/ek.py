import pygame
import time
import random

# Lets go to code now
mode = 0

pygame.init()
display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
bcolor = (220, 181, 181)
car_width = 50
car_height = 100
# start_music = pygame.mixer.Sound("Hurry_Up.mp3")
pygame.mixer.music.load("music1.mp3")
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Racing")
clock = pygame.time.Clock()

spImg = pygame.image.load("rocket1.png")  # load the car image
sp2Img = pygame.image.load("obstacle.png")
bgspImg = pygame.image.load("space.png")
crash_img = pygame.image.load("crash.png")

carImg = pygame.image.load("car1.png")  # load the car image
car2Img = pygame.image.load("car2.png")
bgImg = pygame.image.load("back2.png")

boatImg = pygame.image.load("boat.png")  # load the car image
boat2Img = pygame.image.load("shark.png")
bgbtImg = pygame.image.load("water.png")


def commence():
    global mode
    mode = 0
    menu1_x1 = 80
    menu1_x2 = 205
    menu1_x3 = 350
    menu1_y = 400
    menu2_x = 500
    menu2_y = 400
    menu_width = 100
    menu_height = 50
    while mode == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pygame.draw.rect(gameDisplay, black, (200, 400, 100, 50))

        gameDisplay.fill(bcolor)
        message_display("VVPSA", 100, display_width / 2, display_height / 2)
        pygame.draw.rect(gameDisplay, green, (80, 400, 100, 50))
        pygame.draw.rect(gameDisplay, green, (205, 400, 100, 50))
        pygame.draw.rect(gameDisplay, green, (350, 400, 100, 50))
        pygame.draw.rect(gameDisplay, red, (500, 400, 100, 50))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(mouse)

        if menu1_x1 < mouse[0] < menu1_x1 + menu_width and menu1_y < mouse[1] < menu1_y + menu_height:
            pygame.draw.rect(gameDisplay, blue, (80, 400, 100, 50))
            if click[0] == 1:
                mode = 1
                pygame.display.set_icon(carImg)

        if menu1_x2 < mouse[0] < menu1_x2 + menu_width and menu1_y < mouse[1] < menu1_y + menu_height:
            pygame.draw.rect(gameDisplay, blue, (205, 400, 100, 50))
            if click[0] == 1:
                mode = 2

        if menu1_x3 < mouse[0] < menu1_x3 + menu_width and menu1_y < mouse[1] < menu1_y + menu_height:
            pygame.draw.rect(gameDisplay, blue, (350, 400, 100, 50))
            if click[0] == 1:
                mode = 3
                pygame.display.set_icon(spImg)

        if menu2_x < mouse[0] < menu2_x + menu_width and menu2_y < mouse[1] < menu2_y + menu_height:
            pygame.draw.rect(gameDisplay, blue, (500, 400, 100, 50))
            if click[0] == 1:
                pygame.quit()
                quit()

        message_display("Road bash", 20, menu1_x1 + menu_width / 2, menu1_y + menu_height / 2)
        message_display("Aqua assault", 15, menu1_x2 + menu_width / 2, menu1_y + menu_height / 2)
        message_display("Space race", 20, menu1_x3 + menu_width / 2, menu1_y + menu_height / 2)
        message_display("Exit", 40, menu2_x + menu_width / 2, menu2_y + menu_height / 2)

        pygame.display.update()
        clock.tick(50)


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


# noinspection PyShadowingNames
def crash(x, y):
    gameDisplay.blit(crash_img, (x, y))
    message_display("You Crashed", 115, display_width / 2, display_height / 2)
    pygame.display.update()
    time.sleep(2)
    global mode
    mode = 0
    commence()  # for restart the game
    if mode == 1:
        bgimage=bgImg
        vehicleimg=car2Img

    if mode == 2:
        bgimage=bgbtImg
        vehicleimg=boat2Img

    if mode == 3:
        bgimage = bgspImg
        vehicleimg = sp2Img
    gameloop(bgimage=bgimage,vehicleimg=vehicleimg)


def gameloop(bgimage, vehicleimg ):
    # pygame.mixer.Sound.stop()
    from Hand_detection import stroke,hand
    pygame.mixer.music.play(-1)
    bg_x1 = 0
    bg_x2 = 0
    bg_y1 = 0
    bg_y2 = -600
    bg_speed = 6

    veh_x = ((display_width / 2) - (car_width / 2))
    veh_y = (display_height - car_height)
    car_x_change = 0

    thing_startx = random.randrange(0, 800)
    thing_starty = -600
    thingw = 50
    thingh = 100
    thing_speed = 3
    count = 0
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN or stroke:
                if event.key == pygame.K_LEFT or hand==1:
                    car_x_change = -5
                elif event.key == pygame.K_RIGHT or hand==2:
                    car_x_change = 5

            if event.type == pygame.KEYUP or stroke==0:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or hand:
                    car_x_change = 0

        veh_x += car_x_change

        if veh_x > 800 - car_width:
            crash(veh_x, veh_y)
        if veh_x < 0:
            crash(veh_x - car_width, veh_y)

        if veh_y < thing_starty + thingh:
            if veh_x >= thing_startx and veh_x <= thing_startx + thingw:
                crash(veh_x - 25, veh_y - car_height / 2)
            if veh_x + car_width >= thing_startx and veh_x + car_width <= thing_startx + thingw:
                crash(veh_x, veh_y - car_height / 2)

        gameDisplay.fill(green)  # display green background

        gameDisplay.blit(bgimage, (bg_x1, bg_y1))
        gameDisplay.blit(bgimage, (bg_x2, bg_y2))
        if bgimage == bgImg:
            vehicle(veh_x, veh_y, carImg)
        if bgimage == bgbtImg :
            vehicle(veh_x, veh_y, boatImg)
        if bgimage == bgspImg :
            vehicle(veh_x, veh_y, spImg)

        draw_things(thing_startx, thing_starty, vehicleimg)
        highscore(count)
        count += 1
        thing_speed += 0.05
        thing_starty += thing_speed

        if thing_starty > display_height:
            thing_startx = random.randrange(0, 800)
            thing_starty = -200

        bg_y1 += bg_speed
        bg_y2 += bg_speed

        if bg_y1 >= display_height:
            bg_y1 = -600

        if bg_y2 >= display_height:
            bg_y2 = -600

        pygame.display.update()  # update the screen
        clock.tick(60)  # frame per sec

commence()
if mode == 1:
    bgimage = bgImg
    vehicleimg = car2Img

if mode == 2:
    bgimage = bgbtImg
    vehicleimg = boat2Img

if mode == 3:
    bgimage = bgspImg
    vehicleimg = sp2Img
gameloop(bgimage=bgimage, vehicleimg=vehicleimg)
