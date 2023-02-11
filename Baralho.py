import random


class Baralho:
    def __init__(self, qtdJogos):
        self.influencias = []
        for i in range(0, qtdJogos):
            [self.influencias.append(i) for i in range(0, 5)]
        random.shuffle(self.influencias)
    # duque - 0
    # capitao - 1
    # assasino - 2
    # condessa - 3
    # embaixador - 4
