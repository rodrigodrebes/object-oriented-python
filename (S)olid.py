# Princípio da Responsabilidade Única
# Conjunto coeso e único de dados

# Errado
class SistemaCadastral:
    def cadastrar(self, nome: str, idade: int) -> None:
        if isinstance(nome, str) and isinstance(idade, int):
            print("Acessando o banco de dados...")
            print(f"Cadastrar o usuário {nome}, idade {idade}")
        else:
            print("Dados inválidos")

# Certo
class SistemaCadastral2:
    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__verificar_dados(nome, idade):
            self.__armazenar_usuario(nome, idade)
        else:
            self.__indicar_erro()

    def __verificar_dados(self, nome: str, idade: int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
            return True
        return False

    def __armazenar_usuario(self, nome:str, idade:int) -> None:
        print("Acessando o banco de dados...")
        print(f"O usuário {nome}, idade {idade}, foi cadastrado!")

    def __indicar_erro(self) -> None:
        print("Dados inválidos!")

sistema = SistemaCadastral2()
#Dados válidos
sistema.cadastrar("Rodrigo", 27)
#Dados inválidos
sistema.cadastrar(27, "Lucas")