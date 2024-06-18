from cadastro import Cadastro

class CadastroDiretoria(Cadastro):
    def __init__(self, nome: str, idade: int, endereco: str, telefone: str, email: str, login: str, senha: str, cargo: str) -> None:
        """Construtor da classe CadastroDiretoria

        Args:
            nome (str): nome do funcionário
            idade (int): idade
            endereco (str): endereço do funcionário
            telefone (str): telefone do funcionário
            email (str): email do funcionário
            login (str): login a ser utilizado para logar no sistema
            senha (str): senha a ser utilizada para logar no sistema
            cargo (str): cargo do funcionário
        """
        super().__init__(nome, idade, endereco, telefone, email, login)
        self.cargo = cargo
        self.__senha = senha

    def save(self) -> None:
        """Método para salvar as informações do funcionário no banco de dados
        """
        try:
            data = {
                "nome": self.nome,
                "idade": self.idade,
                "endereco": self.endereco,
                "telefone": self.telefone,
                "email": self.email,
                "login": self._login,
                "senha": self.__senha,
                "cargo": self.cargo
            }
            self.db.insert_data("Diretoria", data)
            print("Dados cadastrados com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar: {e}")
