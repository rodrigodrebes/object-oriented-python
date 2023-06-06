from typing import Type
from casa import Casa

class Pessoa:
    
    def __init__(self, nome: str, local:Type[Casa]) -> None:
        self.__local = local
        self.__nome = nome
    
    def entrar_no_local(self) -> None:
        self.entrarNaCasa()
        self.__local.acender_luzes()
    
    def apresentar_local(self) -> None:
        endereco = self.__local.get_endereco()
        print(endereco)
    
    def entrarNaCasa(self) -> None:
        print("Entrando na casa")