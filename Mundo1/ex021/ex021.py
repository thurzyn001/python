import pygame
import os

pygame.init()

script_dir = os.path.dirname(os.path.abspath(__file__))
music_file_path = os.path.join(script_dir, 'ex021.mp3')

pygame.mixer.music.load(music_file_path)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
