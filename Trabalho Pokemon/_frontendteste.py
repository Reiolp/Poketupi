import pygame # Importa a biblioteca do pygame
from pygame.locals import MOUSEBUTTONDOWN, QUIT # Importa a função de leitura do mouse do Pygame
from sys import exit 
from _backend import pokemon # Importa a biblioteca Pokémon, onde estão armazenadas todas as informações
import random
import _batalhateste # Importa o arquivo contendo todo o código da lógica e estilização da batalha
import os

os.chdir(os.path.dirname(__file__))

pygame.init()
#Criação da tela
tela = pygame.display.set_mode((1530, 900))
pygame.display.set_caption("Seleção de Pokémon")
clock = pygame.time.Clock()

# Verifica se o fundo do menu existe
try:
    fundo_menu = pygame.image.load("fundo.jpg").convert()
    fundo_menu = pygame.transform.scale(fundo_menu, (1530, 900))
except Exception as e:
    print("Erro ao carregar fundo.jpg:", e)
    fundo_menu = pygame.Surface((1530, 900))
    fundo_menu.fill((0, 0, 0))
    
# Verifica se o fundo tela inicial existe
try:
    tela_inicial = pygame.image.load("fundo_inicial.png").convert()
    tela_inicial = pygame.transform.scale(tela_inicial, (1530, 900))
except Exception as e:
    print("Erro ao carregar fundo.jpg:", e)
    tela_inicial = pygame.Surface((1530, 900))
    tela_inicial.fill((0, 0, 0))

fonte = pygame.font.SysFont("arial", 28)
fonte_grande = pygame.font.SysFont("comicsansms", 50)


escolha = fonte_grande.render("Escolha 3 pokemons", True, (0, 0, 0))
fundo_menu.blit(escolha, (520, 800))

pokemon_escolhidos = []
equipe_computador = []
em_batalha = False
modo_tela = "inicio"

