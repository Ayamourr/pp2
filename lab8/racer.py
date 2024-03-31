import pygame
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 100
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 50, 100
OBSTACLE_SPEED = 5
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sideways Dodger")

player = pygame.Rect(SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2, SCREEN_HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)

def create_obstacle():
    return pygame.Rect(random.randint(0, SCREEN_WIDTH - OBSTACLE_WIDTH), -OBSTACLE_HEIGHT, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)

obstacles = [create_obstacle()]

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= OBSTACLE_SPEED
    if keys[pygame.K_RIGHT] and player.right < SCREEN_WIDTH:
        player.x += OBSTACLE_SPEED

    for obstacle in obstacles:
        obstacle.y += OBSTACLE_SPEED

    for obstacle in obstacles:
        if player.colliderect(obstacle):
            running = False

    if not obstacles or obstacles[-1].y > 150:
        obstacles.append(create_obstacle())

    obstacles = [obstacle for obstacle in obstacles if obstacle.y < SCREEN_HEIGHT]

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, player)

    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, obstacle)

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
