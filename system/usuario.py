from abc import ABC, abstractmethod
from database import DataBase

class Usuario(ABC):
    def __init__(self, nome: str, idade: int, endereco: str, telefone: str, email: str, login: str) -> None:
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self._login = login

class Aluno(Usuario):
    def __init__(self, nome : str, idade : int, endereco : str, telefone: str, email : str, login : str, curso : str, matricula : str) -> None:
        super().__init__(nome, idade, endereco, telefone, email, login)
        self.curso = curso
        self.matricula = matricula
        
    '''def ver_notas() -> None:'''

    '''def ver_horario() -> None:'''


class Staff(Usuario):
    def __init__(self, nome: str, idade: int, endereco: str, telefone: str, email: str, login: str, salario: str, nivel : int) -> None:
        super().__init__(nome, idade, endereco, telefone, email, login, nivel)
        self.salario = salario


class Professor(Staff):
    def __init__(self, nome: str, idade: int, endereco: str, telefone: str, email: str, login: str, salario: str, disciplina: str, nivel : int) -> None:
        super().__init__(nome, idade, endereco, telefone, email, login, salario, nivel)
        self.disciplina = disciplina
    
    '''def adicionar_notas(self, db) -> None:'''
        
    '''def alterar_notas()'''

class CorpoEstudantil(Staff):
    def __init__(self, nome: str, idade: int, endereco: str, telefone: str, email: str, login: str, cargo: str, salario: str) -> None:
        super().__init__(nome, idade, endereco, telefone, email, login, salario)
        self.cargo = cargo
    
    def deletar_usuario(colecao, criterio) -> None:
        db.delete_data(colecao, criterio)





