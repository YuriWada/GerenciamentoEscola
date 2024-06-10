from cadastro import *
from menu import *

class SchoolSystem:
    def __init__(self) -> None:
        pass

    def run(self) -> None:
        menuinicial = MenuInicial()
        menuinicial.render()

        option = None
        while option != 0:
            option = int(input("Insira sua opção: "))
            menuinicial.next(option)
            if menuinicial:
                menuinicial.render()