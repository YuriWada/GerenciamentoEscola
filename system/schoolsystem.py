import os
from cadastro import *
from menu import *

class SchoolSystem:
    def run(self) -> None:
        # Roda o menu inicial (interface de usuário)
        menuinicial = MenuInicial()
        while menuinicial is not None:
            os.system('cls')
            menuinicial.render()
            try:
                option = int(input("> Opção (0 para cancelar): "))
                if option == 0:
                    print("> Encerrando...")
                    break
                menuinicial = menuinicial.next(option)
            except ValueError:
                print("Opção inválida! Por favor, insira um número.")