import pygame, sys, random, time,threading  
pygame.mixer.pre_init(frequency=44100,size=-16, channels=2, buffer=512)
pygame.init()
def nhacmario():
    pygame.mixer.music.load("sounds/nhac.wav")
    pygame.mixer.music.play(1)
def nhachiphop():
    x=random.randint(1,2)
    if x==1:
        pygame.mixer.music.load("sounds/híp-hóp.wav")
        pygame.mixer.music.play(1)
    elif x==2:
        pygame.mixer.music.load("sounds/hiphop2.wav")
        pygame.mixer.music.play(1)
