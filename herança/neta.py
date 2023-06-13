from filha import Filha

class Neta(Filha):
        
    def __init__(self, endereco):
      #Referência ao construtor da classe filha
      super().__init__(endereco)