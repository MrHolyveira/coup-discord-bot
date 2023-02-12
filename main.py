import random
from Juiz import Juiz

# LOOP principal do jogo:

# 1º Fase de confirmação de participação:
#   Vai gerar uma lista de pessoas que irão participar.
participantes = ["vudu", "julia", "alex"]

# 2º Fase de criação da partida:
#   A partir da lista de pessoas o uiz criará a partida.

# Criação do juiz
juiz = Juiz(participantes)
# print(juiz.baralho.influencias)

for jogador in juiz.jogadores:
    print('Jogador: '+jogador.nome)
    # print('Baralho: ', jogador.mao)
    print()
# print('Baralho restante:')
# print(juiz.baralho.influencias)

acoesPermitidas = ['1', '2', '3', '4']

# 3º Jogo!

# Turno:

# o jogador escolhido escolhe uma ação:

# for jogadorDaVez in juiz.jogadores:
while True:
    jogadorDaVez = juiz.jogadores.pop(0)
    print("Jogador da rodada: " + jogadorDaVez.nome)
    if jogadorDaVez.moedas <= 10:
        # Espera a ação do jogador
        print("escolha sua ação:")
        # Ações: Renda, Ajuda externa, Golpe de estado, Ação de personagem

        acao = input(
            "1 - Renda, 2 - Ajuda externa, 3 - Golpe de estado, 4 - Ação de personagem")
        if acao in acoesPermitidas:
            match acao:
                # Renda
                case '1':
                    # jogadorDaVez.moedas = jogadorDaVez.moedas + 1
                    # Usar método do jogador
                    # Ajuda externa
                    pass
                case '2':
                    pass
                # Golpe de estado
                case '3':
                    # if jogadorDaVez.moedas >= 7:
                    print(
                        "Selecione o jogador que você deseja dar o golpe de estado:")
                    for i, jogador in enumerate(juiz.jogadores):

                        print('Digite '+str(i + 1)+' para:')
                        print('-------------------------')
                        print('Jogador: '+jogador.nome)
                        print('Baralho: ', jogador.mao)
                        print('-------------------------')

                        print()
                    alvo = int(input(''))-1
                    juiz.golpeDeEstado(juiz.jogadores[alvo])
                # Ação de personagem
                case '4':
                    pass
            # Caso o jogador tiver 10 ou mais moedas ele é obrigado a dar um golpe de estado.

            # Após a escolha essa ação pode ser bloqueada ou contestada, se não for contestada ou bloqueada a ação é bem sucedida.
            # Contestações são resolvidas antes de qualquer ação ou ação contrária
    else:
        # Jogador é obrigado a dar golpe de estado.
        pass
    juiz.jogadores.append(jogadorDaVez)

# juiz.jogadores[2].mao = []
# juiz.golpeDeEstado(juiz.jogadores[2])
# print(juiz.jogadores[2].mao[0].ativo)
# print(juiz.jogadores[2].mao[1].ativo)
