from authentication import Authentication
from usuario import *
from diretoria import Diretoria
from aluno import Aluno
from professor import Professor
from menualuno import MenuAluno
from menuprofessor import MenuProfessor
from menudiretoria import MenuDiretoria
from menu import Menu

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
                aluno = Aluno(dados['nome'], dados['idade'], dados['endereco'], dados['telefone'], dados['email'], dados['login'], dados['curso'], dados['matricula'], dados['disciplinas_matriculadas'])
                return MenuAluno(aluno)
            else:
                print("> Erro ao autenticar, tente novamente!")
                return self
        elif option == 2:
            dict = self.LoginSenha()
            if self._auth.auth("Professores", dict):
                professores = self._db.query_data("Professores", dict)
                dados = professores[0]
                professor = Professor(dados['nome'], dados['idade'], dados['endereco'], dados['telefone'], dados['email'], dados['login'], dados['disciplinas_matriculadas'])
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