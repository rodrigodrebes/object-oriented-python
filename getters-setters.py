class Pessoa: #Substantivo
    
    def __init__(self, nome:str, idade:int) -> None:
        self.__nome = nome #Substantivo
        self.__idade = idade #Substantivo

    def get_idade(self) -> int:
        return self.__idade
    
    def set_idade(self, idade) -> int:
        self.__idade = idade
  
pessoa = Pessoa("Diego", 45)

print(pessoa.get_idade())
pessoa.set_idade(50)
print(pessoa.get_idade())

class Alarme:
    
    def __init__(self, estado: bool) -> None:
        self.__estado = estado
    
    def get_estado(self) -> bool:
        return self.__estado
    
    def set_estado(self, valor: bool) ->None:
        if isinstance(valor, bool):
          self.__estado = valor

al = Alarme(False)
print(al.get_estado())
al.set_estado(10)
print(al.get_estado())
al.set_estado(True)
print(al.get_estado())