from typing import Type
from destinos.interfaces.destinos import DestinoInterface

class PlanejadorDeViagem:
    
    def viajar(self, destino: Type[DestinoInterface])->None:
        return destino.atividade()