class DatabaseConn:
    def __init__(self) -> None:
        # "__" privado
        # "_" protected
        # "" publico

        self.__database = "Postgres"
        self._conn = "//contection_string"
        self.user = "Lhama"

    def get_database(self) -> None:
        print(self.__database)

    def _testing_connection(self) -> None:
        print("Conection Ok!")


class Repository(DatabaseConn):
    
    def __init__(self) -> None:
        super().__init__()
        #print(self.user)
        #print(self.__database) # Erro, elemento privado
        #print(self._conn)
    
    def select(self) -> None:
        self._testing_connection()
        print(f"connection to {self._conn}")
        print("SELECT * FROM table")


db = DatabaseConn()
#print(db.user) # como é publico, printa normalmente
#print(db.__database) # Erro, elemento privado

repo = Repository()
repo.select()
