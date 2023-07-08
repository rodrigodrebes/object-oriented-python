from .interface import Repositorio

class MongoRepositorio(Repositorio):
    
    def inserir(self, dado) ->None:
        print(f'Inserindo {dado} no banco Mongo')

    def excluir(self, dado)->None:
        print(f'Excluindo {dado} do banco Mongo')