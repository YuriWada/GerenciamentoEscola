'''
Class: Usuario
Author: Julia Raposo

'''



class Usuario:
    def __init__(self, nome : str, idade : int, endereco : str, telefone: str, email : str, login : str, nivel : int) -> None:
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self._login = login
        self.nivel = nivel

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
        self.funcao = funcao
        self.salario = salario


class Professor(Staff):
    def __init__(self, nome: str, idade: int, endereco: str, telefone: str, email: str, login: str, funcao: str, salario: str, materia: str, nivel : int) -> None:
        super().__init__(nome, idade, endereco, telefone, email, login, funcao, salario, nivel)
        self.materia = materia
    
    '''def adicionar_notas()'''

    '''def alterar_notas()'''

class CorpoEstudantil(Staff):
    def __init__(self, nome: str, idade: int, endereco: str, telefone: str, email: str, login: str, funcao: str, salario: str) -> None:
        super().__init__(nome, idade, endereco, telefone, email, login, funcao, salario)

    





