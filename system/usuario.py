'''
Class: Usuario
Author: Julia Raposo

'''



class Usuario:
    def __init__(self, nome : str, idade : int, endereco : str, telefone: str, email : str, login : str) -> None:
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self._login = login

    def excluir_conta(self) -> None:
        pass



class Aluno(Usuario):
    def __init__(self, nome : str, idade : int, endereco : str, telefone: str, email : str, login : str, curso : str, matricula : str) -> None:
        super().__init__(nome, idade, endereco, telefone, email, login)
        self.curso = curso
        self.matricula = matricula

    def ver_notas() -> None:
        pass

    def ver_horario() -> None:
        pass


class Professor(Usuario):
    def __init__(self, nome : str, idade : int, endereco : str, telefone: str, email : str, login : str, materia : str, salario : int) -> None:
        super().__init__(nome, idade, endereco, telefone, email, login)
        self.materia = materia
        self.salario = salario

    def adicionar_nota() -> None:
        pass

    def alterar_nota() -> None:
        pass


class Staff(Usuario):
    def __init__(self,nome : str, idade : int, endereco : str, telefone: str, email : str, login : str, funcao : str, salario : int) -> None:
        super().__init__(nome, idade, endereco, telefone, email, login)
        self.funcao = funcao
        self.salario = salario

