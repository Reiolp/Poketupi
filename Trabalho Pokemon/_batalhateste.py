def iniciar_batalha(pokemon_escolhidos, equipe_computador):
    import pygame
    import random
    from _backend import pokemon
    import os
    import copy
    pokemon = copy.deepcopy(pokemon)
    os.chdir(os.path.dirname(__file__))

    

    pygame.init()
    #Musica
    pygame.mixer.music.load("musica_batalha.mp3")
    pygame.mixer.music.play(-1)
    #Tela
    tela = pygame.display.set_mode((1530, 900))
    pygame.display.set_caption("Batalha Pokémon")
    clock = pygame.time.Clock()
    fonte = pygame.font.SysFont("arial", 28)

    def desenhar_barra_hp(x, y, largura, altura, hp):
        pygame.draw.rect(tela, (255, 0, 0), (x, y, largura, altura))
        barra_verde = int(largura * (hp / 100))
        pygame.draw.rect(tela, (0, 255, 0), (x, y, barra_verde, altura))

    def desenhar_tipagens(x, y, largura, altura, tipos):
        espacamento = 10  # espaço entre os tipos
        largura_tipo = (largura - (len(tipos) - 1) * espacamento) // len(tipos)

        cores_por_tipo = {
            "Grass": (0, 180, 0),
            "Flying": (100, 200, 255),
            "Ground": (194, 178, 128),
            "Rock": (120, 72, 0),
            "Bug": (34, 139, 34),
            "Ghost": (128, 0, 128),
            "Fire": (255, 60, 60),
            "Water": (0, 120, 255),
            "Ice": (173, 216, 230),
            "Dark": (0, 0, 0),
            "Fighting": (255, 140, 0),
            "Steel": (169, 169, 169),
            "Psychic": (255, 105, 180),
            "Normal": (255, 255, 255)
        }

        for i, tipo in enumerate(tipos):
            cor = cores_por_tipo.get(tipo, (200, 200, 200))
            rect_x = x + i * (largura_tipo + espacamento)
            pygame.draw.rect(tela, cor, (rect_x, y, largura_tipo, altura))
            pygame.draw.rect(tela, (0, 0, 0), (rect_x, y, largura_tipo, altura), 2)  # borda preta

            # texto do tipo
            cor_texto = (0, 0, 0) if cor[0] > 200 and cor[1] > 200 else (255, 255, 255)
            fonte_tipagem = pygame.font.SysFont("arial", 20)
            texto_render = fonte_tipagem.render(tipo, True, cor_texto)
            texto_rect = texto_render.get_rect(center=(rect_x + largura_tipo // 2, y + altura // 2))
            tela.blit(texto_render, texto_rect)

    fundo_batalha = pygame.image.load("fundobatalha.png").convert()
    fundo_batalha = pygame.transform.scale(fundo_batalha, (1530, 900))

    treinador_cpu_sprite = pygame.image.load("sprites/treinador_cpu.png").convert_alpha()
    treinador_cpu_sprite = pygame.transform.scale(treinador_cpu_sprite, (350, 350))  # Controle de tamanho


    try:
        tela_final = pygame.image.load("fundo_final.png").convert()
        tela_final = pygame.transform.scale(tela_final, (1530, 900))
    except Exception as e:
        print("Erro ao carregar fundo.jpg:", e)
        tela_final = pygame.Surface((1530, 900))
        tela_final.fill((0, 0, 0))

    #sprites para batalhas

    imagens_jogador = {
        "Ararazul": "sprites/Ararazul_costas.png",
        "Bojarro": "sprites/Bojarro_costas.png",
        "Cafasma": "sprites/Cafasma_costa.png",
        "Capilorde": "sprites/Capilorde_costas.png",
        "Cobrata": "sprites/Cobrata_costa.png",
        "Jacarevac": "sprites/Jacarevac_costas.png",
        "Lutandua": "sprites/Lutandua_costas.png",
        "Douraleao": "sprites/Douraleao_costas.png",
        "Piropira": "sprites/Piropira_costas.png",
        "Pistolin": "sprites/Pistolin_costas.png",
        "Sacere": "sprites/Sacere_costas.png",
        "Viramelo": "sprites/Viramelo_costas.png"
    }

    imagens_cpu = {
        "Ararazul": "sprites/Ararazul_frente.png",
        "Bojarro": "sprites/Bojarro_frente.png",
        "Cafasma": "sprites/Cafasma_frente.png",
        "Capilorde": "sprites/Capilorde_frente.png",
        "Cobrata": "sprites/Cobrata_frente.png",
        "Jacarevac": "sprites/Jacarevac_frente.png",
        "Lutandua": "sprites/Lutandua_frente.png",
        "Douraleao": "sprites/Douraleao_frente.png",
        "Piropira": "sprites/Piropira_frente.png",
        "Pistolin": "sprites/Pistolin_frente.png",
        "Sacere": "sprites/Sacere_frente.png",
        "Viramelo": "sprites/Viramelo_frente.png"
    }

    sprites_jogador = {}
    sprites_cpu = {}

    for nome in pokemon:
        try:
            img_j = pygame.transform.scale(pygame.image.load(imagens_jogador[nome]), (300, 300))
            sprites_jogador[nome] = img_j
        except:
            print(f"Imagem do jogador não encontrada para {nome}: {imagens_jogador.get(nome)}")

        try:
            img_c = pygame.transform.scale(pygame.image.load(imagens_cpu[nome]), (300, 300))
            sprites_cpu[nome] = img_c
        except:
            print(f"Imagem da CPU não encontrada para {nome}: {imagens_cpu.get(nome)}")



    pokemon_jogador_index = 0
    pokemon_computador_index = 0
    modo_ataque = False
    mensagem = ""
    mostrar_mensagem = False
    fim_batalha = False
    vencedor = ""
    turno_jogador = True
    mensagem_em_espera = ""
    status_efeitos = {nome: {"sleep": 0, "burn": False, "frozen": False, "def": pkm["stats"]["def"]} for nome, pkm in pokemon.items()}

    class Botao:
        def __init__(self, x, y, largura, altura, imagem_path=None, texto=None, cor=(0, 150, 0)):
            self.rect = pygame.Rect(x, y, largura, altura)
            self.texto = texto
            if imagem_path:
                try:
                    imagem = pygame.image.load(imagem_path).convert_alpha()
                    self.surface = pygame.transform.scale(imagem, (largura, altura))
                except:
                    print(f"[ERRO] Não foi possível carregar a imagem: {imagem_path}")
                    self.surface = pygame.Surface((largura, altura))
                    self.surface.fill((255, 0, 0))
            else:
                self.surface = pygame.Surface((largura, altura))
                self.surface.fill(cor)
                if texto:
                    # Borda escura
                    pygame.draw.rect(self.surface, (30, 30, 30), (0, 0, largura, altura), 4)
                    # Texto com sombra
                    texto_render_sombra = fonte.render(texto, True, (0, 0, 0))
                    texto_render = fonte.render(texto, True, (255, 255, 255))
                    texto_rect = texto_render.get_rect(center=(largura // 2, altura // 2))

                    self.surface.blit(texto_render_sombra, texto_rect.move(2, 2))  # sombra deslocada
                    self.surface.blit(texto_render, texto_rect)



        def desenhar(self, tela):
            tela.blit(self.surface, self.rect)

        def clicado(self, pos):
            return self.rect.collidepoint(pos)


    def pokemon_ativo(equipe, index):
        return pokemon[equipe[index]]
    
    # Cálculo de defesa e tipagens
    def calcular_defesa_modificada(tipo_ataque, nome_inimigo):
        tipos_inimigo = pokemon[nome_inimigo]["tipo"]
        efetividade = pokemon[nome_inimigo]["efetividade"]
        defesa_base = status_efeitos[nome_inimigo]["def"]

        multiplicador_def = 1.0
        status_texto = "efetivo"  # padrão

        if efetividade[2]["Imunidade"] and tipo_ataque in efetividade[2]["Imunidade"]:
            return "imune", defesa_base

        if efetividade[0]["Fraqueza4x"] and tipo_ataque in efetividade[0]["Fraqueza4x"]:
            multiplicador_def *= 0.0
            status_texto = "super_efetivo"
        elif efetividade[0]["Fraqueza2x"] and tipo_ataque in efetividade[0]["Fraqueza2x"]:
            multiplicador_def *= 0.5
            status_texto = "super_efetivo"
        elif efetividade[1]["Resistencia4x"] and tipo_ataque in efetividade[1]["Resistencia4x"]:
            multiplicador_def *= 1.75
            status_texto = "pouco_efetivo"
        elif efetividade[1]["Resistencia2x"] and tipo_ataque in efetividade[1]["Resistencia2x"]:
            multiplicador_def *= 1.25
            status_texto = "pouco_efetivo"

        defesa_final = defesa_base * multiplicador_def
        return status_texto, defesa_final

    def executar_ataque(jogador, inimigo, golpe):
        nonlocal mensagem, mostrar_mensagem
        nome_jogador = jogador["nome"]
        nome_inimigo = inimigo["nome"]
        status_inimigo = status_efeitos[nome_inimigo]

        if golpe["nome"] == "Recover":
            cura = random.randint(20,50)
            jogador["stats"]["hp"] = min(100, jogador["stats"]["hp"] + cura)
            mensagem = f"{nome_jogador} usou Recover e recuperou {cura} de HP!"
            mostrar_mensagem = True
            return
        
        if golpe["nome"] == "Roost":
            cura = random.randint(20,50)
            jogador["stats"]["hp"] = min(100, jogador["stats"]["hp"] + cura)
            mensagem = f"{nome_jogador} usou Roost e recuperou {cura} de HP!"
            mostrar_mensagem = True
            return

        if status_efeitos[nome_jogador]["frozen"] and random.randint(1, 100) <= 80:
            mensagem = f"{nome_jogador} está congelado e não conseguiu atacar!"
            mostrar_mensagem = True
            return

        prioridade = golpe["efeito"] and golpe["efeito"]["nome"] == "Priority Attack"
        acerto = 100 if prioridade else random.randint(1, 100)

        if acerto <= golpe["precisao"]:
            efetividade_texto, defesa_modificada = calcular_defesa_modificada(golpe["tipo"], nome_inimigo)
            if efetividade_texto == "imune":
                mensagem = f"{nome_jogador} usou {golpe['nome']}, mas não teve efeito em {nome_inimigo}!"
                mostrar_mensagem = True
                return
            dano_base = golpe["dano"] * (1 - defesa_modificada / 100)
            buff_atk = status_efeitos[nome_jogador].get("buff", 1.0)
            dano = int(dano_base * buff_atk)

            dano = max(dano, 0)
            inimigo["stats"]["hp"] -= dano
            mensagem = f"{nome_jogador} usou {golpe['nome']}! Causou {dano} de dano!"
            if efetividade_texto == "super_efetivo":
                mensagem += " Foi super efetivo!"
            elif efetividade_texto == "pouco_efetivo":
                mensagem += " Não foi muito efetivo..."
            elif efetividade_texto == "efetivo":
                 
                 mensagem += " Foi efetivo."


            efeito = golpe.get("efeito")

            if efeito and "nome" in efeito and "chance" in efeito and random.randint(1, 100) <= efeito["chance"]:
                tipo = efeito["nome"]

                if tipo == "Burn":
                    status_inimigo["burn"] = True
                    mensagem += f" {nome_inimigo} foi queimado!"
                elif tipo == "Freeze":
                    status_inimigo["frozen"] = True
                    mensagem += f" {nome_inimigo} foi congelado!"
                elif tipo == "Sleep":
                    status_inimigo["sleep"] = 2
                    mensagem += f" {nome_inimigo} adormeceu!"
                elif tipo == "Lower Defense":
                    nova_def = int(status_inimigo["def"] * 0.8)
                    status_inimigo["def"] = max(nova_def, 1)
                    mensagem += f" A defesa de {nome_inimigo} caiu!"
                elif tipo == "Flinch":
                    status_inimigo["flinch"] = True
                elif tipo == "Raise Speed":
                    jogador["stats"]["speed"] = int(jogador["stats"]["speed"] * 1.25)
                    mensagem += f" A velocidade de {nome_jogador} aumentou!"
                elif tipo == "Buff":
                    if "buff" not in status_efeitos[nome_jogador]:
                        status_efeitos[nome_jogador]["buff"] = 1.2
                    else:
                        status_efeitos[nome_jogador]["buff"] *= 1.2
                    mensagem += f" O poder de ataque de {nome_jogador} aumentou!"
                elif tipo == "Recoil":
                    recoil_dano = int(dano * 0.2)
                    jogador["stats"]["hp"] -= recoil_dano
                    mensagem += f" {nome_jogador} sofreu {recoil_dano} de recuo!"
                elif tipo == "Self Lower Defense":
                    nova_def = int(status_efeitos[nome_jogador]["def"] * 0.8)
                    status_efeitos[nome_jogador]["def"] = max(nova_def, 1)
                    mensagem += f" A defesa de {nome_jogador} caiu!"
                elif tipo == "Buff Defense":
                    status_efeitos[nome_jogador]["def"] = int(status_efeitos[nome_jogador]["def"] * 1.25)
                    mensagem += f" A defesa de {nome_jogador} aumentou!"

        else:
            mensagem = f"{nome_jogador} usou {golpe['nome']}... mas errou!"

        mostrar_mensagem = True

    def verificar_fim():
        nonlocal fim_batalha, vencedor
        todos_ko_jogador = all(pokemon[p]["stats"]["hp"] <= 0 for p in pokemon_escolhidos)
        todos_ko_cpu = all(pokemon[p]["stats"]["hp"] <= 0 for p in equipe_computador)
        if todos_ko_jogador:
            fim_batalha = True
            vencedor = "Computador"
            pygame.mixer.music.load("musica_perdedor.mp3")
            pygame.mixer.music.play(1)
            
        elif todos_ko_cpu:
            fim_batalha = True
            vencedor = "Jogador"
            pygame.mixer.music.load("musica_vencedor.mp3")
            pygame.mixer.music.play(1)
            
    def escolher_proximo_pokemon(equipe):
        for i, nome in enumerate(equipe):
            if pokemon[nome]["stats"]["hp"] > 0:
                return i
        return 0

    botao_atacar = Botao(50, 650, 250, 150, imagem_path="btn_atacar.png")
    botao_trocar = Botao(320, 650, 250, 150, imagem_path="btn_trocar.png")
    botao_efeito = Botao(50, 120, 120, 25, texto="Efeito Ativo!", cor=(200, 100, 100))
    botao_mensagem = Botao(50, 620, 1430, 50, texto="", cor=(50, 50, 50))
    botao_reiniciar = Botao(480, 585, 255, 80, texto="Reiniciar")
    botao_sair = Botao(790, 585, 255,80, texto="Sair")
    botoes_golpes = []

    #animação de batalha
    def animar_entrada(sprite, inicio_x, fim_x, y, duration=500):
        tempo_inicial = pygame.time.get_ticks()
        while True:
            tempo_atual = pygame.time.get_ticks()
            t = min((tempo_atual - tempo_inicial) / duration, 1)
            x = inicio_x + (fim_x - inicio_x) * t
            tela.blit(fundo_batalha, (0, 0))
            tela.blit(sprite, (x, y))
            pygame.display.flip()
            clock.tick(60)
            if t >= 1:
                break

        def animar_dano(sprite, x, y):
            for _ in range(3):
                tela.blit(fundo_batalha, (0, 0))
                tela.blit(sprite, (x + 10, y))
                pygame.display.flip()
                pygame.time.delay(50)

                tela.blit(fundo_batalha, (0, 0))
                tela.blit(sprite, (x - 10, y))
                pygame.display.flip()
                pygame.time.delay(50)


    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                pos = pygame.mouse.get_pos()

                if fim_batalha:
                    if botao_reiniciar.clicado(pos):
                        pygame.mixer.music.stop()
                        return  # volta para o menu inicial
                    if botao_sair.clicado(pos):
                        pygame.quit()
                        exit()
                elif mostrar_mensagem:
                    mostrar_mensagem = False
                elif not fim_batalha:
                    if turno_jogador:
                        if not modo_ataque:
                            if botao_atacar.clicado(pos):
                                modo_ataque = True
                            elif botao_trocar.clicado(pos):
                                pokemon_jogador_index = (pokemon_jogador_index + 1) % 3
                                mensagem = f"{pokemon_ativo(pokemon_escolhidos, pokemon_jogador_index)['nome']} entrou em campo!"
                                mostrar_mensagem = True
                                turno_jogador = False
                        else:
                            for botao, golpe in botoes_golpes:
                                if botao.clicado(pos):
                                    jogador = pokemon_ativo(pokemon_escolhidos, pokemon_jogador_index)
                                    cpu = pokemon_ativo(equipe_computador, pokemon_computador_index)
                                    if jogador["stats"]["hp"] <= 0:
                                        mensagem = f"{jogador['nome']} está desmaiado e não pode atacar!"
                                        mostrar_mensagem = True
                                        modo_ataque = False
                                        return
                                    executar_ataque(jogador, cpu, golpe)
                                    modo_ataque = False
                                    verificar_fim()
                                    if not fim_batalha:
                                        turno_jogador = False

        jogador = pokemon_ativo(pokemon_escolhidos, pokemon_jogador_index)
        cpu = pokemon_ativo(equipe_computador, pokemon_computador_index)
        if not turno_jogador and not fim_batalha and not mostrar_mensagem:
            jogador = pokemon_ativo(pokemon_escolhidos, pokemon_jogador_index)
            cpu = pokemon_ativo(equipe_computador, pokemon_computador_index)
            if cpu["stats"]["hp"] <= 0:
                mensagem = f"{cpu['nome']} está desmaiado e não pode atacar!"
                mostrar_mensagem = True
            else:
                if not status_efeitos[cpu["nome"]].get("flinch"):
                    golpe_cpu = random.choice(cpu["moveset"])
                    executar_ataque(cpu, jogador, golpe_cpu)
                else:
                    mensagem = f"{cpu['nome']} hesitou devido ao flinch!"
                    status_efeitos[cpu["nome"]]["flinch"] = False
                    mostrar_mensagem = True
        
            if status_efeitos[jogador["nome"]]["burn"]:
                jogador["stats"]["hp"] -= int(0.05 * 100)
                mensagem += f" {jogador['nome']} sofreu dano de queimadura!"
                mostrar_mensagem = True
            verificar_fim()
            if jogador["stats"]["hp"] <= 0:
                pokemon_jogador_index = escolher_proximo_pokemon(pokemon_escolhidos)
                mensagem += f" {pokemon[pokemon_escolhidos[pokemon_jogador_index]]['nome']} entrou em campo!"
                mostrar_mensagem = True
            if cpu["stats"]["hp"] <= 0:
                pokemon_computador_index = escolher_proximo_pokemon(equipe_computador)
                mensagem += f" {pokemon[equipe_computador[pokemon_computador_index]]['nome']} entrou em campo!"
                mostrar_mensagem = True
            turno_jogador = True

        tela.blit(fundo_batalha, (0, 0))

        texto_j = fonte.render(f"{jogador['nome']} - HP: {jogador['stats']['hp']}", True, (0, 0, 0))
        texto_c = fonte.render(f"{cpu['nome']} - HP: {cpu['stats']['hp']}", True, (0, 0, 0))
        tela.blit(texto_j, (250, 85))
        tela.blit(texto_c, (1100, 85))

        desenhar_barra_hp(50, 90, 200, 20, jogador['stats']['hp'])
        desenhar_tipagens(50, 60, 200, 20, jogador["tipo"])
        # Mostrar efeitos ativos abaixo do HP
        efeitos_ativos = status_efeitos[jogador["nome"]]
        pos_y = 120  # posição inicial abaixo da barra de HP
        if efeitos_ativos.get("burn"):
            botao_burn = Botao(50, pos_y, 200, 30, texto="Burn", cor=(200, 0, 0))
            botao_burn.desenhar(tela)
            pos_y += 35

        if efeitos_ativos.get("frozen"):
            botao_frozen = Botao(50, pos_y, 200, 30, texto="Freeze", cor=(100, 200, 255))
            botao_frozen.desenhar(tela)
            pos_y += 35

        if efeitos_ativos.get("sleep", 0) > 0:
            botao_sleep = Botao(50, pos_y, 200, 30, texto="Sleep", cor=(0, 200, 0))
            botao_sleep.desenhar(tela)
            pos_y += 35

        if "buff" in efeitos_ativos:
            botao_buff = Botao(50, pos_y, 200, 30, texto="Attack ↑", cor=(0, 180, 0))
            botao_buff.desenhar(tela)
            pos_y += 35

        if efeitos_ativos.get("def", 0) > jogador["stats"]["def"]:
            botao_buff_def = Botao(50, pos_y, 200, 30, texto="Defense ↑", cor=(0, 180, 0))
            botao_buff_def.desenhar(tela)
            pos_y += 35
        elif efeitos_ativos.get("def", 0) < jogador["stats"]["def"]:
            botao_debuff_def = Botao(50, pos_y, 200, 30, texto="Defense ↓", cor=(180, 100, 0))
            botao_debuff_def.desenhar(tela)
            pos_y += 35
            

        efeitos_ativos_cpu = status_efeitos[cpu["nome"]]
        pos_y = 120  # posição inicial abaixo da barra de HP
        if efeitos_ativos_cpu.get("burn"):
            botao_burn = Botao(900, pos_y, 200, 30, texto="Burn", cor=(200, 0, 0))
            botao_burn.desenhar(tela)
            pos_y += 35

        if efeitos_ativos_cpu.get("frozen"):
            botao_frozen = Botao(900, pos_y, 200, 30, texto="Freeze", cor=(100, 200, 255))
            botao_frozen.desenhar(tela)
            pos_y += 35

        if efeitos_ativos_cpu.get("sleep", 0) > 0:
            botao_sleep = Botao(900, pos_y, 200, 30, texto="Sleep", cor=(0, 200, 0))
            botao_sleep.desenhar(tela)
            pos_y += 35

        if "buff" in efeitos_ativos_cpu:
            botao_buff = Botao(900, pos_y, 200, 30, texto="Attack ↑", cor=(0, 180, 0))
            botao_buff.desenhar(tela)
            pos_y += 35

        if efeitos_ativos_cpu.get("def", 0) > cpu["stats"]["def"]:
            botao_buff_def = Botao(900, pos_y, 200, 30, texto="Defense ↑", cor=(0, 180, 0))
            botao_buff_def.desenhar(tela)
            pos_y += 35
        elif efeitos_ativos_cpu.get("def", 0) < cpu["stats"]["def"]:
            botao_debuff_def = Botao(900, pos_y, 200, 30, texto="Defense ↓", cor=(180, 100, 0))
            botao_debuff_def.desenhar(tela)
            pos_y += 35
        desenhar_barra_hp(900, 90, 200, 20, cpu['stats']['hp'])
        desenhar_tipagens(900, 60, 200, 20, cpu["tipo"])

        

        if jogador['nome'] in sprites_jogador:
            tela.blit(sprites_jogador[jogador['nome']], (300, 450))  # nova posição do jogador

        if cpu['nome'] in sprites_cpu:
            tela.blit(treinador_cpu_sprite, (900, 175))
            tela.blit(sprites_cpu[cpu['nome']], (750, 300))          # nova posição do CPU



        if mensagem and mostrar_mensagem:
            botao_mensagem.surface.fill((30, 30, 30))
            texto_msg = fonte.render(mensagem, True, (255, 255, 0))
            botao_mensagem.surface.blit(texto_msg, (10, 10))
            botao_mensagem.desenhar(tela)

        if fim_batalha:
            tela.blit(tela_final,(0, 0))
            fonte_grande = pygame.font.SysFont("comicsansms", 64)
            fim_texto = fonte_grande.render(vencedor, True, (0, 0, 0))
            tela.blit(fim_texto, (550, 400))
            desenvolvedores_texto = [
                "Desenvolvedores:",
                "Douglas Santana De Oliveira",
                "Luís Octávio Lacerda Pereira",
                "Miguel Anderson Albino Do Carmo"
            ]
            y_inicial = 50
            espacamento = 35  
            for i, linha in enumerate(desenvolvedores_texto):
                texto = fonte.render(linha, True, (0, 0, 0))
                tela.blit(texto, (30, y_inicial + i * espacamento))

        elif turno_jogador and not mostrar_mensagem:
            if not modo_ataque:
                botao_atacar.desenhar(tela)
                botao_trocar.desenhar(tela)
            else:
                botoes_golpes.clear()
                cores_por_tipo = {
                    "Grass": (0, 180, 0),
                    "Flying": (100, 200, 255),
                    "Ground": (194, 178, 128),
                    "Rock": (120, 72, 0),
                    "Bug": (34, 139, 34),
                    "Ghost": (128, 0, 128),
                    "Fire": (255, 60, 60),
                    "Water": (0, 120, 255),
                    "Ice": (173, 216, 230),
                    "Dark": (0, 0, 0),
                    "Fighting": (255, 140, 0),
                    "Steel": (169, 169, 169),
                    "Psychic": (255, 105, 180),
                    "Normal": (255, 255, 255)
                }
                for i, golpe in enumerate(jogador["moveset"]):
                    tipo = golpe["tipo"]
                    cor = cores_por_tipo.get(tipo, (100, 100, 255))  # cor padrão

                    botao = Botao(50, 600 + i * 50, 400, 40, texto=None, cor=cor)

                    if tipo in ["Normal", "Steel"]:
                        cor_fonte = (0, 0, 0)  # Preto para botões claros
                    else:
                        cor_fonte = (255, 255, 255)  # Branco para botões escuros

                    texto_render = fonte.render(golpe["nome"], True, cor_fonte)
                    texto_rect = texto_render.get_rect(center=(400 // 2, 40 // 2))
                    botao.surface.blit(texto_render, texto_rect)

                    botoes_golpes.append((botao, golpe))
                    botao.desenhar(tela)
                # Verifica se o mouse está sobre algum botão de ataque
                mouse_pos = pygame.mouse.get_pos()
                for botao, golpe in botoes_golpes:
                    if botao.rect.collidepoint(mouse_pos):
                        # Dados do golpe
                        dano = golpe["dano"]
                        tipo = golpe["tipo"]
                        precisao = golpe["precisao"]
                        efeito_obj = golpe.get("efeito")
                        efeito = efeito_obj.get("nome") if efeito_obj else "Nenhum"
                        chance = efeito_obj.get("chance") if efeito_obj else 0


                        # Cria o texto de descrição
                        descricao = f"Dano: {dano}  |  Precisão: {precisao}%  |  Tipo: {tipo}  |  Efeito: {efeito} ({chance}%)"
                        texto_info = fonte.render(descricao, True, (255, 255, 255))

                        # Caixa de fundo
                        info_box = pygame.Surface((texto_info.get_width() + 20, texto_info.get_height() + 10))
                        info_box.fill((50, 50, 50))
                        info_box.blit(texto_info, (10, 5))

                        # Posição da caixa (ajustável)
                        tela.blit(info_box, (500, 820))  # ou mouse_pos para seguir o cursor
                        break  # só mostra 1 por vez



        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
