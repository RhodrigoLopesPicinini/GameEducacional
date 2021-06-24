# [ini] Setup Inicial e Registro
import pygame
import random
import time

from funcoes import randomizer

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

# [ini] Posição Objetos
LixoX_vidro = 360
LixoX_metal = 239
LixoX_plastico = 122
LixoX_papel = 479
LixoX_organico = 598
LixoY = altura * 0.74
LixoLargura = 99
garrafa_altura = 95
garrafa_largura = 75
bola_altura = 35
bola_largura = 35
copo_altura = 75
copo_largura = 70
lata_altura = 60
lata_largura = 35
maca_altura = 50
maca_largura = 35
# [fim]

fps = pygame.time.Clock()

largeText = pygame.font.Font("freesansbold.ttf", 20)

# [ini] Funções Secundárias 
def text_objects(texto, fonte, branco):
    textSurface = fonte.render(texto, True, branco)
    return textSurface, textSurface.get_rect()

def texto_display(text, x, y, size):
    largeText = pygame.font.Font("freesansbold.ttf", size)
    TextSurf, TextRect = text_objects(text, largeText, branco)
    TextRect.center = (x, y)
    display.blit(TextSurf, TextRect)
    pygame.display.update()

def pontuação_display(display, x, y, pontuação, cor):
    pontos = largeText.render("Pontuação: " + str(pontuação), True, cor)
    display.blit(pontos, (x, y))

def vidas_display(display, x, y, vidas, cor):
    pontos = largeText.render("Vidas: " + str(vidas), True, cor)
    display.blit(pontos, (x, y)) 
   
def perdeu(pontuação):
    texto_display("Game Over!" + " Sua pontuação: " + str(pontuação), 300, 300, 40)
    time.sleep(4)
    jogo()

# [fim]

