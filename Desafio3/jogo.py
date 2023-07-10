class Jogo:
    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2

    def jogar_rodada(self):
        escolha1 = self.jogador1.jogar()
        escolha2 = self.jogador2.jogar()
        print(f'{self.jogador1.nome} escolheu {escolha1}')
        print(f'{self.jogador2.nome} escolheu {escolha2}')

        if escolha1 == escolha2:
            print('Empate!')
        elif (escolha1 == 'Pedra' and escolha2 == 'Tesoura') or \
            (escolha1 == 'Papel' and escolha2 == 'Pedra') or \
            (escolha1 == 'Tesoura' and escolha2 == 'Papel'):
            self.jogador1.incrementar_vitoria()
            print(f'{self.jogador1.nome} ganhou!')
        else:
            self.jogador2.incrementar_vitoria()
            print(f'{self.jogador2.nome} ganhou!')