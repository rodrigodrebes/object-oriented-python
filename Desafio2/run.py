from model.elevador import Elevador
from controller.gerenciador_de_elevadores import GerenciadorDeElevadores

gerenciadorDeElevadores = GerenciadorDeElevadores(
    Elevador(1), Elevador(2)
)

while (True):
    elevadorId = int(input('Defina o elevador: '))
    andar = int(input('Defina um andar: '))

    response = gerenciadorDeElevadores.locomover(andar, elevadorId)
    print(response)
    print()