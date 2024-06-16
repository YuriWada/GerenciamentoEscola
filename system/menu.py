from abc import ABC, abstractmethod
from authentication import Authentication
from usuario import *
from database import DataBase
from typing import Type

class Menu(ABC):
    def __init__(self, title : str) -> None:
        """Construtor da classe Menu(abstrata)

        Args:
            title (str): título (nenhum)
        """
        self._title = title
        self._options = []
        self._db = DataBase()

    @abstractmethod
    def next(self, option : int) -> None:
        """Método para puxar o próximo menu

        Args:
            option (int): opções do menu
        """
        pass

    def render(self) -> None:
        """Renderiza o menu na interface de usuário
        """
        border = '=' * (len(self._title) + 5)
        print(border)
        print(f"|| {self._title}")
        print(border + "\n")

        for i, opt in enumerate(self._options, 1):
            print(f"> {i}. {opt}")
            
        print()

class MenuInicial(Menu):
    def __init__(self) -> None:
        """Construtor da classe MenuInicial
        """
        super().__init__("Bem-vindo")
        self._options = ['Área Aluno', 'Área Professor', 'Área Staff']
        self._auth = Authentication()

    def LoginSenha(self) -> dict:
        """Renderiza a entrada de login e senha do usuário

        Returns:
            dict: dicionário com login e senha inseridos
        """
        print("> Login:")
        login = input()
        print("> Senha:")
        senha = input()
        dict = {"login": login, "senha": senha}
        return dict

    def next(self, option : int) -> object:
        """Método com o próximo menu
        Args:
            option (int): opção escolhida

        Returns:
            object: retorna um objeto do próximo menu
        """
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
    def __init__(self, aluno : Type[Aluno]) -> None:
        """Construtor da classe MenuAluno

        Args:
            aluno (object): instância da classe Aluno
        """
        self.aluno = aluno
        super().__init__(f"Olá, {aluno.nome}, {aluno.matricula}!")
        self._options = ['Ver notas', 'Ver turmas', 'Acessar calendário']

    def next(self, option : int) -> None:
        """Método com o próximo menu
        Args:
            option (int): opção escolhida

        Returns:
            object: retorna um objeto do próximo menu
        """
        if option == 1:
            notas = self.aluno.buscar_notas()
            if notas:
                for nota in notas:
                    print(f"Turma: {nota['turma']}, nota: {nota['nota']}")
            else:
                print("Nenhuma nota registrada no sistema!")
            return self
        elif option == 2:
            turmas = self.aluno.busca_turmas_matriculadas()
            if turmas:
                print("Turma(s) matriculada(s):")
                for turma in turmas:
                    print(f"> {turma}")
            else:
                print("O aluno não está matriculado em nenhuma turma!")
            return self

class MenuProfessor(Menu):
    def __init__(self, professor : Type[Professor]) -> None:
        """Construtor da classe MenuProfessor

        Args:
            professor (object): instância da classe Professor
        """
        self.professor = professor
        super().__init__(f"Olá, {professor.nome}!")
        self._options = ['Ver turmas', 'Acessar calendário']

    def next(self, option : int) -> None:
        """Método com o próximo menu
        Args:
            option (int): opção escolhida

        Returns:
            object: retorna um objeto do próximo menu
        """
        if option == 1:
            return self
