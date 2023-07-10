import random

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.vitorias = 0

    def jogar(self):
        return random.choice(['Pedra', 'Papel', 'Tesoura'])
    
    def incrementar_vitoria(self):
        self.vitorias += 1