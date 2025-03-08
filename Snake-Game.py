# setting up the libraries 
import pygame
import time 
import random 

# speed of the snake
Speed_Of_Snake = 15

# size of the window 
Size_Window_x = 720
Size_Window_y = 480

# Important colors 
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# setting up pygame
pygame.init()

# setting up the game window 
pygame.display.set_caption('Snake-Game; Dagimawi')
game_window = pygame.display.set_mode((Size_Window_x , Size_Window_y))

#controller for the fps 
fps = pygame.time.Clock()

