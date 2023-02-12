class Influencia:
    def __init__(self, id):
        influenciaNome = [
            'Duque',
            'Capitão',
            'Assassino',
            'Condessa',
            'Embaixador'
        ]
        self.id = id
        self.nome = influenciaNome[id]
        self.ativo = True

    def setAtivo(ativo):
        self.ativo = ativo
