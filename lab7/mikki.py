import pygame
import sys
import datetime

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Clock with Moving Hands')

new_width = 800
new_height = 600

# Load the images for the clock face and hands
# Replace the strings below with the actual paths to your image files
clock_image = pygame.image.load("C:\\Users\\ayaul\\Downloads\\MicrosoftTeams-image (2).png")
clock_image = pygame.transform.smoothscale(clock_image, (new_width, new_height))
right_hand_image = pygame.image.load("C:\\Users\\ayaul\\Downloads\\MicrosoftTeams-image (4).png")
left_hand_image = pygame.image.load("C:\\Users\\ayaul\\Downloads\\MicrosoftTeams-image (3).png")


hand_center = (screen_width // 2, screen_height // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = datetime.datetime.now()

    minute_angle = 6 * current_time.minute  # 360 degrees / 60 minutes
    second_angle = 6 * current_time.second  # 360 degrees / 60 seconds

    # Rotate hand images
    rotated_right_hand = pygame.transform.rotate(right_hand_image, -minute_angle)
    rotated_left_hand = pygame.transform.rotate(left_hand_image, -second_angle)

    # Get the new rects for the rotated images
    right_hand_rect = rotated_right_hand.get_rect(center=hand_center)
    left_hand_rect = rotated_left_hand.get_rect(center=hand_center)

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Blit the images to the screen at their new positions
    screen.blit(clock_image, (0, 0))
    screen.blit(rotated_right_hand, right_hand_rect)
    screen.blit(rotated_left_hand, left_hand_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
