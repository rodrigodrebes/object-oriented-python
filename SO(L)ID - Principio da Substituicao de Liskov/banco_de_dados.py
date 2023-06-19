from typing import Type

class Conexao:
    
    def conectar(self):
        print("Conectando ao DB...")
    

    def desconectar(self):
        print("Desconectando do DB...")

class MySqlRepo(Conexao):
    
    def __init__(self) -> None:
        super().__init__()
    
    def select(self):
        self.conectar()
        print("SELECT * FROM tabela")

class CasoDeUso:
    def buscar(self, db_repo:Type[MySqlRepo]):
        db_repo.select()