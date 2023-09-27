import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input('Agora você escuta?')
#Comando de input digitado para ouvir devido imcompatibilidade