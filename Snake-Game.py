import pygame
import time
import random

# Game settings
INITIAL_SNAKE_SPEED = 10  # Starting speed
SNAKE_SPEED_INCREMENT = 1  # Speed increase per score milestone
SNAKE_SPEED_ACCELERATION = 0.2  # Acceleration after reaching high score
SCORE_THRESHOLD = 10  # Score at which speed increases slightly
SECOND_SPEED_THRESHOLD = 50  # Score threshold for faster increases
MAX_SPEED = 25  # Max speed of the snake

WINDOW_WIDTH = 720
WINDOW_HEIGHT = 480

# Colors
COLOR_BLACK = pygame.Color(0, 0, 0)
COLOR_WHITE = pygame.Color(255, 255, 255)
COLOR_RED = pygame.Color(255, 0, 0)
COLOR_GREEN = pygame.Color(0, 255, 0)
COLOR_BLUE = pygame.Color(0, 0, 255)
COLOR_YELLOW = pygame.Color(255, 255, 0)

# Initialize pygame
pygame.init()

# Initialize the mixer for sound effects and music
pygame.mixer.init()

# Load sound effects
eat_sound = pygame.mixer.Sound('eating.mp3')  # Replace with your file path
game_over_sound = pygame.mixer.Sound('over.mp3')  # Replace with your file path

# Load and play background music
pygame.mixer.music.load('background.mp3')  # Replace with your file path
pygame.mixer.music.play(-1, 0.0)  # Loop the music indefinitely

# Create game window
pygame.display.set_caption('Snake Game')
game_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set FPS controller
clock = pygame.time.Clock()

# Snake initial position and body structure
snake_head_position = [100, 50]
snake_body_segments = [[100, 50], [90, 50], [80, 50], [70, 50]]

