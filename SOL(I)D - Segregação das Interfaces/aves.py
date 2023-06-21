from interface import AveTerrestre, AveVoadora

class Canario (AveVoadora):
    def comer(self):
        print("estou comendo")
    
    def voar(self):
        print("estou voando")

    def cantar(self):
        print("estou cantando")


class Pinguim(AveTerrestre):
    def comer(self):
        print("estou comendo")
        self.__descansar()

    def __descansar(self):
        print("agora vou descansar")