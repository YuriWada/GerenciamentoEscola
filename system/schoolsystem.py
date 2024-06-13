from cadastro import *
from menu import *

class SchoolSystem:
    def run(self) -> None:
        menuinicial = MenuInicial()
        menuinicial.render()
        while menuinicial is not None:
            try:
                option = int(input("> Opção (0 para cancelar): "))
                menuinicial = menuinicial.next(option)
            except ValueError:
                print("Opção inválida! Por favor, insira um número.")