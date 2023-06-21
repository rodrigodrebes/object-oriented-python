from engenheiro import Engenheiro
from terrenos.quadrado import TerrenoQuadrado
from terrenos.retangular import TerrenoRetangular

rodrigo = Engenheiro("Rodrigo")
quadrado = TerrenoQuadrado(5)
retangular = TerrenoRetangular(2,3)

rodrigo.medir_area(quadrado)
rodrigo.medir_area(retangular)