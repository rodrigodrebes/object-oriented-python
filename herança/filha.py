from mae import Mae

class Filha(Mae):
    
    def __init__(self, endereco):
        #Referência ao construtor da classe mãe
        super().__init__(endereco)
    
    def brincar(self, brinquedo: str)-> None:
        print(f"Estou brincando com {brinquedo}")