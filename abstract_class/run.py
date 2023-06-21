from abs_class import AbstractClass

class Filha(AbstractClass):
    def apresentar_metodo(self)->None:
        print(self.atributo)
    
    #Elemento obrigatoriamente implementado
    def metodo_abstrato(self) -> None:
        print("Implementando método abstrato")


filha = Filha()
filha.apresentar_metodo()
filha.metodo("estou aqui")
filha.metodo_abstrato()

# Erro: não se pode instanciar classe Abstrata
# abstractclass = AbstractClass()
# abstractclass.metodo("Fazendo algo")