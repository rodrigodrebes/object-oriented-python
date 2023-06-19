class PessoaA:
    
    def se_apresentar(self):
        print("Olá, sou a Pessoa A")

class PessoaB(PessoaA):
    
    def __init__(self) -> None:
        super().__init__()

    def se_apresentar(self):
        print("Estou alterando esse método")

class PessoaC(PessoaB):
    
    def __init__(self) -> None:
        super().__init__()
    
    def se_apresentar(self):
        print("Alterando novamente")

roberto = PessoaA()
luiz = PessoaB()
ana = PessoaC()

roberto.se_apresentar()
luiz.se_apresentar()
ana.se_apresentar()