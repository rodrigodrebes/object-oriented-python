from typing import Type
from db.interface import Repositorio
from db.mongo_repository import MongoRepositorio
from db.mysql_repository import MySqlRepositorio

class Usuario:
    
    def __init__(self, repositorio: Type[Repositorio]) -> None:
        self.__repositorio = repositorio 
    

    def armazenar_dados(self, dado: any)->None:
        self.__repositorio.inserir(dado)

    def remover_dados(self, dado:any)->None:
        self.__repositorio.excluir(dado)

usuario = Usuario(MySqlRepositorio())
usuario.armazenar_dados(23)


usuario2 = Usuario(MongoRepositorio())
usuario2.armazenar_dados("Artigo Científico")

