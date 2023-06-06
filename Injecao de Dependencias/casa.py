
class Casa:
    
    def __init__(self) -> None:
        self.__endereco = "Rua dos Limoeiros"
    
    def acender_luzes(self) -> None:
        print("Estou acendendo as luzes")
    
    def get_endereco(self)->str:
        return self.__endereco