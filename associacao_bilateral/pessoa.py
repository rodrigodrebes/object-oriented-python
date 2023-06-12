class Pessoa:
    
    def __init__(self, nome: str) -> None:
        self.__local = None
        self.__nome = nome
    
    def entrarNaCasa(self) -> None:
        print("Entrando na casa")

    def entrar_no_local(self) -> None:
        self.entrarNaCasa()
        self.__local.acender_luzes()
    
    def apresentar_local(self) -> None:
        endereco = self.__local.get_endereco()
        print(endereco)
    
    def se_apresentar(self)->None:
        print(f"Ola, eu sou {self.__nome}")
    
    def set_local(self, local: any) -> None:
        self.__local = local

    def get_local(self)->any:
        return self.__local