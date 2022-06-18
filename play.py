import pygame, sys, utils, random, time
from button import Button

# check whether a coordinate lies outside window or not
def isOutside(pos):
    if (pos[0]<0 or pos[0]>utils.length-10) or (pos[1]<10 or pos[1]>utils.breadth-10):
        return True
    else:
        return False


# finding nearest neighbouring coordinate of the invalid fruit position
def find_pos(start, snake_body):

    length = 1
    bound1 = True
    bound2 = True
    bound3 = True
    bound4 = True

    while (bound1 == True) and (bound2 == True) and (bound3 == True) and (bound4 == True):
        
        length += 2

        start = start[0]-10, start[1]-10
        end = start[0]+(length*10)-10, start[1]

        if isOutside(start) and isOutside(end):
            bound1 = False

        if bound1 == True:
            temp = start

            while temp[0]<=end[0]:
                if (not isOutside(temp)) and (temp not in utils.blocks) and (temp not in snake_body):
                    return temp
                temp = temp[0]+10,temp[1]

        start = end
        end = start[0], start[1]+(length*10)-10

        if isOutside(start) and isOutside(end):
            bound2 = False

        if bound2 == True:
            temp = start

            while temp[1]<=end[1]:
                if (not isOutside(temp)) and (temp not in utils.blocks) and (temp not in snake_body):
                    return temp
                temp = temp[0],temp[1]+10

        start = end
        end = start[0]-(length*10)+10, start[1]

        if isOutside(start) and isOutside(end):
            bound3 = False

        if bound3 == True:
            temp = start

            while temp[0]>=end[0]:
                if (not isOutside(temp)) and (temp not in utils.blocks) and (temp not in snake_body):
                    return temp
                temp = temp[0]-10,temp[1]

        start = end
        end = start[0], start[1]-(length*10)+10

        if isOutside(start) and isOutside(end):
            bound4 = False

        if bound4 == True:
            temp = start

            while temp[1]>=end[1]:
                if (not isOutside(temp)) and (temp not in utils.blocks) and (temp not in snake_body):
                    return temp
                temp = temp[0],temp[1]-10

    return None  

