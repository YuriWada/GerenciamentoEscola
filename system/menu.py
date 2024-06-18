from abc import ABC, abstractmethod
from usuario import *
from database import DataBase
from calendario import Calendario

class Menu(ABC):
    def __init__(self, title : str) -> None:
        """Construtor da classe Menu(abstrata)

        Args:
            title (str): título (nenhum)
        """
        self._title = title
        self._options = []
        self._db = DataBase()
        self.calendario = Calendario()

    @abstractmethod
    def next(self, option : int) -> None:
        """Método para puxar o próximo menu

        Args:
            option (int): opções do menu
        """
        pass

    def render(self) -> None:
        """Renderiza o menu na interface de usuário
        """
        border = '=' * (len(self._title) + 5)
        print(border)
        print(f"|| {self._title}")
        print(border + "\n")

        for i, opt in enumerate(self._options, 1):
            print(f"> {i}. {opt}")
            
        print()
