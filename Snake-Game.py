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
    
    # game will quit after 3 seconds
    time.sleep(3)

    # shutting off pygame
    pygame.quit()
    # shutting off the program
    quit()

    # Main function 
    while True:
        # dealing with key events 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
        
        # If I press 2 keys together. I don't want to move 2 dierctions together
        if change_to == 'UP' and Direction != 'DOWN':
            Direction = 'UP'
        if change_to == 'DOWN' and Direction != 'UP':
            Direction = 'DOWN'
        if change_to == 'LEFT' and Direction != 'RIGHT':
            Direction = 'LEFT'
        if change_to == 'RIGHT' and Direction != 'LEFT':
            Direction = 'RIGHT'
        
        # moving the snake
        if Direction == 'UP':
            Postion_Of_Snake[1] -= 10
        if Direction == 'DOWN':
            Postion_Of_Snake[1] += 10
        if Direction == 'LEFT':
            Postion_Of_Snake[0] -= 10
        if Direction == 'RIGHT':
            Postion_Of_Snake[0] += 10
        
        # mechanism for growing the snakes body, if snake eats fruit socre +10
        Body_Of_Snake.insert(0, list(Postion_Of_Snake))
    if Postion_Of_Snake[0] == Position_of_Fruit[0] and Postion_Of_Snake[1] == Position_of_Fruit[1]:
        Score += 10
        Spawn_Fruit = False
    else:
        Body_Of_Snake.pop()
        
    if not Spawn_Fruit:
        Position_of_Fruit = [random.randrange(1, (Size_Window_x//10)) * 10, 
                          random.randrange(1, (Size_Window_y//10)) * 10]
        
    Spawn_Fruit = True
    game_window.fill(black)
    
    for pos in Body_Of_Snake:
        pygame.draw.rect(game_window, green, pygame.Rect(
          pos[0], pos[1], 10, 10))
        
    pygame.draw.rect(game_window, white, pygame.Rect(
      Position_of_Fruit[0], Position_of_Fruit[1], 10, 10))

    # condtions to end the game 
    if Postion_Of_Snake[0] < 0 or Postion_Of_Snake[0] > Size_Window_x-10:
        game_over()
    if Postion_Of_Snake[1] < 0 or Postion_Of_Snake[1] > Size_Window_y-10:
        game_over()
    # Touching the snakes body 
    for block in Body_Of_Snake[1:]:
        if Postion_Of_Snake[0] == block[0] and Postion_Of_Snake[1] == block[1]:
            game_over()
    
    # displaying score continuously
    Show_Score(1, white, 'times new roman', 20)
    
    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(Speed_Of_Snake)