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

    def LoginSenha(self) -> dict:
        print("> Login:")
        login = input()
        print("> Senha:")
        senha = input()
        dict = {"login": login, "senha": senha}
        return dict

    def next(self, option : int) -> None:
        if option == 1:
            dict = self.LoginSenha()
            if self._auth.auth("Alunos", dict):
                alunos = self._db.query_data("Alunos", dict)
                dados = alunos[0]
                aluno = Aluno(dados['nome'], dados['idade'], dados['endereco'], dados['telefone'], dados['email'], dados['login'], dados['curso'], dados['matricula'], dados['turmas_matriculadas'])
                return MenuAluno(aluno)
            else:
                print("> Erro ao autenticar, tente novamente!")
                return self
        elif option == 2:
            dict = self.LoginSenha()
            if self._auth.auth("Professores", dict):
                professores = self._db.query_data("Professores", dict)
                dados = professores[0]
                professor = Professor(dados['nome'], dados['idade'], dados['endereco'], dados['telefone'], dados['email'], dados['login'], dados['disciplina'], dados['turmas_matriculadas'])
            return MenuProfessor(professor)
        else:
            print("Área Staff")
            return self

class MenuAluno(Menu):
    def __init__(self, aluno : object) -> None:
        self.aluno = aluno
        super().__init__(f"Olá, {aluno.nome}, {aluno.matricula}!")
        self._options = ['Ver notas', 'Ver turmas', 'Acessar calendário']

    def next(self, option : int) -> None:
        if option == 1:
            return self

class MenuProfessor(Menu):
    def __init__(self, professor : object) -> None:
        self.professor = professor
        super().__init__(f"Olá, {professor.nome}!")
        self._options = ['Ver turmas', 'Acessar calendário']

    def next(self, option : int) -> None:
        if option == 1:
            return self
