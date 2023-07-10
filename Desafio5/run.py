from planejador import PlanejadorDeViagem
from destinos.belo_horizonte import BeloHorizonte
from destinos.fortaleza import Fortaleza
from destinos.riodejaneiro import RioDeJaneiro


planejadorDeViagem = PlanejadorDeViagem()

while(True):
    destino = None

    destino_de_viagem = input("Selecione o Destino: ")

    if(destino_de_viagem == "1"): 
      destino = BeloHorizonte()
      
    elif(destino_de_viagem =="2"): 
      destino = Fortaleza()  
    
    elif(destino_de_viagem == "3"): 
      destino = RioDeJaneiro()
    

    atividade = planejadorDeViagem.viajar(destino)
    print(atividade)
    break
