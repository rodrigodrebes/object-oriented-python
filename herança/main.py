from mae import Mae
from filha import Filha
from neta import Neta


ana = Mae("Rua das Laranjeiras")

roberta = Filha("Rua dos Mouros")
roberta.estudar()
roberta.brincar("boneca")
print(roberta.endereco)

print(ana.endereco)

laura = Neta("Salgado Filho")
print(laura.endereco)