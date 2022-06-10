import pygame, sys, utils, playground, speed
from button import Button

def run(SCREEN):
    pygame.display.set_caption("Snake Game - Settings")

    while True:
        SCREEN.fill(utils.white)

        MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = utils.get_font('times new roman', 100).render("SETTINGS", True, "black")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 50))

        PLAYGROUND_BUTTON = Button(pos=(400, 200), text_input="SELECT PLAYGROUND", font=utils.get_font('Calibri', 50), hovering_color="red", selected_color="green", deselected_color="black")
        SPEED_BUTTON = Button(pos=(400, 300), text_input="CHANGE SNAKE SPEED", font=utils.get_font('Calibri', 50), hovering_color="red", selected_color="green", deselected_color="black")
        BACK_BUTTON = Button(pos=(400, 400), text_input="BACK", font=utils.get_font('Calibri', 50), hovering_color="red", selected_color="green", deselected_color="black")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAYGROUND_BUTTON, SPEED_BUTTON, BACK_BUTTON]:
            button.render(MOUSE_POS, SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAYGROUND_BUTTON.isClicked(MOUSE_POS):
                    playground.run(SCREEN)
                if SPEED_BUTTON.isClicked(MOUSE_POS):
                    speed.run(SCREEN)
                if BACK_BUTTON.isClicked(MOUSE_POS):
                    return

        pygame.display.update()



