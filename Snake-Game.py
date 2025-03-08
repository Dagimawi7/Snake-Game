import pygame
import time
import random

# Game settings
SNAKE_SPEED = 15
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 480

# Colors
COLOR_BLACK = pygame.Color(0, 0, 0)
COLOR_WHITE = pygame.Color(255, 255, 255)
COLOR_RED = pygame.Color(255, 0, 0)
COLOR_GREEN = pygame.Color(0, 255, 0)
COLOR_BLUE = pygame.Color(0, 0, 255)

# Initialize pygame
pygame.init()

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

# Initial movement direction
current_direction = 'RIGHT'
next_direction = current_direction

# Player score
player_score = 0

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
    game_screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Main game loop
while True:
    for event in pygame.event.get():
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
        fruit_available = False
    else:
        snake_body_segments.pop()
        
    if not fruit_available:
        fruit_position = [random.randrange(1, (WINDOW_WIDTH // 10)) * 10, 
                          random.randrange(1, (WINDOW_HEIGHT // 10)) * 10]
        fruit_available = True

    # Update screen
    game_screen.fill(COLOR_BLACK)
    
    # Draw snake
    for segment in snake_body_segments:
        pygame.draw.rect(game_screen, COLOR_GREEN, pygame.Rect(segment[0], segment[1], 10, 10))
    
    # Draw fruit
    pygame.draw.rect(game_screen, COLOR_WHITE, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Check for collisions with wall
    if snake_head_position[0] < 0 or snake_head_position[0] >= WINDOW_WIDTH:
        handle_game_over()
    if snake_head_position[1] < 0 or snake_head_position[1] >= WINDOW_HEIGHT:
        handle_game_over()

    # Check for collisions with itself
    for segment in snake_body_segments[1:]:
        if snake_head_position[0] == segment[0] and snake_head_position[1] == segment[1]:
            handle_game_over()

    # Display score
    display_score(COLOR_WHITE, 'times new roman', 20)
    
    # Refresh game screen
    pygame.display.update()
    
    # Control game speed
    clock.tick(SNAKE_SPEED)
