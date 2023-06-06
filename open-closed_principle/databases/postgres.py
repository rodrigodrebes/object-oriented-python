class PostgresDB:
    
    def __init__(self) -> None:
        self.__conexao = "PostgreSQL"
    
    def conectar(self) -> str:
        print("Conectando ao Banco de Dados...")
        return self.__conexao

    def desconectar(self) -> str:
        print("Desconectando do Banco de Dados...")