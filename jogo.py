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

# [ini] Objetos
garrafa_som = pygame.mixer.Sound("assets/garrafa_som.wav")
copo_som = pygame.mixer.Sound("assets/copo_som.wav")
maca_som = pygame.mixer.Sound("assets/maca_som.wav")
lata_som = pygame.mixer.Sound("assets/lata_som.wav")
bola_som = pygame.mixer.Sound("assets/bola_som.wav")
lixo_papel = pygame.image.load("assets/Papel_.png")
lixo_metal = pygame.image.load("assets/Metal_.png")
lixo_plastico = pygame.image.load("assets/Plástico_.png")
lixo_vidro = pygame.image.load("assets/Vidro_.png")
lixo_organico = pygame.image.load("assets/Orgânico_.png")
garrafa_vidro = pygame.image.load("assets/garrafa_vidro.png")
lata_metal = pygame.image.load("assets/lata_metal.png")
copo_plastico = pygame.image.load("assets/copo_plastico.png")
bola_papel = pygame.image.load("assets/bola_papel.png")
maça_organico = pygame.image.load("assets/maça_organico.png")
# [fim]

# [ini] RGB
preto = (0, 0, 0)
branco = (255, 255, 255)
# [fim]

# [ini] Tamanho da Janela (Largura/Width e Altura/Height)
largura = 800
altura = 600
display = pygame.display.set_mode(
    (largura, altura)
)
# [fim]