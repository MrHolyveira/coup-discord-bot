import random

from Baralho import Baralho
from Jogador import Jogador
from Influencia import Influencia


class Juiz:
    def __init__(self, participantes, regraDaCondensa=False, regraDoCapitao=False, jogoContado=True, tempoDeEspera=120):
        self.regraDaCondensa = regraDaCondensa
        self.regraDoCapitao = regraDoCapitao
        self.tempoDeEspera = tempoDeEspera  # em segundos
        # de acordo com a regra: Sempre que um jogador perder uma influência dele deve virar uma de suas cartas para cima.
        self.jogoContado = jogoContado
        self.qtdJogadores = len(participantes)  # minimo 3 jogadores
        self.jogadores = []

        # Criação do baralho
        if 3 <= self.qtdJogadores <= 6:  # de 3 a 6 pessoas
            self.baralho = Baralho(3)
        elif 7 <= self.qtdJogadores <= 8:  # de 7 a 8 pessoas
            self.baralho = Baralho(4)
        elif 9 <= self.qtdJogadores <= 10:  # de 9 a 10 pessoas
            self.baralho = Baralho(5)
        # Criação dos jogadores e distribuição das influências:
        for jogador in participantes:
            self.jogadores.append(
                Jogador(nome=jogador, influencia1=Influencia(self.baralho.influencias.pop()), influencia2=Influencia(self.baralho.influencias.pop())))
        # Deixa aleatório a ordem para começar o jogo
        random.shuffle(self.jogadores)

    def saida(x):
        print(x)

    def entrada():
        return input(x)

    def criacaoPartida(self):
        self.saida("Bem-vindo ao coup do Pitinho rosa")
        self.saida("Por favor vamos criar as regras aqui")
        self.saida("Quantos jogadores v達o jogar?")
        self.qtdeJogadores = self.entrada()
        self.saida(
            "A condensa vai poder bloquear outros jogadores? Digite 0 para n達o, 1 para sim")
        self.regraDaCondensa = self.entrada()
        self.saida(
            "O capitão e o embaixador podem bloquear o roubo de um outro capit達o? 1=s 0=n")
        self.regraDoCapitao = self.entrada()
        self.saida("quanto tempo vc quer de espera? escreva em segundos")
        self.tempoDeEspera = self.entrada()
        self.saida("vc quer que possa contar cartas ? 1=s 0=n")
        self.jogoContado = self.entrada()

        # x-x-x
        # criou tudo que eh ecessario
        # quem comeca
        # sortear os jogadores como se fosse um dado ?

        # primeiro jogador, oque quer fazer ? aperte o butao
        # regras definidas

    # como dar carta adicionar stack ?

    def darCarta(jogador, carta):
        jogador.influencia2 = carta

    def tirarCarta(jogador):
        pass

    def tempoEspera():
        pass

    # funcoes de verificac
    def verificarMoedas():
        pass

    def verificarJogada():
        pass

    def darMoedaS(jogador):
        verificarMoedas()
        jogador.moedas = jogador.moedas+1
        pass

    def tirarMoedas(jogador):
        verificarMoedas()
        jogador.moedas = jogador.moedas-1
        pass

    def criarJogadores(numbers, nomes):
        jogadores = []
        # x vai ser os nomes
        for x in range(numbers):
            jogadores.append(Jogador(nomes[x]))
        return jogadores

    def golpeDeEstado(self, jogador):

        if jogador.mao[0].ativo and jogador.mao[1].ativo:
            influenciaSelecionada = jogador.aguardeAcao(
                "Selecione qual influência você vai perder: ")

            jogador.perderInfluencia(int(influenciaSelecionada))
            print("Golpe de estado dado em:")
            print(jogador.nome)
        else:
            jogador.perderInfluencia(1)
            jogador.perderInfluencia(2)
            self.jogadores.remove(jogador)
            print(jogador.nome, "Perdeu todas suas influências e está fora do jogo!")
            print("Mão do jogador: ")
            print(jogador.mao)
