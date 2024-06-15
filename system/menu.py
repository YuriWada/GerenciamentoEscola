from abc import ABC, abstractmethod
from authentication import Authentication
from usuario import *
from database import DataBase

class Menu(ABC):
    def __init__(self, title : str) -> None:
        self._title = title
        self._options = []
        self._db = DataBase()

    # Método que puxa o próximo menu de usuário
    @abstractmethod
    def next(self, option : int) -> None:
        pass

    # Renderiza o menu
    def render(self) -> None:
        border = '=' * (len(self._title) + 5)
        print(border)
        print(f"|| {self._title}")
        print(border + "\n")

        for i, opt in enumerate(self._options, 1):
            print(f"> {i}. {opt}")
            
        print()

class MenuInicial(Menu):
    def __init__(self) -> None:
        super().__init__("Bem-vindo")
        self._options = ['Área Aluno', 'Área Professor', 'Área Staff']
        self._auth = Authentication()
        
    def next(self, option : int) -> None:
        if option == 1:
            print("> Login:")
            login = input()
            print("> Senha:")
            senha = input()
            dict = {"login": login, "senha": senha}
            if self._auth.auth("Alunos", dict):
                alunos = self._db.query_data("Alunos", dict)
                dados = alunos[0]
                aluno = Aluno(dados['nome'], dados['idade'], dados['endereco'], dados['telefone'], dados['email'], dados['login'], dados['curso'], dados['matricula'])
                return MenuAluno(aluno)
            else:
                print("> Erro ao autenticar, tente novamente!")
                return self
        elif option == 2:
            print("Opção 2 - Ok")
            return self
        else:
            print("Opção inválida!")
            return self

class MenuAluno(Menu):
    def __init__(self, aluno : object) -> None:
        self.aluno = aluno
        super().__init__(f"Olá, {aluno.nome}!")
        self._options = ['Ver notas', 'Ver turmas', 'Acessar calendário']

    def next(self, option : int) -> None:
        if option == 1:
            return self
