from abc import ABC, abstractmethod
from pymongo import errors
from database import DataBase
from typing import List

class Turma(ABC):
    def __init__(self, nome : str, materia : str, horarios : List[str], professor : dict = None, alunos : List[dict] = None) -> None:
        self.nome = nome
        self.materia = materia
        self.horarios = horarios
        self.professor = professor
        self.alunos = alunos
        self.db = DataBase()

    def media_notas(self) -> float:
        try:
            infos = self.db.query_data(self.nome, {"notas"})
            notas = [info['nota'] for info in infos if 'nota' in info]
            if not notas:
                raise ValueError("Nenhuma nota registrada no sistema!")
            media = sum(notas) / len(notas)
            return media
        except errors.PyMongoError as e:
            print(f"Erro ao consultar notas no MongoDB: {e}")
        except Exception as e:
            print(f"Erro ao calcular a média das notas: {e}")

    def listagem_alunos(self) -> list:
        try:
            infos = self.db.query_data(self.nome, {"nomes"})
            nomes = [info['nome'] for info in infos if 'nome' in info]
            if not nomes:
                raise ValueError("Nenhum nome encontrado no sistema!")
            return nomes
        except errors.PyMongoError as e:
            print(f"Erro ao consultar nomes no MongoDB: {e}")
        except Exception as e:
            print(f"Erro ao encontrar nomes: {e}")

    def horarios_turma(self) -> list:
        try:
            return self.horarios
        except Exception as e:
            print(f"Erro ao encontrar os horarios: {e}")
