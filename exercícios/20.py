import pygame
pygame.init()

pygame.mixer.music.load('exercícios/01.mp3')

pygame.mixer.music.play()

input()

pygame.event.wait()
