import hashlib
from abc import ABC, abstractmethod
from database import DataBase
from typing import List, Type
from calendario import Calendario
# from usuario import *

class Cadastro(ABC):
    def __init__(self, nome : str, idade : int, endereco : str, telefone : str, email : str, login : str) -> None:
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self._login = login
        self.validar_dados()

        # Database setup
        self.db = DataBase()

    # Validação dos dados
    def validar_idade(self) -> None:
        if self.idade <= 0:
            raise ValueError("A idade deve ser maior que 0")
        
    def validar_email(self) -> None:
        if "@" not in self.email or "." not in self.email:
            raise ValueError("E-mail inválido")
    
    def validar_telefone(self) -> None:
        if not self.telefone.isdigit() or len(self.telefone) < 9:
            raise ValueError("Telefone Inválido")
        
    def _validar_login(self) -> None:
        if not self._login:
            raise ValueError("O campo login deve ser preenchido")
    
    # Método geral de validação
    def validar_dados(self) -> None:
        self.validar_idade()
        self.validar_email()
        self.validar_telefone()
        self._validar_login()

    # Salva os dados no BD
    @abstractmethod
    def save(self) -> None:
        pass

# Cadastro do Aluno
class CadastroAluno(Cadastro):
    def __init__(self, nome : str, idade : int, endereco : str, telefone : str, email : str, login : str, senha : str, curso : str, matricula : str, turmas_matriculadas : List[str]) -> None:
        super().__init__(nome, idade, endereco, telefone, email, login)
        self.curso = curso
        self.matricula = matricula
        self.__senha = senha
        self.turmas_matriculadas = turmas_matriculadas

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
                "curso": self.curso,
                "matricula": self.matricula,
                "turmas_matriculadas" : self.turmas_matriculadas
            }
            self.db.insert_data("Alunos", data)
            print("Dados cadastrados com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar: {e}")
    
class CadastroProfessor(Cadastro):
    def __init__(self, nome: str, idade: int, endereco: str, telefone: str, email: str, login: str, senha: str, disciplina: str, turmas_matriculadas : List[str]) -> None:
        super().__init__(nome, idade, endereco, telefone, email, login)
        self.disciplina = disciplina
        self.__senha = senha
        self.turmas_matriculadas = turmas_matriculadas

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
                "disciplina": self.disciplina,
                "turmas_matriculadas": self.turmas_matriculadas
            }
            self.db.insert_data("Professores", data)
            print("Dados cadastrados com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar: {e}")

class CadastroStaff(Cadastro):
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
            self.db.insert_data("Staff", data)
            print("Dados cadastrados com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar: {e}")

class CadastroTurma:
    def __init__(self, nome : str, materia : str, horarios : List[str], professor : str, alunos : List[dict] = None) -> None:
        self.nome = nome
        self.materia = materia
        self.horarios = horarios
        self.professor = professor
        self.alunos = alunos
        self.db = DataBase()
        # self.calendario = Calendario()

    # Verifica se uma aula já foi cadastrada no horário indicado
    def validacao_dados(self) -> bool:
        try:
            turmas = self.db.query_data("Turmas")
            lista_horarios = []
            if turmas:
                for turma in turmas:
                    lista_horarios.append(turma["horarios"])
            for horarios in lista_horarios:
                if sorted(self.horarios) == sorted(horarios):
                    print("Aula já cadastrada em horário indicado!")
                    return False
            return True
        except Exception as e:
            print(f"Erro ao validar dados: {e}")

    def save(self) -> None:
        try:
            if self.validacao_dados():
                data = {
                    "nome": self.nome,
                    "materia": self.materia,
                    "horarios": self.horarios,
                    "professor": self.professor,
                    "alunos": self.alunos
                }
                self.db.insert_data("Turmas", data)
                self.db.empty_collection(self.nome)
                print("Turma cadastrada com sucesso!")
            else:
                print("Turma não cadastrada, tente novamente!")
        except Exception as e:
            print(f"Erro ao cadastrar: {e}")
