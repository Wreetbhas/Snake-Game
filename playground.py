import pygame, sys, utils
from button import Button


def run(SCREEN):
    pygame.display.set_caption("Snake Game - Select Playground")

    while True:
        SCREEN.fill(utils.white)

        GR1_BUTTON = Button(pos=(400, 150), text_input="PLAYGROUND 1", font=utils.get_font('times new roman', 50), hovering_color="red", selected_color="green", deselected_color="black")
        GR2_BUTTON = Button(pos=(400, 250), text_input="PLAYGROUND 2", font=utils.get_font('times new roman', 50), hovering_color="red", selected_color="green", deselected_color="black")
        GR3_BUTTON = Button(pos=(400, 350), text_input="PLAYGROUND 3", font=utils.get_font('times new roman', 50), hovering_color="red", selected_color="green", deselected_color="black")

        ground_no = utils.playground_no            

        if ground_no == 1:
            GR1_BUTTON.select()            
        elif ground_no == 2:
            GR2_BUTTON.select()
        else:
            GR3_BUTTON.select()        

        BACK_BUTTON = Button(pos=(400, 450), text_input="BACK", font=utils.get_font('Calibri', 25), hovering_color="red", selected_color="green", deselected_color="black")

        MOUSE_POS = pygame.mouse.get_pos()

        for button in [GR1_BUTTON, GR2_BUTTON, GR3_BUTTON, BACK_BUTTON]:
            button.render(MOUSE_POS, SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GR1_BUTTON.isClicked(MOUSE_POS):
                    GR1_BUTTON.select()  
                    GR2_BUTTON.deselect()
                    GR3_BUTTON.deselect()

                    utils.playground_no = 1
                    utils.blocks = set()            
                    
                if GR2_BUTTON.isClicked(MOUSE_POS):
                    GR2_BUTTON.select()  
                    GR1_BUTTON.deselect()
                    GR3_BUTTON.deselect()

                    utils.playground_no = 2
                    utils.blocks = set()

                    # generating coordinate of each block of boundary  
                    for i in range(0,utils.length,10):
                        utils.blocks.add((i,10))
                    for i in range(20,utils.breadth,10):
                        utils.blocks.add((utils.length-10,i))
                    for i in range(utils.length-20,-10,-10):
                        utils.blocks.add((i,utils.breadth-10))
                    for i in range(utils.breadth-20,10,-10):
                        utils.blocks.add((0,i))      
                    
                if GR3_BUTTON.isClicked(MOUSE_POS):
                    GR3_BUTTON.select()  
                    GR1_BUTTON.deselect()
                    GR2_BUTTON.deselect()

                    utils.playground_no = 3
                    utils.blocks = set()

                    # generating coordinate of each block of obstucles

                    # length of each obstucle is proportional to the length/breadth of window
                    # so, values of x and y are set according to the dimensions of window

                    x = ((utils.length//4)//10)*10
                    y = ((int(utils.breadth*0.75))//10)*10
                    for i in range(10,y,10):
                        utils.blocks.add((x,i))
                    
                    y += 30 
                    for i in range(0,x,10):
                        utils.blocks.add((i,y))

                    x = ((int(utils.length*0.75))//10)*10
                    y = ((utils.breadth//4)//10)*10
                    for i in range(x,utils.length,10):
                        utils.blocks.add((i,y))
                    
                    y += 40
                    for i in range(y,utils.breadth,10):
                        utils.blocks.add((x,i))

                if BACK_BUTTON.isClicked(MOUSE_POS):
                    return        


        pygame.display.update()