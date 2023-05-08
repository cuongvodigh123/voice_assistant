import pygame, sys, random, time,threading  
pygame.mixer.pre_init(frequency=44100,size=-16, channels=2, buffer=512)
pygame.init()
def nhacmario():
    pygame.mixer.music.load("sounds/nhac.wav")
    pygame.mixer.music.play(1)