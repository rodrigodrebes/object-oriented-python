from casa import Casa
from pessoa import Pessoa
# Injeção de Dependências: ações de um objeto dependem de outro objeto
# Pode não ser interessante, já que gera alto acoplamento entre classes (resolução = Interfaces e Herança)

casa_de_amigo = Casa()
ana = Pessoa("Ana", casa_de_amigo)

ana.apresentar_local()
ana.entrar_no_local()