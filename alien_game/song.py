import pygame
import time

def play_music(song_path):
    # Initialize Pygame and mixer
    pygame.init()
    pygame.mixer.init()


    # Load and play music
    try:
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play(-1)  # Loop forever
        print("Music playing...")
    except pygame.error as e:
        print("Failed to load music:", e)
        return

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        time.sleep(0.01)

    # Cleanup
    pygame.mixer.music.stop()
    pygame.quit()