# Criação da classe para gerência de botões
class Botao:
    def __init__(self, x, y, largura, altura, imagem_path=None, nome_pokemon=None, texto=None, cor=(0, 150, 0), fonte=None):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.nome = nome_pokemon
        self.texto = texto

        # Usa a fonte padrão se nenhuma for fornecida
        if fonte is None:
            fonte = pygame.font.SysFont(None, 36)
        self.fonte = fonte

        if imagem_path:
            try:
                self.imagem = pygame.image.load(imagem_path).convert_alpha()
                self.imagem = pygame.transform.scale(self.imagem, (largura, altura))
            except Exception as e:
                print(f"Erro ao carregar {imagem_path}: {e}")
                self.imagem = pygame.Surface((largura, altura))
                self.imagem.fill((255, 0, 0))
        else:
            # Cria uma superfície com cor de fundo
            self.imagem = pygame.Surface((largura, altura))
            self.imagem.fill(cor)

            if texto:
                texto_render = self.fonte.render(texto, True, (255, 255, 255))
                texto_rect = texto_render.get_rect(center=(largura // 2, altura // 2))
                self.imagem.blit(texto_render, texto_rect)

    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect)

    def clicado(self, pos):
        return self.rect.collidepoint(pos)

# Caso a lista pokemon_escolhidos tenha menos do que 3 elementos, adicionar Pokémon
def escolher_pokemon(nome):
    if len(pokemon_escolhidos) < 3 and nome not in pokemon_escolhidos:
        pokemon_escolhidos.append(nome)

def gerar_equipe_computador():
    nomes_disponiveis = list(pokemon.keys())
    for nome_jogador in pokemon_escolhidos:
        if nome_jogador in nomes_disponiveis:
            nomes_disponiveis.remove(nome_jogador)
    equipe = random.sample(nomes_disponiveis, 3)
    return equipe

def randomizar_time_jogador():
    global pokemon_escolhidos, equipe_computador
    todos = list(pokemon.keys())
    pokemon_escolhidos = random.sample(todos, 3)
    equipe_computador = []

def iniciar_batalha():
    global em_batalha, modo_tela
    print("[DEBUG] Iniciando batalha com:", pokemon_escolhidos)
    _batalhateste.iniciar_batalha(pokemon_escolhidos,equipe_computador)
    em_batalha = False
    pokemon_escolhidos.clear()
    equipe_computador.clear()
    modo_tela = "inicio"

# Criação dos botões dos Pokémon
botoes = [
    Botao(100, 50, 250, 250, "Ararazul.png", "Ararazul"),
    Botao(370, 50, 250, 250, "Bojarro.png", "Bojarro"),
    Botao(640, 50, 250, 250, "Viramelo.png", "Viramelo"),
    Botao(910, 50, 250, 250, "Cafasma.png", "Cafasma"),
    Botao(1180, 50, 250, 250, "Capilorde.png", "Capilorde"),
    Botao(100, 320, 250, 250, "Cobrata.png", "Cobrata"),
    Botao(370, 320, 250, 250, "Piropira.png", "Piropira"),
    Botao(640, 320, 250, 250, "Jacarevac.png", "Jacarevac"),
    Botao(910, 320, 250, 250, "Lutandua.png", "Lutandua"),
    Botao(1180, 320, 250, 250, "Douraleao.png", "Douraleao"),
    Botao(1180, 590, 250, 250, "Pistolin.png", "Pistolin"),
    Botao(100, 590, 250, 250, "Sacere.png", "Sacere"),
]

botao_confirmar = Botao(640, 720, 250, 70, texto="Confirmar Batalha", cor=(0, 100, 255))
botao_randomizar = Botao(640, 590, 250, 120, "Queme.jpg", "Queme")
botao_comecar = Botao(530, 450, 400, 150)

# Logo IFTM
try:
    logo_instituto = pygame.image.load("logo_instituto.png").convert_alpha()
    logo_instituto = pygame.transform.scale(logo_instituto, (50, 50))
except Exception as e:
    print("Erro ao carregar logo_instituto:", e)
    logo_instituto = pygame.Surface((50, 50))
    logo_instituto.fill((100, 100, 100))

#loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            rodando = False
        if evento.type == MOUSEBUTTONDOWN and evento.button == 1:
            pos = pygame.mouse.get_pos()
            if modo_tela == "inicio":
                if botao_comecar.clicado(pos):
                    pygame.mixer.music.load("musica_menu.mp3")
                    pygame.mixer.music.play(-1)
                    modo_tela = "selecao"
            elif modo_tela == "selecao":
                for botao in botoes:
                    if botao.clicado(pos):
                        escolher_pokemon(botao.nome)
                if botao_randomizar.clicado(pos):
                    randomizar_time_jogador()
                if len(pokemon_escolhidos) == 3 and not equipe_computador:
                    equipe_computador = gerar_equipe_computador()
                if len(pokemon_escolhidos) == 3 and equipe_computador:
                    if botao_confirmar.clicado(pos):
                        iniciar_batalha()

    if modo_tela == "inicio":
        tela.blit(tela_inicial,(0, 0))
    elif modo_tela == "selecao":
        tela.blit(fundo_menu, (0, 0))
        for botao in botoes:
            botao.desenhar(tela)
        botao_randomizar.desenhar(tela)
        if len(pokemon_escolhidos) == 3 and equipe_computador:
            botao_confirmar.desenhar(tela)
        tela.blit(logo_instituto, (1430, 790))

        status_msg = "" if len(pokemon_escolhidos) < 3 else "Equipe completa!"
        texto_status = fonte.render(status_msg, True, (0, 0, 255))
        tela.blit(texto_status, (360, 600))

        titulo = fonte.render("Sua equipe:", True, (0, 200, 255))
        tela.blit(titulo, (360, 640))
        for i, nome in enumerate(pokemon_escolhidos):
            texto = fonte.render(f"{i + 1}. {nome}", True, (0, 200, 255))
            tela.blit(texto, (360, 640 + (i + 1) * 30))

        if equipe_computador:
            titulo_cpu = fonte.render("Equipe IA:", True, (255, 100, 100))
            tela.blit(titulo_cpu, (900, 640))
            for i, nome in enumerate(equipe_computador):
                texto = fonte.render(f"{i + 1}. {nome}", True, (255, 100, 100))
                tela.blit(texto, (900, 640 + (i + 1) * 30))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
