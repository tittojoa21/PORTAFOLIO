import pygame
import random

pygame.init()

# Screen dimensions
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tron Game with AI')

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Game settings
block_size = 10
speed = 10

clock = pygame.time.Clock()

# Player and AI starting positions
player_pos = [100, 50]
ai_pos = [500, 350]

# Movement vectors
player_mov = [block_size, 0]
ai_mov = [-block_size, 0]

# Trails
player_trail = []
ai_trail = []

# Font for end game message
font = pygame.font.SysFont(None, 35)

def draw_trails(trails, color):
    for block in trails:
        pygame.draw.rect(screen, color, [block[0], block[1], block_size, block_size])

def message(msg, color):
    screen.fill(black)
    msg = font.render(msg, True, color)
    screen.blit(msg, [width / 6, height / 2])
    pygame.display.update()
    pygame.time.wait(2000)

def is_collision(x, y, trail, walls=True):
    if walls and (x < 0 or x >= width or y < 0 or y >= height):
        return True
    return [x, y] in trail

def ai_move(ai_pos, ai_mov, player_trail, ai_trail):
    # Check for immediate collision in the current direction
    next_pos = [ai_pos[0] + ai_mov[0], ai_pos[1] + ai_mov[1]]
    if is_collision(next_pos[0], next_pos[1], player_trail + ai_trail[:-1]):
        # Try to turn left
        new_mov = [-ai_mov[1], ai_mov[0]]
        next_pos = [ai_pos[0] + new_mov[0], ai_pos[1] + new_mov[1]]
        if not is_collision(next_pos[0], next_pos[1], player_trail + ai_trail[:-1]):
            return new_mov
        
        # If left is not an option, try to turn right
        new_mov = [ai_mov[1], -ai_mov[0]]
        next_pos = [ai_pos[0] + new_mov[0], ai_pos[1] + new_mov[1]]
        if not is_collision(next_pos[0], next_pos[1], player_trail + ai_trail[:-1]):
            return new_mov

        # No move is possible (trapped), continue forward and lose
        return ai_mov
    else:
        # No immediate collision, continue in the same direction
        return ai_mov

def game_loop():
    global player_pos, player_mov, ai_pos, ai_mov
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_mov = [-block_size, 0]
                elif event.key == pygame.K_RIGHT:
                    player_mov = [block_size, 0]
                elif event.key == pygame.K_UP:
                    player_mov = [0, -block_size]
                elif event.key == pygame.K_DOWN:
                    player_mov = [0, block_size]

        
        player_pos[0] += player_mov[0]
        player_pos[1] += player_mov[1]
        player_trail.append(list(player_pos))

        
        ai_mov = ai_move(ai_pos, ai_mov, player_trail, ai_trail)
        ai_pos[0] += ai_mov[0]
        ai_pos[1] += ai_mov[1]
        ai_trail.append(list(ai_pos))

        
        if (player_pos in player_trail[:-1] or
            player_pos in ai_trail or
            player_pos[0] < 0 or player_pos[0] >= width or
            player_pos[1] < 0 or player_pos[1] >= height):
            message("Player lost!", red)
            game_over = True

        if (ai_pos in ai_trail[:-1] or
            ai_pos in player_trail or
            ai_pos[0] < 0 or ai_pos[0] >= width or
            ai_pos[1] < 0 or ai_pos[1] >= height):
            message("AI lost!", blue)
            game_over = True
        screen.fill(black)

        
        draw_trails(player_trail, blue)
        draw_trails(ai_trail, red)

        
        pygame.display.update()

        
        if game_over:
            break

        clock.tick(speed)

    # Quit the game
    pygame.quit()
    quit()

# Start the game
game_loop()