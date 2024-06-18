from abc import ABC, abstractmethod
from database import DataBase

class Cadastro(ABC):
    def __init__(self, nome : str, idade : int, endereco : str, telefone : str, email : str, login : str) -> None:
        """Construtor da classe Cadastro

        Args:
            nome (str): nome registrado
            idade (int): idade registrada
            endereco (str): endereço registrado
            telefone (str): telefone registrado
            email (str): email registrado
            login (str): login utilizado para logar no sistema
        """
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self._login = login

        # Database setup
        self.db = DataBase()

    @abstractmethod
    def save(self) -> None:
        """Método utilizado para salvar os dados no Banco de Dados
        """
        pass
