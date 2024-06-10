from abc import ABC, abstractmethod

class Menu(ABC):
    def __init__(self, options, title="Tela de Login") -> None:
        self._title = title
        self._options = options

    @abstractmethod
    def next(self, option : int) -> None:
        pass

    def render(self) -> None:
        border = '=' * (len(self._title) + 5)
        print(border)
        print("|| " + self._title + "\n")
        print(border + "\n\n")

        for opt in self._options:
            print(opt)

class MenuInicial(Menu):
    def __init__(self) -> None:
        options = ['1 - Área Aluno', '2 - Área Professor', '3 - Área Staff']
        title = 'Bem-vindo'
        super().__init__(options, title)
        
    def next(self, option : int) -> None:
        if option == 1:
            print("Ok")
            #menuAluno = MenuAluno(aluno)
            #return menuAluno

"""class MenuAluno(Menu):
    def __init__(self, aluno) -> None:
        options = """
