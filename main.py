import pygame, sys, utils, play, settings
from button import Button

# Initialise game window
SCREEN = pygame.display.set_mode((utils.length, utils.breadth))
pygame.display.set_caption("Snake Game - Menu")


pygame.init()

def run():

    while True:
        SCREEN.fill(utils.white)

        MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = utils.get_font('times new roman', 100).render("MAIN MENU", True, "black")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 50))

        PLAY_BUTTON = Button(pos=(400, 200), text_input="PLAY", font=utils.get_font('Calibri', 50), hovering_color="red", selected_color="green", deselected_color="black")
        SETTINGS_BUTTON = Button(pos=(400, 300), text_input="SETTINGS", font=utils.get_font('Calibri', 50), hovering_color="red", selected_color="green", deselected_color="black")
        QUIT_BUTTON = Button(pos=(400, 400), text_input="QUIT", font=utils.get_font('Calibri', 50), hovering_color="red", selected_color="green", deselected_color="black")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, SETTINGS_BUTTON, QUIT_BUTTON]:
            button.render(MOUSE_POS, SCREEN)

        # handling key events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.isClicked(MOUSE_POS):
                    play.run(SCREEN)
                if SETTINGS_BUTTON.isClicked(MOUSE_POS):
                    settings.run(SCREEN)
                if QUIT_BUTTON.isClicked(MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()


run()

