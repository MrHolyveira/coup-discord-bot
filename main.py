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
    print('Baralho: ', jogador.mao)
    print()
print('Baralho restante:')
print(juiz.baralho.influencias)

# 3º Jogo!
