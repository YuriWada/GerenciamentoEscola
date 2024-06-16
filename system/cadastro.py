import hashlib
from abc import ABC, abstractmethod
from database import DataBase
from typing import List, Type
from calendario import Calendario
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

    def validar_idade(self) -> None:
        """Valida se a idade é maior que zero

        Raises:
            ValueError: se a idade for menor ou igual a zero
        """
        if self.idade <= 0:
            raise ValueError("A idade deve ser maior que 0")
        
    def validar_email(self) -> None:
        """Valida se o email possui formato correto

        Raises:
            ValueError: Se a str inserida não possuir @ ou .
        """
        if "@" not in self.email or "." not in self.email:
            raise ValueError("E-mail inválido")
    
    def validar_telefone(self) -> None:
        """Valida se o telefone possui formato correto

        Raises:
            ValueError: Se o telefone não possuir digitos ou for menor que 9
        """
        if not self.telefone.isdigit() or len(self.telefone) < 9:
            raise ValueError("Telefone Inválido")
        
    def _validar_login(self) -> None:
        """Valida se o login foi preenchido

        Raises:
            ValueError: Se o campo login não foi preenchido
        """
        if not self._login:
            raise ValueError("O campo login deve ser preenchido")
    
    def validar_dados(self) -> None:
        """Valida os dados inseridos
        """
        self.validar_idade()
        self.validar_email()
        self.validar_telefone()
        self._validar_login()

    @abstractmethod
    def save(self) -> None:
        """Método utilizado para salvar os dados no Banco de Dados
        """
        pass

# Cadastro do Aluno
class CadastroAluno(Cadastro):
    def __init__(self, nome : str, idade : int, endereco : str, telefone : str, email : str, login : str, senha : str, curso : str, matricula : str, turmas_matriculadas : List[str]) -> None:
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

# Cadastro da Turma
class CadastroTurma:
    def __init__(self, nome : str, materia : str, horarios : List[str], professor : str, alunos : List[dict] = None) -> None:
        """Construtor da classe CadastroTurma

        Args:
            nome (str): nome da turma
            materia (str): materia associada à turma
            horarios (List[str]): lista de horários da turma
            professor (str): nome do professor associado à turma
            alunos (List[dict], optional): lista de alunos matriculados na turma. Defaults to None.
        """
        self.nome = nome
        self.materia = materia
        self.horarios = horarios
        self.professor = professor
        self.alunos = alunos
        self.db = DataBase()
        # self.calendario = Calendario()

    def validacao_dados(self) -> bool:
        """Verifica se uma turma já foi cadastrada em um mesmo horário, para não haver conflitos.

        Returns:
            bool: true - se os dados foram validados com sucesso (não há conflito), false - se não foram validados
        """
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
        """Salva os dados da turma no banco de dados em duas coleções:
        Turmas: coleção com todas as turmas, indicando para cada turma
        nome, matéria, lista de horarios, profesor e alunos matriculados.
        Turma[digito]: coleção própria para a turma, contendo alunos e notas.
        """
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