def getRandPos(snake_body):
    fruit_position = (random.randrange(0, ((utils.length-10)//10)) * 10, random.randrange(10, ((utils.breadth-10)//10)) * 10)

    if (fruit_position in utils.blocks) or (fruit_position in snake_body):
        return find_pos(fruit_position, snake_body)
    
    return fruit_position


def show_score(SCREEN):
    score_font = pygame.font.SysFont('times new roman', 12)

    score_surface = score_font.render('Score : ' + str(score), True, utils.black)

    score_rect = score_surface.get_rect()

    score_rect.midtop = (utils.length//2, -2)

    SCREEN.blit(score_surface, score_rect)

def pause(SCREEN, NEW_BUTTON, BACK_BUTTON, PAUSE_BUTTON):

    while True:
        pygame.draw.rect(SCREEN, utils.white, pygame.Rect(0,0,utils.length,10))   
        CONTINUE_BUTTON = Button(pos=(75, 6), text_input="CONTINUE", font=utils.get_font('Calibri', 10), hovering_color="red", selected_color="green", deselected_color="black")        

        MOUSE_POS = pygame.mouse.get_pos()

        for button in [NEW_BUTTON, CONTINUE_BUTTON, BACK_BUTTON]:
            button.render(MOUSE_POS, SCREEN)

        show_score(SCREEN)        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NEW_BUTTON.isClicked(MOUSE_POS):
                    run(SCREEN)
                if CONTINUE_BUTTON.isClicked(MOUSE_POS):
                    pygame.draw.rect(SCREEN, utils.white, pygame.Rect(60,0,40,10)) 
                    PAUSE_BUTTON.render(MOUSE_POS, SCREEN)
                    return
                if BACK_BUTTON.isClicked(MOUSE_POS):
                    import main
                    main.run()            

        pygame.display.update()       


def game_over(SCREEN):
    time.sleep(1)

    SCREEN.fill(utils.white)

    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)
	
	# creating a text surface on which text
	# will be drawn
    game_over_surface = my_font.render('Your Score : ' + str(score), True, utils.black)
	
	# create a rectangular object for the text
	# surface object
    game_over_rect = game_over_surface.get_rect()
	
	# setting position of the text
    game_over_rect.midtop = (utils.length/2, utils.breadth/4)
	
	# blit will draw the text on screen
    SCREEN.blit(game_over_surface, game_over_rect)

    while True:
        NEW_BUTTON = Button(pos=((utils.length/2)-80, utils.breadth/2), text_input="NEW GAME", font=utils.get_font('times new roman', 25), hovering_color="red", selected_color="green", deselected_color="black")
        BACK_BUTTON = Button(pos=((utils.length/2)+125, utils.breadth/2), text_input="BACK", font=utils.get_font('times new roman', 25), hovering_color="red", selected_color="green", deselected_color="black")

        MOUSE_POS = pygame.mouse.get_pos()
        
        for button in [NEW_BUTTON, BACK_BUTTON]:
            button.render(MOUSE_POS, SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NEW_BUTTON.isClicked(MOUSE_POS):
                    run(SCREEN)
                if BACK_BUTTON.isClicked(MOUSE_POS):
                    import main
                    main.run()            
            
        pygame.display.update() 

def run(SCREEN):
    pygame.display.set_caption('Snake Game - Play')

    # initial score
    global score
    score = 0

    # FPS (frames per second) controller
    fps = pygame.time.Clock()

    # defining snake default position
    snake_position = [50, 50]

    # defining first 4 blocks of snake body
    snake_body = [(50, 50),
                  (40, 50),
                  (30, 50),
                  (20, 50)
                 ]

    snake_body_set = set(snake_body)

    fruit_position = getRandPos(snake_body_set)
    fruit_spawn = True

    SCREEN.fill(utils.blue)

    pygame.draw.rect(SCREEN, utils.white, pygame.Rect(0,0,utils.length,10))   

    NEW_BUTTON = Button(pos=(25, 6), text_input="NEW GAME", font=utils.get_font('Calibri', 10), hovering_color="red", selected_color="green", deselected_color="black")
    PAUSE_BUTTON = Button(pos=(75, 6), text_input="PAUSE", font=utils.get_font('Calibri', 10), hovering_color="red", selected_color="green", deselected_color="black")        
    BACK_BUTTON = Button(pos=(115, 6), text_input="BACK", font=utils.get_font('Calibri', 10), hovering_color="red", selected_color="green", deselected_color="black")

    MOUSE_POS = pygame.mouse.get_pos()

    for button in [NEW_BUTTON, PAUSE_BUTTON, BACK_BUTTON]:
        button.render(MOUSE_POS, SCREEN)

    for pos in utils.blocks:
        pygame.draw.rect(SCREEN, utils.red, pygame.Rect(pos[0], pos[1], 10, 10))     

    pygame.draw.rect(SCREEN, utils.black, pygame.Rect(snake_position[0], snake_position[1], 10, 10))

    for pos in snake_body[1:]:
        pygame.draw.rect(SCREEN, utils.green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(SCREEN, utils.white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))     

    # default snake direction
    direction = 'RIGHT'
    change_to = direction

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if NEW_BUTTON.isClicked(MOUSE_POS):
                    run(SCREEN)
                if PAUSE_BUTTON.isClicked(MOUSE_POS):
                    pause(SCREEN, NEW_BUTTON, BACK_BUTTON, PAUSE_BUTTON)
                if BACK_BUTTON.isClicked(MOUSE_POS):
                    import main
                    main.run()
                
            
        # Snake cannot go towards opposite of the direction currently moving
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            if snake_position[1] > 10:
                snake_position[1] -= 10
            else:
                snake_position[1] = utils.breadth - 10
        if direction == 'DOWN':
            if snake_position[1] < utils.breadth:
                snake_position[1] += 10
            else:
                snake_position[1] = 10
        if direction == 'LEFT':
            if snake_position[0] > 0:
                snake_position[0] -= 10
            else:
                snake_position[0] = utils.length - 10
        if direction == 'RIGHT':
            if snake_position[0] < utils.length:
                snake_position[0] += 10
            else:
                snake_position[0] = 0

        # Snake body growing mechanism
        # if fruits and snakes collide then scores
        # will be incremented by 10
        snake_body.insert(0, tuple(snake_position))
        snake_body_set.add(tuple(snake_position))
        pygame.draw.rect(SCREEN, utils.green, pygame.Rect(snake_body[1][0], snake_body[1][1], 10, 10))
        pygame.draw.rect(SCREEN, utils.black, pygame.Rect(snake_position[0], snake_position[1], 10, 10))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            poped = snake_body.pop()
            pygame.draw.rect(SCREEN, utils.blue, pygame.Rect(poped[0], poped[1], 10, 10))
            snake_body_set.remove(tuple(poped))

        if not fruit_spawn:
            fruit_position = getRandPos(snake_body_set)

        if fruit_position == None:
            game_over(SCREEN)

        fruit_spawn = True

        pygame.draw.rect(SCREEN, utils.white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))  

        # Game Over conditions
        if tuple(snake_position) in utils.blocks:
            game_over(SCREEN)
        
        # Touching the snake body
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over(SCREEN)   

        pygame.draw.rect(SCREEN, utils.white, pygame.Rect(0,0,utils.length,10))   

        NEW_BUTTON = Button(pos=(25, 6), text_input="NEW GAME", font=utils.get_font('Calibri', 10), hovering_color="red", selected_color="green", deselected_color="black")
        PAUSE_BUTTON = Button(pos=(75, 6), text_input="PAUSE", font=utils.get_font('Calibri', 10), hovering_color="red", selected_color="green", deselected_color="black")        
        BACK_BUTTON = Button(pos=(115, 6), text_input="BACK", font=utils.get_font('Calibri', 10), hovering_color="red", selected_color="green", deselected_color="black")

        MOUSE_POS = pygame.mouse.get_pos()

        for button in [NEW_BUTTON, PAUSE_BUTTON, BACK_BUTTON]:
            button.render(MOUSE_POS, SCREEN)

        show_score(SCREEN)

        # Refresh game screen
        pygame.display.update()

        # Frame Per Second /Refresh Rate
        fps.tick(utils.snake_speed)
