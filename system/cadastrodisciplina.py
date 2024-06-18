from database import DataBase
from abc import ABC, abstractmethod

class CadastroDisciplina(ABC):
    def __init__(self) -> None:
        """Interface para Cadastro de Disciplinas

        Args:
            db (any): instância da classe de Banco de Dados
        """
        self.db = DataBase()

    @abstractmethod
    def valida_dados(self) -> bool:
        """Valida os dados dos construtores

        Returns:
            bool: retorna True se os dados são válidos. False se são inválidos.
        """
        pass

    @abstractmethod
    def save(self) -> bool:
        """Salva os dados no banco de dados.

        Returns:
            bool: retorna True se os dados foram salvos. False se não foram salvos.
        """
        pass
