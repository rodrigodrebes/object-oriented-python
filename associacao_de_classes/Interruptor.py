class Interruptor:
    def __init__(self, comodo: str) -> None:
        self.__comodo = comodo
    
    def acender(self):
        print(f"Acendendo o(a) {self.__comodo}")
    
    def apagar(self):
        print(f"Apagando o(a) {self.__comodo}")