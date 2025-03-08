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

# setting up the snakes default postion 
Postion_Of_Snake = [100, 50]

#setting up frist 4 blocks of the snakes body 
Body_Of_Snake = [[100, 50], [90, 50], [80, 50], [70, 50]]

# positon of the Fruit & spwan of fruit
Position_of_Fruit = [random.randrange(1, (Size_Window_x//10)) * 10, random.randrange(1, (Size_Window_y//10)) * 10]
Spawn_Fruit = True 

# making the default direction for the snake to the right direction 
Direction = 'RIGHT'
change_To = Direction

# Starting score 
Score = 0

# showing the score function
def Show_Score(choice, color, font, size):

    # seeting up font object for score_font
    Score_font = pygame.font.SysFont(font, size)

    # setting the dispay for the surface object 
    Score_Surface = Score_font.render('Score : ' + str(Score), True, color)

    # Adding a rectangule object for the text surface object 
    Score_Rect =  Score_Surface.get_rect()

    # showing the text
    game_window.blit(Score_Surface, Score_Rect)

# function for Game over 
def Game_Over():

    # setting up font object for my_font
    My_Font = pygame.font.SysFont('times new roman', 50)

    # adding a text surface where text will be displayed
    Game_Over_Surface = My_Font.render('Your Score is : ' + str(Score), True, red)

    # Adding a rectangule object for the text surface object
    Game_Over_Rect = Game_Over_Surface.get_rect()

    # adding postion for the text
    Game_Over_Rect.midtop = (Size_Window_x/2, Size_Window_y/4)

    # blit will draw the text on screen
    game_window.blit(Game_Over_Surface, Game_Over_Rect)
    pygame.display.flip()
    