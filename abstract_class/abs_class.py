from abc import ABC, abstractmethod

#para ter uma classe abstrata em python, deve haver no mínimo um método abstrato

class AbstractClass(ABC):
    
    def __init__(self) -> None:
        self.atributo = "Olá mundo"

    def metodo(self, elemento: str)->None:
        print(elemento)
        
    @abstractmethod
    def metodo_abstrato(self)->None:
        pass