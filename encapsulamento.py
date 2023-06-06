class Pessoa:
    
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def correr(self):
        print("estou correndo")
    
    def beber(self, bebida):
        if bebida == "cerveja":
            self.__apresentar_documento()
        print("bebendo...")

    #Métodos privados começam por "__"
    def __apresentar_documento(self):
        print(self.__cpf)
    

pessoa = Pessoa("Rodrigo", 32, '055-555-555-88')

pessoa.beber('cerveja')
pessoa.beber('coca-cola')


class Calculadora:
    def calcular(self, op, x, y):
        if op == "+":
            return self.__adicionar(x,y)
        elif op == "-":
            return self.__subtrair(x,y)
        else:
            print("Operação inválida")
    
    def __adicionar(self, x ,y):
        return x + y

    def __subtrair(self, x,y):
        return x-y

calculadora = Calculadora()
resultadoSoma = calculadora.calcular('+', 3, 2)
resultadoSubtracao = calculadora.calcular('-', 5, 5)
print(resultadoSoma, resultadoSubtracao)
