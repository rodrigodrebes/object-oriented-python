from typing import Type
import Interruptor


class Pessoa:
    
    def acender_luz(self, interruptor: Interruptor):
        interruptor.acender()

    def apagar_luz(self, interruptor: Interruptor):
        interruptor.apagar()
    
    def dormir(self):
        print("Fui dormir")