# Fruit initial position
fruit_position = [random.randrange(1, (WINDOW_WIDTH // 10)) * 10, 
                  random.randrange(1, (WINDOW_HEIGHT // 10)) * 10]
fruit_available = True

# Big fruit variables
big_fruit_position = [0, 0]
big_fruit_available = False
big_fruit_eaten = False

# Player score and small fruit count
player_score = 0
small_fruit_count = 0

# Initial movement direction
current_direction = 'RIGHT'
next_direction = current_direction

def display_score(font_color, font_style, font_size):
    font = pygame.font.SysFont(font_style, font_size)
    score_surface = font.render('Score: ' + str(player_score), True, font_color)
    score_rect = score_surface.get_rect()
    game_screen.blit(score_surface, score_rect)

def handle_game_over():
    font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = font.render('Your Score: ' + str(player_score), True, COLOR_RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 4)
    
    # Display the Game Over message
    game_screen.blit(game_over_surface, game_over_rect)
    
    # Game over background (optional)
    pygame.draw.rect(game_screen, COLOR_BLACK, (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT), width=0)
    
    # Display play again or quit message
    font = pygame.font.SysFont('times new roman', 30)
    play_again_surface = font.render('Press C to Play Again or Q to Quit', True, COLOR_WHITE)
    play_again_rect = play_again_surface.get_rect()
    play_again_rect.midtop = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    game_screen.blit(play_again_surface, play_again_rect)

    pygame.display.flip()
    game_over_sound.play()  # Play sound when the game is over

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    # Reset the game
                    reset_game()
                    waiting_for_input = False

def reset_game():
    global snake_head_position, snake_body_segments, fruit_position, fruit_available, big_fruit_position, big_fruit_available, big_fruit_eaten, player_score, small_fruit_count, current_direction
    snake_head_position = [100, 50]
    snake_body_segments = [[100, 50], [90, 50], [80, 50], [70, 50]]
    fruit_position = [random.randrange(1, (WINDOW_WIDTH // 10)) * 10, 
                      random.randrange(1, (WINDOW_HEIGHT // 10)) * 10]
    fruit_available = True
    big_fruit_position = [0, 0]
    big_fruit_available = False
    big_fruit_eaten = False
    player_score = 0
    small_fruit_count = 0
    current_direction = 'RIGHT'

# Main game loop
SNAKE_SPEED = INITIAL_SNAKE_SPEED  # Starting speed

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # This handles the window close button
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                next_direction = 'UP'
            if event.key == pygame.K_DOWN:
                next_direction = 'DOWN'
            if event.key == pygame.K_LEFT:
                next_direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                next_direction = 'RIGHT'

    # Ensure the snake does not reverse
    if next_direction == 'UP' and current_direction != 'DOWN':
        current_direction = 'UP'
    if next_direction == 'DOWN' and current_direction != 'UP':
        current_direction = 'DOWN'
    if next_direction == 'LEFT' and current_direction != 'RIGHT':
        current_direction = 'LEFT'
    if next_direction == 'RIGHT' and current_direction != 'LEFT':
        current_direction = 'RIGHT'

    # Move snake head
    if current_direction == 'UP':
        snake_head_position[1] -= 10
    if current_direction == 'DOWN':
        snake_head_position[1] += 10
    if current_direction == 'LEFT':
        snake_head_position[0] -= 10
    if current_direction == 'RIGHT':
        snake_head_position[0] += 10

    # Snake eating fruit logic
    snake_body_segments.insert(0, list(snake_head_position))
    if snake_head_position[0] == fruit_position[0] and snake_head_position[1] == fruit_position[1]:
        player_score += 10
        small_fruit_count += 1
        eat_sound.play()  # Play sound when fruit is eaten
        fruit_available = False
    else:
        snake_body_segments.pop()

    # Spawn a big fruit after eating 5 small fruits
    if small_fruit_count >= 5 and not big_fruit_available:
        big_fruit_position = [random.randrange(1, (WINDOW_WIDTH // 10)) * 10, 
                              random.randrange(1, (WINDOW_HEIGHT // 10)) * 10]
        big_fruit_available = True
        small_fruit_count = 0  # Reset small fruit count after spawning big fruit

    # Check if snake eats the big fruit
    if big_fruit_available and snake_head_position[0] == big_fruit_position[0] and snake_head_position[1] == big_fruit_position[1]:
        player_score += 50  # Big fruit gives more points
        big_fruit_eaten = True
        eat_sound.play()  # Play sound when big fruit is eaten
        big_fruit_available = False
        small_fruit_count = 0  # Reset small fruit count after eating a big fruit
        snake_body_segments.append(snake_body_segments[-1])  # Grow snake after eating big fruit

    if not fruit_available:
        fruit_position = [random.randrange(1, (WINDOW_WIDTH // 10)) * 10, 
                          random.randrange(1, (WINDOW_HEIGHT // 10)) * 10]
        fruit_available = True

    # Increase difficulty based on score
    if player_score >= SECOND_SPEED_THRESHOLD:
        # Fastest speed (more significant increase)
        SNAKE_SPEED = INITIAL_SNAKE_SPEED + (SNAKE_SPEED_INCREMENT * (player_score // SECOND_SPEED_THRESHOLD))
        if SNAKE_SPEED > MAX_SPEED:
            SNAKE_SPEED = MAX_SPEED
    elif player_score >= SCORE_THRESHOLD:
        # Increase speed after every 10 points
        SNAKE_SPEED = INITIAL_SNAKE_SPEED + (SNAKE_SPEED_INCREMENT * (player_score // SCORE_THRESHOLD))

    # Update screen
    game_screen.fill(COLOR_BLACK)
    
    # Draw snake
    for segment in snake_body_segments:
        pygame.draw.rect(game_screen, COLOR_GREEN, pygame.Rect(segment[0], segment[1], 10, 10))
    
    # Draw fruit
    pygame.draw.rect(game_screen, COLOR_WHITE, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
    
    # Draw big fruit if available
    if big_fruit_available:
        pygame.draw.rect(game_screen, COLOR_YELLOW, pygame.Rect(big_fruit_position[0], big_fruit_position[1], 20, 20))  # Big fruit is larger

    # Check for collisions with wall
    if snake_head_position[0] < 0 or snake_head_position[0] >= WINDOW_WIDTH:
        handle_game_over()
    if snake_head_position[1] < 0 or snake_head_position[1] >= WINDOW_HEIGHT:
        handle_game_over()

    # Check for collisions with itself
    if snake_head_position in snake_body_segments[1:]:
        handle_game_over()

    # Display score
    display_score(COLOR_WHITE, 'times new roman', 20)

    # Update the game window
    pygame.display.update()

    # Control the speed of the snake
    clock.tick(SNAKE_SPEED)
