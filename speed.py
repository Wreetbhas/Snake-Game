import pygame, sys, utils
from button import Button


def run(SCREEN):
    pygame.display.set_caption("Snake Game - Change Snake Speed")

    while True:
        SCREEN.fill(utils.white)

        LOW_BUTTON = Button(pos=(400, 150), text_input="LOW", font=utils.get_font('times new roman', 50), hovering_color="red", selected_color="green", deselected_color="black")
        MEDIUM_BUTTON = Button(pos=(400, 250), text_input="MEDIUM", font=utils.get_font('times new roman', 50), hovering_color="red", selected_color="green", deselected_color="black")
        HIGH_BUTTON = Button(pos=(400, 350), text_input="HIGH", font=utils.get_font('times new roman', 50), hovering_color="red", selected_color="green", deselected_color="black")

        speed = utils.snake_speed

        if speed == utils.low:
            LOW_BUTTON.select()            
        elif speed == utils.medium:
            MEDIUM_BUTTON.select()
        else:
            HIGH_BUTTON.select()

        BACK_BUTTON = Button(pos=(400, 450), text_input="BACK", font=utils.get_font('Calibri', 25), hovering_color="red", selected_color="green", deselected_color="black")

        MOUSE_POS = pygame.mouse.get_pos()

        for button in [LOW_BUTTON, MEDIUM_BUTTON, HIGH_BUTTON, BACK_BUTTON]:
            button.render(MOUSE_POS, SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LOW_BUTTON.isClicked(MOUSE_POS):
                    LOW_BUTTON.select()
                    MEDIUM_BUTTON.deselect()
                    HIGH_BUTTON.deselect()

                    utils.snake_speed = utils.low

                if MEDIUM_BUTTON.isClicked(MOUSE_POS):
                    MEDIUM_BUTTON.select()
                    LOW_BUTTON.deselect()
                    HIGH_BUTTON.deselect()

                    utils.snake_speed = utils.medium

                if HIGH_BUTTON.isClicked(MOUSE_POS):
                    HIGH_BUTTON.select()
                    LOW_BUTTON.deselect()
                    MEDIUM_BUTTON.deselect()

                    utils.snake_speed = utils.high

                if BACK_BUTTON.isClicked(MOUSE_POS):
                    return 
        pygame.display.update()
                
                

            
