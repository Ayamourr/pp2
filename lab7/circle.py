import pygame
import sys

pygame.init()

screen_width, screen_height = (300, 300)
screen = pygame.display.set_mode((screen_width, screen_height))

red = (255, 0, 0)

ball_x, ball_y = screen_height//2, screen_width//2
ball_radius = 25
move = 20

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        
        elif event.type == pygame.KEYDOWN:
            new_x, new_y = ball_x, ball_y  
            if event.key == pygame.K_UP:
                new_y = ball_y - move
            if event.key == pygame.K_DOWN:
                new_y = ball_y + move
            if event.key == pygame.K_LEFT:
                new_x = ball_x - move
            if event.key == pygame.K_RIGHT:
                new_x = ball_x + move
            
            if 0 + ball_radius <= new_x <= screen_width - ball_radius:
                ball_x = new_x
            if 0 + ball_radius <= new_y <= screen_height - ball_radius:
                ball_y = new_y



    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, red, (ball_x, ball_y), 25)

    pygame.display.flip()

pygame.quit()
sys.exit()