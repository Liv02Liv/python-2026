#%%
#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.init()
pygame.mixer.music.load("Victor Santos - Tenho Medo (Clipe Oficial) - Victor Santos (youtube).mp3")
pygame.mixer.music.play()
pygame.event.wait()