# [ini] Setup Inicial e Registro
import pygame
import random
import time

pygame.init() #Pygame iniciado

log = open("log.txt", "a")
nome = input("Nome: ")
email = input("Email: ")
log.write("Nome: " + nome + "/" + "Email: " + email)
log.write("\n")
log.close()

pygame.display.set_caption("Coleta Seletiva Divertida") #Título da janela
icone = pygame.image.load("assets/icone.png")
background = pygame.image.load("assets/Background.png")
pygame.display.set_icon(icone)
# [fim]