from abc import ABC, abstractmethod
from pymongo import errors
from database import DataBase
from typing import List

class Turma(ABC):
    def __init__(self, nome : str) -> None:
        """Construtor da classe Turma

        Args:
            nome (str): nome da turma[digito]
        """
        self.nome = nome
        self.db = DataBase()

    def media_notas(self) -> float:
        """Método para obter a média aritmética de notas da turma

        Raises:
            ValueError: se nenhuma nota foi registrada no sistema

        Returns:
            float: a média aritmética de notas
        """
        try:
            infos = self.db.query_data(self.nome, {})
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
        """Método para lista os alunos matriculados na turma

        Raises:
            ValueError: se nenhum aluno está matriculado

        Returns:
            list: lista de alunos matriculados
        """
        try:
            infos = self.db.query_data(self.nome)
            nomes = [info['nome'] for info in infos if 'nome' in info]
            if not nomes:
                raise ValueError("Não há alunos matriculados na turma!")
            return nomes
        except errors.PyMongoError as e:
            print(f"Erro ao consultar nomes no MongoDB: {e}")
        except Exception as e:
            print(f"Erro ao encontrar nomes: {e}")

    def horarios_turma(self) -> list:
        """Método para verificar os horários da turma

        Raises:
            ValueError: Se nenhuma informação sobre a turma foi encontrada

        Returns:
            list: lista contendo os horários associados à turma
        """
        try:
            infos = self.db.query_data("Turmas", {"nome": self.nome})
            if not infos:
                raise ValueError("Nenhuma informação sobre a turma registrada no sistema!")
            horarios = [info['horarios'] for info in infos if 'horarios' in info]
            return horarios
        except Exception as e:
            print(f"Erro ao encontrar os horarios: {e}")
