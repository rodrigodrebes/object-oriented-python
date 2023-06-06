class Erro:
    
    def __init__(self, estado) -> None:
        self.estado = estado
    
    @staticmethod #contexto único e separado da classe
    def protocolo():
        print("Protocolo apresenta erro")
    
    @staticmethod
    def entrada():
        print("Parâmetros incorretos")

Erro.protocolo()