# Open / Closed Principle
# Entradas diferentes geram ações diferentes
# Classes devem estar abertas para extensão e fechadas para modificações

# Classe extremamente fechada para extensão (ERRADA)
class Circo:
    
    def apresentar(self, tipo):
        if tipo == 1:
            self.apresentar_malabarista()
        if tipo ==2:
            self.apresentar_palhaco()
    
    def apresentar_malabarista(self):
        print("Malabarista irá se apresentar agora")

    def apresentar_palhaco(self):
        print("Palhaço irá se apresentar agora")


# Classe com módulo aberto disponível para extensão (CERTA)
class Circo2:
    def apresentar(self, apresentador: any):
      apresentador.apresentar_show()
    

class Malabarista:
        def apresentar_show(self):
          print("Malabarista irá se apresentar agora")

class Palhaco:
        def apresentar_show(self):
          print("Palhaço irá se apresentar agora")

circo = Circo2()
malabarista = Malabarista()
palhaco = Palhaco()

circo.apresentar(malabarista)
circo.apresentar(palhaco)
