from abc import ABC, abstractmethod

class Menu(ABC):
    def __init__(self, title : str) -> None:
        self._title = title
        self._options = []

    @abstractmethod
    def next(self, option : int) -> None:
        pass

    def render(self) -> None:
        border = '=' * (len(self._title) + 5)
        print(border)
        print(f"|| {self._title}")
        print(border + "\n")

        for i, opt in enumerate(self._options, 1):
            print(f"> {i}. {opt}")

        print()

class MenuInicial(Menu):
    def __init__(self) -> None:
        super().__init__("Bem-vindo")
        self._options = ['Área Aluno', 'Área Professor', 'Área Staff']
        
    def next(self, option : int) -> None:
        if option == 1:
            print("Opção 1 - Ok")
        elif option == 2:
            print("Opção 2 - Ok")
            return None
        else:
            print("Opção inválida!")
            return self

"""class MenuAluno(Menu):
    def __init__(self, aluno) -> None:
        options = """
