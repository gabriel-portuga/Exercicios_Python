import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input('Precione qualquer tecla para para!')
pygame.mixer.stop()