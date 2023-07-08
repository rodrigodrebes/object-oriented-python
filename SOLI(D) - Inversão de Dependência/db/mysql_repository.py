from .interface import Repositorio

class MySqlRepositorio(Repositorio):
    
    def inserir(self, dado) ->None:
        print(f'Inserindo {dado} no banco MySQL')

    def excluir(self, dado)->None:
        print(f'Excluindo {dado} do banco MySQL')