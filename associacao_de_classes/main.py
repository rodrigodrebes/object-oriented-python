from Pessoa import Pessoa
from Interruptor import Interruptor

rodrigo = Pessoa()

interruptor_quarto = Interruptor("Quarto")
interruptor_cozinha = Interruptor("Cozinha")

interruptor_quarto.acender() # Instanciação direta da classe
rodrigo.apagar_luz(interruptor_cozinha) #Instancia a partir de Pessoa
rodrigo.apagar_luz(interruptor_quarto)
rodrigo.dormir()