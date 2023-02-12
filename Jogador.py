class Jogador:
    def __init__(self, nome, influencia1, influencia2):
        self.nome = nome
        self.mao = [influencia1, influencia2]
        self.moedas = 2

    def bloqueio():
        print("Bloqueio")

    def contesta():
        print("Contesta")

    def renda():
        print("Renda")

    def ajudaExterna():
        print("Ajuda Externa")

    def perderMoeda():
        print("Perder Moeda")

    # Necessário ter um método para cada forma de perder influência?
    # Fomas de perder influência:
    # Golpe de estado
    # Assasinato
    # Contestação errada
    # Contestação certa
    # Criei um método genérico de perder influência para debatermos esse ponto depois
    def golpeEstado(influencia):

        print("Golpe de Estado")

    def mensagemPrivada(self, mensagem):
        print(self.nome+':', mensagem)

    def aguardeAcao(self, mensagem):
        return input(self.nome+': '+mensagem)

    def perderInfluencia(self, influencia):
        self.mao[influencia-1].ativo = False

    def mostrarMao(self):
        for i, influencia in enumerate(self.mao):
            if influencia.ativo:
                print(i+1, "-", influencia.nome)
