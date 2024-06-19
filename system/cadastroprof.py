from cadastro import Cadastro
from typing import List

class CadastroProfessor(Cadastro):
    def __init__(self, nome: str, idade: int, endereco: str, telefone: str, email: str, login: str, senha: str, disciplinas_matriculadas : List[str] = None) -> None:
        """Construtor da classe CadastroProfessor

        Args:
            nome (str): nome do professor
            idade (int): idade do professor
            endereco (str): endereço do professor
            telefone (str): telefone do professor
            email (str): email do professor
            login (str): login utilizado para logar no sistema
            senha (str): senha utilizada para logar no sistema
            disciplinas_matriculadas (List[str]): lista de disciplinas matriculadas
        """
        super().__init__(nome, idade, endereco, telefone, email, login)
        self.__senha = senha
        self.disciplinas_matriculadas = disciplinas_matriculadas

    def save(self) -> None:
        """Salva os dados no banco de dados da coleção Professores
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
            }
            self.db.insert_data("Professores", data)
            print("Dados cadastrados com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar: {e}")