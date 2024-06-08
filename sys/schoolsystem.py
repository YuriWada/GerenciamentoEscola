from cadastro import *

class SchoolSystem:
    def __init__(self) -> None:
        pass

    def run(self) -> None:
        print("Ok")
        aluno01 = CadastroAluno(
            nome = "Yuri",
            idade = 24,
            endereco = "Brasil",
            telefone = "31983657402",
            email = "yuri.wadah@gmail.com",
            login = "YuriWada",
            senha = "12345",
            curso = "EngSistemas",
            matricula = "2023431004"
        )
        aluno01.exibe_dados()