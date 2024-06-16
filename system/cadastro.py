from abc import ABC, abstractmethod
from database import DataBase
from typing import List
# from usuario import *

class Cadastro(ABC):
    def __init__(self, nome : str, idade : int, endereco : str, telefone : str, email : str, login : str) -> None:
        """Construtor da classe Cadastro

        Args:
            nome (str): nome registrado
            idade (int): idade registrada
            endereco (str): endereço registrado
            telefone (str): telefone registrado
            email (str): email registrado
            login (str): login utilizado para logar no sistema
        """
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self._login = login
        self.validar_dados()

        # Database setup
        self.db = DataBase()

    @abstractmethod
    def save(self) -> None:
        """Método utilizado para salvar os dados no Banco de Dados
        """
        pass

# Cadastro do Aluno
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

# Cadastro do Professor
class CadastroProfessor(Cadastro):
    def __init__(self, nome: str, idade: int, endereco: str, telefone: str, email: str, login: str, senha: str, disciplina: str, turmas_matriculadas : List[str]) -> None:
        """Construtor da classe CadastroProfessor

        Args:
            nome (str): nome do professor
            idade (int): idade do professor
            endereco (str): endereço do professor
            telefone (str): telefone do professor
            email (str): email do professor
            login (str): login utilizado para logar no sistema
            senha (str): senha utilizada para logar no sistema
            disciplina (str): disciplinas nas quais leciona
            turmas_matriculadas (List[str]): lista de turmas matriculadas
        """
        super().__init__(nome, idade, endereco, telefone, email, login)
        self.disciplina = disciplina
        self.__senha = senha
        self.turmas_matriculadas = turmas_matriculadas

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
                "disciplina": self.disciplina,
                "turmas_matriculadas": self.turmas_matriculadas
            }
            self.db.insert_data("Professores", data)
            print("Dados cadastrados com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar: {e}")

class CadastroDiretoria(Cadastro):
    def __init__(self, nome: str, idade: int, endereco: str, telefone: str, email: str, login: str, senha: str, cargo: str) -> None:
        super().__init__(nome, idade, endereco, telefone, email, login)
        self.cargo = cargo
        self.__senha = senha

    def save(self) -> None:
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
