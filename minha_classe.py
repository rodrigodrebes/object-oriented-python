class ControleRemoto:
    
    #Método construtor
    def __init__(self, televisao, comodo):
        self.televisao = televisao
        self.comodo = comodo

    #Métodos da classe
    def avancar_canal(self):
        print("Canal avançado!")

    def voltar_canal(self):
        print("Voltar o canal")

    def escolher_canal(self, canal):
        print(f"Alterado para o canal: {canal}")

controleSala = ControleRemoto("Samsumg", "Sala")
print(controleSala.comodo)
print(controleSala.televisao)
controleSala.avancar_canal()
controleSala.escolher_canal(12)

