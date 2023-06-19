#Mesma funcionalidade para mesmo método
#Subtipos intercambiáveis
#Elemento genérico deve estar no topo da Herança
#Herança deve servir para COMPLEMENTAÇÃO

from typing import Type

class Animal:
    def comer(self):
        print("O Animal esta comendo")
    
    def dormir(self):
        print("O Animal está dormindo")

    def andar(self):
        print("O animal está andando na jaula")

class Aves(Animal):
    def __init__(self) -> None:
        super().__init__()
    
    def cantar(self):
        print("A Ave está cantando")

class Pinguim(Aves):
    
    def __init__(self) -> None:
        super().__init__()
    
    def escorregar(self):
        print("O pinguim está escorregando no gelo")

class Pessoa:
    def observar(self, animal:Type[Animal]):
        animal.comer()

roberto = Pessoa()
pinguim = Aves()
roberto.observar(pinguim)