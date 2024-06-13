import pymongo
from abc import ABC
from usuario import Professor, Aluno
from database import DataBase

db = DataBase()

class Turmas(ABC):
    def __init__(self, codigo: str) -> None:
        self.codigo_turma = codigo

    def criar_turma(self) -> None:
        try:
            db.create_collection(self.codigo_turma)
        except Exception as e:
            print(f'Erro ao criar a turma: {e}')



            


    