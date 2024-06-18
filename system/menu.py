from abc import ABC, abstractmethod
from authentication import Authentication
from usuario import *
from database import DataBase
from typing import Type
from calendario import Calendario

class Menu(ABC):
    def __init__(self, title : str) -> None:
        """Construtor da classe Menu(abstrata)

        Args:
            title (str): título (nenhum)
        """
        self._title = title
        self._options = []
        self._db = DataBase()
        self.calendario = Calendario()

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
        self._options = ['Área Aluno', 'Área Professor', 'Área Diretoria']
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
                print("> Erro ao autenticar, tente novamente!")
                return self
        elif option == 3:
            dict = self.LoginSenha()
            if self._auth.auth("Diretoria", dict):
                diretoria = self._db.query_data("Diretoria", dict)
                dados = diretoria[0]
                funcionario = Diretoria(dados['nome'], dados['idade'], dados['endereco'], dados['telefone'], dados['email'], dados['login'], dados['cargo'])
                return MenuDiretoria(funcionario)
            else:
                print("> Erro ao autenticar, tente novamente!")
                return self
        else:
            print("Opção inválida! Tente novamente")
            return self

class MenuAluno(Menu):
    def __init__(self, aluno : Type[Aluno]) -> None:
        """Construtor da classe MenuAluno

        Args:
            aluno (object): instância da classe Aluno
        """
        self.aluno = aluno
        super().__init__(f"Olá, {aluno.nome}, {aluno.matricula}!")
        self._options = ['Ver notas', 'Ver turmas', 'Acessar calendário Escolar']

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
        elif option == 3:
            print("> 1. Exibir calendário do mês")
            print("> 2. Exibir calendário do ano")
            try:
                sub_option = int(input("> Escolha uma opção: "))
                if sub_option == 1:
                    self.calendario.exibir_calendario()
                elif sub_option == 2:
                    self.calendario.exibir_calendario_anual()
                else:
                    print("Opção inválida! Tente novamente")
            except ValueError:
                print("Opção inválida! Por favor, insira um número.")
            return self
        else:
            print("Opção inválida! Tente novamente")
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
        if option == 2:
            print("> 1. Exibir calendário do mês")
            print("> 2. Exibir calendário do ano")
            sub_option = int(input("> Escolha uma opção: "))
            if sub_option == 1:
                self.calendario.exibir_calendario()
            elif sub_option == 2:
                self.calendario.exibir_calendario_anual()
            else:
                print("Opção inválida!")
            return self

class MenuDiretoria(Menu):
    def __init__(self, diretoria : Type[Diretoria]) -> None:
        self.funcionario = diretoria
        super().__init__(f"Olá, {diretoria.cargo}!")
        self._options = ['Alunos', 'Professores', 'Diretoria', 'Acessar turmas', 'Acessar Calendário']

    def next(self, option : int) -> None:
        if option == 1:
            print("> 1. Exibir lista de alunos")
            print("> 2. Cadastrar novo aluno")
            print("> 3. Editar informações de aluno")
            sub_option = int(input("> Escolha uma opção:"))
            if sub_option == 1:
                print("================================")
                print("xxx Exibindo lista de alunos xxx")
                infos = self._db.query_data("Alunos")
                for e, info in enumerate(infos):
                    print("================================")
                    print(f"{e+1}. {info.get('nome')}")
                    print(f"Idade: {info.get('idade')}")
                    print(f"E-mail: {info.get('email')}")
                    print(f"Curso: {info.get('curso')}")
                    print(f"Matrícula: {info.get('matricula')}")
                    print("Turmas:")
                    if info.get('turmas_matriculadas'):
                        for turma in info.get('turmas_matriculadas'):
                            print(f". {turma}")
            elif sub_option == 2:
                self.funcionario.cadastrar_aluno()
            elif sub_option == 3:
                self.funcionario.editar_infos("Alunos")
            else:
                print("Opção inválida!")
            return self
        elif option == 2:
            print("> 1. Exibir lista de professores")
            print("> 2. Cadastrar novo professor")
            print("> 3. Editar informações de professor")
            sub_option = int(input("> Escolha uma opção:"))
            if sub_option == 1:
                print("======================================")
                print("xxx Exibindo lista de professores xxx")
                infos = self._db.query_data("Professores")
                for e, info in enumerate(infos):
                    print("======================================")
                    print(f"{e+1}. {info.get('nome')}")
                    print(f"Idade: {info.get('idade')}")
                    print(f"E-mail: {info.get('email')}")
                    print(f"Disciplina: {info.get('disciplina')}")
                    print("Turmas:")
                    if info.get('turmas_matriculadas'):
                        for turma in info.get('turmas_matriculadas'):
                            print(f". {turma}")
            elif sub_option == 2:
                self.funcionario.cadastrar_professor()
            elif sub_option == 3:
                self.funcionario.editar_infos("Professores")
            else:
                print("Opção inválida!")
            return self
        elif option == 3:
            print("> 1. Exibir lista de funcionários")
            print("> 2. Editar informação de funcionário")
            sub_option = int(input("> Escolha uma opção:"))
            if sub_option == 1:
                print("======================================")
                print("xxx Exibindo lista de funcionários xxx")
                infos = self._db.query_data("Diretoria")
                for e, info in enumerate(infos):
                    print("======================================")
                    print(f"{e+1}. {info.get('nome')}")
                    print(f"Idade: {info.get('idade')}")
                    print(f"E-mail: {info.get('email')}")
                    print(f"Cargo: {info.get('cargo')}")
            elif sub_option == 2:
                self.funcionario.editar_infos("Diretoria")
            return self
        elif option == 4:
            return self
        elif option == 5:
            print("> 1. Exibir calendário do mês")
            print("> 2. Exibir calendário do ano")
            print("> 3. Inserir novo evento")
            print("> 4. Modificar evento")
            print("> 5. Apagar evento")
            try:
                sub_option = int(input("> Escolha uma opção: "))
                if sub_option == 1:
                    self.calendario.exibir_calendario()
                elif sub_option == 2:
                    self.calendario.exibir_calendario_anual()
                elif sub_option == 3:
                    print("> Criar novo evento")
                    self.funcionario.inserir_evento_calendario()
                elif sub_option == 4:
                    print("> Modificar evento")
                    self.funcionario.modificar_evento_calendario()
                elif sub_option == 5:
                    print("Apagar evento")
                    self.funcionario.apagar_evento_calendario()
                else:
                    print("Opção inválida! Tente novamente")
            except ValueError:
                print("Opção inválida! Por favor, insira um número.")
            return self