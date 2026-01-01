import pygame
import time, random, cv2
from game.utils import vehicle,draw_things,highscore,message_display
from game.media import *
mode = 0


import pygame_gui


def commence():
    global mode
    mode = 0
    
    # UI Manager
    manager = pygame_gui.UIManager((display_width, display_height), 'theme.json')
    
    # Layout constants
    center_x = display_width / 2
    start_y = 200
    gap = 60
    btn_size = (250, 50)
    
    # Create Title Label
    title_rect = pygame.Rect(0, 80, display_width, 80)
    pygame_gui.elements.UILabel(relative_rect=title_rect,
                                text='VVPSA RACING',
                                manager=manager,
                                object_id='#main_menu_title')

    # Create Buttons
    btn_road = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((center_x - btn_size[0]/2, start_y), btn_size),
                                            text='ROAD BASH',
                                            manager=manager)
                                            
    btn_aqua = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((center_x - btn_size[0]/2, start_y + gap), btn_size),
                                            text='AQUA ASSAULT',
                                            manager=manager)
                                            
    btn_space = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((center_x - btn_size[0]/2, start_y + gap*2), btn_size),
                                             text='SPACE RACE',
                                             manager=manager)
                                             
    btn_exit = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((center_x - btn_size[0]/2, start_y + gap*3), btn_size),
                                            text='EXIT GAME',
                                            manager=manager)

    clock = pygame.time.Clock()

    while mode == 0:
        time_delta = clock.tick(60)/1000.0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            # Pass events to UI Manager
            manager.process_events(event)
            
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == btn_road:
                    mode = 1
                    pygame.display.set_icon(carImg)
                if event.ui_element == btn_aqua:
                    mode = 2
                if event.ui_element == btn_space:
                    mode = 3
                    pygame.display.set_icon(spImg)
                if event.ui_element == btn_exit:
                    pygame.quit()
                    quit()

        manager.update(time_delta)
        
        gameDisplay.fill(bcolor) # Keep background color or change to theme dark
        gameDisplay.fill(bcolor) # Use theme background for menu

        
        manager.draw_ui(gameDisplay)
        pygame.display.update()




def crash(x, y):
    # Create a local manager for the crash screen
    manager = pygame_gui.UIManager((display_width, display_height), 'theme.json')
    
    # Game Over Window
    rect = pygame.Rect(0, 0, 400, 300)
    rect.center = (display_width/2, display_height/2)
    
    window = pygame_gui.elements.UIWindow(rect=rect,
                                          manager=manager,
                                          window_display_title="GAME OVER")
                                          
    pygame_gui.elements.UILabel(relative_rect=pygame.Rect(0, 50, 360, 50),
                                text="YOU CRASHED!",
                                manager=manager,
                                container=window,
                                object_id='#main_menu_title') # Re-use big font
                                
    restart_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(80, 150, 200, 50),
                                               text='MAIN MENU',
                                               manager=manager,
                                               container=window)

    running = True
    clock = pygame.time.Clock()
    
    while running:
        time_delta = clock.tick(60)/1000.0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            manager.process_events(event)
            
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == restart_btn:
                    running = False
                    
        manager.update(time_delta)
        # Draw semi-transparent overlay
        s = pygame.Surface((display_width,display_height))
        s.set_alpha(10)
        s.fill((0,0,0))
        gameDisplay.blit(s, (0,0))
        
        manager.draw_ui(gameDisplay)
        pygame.display.update()

    global mode
    mode = 0
    commence()  # for restart the game
    
    bgimage = None
    vehicleimg = None
    
    if mode == 1:
        bgimage=bgImg
        vehicleimg=car2Img

    if mode == 2:
        bgimage=bgbtImg
        vehicleimg=boat2Img

    if mode == 3:
        bgimage = bgspImg
        vehicleimg = sp2Img
        
    if bgimage is not None:
        gameloop(bgimage=bgimage,vehicleimg=vehicleimg)

def gameloop(bgimage, vehicleimg ):
    # pygame.mixer.Sound.stop()
    import game.Hand_detection as h
    
    # In-Game UI Manager
    manager = pygame_gui.UIManager((display_width, display_height), 'theme.json')
    score_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(10, 10, 200, 50),
                                              text="Score: 0",
                                              manager=manager)
    
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
    detector = h.HandDetector(maxHands=1)
    cap = cv2.VideoCapture(0)

    clock = pygame.time.Clock() # Ensure we have local clock ref if needed, usually global

    while not gameExit:
        time_delta = clock.tick(60)/1000.0
        
        stroke = 0
        ret, image = cap.read()
        if not ret:
            continue
            
        # Flip image for mirror view
        image = cv2.flip(image, 1)
        
        image = detector.findHands(image)
        lmList = detector.findPosition(image)
        
        if len(lmList) != 0:
            # Tip of Index Finger is id 8
            x1 = lmList[8][1]
            
            # Screen width for camera is usually 640. Center is 320.
            if x1 < 320:
                car_x_change = -6
            else:
                car_x_change = 6
        else:
            # If no hand is detected, we can either stop or keep momentum. 
            pass


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                quit()
            manager.process_events(event)
            
        veh_x += car_x_change
        # car_x_change /= (abs(car_x_change)+1) # Removed friction for cleaner control

        if veh_x > 800 - car_width:
            crash(veh_x, veh_y)
            return # Exit loop after crash
        if veh_x < 0:
            crash(veh_x - car_width, veh_y)
            return

        if veh_y < thing_starty + thingh:
            if veh_x >= thing_startx and veh_x <= thing_startx + thingw:
                crash(veh_x - 25, veh_y - car_height / 2)
                return
            if veh_x + car_width >= thing_startx and veh_x + car_width <= thing_startx + thingw:
                crash(veh_x, veh_y - car_height / 2)
                return

        gameDisplay.fill(green)  # display green background

        gameDisplay.blit(bgimage, (bg_x1, bg_y1))
        gameDisplay.blit(bgimage, (bg_x2, bg_y2))
        
        # Show the camera feed with landmarks
        cv2.imshow("Hand Controller", image)
        
        if bgimage == bgImg:
            vehicle(veh_x, veh_y, carImg)
        if bgimage == bgbtImg:
            vehicle(veh_x, veh_y, boatImg)
        if bgimage == bgspImg:
            vehicle(veh_x, veh_y, spImg)

        draw_things(thing_startx, thing_starty, vehicleimg)
        
        # Update Score Label
        score_label.set_text("Score: " + str(count))
        
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
        
        # Update and Draw UI
        manager.update(time_delta)
        manager.draw_ui(gameDisplay)

        pygame.display.update()  # update the screen
        # clock.tick(60) # Moved to top

        k = cv2.waitKey(1)
        if k == 32:
            break
    cap.release()
    cv2.destroyAllWindows()

