from system.cadastro import *
from system.menu import *

class SchoolSystem:
    def __init__(self) -> None:
        pass

    def run(self) -> None:
        menuinicial = MenuInicial()
        while menuinicial is not None:
            menuinicial.render()
            try:
                option = int(input("> Opção (0 para cancelar): "))
                menuinicial = menuinicial.next(option)
            except ValueError:
                print("Opção inválida! Por favor, insira um número.")