# [ini] Função Primária (Jogo)
def jogo():

    pygame.mixer.music.load("assets/background_music.mp3")
    pygame.mixer.music.set_volume(0.050)
    pygame.mixer.music.play(-1)
    lixoPosX = random.randrange(0, 725)
    n = random.randrange(0, 5)
    movimento = 0
    lixoPosY = -220
    lixoPosX = largura * 0.45
    velocidade = random.randrange(2, 6)
    pontuação = 0
    vidas = 3        
    
    while True:
        display.blit(randomizer(n, garrafa_vidro, lata_metal, copo_plastico, bola_papel, maça_organico), (lixoPosX, lixoPosY))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    movimento = -5
                elif evento.key == pygame.K_RIGHT:
                    movimento = 5
            if evento.type == pygame.KEYUP:
                movimento = 0 
        pygame.display.update()
        display.blit(background, (0, 0))
        display.blit(lixo_papel, (LixoX_papel, LixoY))
        display.blit(lixo_metal, (LixoX_metal, LixoY))
        display.blit(lixo_plastico, (LixoX_plastico, LixoY))
        display.blit(lixo_vidro, (LixoX_vidro, LixoY))
        display.blit(lixo_organico, (LixoX_organico, LixoY))    
        lixoPosX = lixoPosX + movimento
        lixoPosY = lixoPosY + velocidade
        # [ini] Sistema de Colisão
        if n == 0:
            if LixoY < lixoPosY + garrafa_altura:
                if LixoX_vidro < lixoPosX and LixoX_vidro + LixoLargura > lixoPosX or lixoPosX + garrafa_largura > LixoX_vidro and lixoPosX + garrafa_largura < LixoX_vidro + LixoLargura:
                    pontuação += 1
                    pygame.mixer.Sound.play(garrafa_som)
                    lixoPosY = -220
                    n = random.randrange(0, 5)
                    randomizer(n, garrafa_vidro, lata_metal, copo_plastico, bola_papel, maça_organico)
                    velocidade = random.randrange(2, 6)
                    lixoPosX = random.randrange(0, 725)
                else:
                    vidas -= 1
                    lixoPosY = -220
                    n = random.randrange(0, 5)
                    randomizer(n, garrafa_vidro, lata_metal, copo_plastico, bola_papel, maça_organico)
                    velocidade = random.randrange(2, 6)
                    lixoPosX = random.randrange(0, 725)   
        elif n == 1:
            if LixoY < lixoPosY + lata_altura:
                if LixoX_metal < lixoPosX and LixoX_metal + LixoLargura > lixoPosX or lixoPosX + lata_largura > LixoX_metal and lixoPosX + lata_largura < LixoX_metal + LixoLargura:
                    pontuação += 1
                    pygame.mixer.Sound.play(lata_som)
                    lixoPosY = -220
                    n = random.randrange(0, 5)
                    randomizer(n, garrafa_vidro, lata_metal, copo_plastico, bola_papel, maça_organico)
                    velocidade = random.randrange(2, 6)
                    lixoPosX = random.randrange(0, 725)
                else:
                    vidas -= 1
                    lixoPosY = -220
                    n = random.randrange(0, 5)
                    randomizer(n, garrafa_vidro, lata_metal, copo_plastico, bola_papel, maça_organico)
                    velocidade = random.randrange(2, 6)
                    lixoPosX = random.randrange(0, 725)
        elif n == 2:
            if LixoY < lixoPosY + copo_altura:
                if LixoX_plastico < lixoPosX and LixoX_plastico + LixoLargura > lixoPosX or lixoPosX + copo_largura > LixoX_plastico and lixoPosX + copo_largura < LixoX_plastico + LixoLargura:
                    pontuação += 1
                    pygame.mixer.Sound.play(copo_som)
                    lixoPosY = -220
                    n = random.randrange(0, 5)
                    randomizer(n, garrafa_vidro, lata_metal, copo_plastico, bola_papel, maça_organico)
                    velocidade = random.randrange(2, 6)
                    lixoPosX = random.randrange(0, 725)
                else:
                    vidas -= 1
                    lixoPosY = -220
                    n = random.randrange(0, 5)
                    randomizer(n, garrafa_vidro, lata_metal, copo_plastico, bola_papel, maça_organico)
                    velocidade = random.randrange(2, 6)
                    lixoPosX = random.randrange(0, 725)                    
        elif n == 3:
            if LixoY < lixoPosY + bola_altura:
                if LixoX_papel < lixoPosX and LixoX_papel + LixoLargura > lixoPosX or lixoPosX + bola_largura > LixoX_papel and lixoPosX + bola_largura < LixoX_papel + LixoLargura:
                    pontuação += 1
                    pygame.mixer.Sound.play(bola_som)
                    lixoPosY = -220
                    n = random.randrange(0, 5)
                    randomizer(n, garrafa_vidro, lata_metal, copo_plastico, bola_papel, maça_organico)
                    velocidade = random.randrange(2, 6)
                    lixoPosX = random.randrange(0, 725)
                else:
                    vidas -= 1
                    lixoPosY = -220
                    n = random.randrange(0, 5)
                    randomizer(n, garrafa_vidro, lata_metal, copo_plastico, bola_papel, maça_organico)
                    velocidade = random.randrange(2, 6)
                    lixoPosX = random.randrange(0, 725)                    
        elif n == 4:
            if LixoY < lixoPosY + maca_altura:
                if LixoX_organico < lixoPosX and LixoX_organico + LixoLargura > lixoPosX or lixoPosX + maca_largura > LixoX_organico and lixoPosX + maca_largura < LixoX_organico + LixoLargura:
                    pontuação += 1
                    pygame.mixer.Sound.play(maca_som)  
                    lixoPosY = -220
                    n = random.randrange(0, 5)
                    randomizer(n, garrafa_vidro, lata_metal, copo_plastico, bola_papel, maça_organico)
                    velocidade = random.randrange(2, 6)
                    lixoPosX = random.randrange(0, 725)
                else:
                    vidas -= 1
                    lixoPosY = -220
                    n = random.randrange(0, 5)
                    randomizer(n, garrafa_vidro, lata_metal, copo_plastico, bola_papel, maça_organico) 
                    velocidade = random.randrange(2, 6)
                    lixoPosX = random.randrange(0, 725)
        if vidas == 0:
            perdeu(pontuação) 
        # [fim]