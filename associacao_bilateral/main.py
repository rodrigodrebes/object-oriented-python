from pessoa import Pessoa
from casa import Casa

casa_da_ana = Casa()
ana = Pessoa("Ana")
pedro = Pessoa("Pedro")

ana.set_local(casa_da_ana)
casa_da_ana.set_proprietario(pedro)

proprietario = casa_da_ana.get_proprietario()
proprietario.se_apresentar()

ana.apresentar_local()
