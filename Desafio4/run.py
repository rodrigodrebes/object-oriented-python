from models.livro import Livro
from models.biblioteca import Biblioteca

ontheroad = Livro("On the Road", "Jack Kerouac", 1952)
a_uruguaia=Livro("A Uruguaia", "Pedro Mairal", 2005)

biblioteca = Biblioteca()

biblioteca.adicionar_livro(ontheroad)
biblioteca.adicionar_livro(a_uruguaia)

biblioteca.listar_livros()