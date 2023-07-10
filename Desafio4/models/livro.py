

class Livro:
    __id_atual = 0 

    def __init__(self, titulo: str, autor: str, ano: int) -> None:
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__id = Livro.__id_atual
        Livro.__id_atual += 1  

    def set_titulo(self, titulo):
        self.__titulo = titulo
    
    def get_titulo(self):
        return self.__titulo

    def set_autor(self, autor):
        self.__autor=autor
    
    def get_autor(self):
        return self.__autor

    def get_id(self):
        return self.__id
