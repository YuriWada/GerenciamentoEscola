from abc import ABC, abstractmethod
from pymongo import errors
from database import DataBase

class Disciplina(ABC):
    def __init__(self, nome : str) -> None:
        """Construtor da classe Disciplina

        Args:
            nome (str): nome da Disciplina[digito]
        """
        self.nome = nome
        self.db = DataBase()

    def media_notas(self) -> float:
        """
        Calcula a média aritmética das notas registradas para a Disciplina.

        Raises:
            ValueError: Se nenhuma nota foi registrada para a Disciplina.

        Returns:
            float: A média aritmética das notas.

        Notes:
            Este método realiza uma consulta ao banco de dados para obter as notas registradas.
            Caso nenhuma nota seja encontrada, um ValueError é levantado.

        Example:
            ```
            media = obj.media_notas()
            print(f"Média das notas: {media}")
            ```
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
        """
        Retorna uma lista com os nomes dos alunos matriculados na Disciplina.

        Raises:
            ValueError: Se nenhum aluno está matriculado na Disciplina.

        Returns:
            list: Lista contendo os nomes dos alunos matriculados.

        Notes:
            Este método realiza uma consulta ao banco de dados para obter os nomes dos alunos matriculados.
            Caso nenhum aluno esteja matriculado, um ValueError é levantado.

        Example:
            ```
            alunos = obj.listagem_alunos()
            for aluno in alunos:
                print(aluno)
            ```
        """
        try:
            infos = self.db.query_data(self.nome)
            nomes = [info['nome'] for info in infos if 'nome' in info]
            if not nomes:
                raise ValueError("Não há alunos matriculados na Disciplina!")
            return nomes
        except errors.PyMongoError as e:
            print(f"Erro ao consultar nomes no MongoDB: {e}")
        except Exception as e:
            print(f"Erro ao encontrar nomes: {e}")

    def horarios_disciplina(self) -> list:
        """
        Retorna uma lista com os horários associados à Disciplina.

        Raises:
            ValueError: Se nenhuma informação sobre a Disciplina foi encontrada.

        Returns:
            list: Lista contendo os horários associados à Disciplina.

        Notes:
            Este método realiza uma consulta ao banco de dados para obter os horários associados à Disciplina.
            Caso nenhuma informação sobre a Disciplina seja encontrada, um ValueError é levantado.

        Example:
            ```
            horarios = obj.horarios_disciplina()
            for horario in horarios:
                print(horario)
            ```
        """
        try:
            infos = self.db.query_data("Disciplinas", {"nome": self.nome})
            if not infos:
                raise ValueError("Nenhuma informação sobre a Disciplina registrada no sistema!")
            horarios = [info['horarios'] for info in infos if 'horarios' in info]
            return horarios
        except Exception as e:
            print(f"Erro ao encontrar os horarios: {e}")
