from jogador import Jogador
from jogo import Jogo

jogador1 = Jogador("Pedro")
jogador2 = Jogador("João")
jogo = Jogo(jogador1, jogador2)

for _ in range(5):  # Jogue 5 rodadas
    jogo.jogar_rodada()

print(f'{jogador1.nome} ganhou {jogador1.vitorias} vez(es)')
print(f'{jogador2.nome} ganhou {jogador2.vitorias} vez(es)')