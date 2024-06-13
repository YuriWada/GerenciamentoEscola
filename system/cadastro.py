import hashlib
from abc import ABC, abstractmethod
from database import DataBase

class Cadastro(ABC):
    def __init__(self, nome : str, idade : int, endereco : str, telefone : str, email : str, login : str) -> None:
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self._login = login
        self.validar_dados()

        # Database setup
        self.db = DataBase()

    # Validação dos dados
    def validar_idade(self) -> None:
        if self.idade <= 0:
            raise ValueError("A idade deve ser maior que 0")
        
    def validar_email(self) -> None:
        if "@" not in self.email or "." not in self.email:
            raise ValueError("E-mail inválido")
    
    def validar_telefone(self) -> None:
        if not self.telefone.isdigit() or len(self.telefone) < 9:
            raise ValueError("Telefone Inválido")
        
    def _validar_login(self) -> None:
        if not self._login:
            raise ValueError("O campo login deve ser preenchido")
    
    # Método geral de validação
    def validar_dados(self) -> None:
        self.validar_idade()
        self.validar_email()
        self.validar_telefone()
        self._validar_login()

    # Salva os dados no BD
    @abstractmethod
    def save(self) -> None:
        pass

# Cadastro do Aluno
class CadastroAluno(Cadastro):
    def __init__(self, nome : str, idade : int, endereco : str, telefone : str, email : str, login : str, senha : str, curso : str, matricula : str) -> None:
        super().__init__(nome, idade, endereco, telefone, email, login)
        self.curso = curso
        self.matricula = matricula
        self.__senha = senha

    def save(self) -> None:
        try:
            data = {
                "nome": self.nome,
                "idade": self.idade,
                "endereco": self.endereco,
                "telefone": self.telefone,
                "email": self.email,
                "login": self._login,
                "senha": self.__senha,
                "curso": self.curso,
                "matricula": self.matricula
            }
            self.db.insert_data("Alunos", data)
            print("Dados cadastrados com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar: {e}")
    
class CadastroProfessor(Cadastro):
    def __init__(self, nome: str, idade: int, endereco: str, telefone: str, email: str, login: str, senha: str, disciplina: str) -> None:
        super().__init__(nome, idade, endereco, telefone, email, login)
        self.disciplina = disciplina
        self.__senha = senha

    def save(self) -> None:
        try:
            data = {
                "nome": self.nome,
                "idade": self.idade,
                "endereco": self.endereco,
                "telefone": self.telefone,
                "email": self.email,
                "login": self._login,
                "senha": self.__senha,
                "disciplina": self.disciplina
            }
            self.db.insert_data("Professores", data)
            print("Dados cadastrados com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar: {e}")

class CadastroStaff(Cadastro):
    def __init__(self, nome: str, idade: int, endereco: str, telefone: str, email: str, login: str, senha: str, cargo: str) -> None:
        super().__init__(nome, idade, endereco, telefone, email, login)
        self.cargo = cargo
        self.__senha = senha

    def save(self) -> None:
        try:
            data = {
                "nome": self.nome,
                "idade": self.idade,
                "endereco": self.endereco,
                "telefone": self.telefone,
                "email": self.email,
                "login": self._login,
                "senha": self.__senha,
                "cargo": self.cargo
            }
            self.db.insert_data("Staff", data)
            print("Dados cadastrados com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar: {e}")