import os
import pygame

# Initialize Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Pygame Music Player')

# Define music and image mappings with corrected file paths
music_dir = r"C:\Users\ayaul\Downloads\skz"
music_files = {
    r"c:\Users\ayaul\Downloads\skz\13.mp3": r"c:\Users\ayaul\Downloads\img\13.jpg",
    r"c:\Users\ayaul\Downloads\skz\volcano.mp3": r"c:\Users\ayaul\Downloads\img\volcano.jpg",
    r"c:\Users\ayaul\Downloads\skz\wish you back.mp3": r"c:\Users\ayaul\Downloads\img\wish you back.jpg",
    r"c:\Users\ayaul\Downloads\skz\close.mp3": r"c:\Users\ayaul\Downloads\img\close.jpg",
    r"c:\Users\ayaul\Downloads\skz\voices.mp3": r"c:\Users\ayaul\Downloads\img\voices.jpg",
    r"c:\Users\ayaul\Downloads\skz\cover me.mp3": r"c:\Users\ayaul\Downloads\img\cover me.jpg",
    r"c:\Users\ayaul\Downloads\skz\streetlight.mp3": r"c:\Users\ayaul\Downloads\img\streetlight.jpg",
    r"c:\Users\ayaul\Downloads\skz\eternity.mp3": r"c:\Users\ayaul\Downloads\img\eternity.jpg",
    r"c:\Users\ayaul\Downloads\skz\alien.mp3": r"c:\Users\ayaul\Downloads\img\alien.jpg"
}
tracks = list(music_files.keys())  # Use the music files directly from the dictionary
current_track = 0
pygame.mixer.music.load(tracks[current_track])

def play_track(index):
    global current_track
    current_track = index
    pygame.mixer.music.load(tracks[current_track])
    pygame.mixer.music.play()
    update_display()

def update_display():
    screen.fill((0, 0, 0))  # Fill the screen with black
    
    # Load and display the corresponding image
    image_path = music_files[tracks[current_track]]
    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (400, 400))  # Adjust the scaling as needed
    screen.blit(image, (200, 200))  # Center the image
    
    # Display track info
    font = pygame.font.Font(None, 30)
    track_name = os.path.basename(tracks[current_track]).split('.')[0]  # Extract the track name without the file extension
    text = font.render(track_name, True, (255, 255, 255))
    text_rect = text.get_rect(center=(400, 50))  # Adjust text position as needed
    screen.blit(text, text_rect)
    pygame.display.flip()

# Initial display update
update_display()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Play/Pause
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:  # Stop
                pygame.mixer.music.stop()
            elif event.key == pygame.K_RIGHT:  # Next
                play_track((current_track + 1) % len(tracks))
            elif event.key == pygame.K_LEFT:  # Previous
                play_track((current_track - 1) % len(tracks))

pygame.quit()
