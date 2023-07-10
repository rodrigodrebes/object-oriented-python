class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def remover_livro(self, livro):
        self.livros.remove(livro)

    def listar_livros(self):
        for livro in self.livros:
            print(f'ID: {livro.get_id()}, Título: {livro.get_titulo()}, Autor: {livro.get_autor()}')
