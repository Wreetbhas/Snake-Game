import pygame

# Window dimension
length = 800
breadth = 500

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
blue = pygame.Color(0,0,255)
green = pygame.Color(0,255,0)

# initialize playground type
playground_no = 1

#initialize snake speed
low = 5
medium = 10
high = 15
snake_speed = medium

#initialize obstucles i.e. block positions
blocks = set()

def get_font(font,size):
    return pygame.font.SysFont(font, size)