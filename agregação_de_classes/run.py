from produtos import Produtos
from carrinho import CarrinhoDeCompras

carrinho = CarrinhoDeCompras()
monitor = Produtos("Monitor", 1500)
cerveja = Produtos("Cerveja", 4)

carrinho.adicionar_produto(monitor)
carrinho.adicionar_produto(cerveja)

carrinho.finalizar_compra()