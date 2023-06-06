class MinhaClasse:
    
    estatico = 'Caneta'

    def __init__(self, estado) -> None:
        self.estado = estado
    
    def print_estatico(self):
        print(self.estatico)

    @classmethod
    def mudar_estatico(cls):
        cls.estatico = "Tesoura"

obj1 = MinhaClasse(True)

#Contexto de Classe e objeto são os mesmos:
print(MinhaClasse.estatico)
print(obj1.estatico)

#Contexto de Classe é passado aos objetos, mas não vice-versa
MinhaClasse.estatico = "Lápis"
print(MinhaClasse.estatico)
print(obj1.estatico)

#Contexto de Classe 
MinhaClasse.mudar_estatico()
print(MinhaClasse.estatico)


# Para evitar isso, deve-se usar @classmethod
class Loja:

    tarifa = 1.5

    def __init__(self, endereco):
        self.__endereco = endereco
    
    def apresentar_endereco(self):
        print(self.__endereco)
    
    @classmethod
    def vender(cls) -> int:
        return 40 * cls.tarifa
    
    @classmethod
    def alterar_tarifa(cls, nova_tarifa: int) -> None:
        cls.tarifa = nova_tarifa

loja_cidade = Loja("Porto Alegre")
loja_praia = Loja("Tramandai")

loja_praia.apresentar_endereco()
loja_cidade.apresentar_endereco()

print(loja_praia.vender())
print(loja_cidade.vender())

loja_praia.alterar_tarifa(2.50)

print(loja_praia.vender())
print(loja_cidade.vender())