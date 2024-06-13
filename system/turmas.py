import pymongo
from usuario import Professor, Aluno
from abc import ABC

class Turmas(ABC):
    def criar_turma() -> None:
        
