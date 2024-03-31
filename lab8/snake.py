import pygame
import random

pygame.init()

print("Pygame initialized successfully.")

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRIDSIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRIDSIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRIDSIZE
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

print("Pygame window opened successfully.")

def draw_grid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x * GRIDSIZE, y * GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, WHITE, r)
            else:
                rr = pygame.Rect((x * GRIDSIZE, y * GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, BLACK, rr)

def main():
    print("Starting the game loop.")
    
    clock = pygame.time.Clock()
    snake_pos = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
    snake_direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
    snake_color = GREEN
    food_pos = (random.randint(0, GRID_WIDTH-1) * GRIDSIZE, random.randint(0, GRID_HEIGHT-1) * GRIDSIZE)
    food_color = RED
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != 'DOWN':
                    snake_direction = 'UP'
                elif event.key == pygame.K_DOWN and snake_direction != 'UP':
                    snake_direction = 'DOWN'
                elif event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                    snake_direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                    snake_direction = 'RIGHT'

        if snake_direction == 'UP':
            snake_pos.insert(0, (snake_pos[0][0], snake_pos[0][1] - GRIDSIZE))
        elif snake_direction == 'DOWN':
            snake_pos.insert(0, (snake_pos[0][0], snake_pos[0][1] + GRIDSIZE))
        elif snake_direction == 'LEFT':
            snake_pos.insert(0, (snake_pos[0][0] - GRIDSIZE, snake_pos[0][1]))
        elif snake_direction == 'RIGHT':
            snake_pos.insert(0, (snake_pos[0][0] + GRIDSIZE, snake_pos[0][1]))
        
        if snake_pos[0] in snake_pos[1:]:
            print("Snake collided with itself!")
            running = False
        if (snake_pos[0][0] >= SCREEN_WIDTH or snake_pos[0][0] < 0 or 
            snake_pos[0][1] >= SCREEN_HEIGHT or snake_pos[0][1] < 0):
            print("Snake collided with the border!")
            running = False

        if snake_pos[0] == food_pos:
            score += 1
            snake_pos.append(snake_pos[-1])
            food_pos = (random.randint(0, GRID_WIDTH-1) * GRIDSIZE, random.randint(0, GRID_HEIGHT-1) * GRIDSIZE)
        else:
            snake_pos.pop()
        
        draw_grid(screen)
        for pos in snake_pos:
            pygame.draw.rect(screen, snake_color, (pos[0], pos[1], GRIDSIZE, GRIDSIZE))
        pygame.draw.rect(screen, food_color, (food_pos[0], food_pos[1], GRIDSIZE, GRIDSIZE))

        pygame.display.update()

        clock.tick(10 + score)
    
    pygame.quit()
    print("Game over! Your score was:", score)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("An error occurred:", str(e))
        pygame.quit()
        raise
