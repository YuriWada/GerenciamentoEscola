'''
Class: Usuario
Author: Julia Raposo

'''

from database import DataBase

class Usuario:
    def __init__(self, nome : str, idade : int, endereco : str, telefone: str, email : str, login : str, nivel : int) -> None:
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.nivel = nivel
        self._login = login
        self.db = DataBase()

    '''def excluir_conta(self) -> None:'''



class Aluno(Usuario):
    def __init__(self, nome : str, idade : int, endereco : str, telefone: str, email : str, login : str, curso : str, matricula : str, nivel : int) -> None:
        super().__init__(nome, idade, endereco, telefone, email, login, nivel)
        self.curso = curso
        self.matricula = matricula


    '''def ver_notas() -> None:'''

    '''def ver_horario() -> None:'''


class Staff(Usuario):
    def __init__(self, nome: str, idade: int, endereco: str, telefone: str, email: str, login: str, funcao : str, salario: str, nivel : int) -> None:
        super().__init__(nome, idade, endereco, telefone, email, login, nivel)
        self.salario = salario


class Professor(Staff):
    def __init__(self, nome: str, idade: int, endereco: str, telefone: str, email: str, login: str, funcao: str, salario: str, materia: str, nivel : int) -> None:
        super().__init__(nome, idade, endereco, telefone, email, login, funcao, salario, nivel)
        self.materia = materia
    
    '''def adicionar_notas()'''

    '''def alterar_notas()'''

class CorpoEstudantil(Staff):
    def __init__(self, nome: str, idade: int, endereco: str, telefone: str, email: str, login: str, cargo: str, salario: str) -> None:
        super().__init__(nome, idade, endereco, telefone, email, login, salario)
        self.cargo = cargo
    





