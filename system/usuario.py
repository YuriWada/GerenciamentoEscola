from abc import ABC
from database import DataBase

class Usuario(ABC):
    def __init__(self, nome: str, idade: int, endereco: str, telefone: str, email: str, login: str) -> None:
        """Classe pai Usuário

        Args:
            nome (str): nome do usuário
            idade (int): idade do usuário
            endereco (str): endereço do usuário
            telefone (str): telefone do usuário
            email (str): e-mail do usuário
            login (str): login do usuário
        """
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self._login = login
        self.db = DataBase()

