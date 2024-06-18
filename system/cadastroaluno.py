from cadastro import Cadastro
from typing import List

class CadastroAluno(Cadastro):
    def __init__(self, nome : str, idade : int, endereco : str, telefone : str, email : str, login : str, senha : str, curso : str, matricula : str, turmas_matriculadas : List[str] = None) -> None:
        """Construtor da classe CadastroAluno

        Args:
            nome (str): nome do aluno
            idade (int): idade do aluno
            endereco (str): endereço do aluno
            telefone (str): telefone do aluno
            email (str): email do aluno
            login (str): login utilizado para logar no sistema
            senha (str): senha utilizada para logar no sistema
            curso (str): curso matriculado
            matricula (str): número da matrícula
            turmas_matriculadas (List[str]): lista de turmas matriculadas
        """
        super().__init__(nome, idade, endereco, telefone, email, login)
        self.curso = curso
        self.matricula = matricula
        self.__senha = senha
        self.turmas_matriculadas = turmas_matriculadas

    def save(self) -> None:
        """Salva os dados no banco de dados da coleção Alunos
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
                "curso": self.curso,
                "matricula": self.matricula,
                "turmas_matriculadas" : self.turmas_matriculadas
            }
            self.db.insert_data("Alunos", data)
            print("Dados cadastrados com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar: {e}")