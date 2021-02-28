#Aula08 Exercicio 06 (na verdade é o 021 do) Curso em Vídeo Python
#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
pygame.init()
pygame.mixer.music.load('Aula08Modulos06.mp3')
pygame.mixer.music.play()
pygame.event.wait()