from abc import ABC
from database import DataBase

class Usuario(ABC):
    def __init__(self, nome: str, idade: int, endereco: str, telefone: str, email: str, login: str) -> None:
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self._login = login
        self.db = DataBase()

