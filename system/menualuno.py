from usuario import *
from typing import Type
from aluno import Aluno
from menu import Menu

class MenuAluno(Menu):
    def __init__(self, aluno : Type[Aluno]) -> None:
        """Construtor da classe MenuAluno

        Args:
            aluno (object): instância da classe Aluno
        """
        self.aluno = aluno
        super().__init__(f"Olá, {aluno.nome}, {aluno.matricula}!")
        self._options = ['Ver notas', 'Ver Disciplinas', 'Acessar calendário Escolar']

    def next(self, option : int) -> None:
        """Método com o próximo menu
        Args:
            option (int): opção escolhida

        Returns:
            object: retorna um objeto do próximo menu
        """
        if option == 1:
            notas = self.aluno.buscar_notas()
            if notas:
                for nota in notas:
                    print(f"Disciplina: {nota['disciplina']}, nota: {nota['nota']}")
            else:
                print("Nenhuma nota registrada no sistema!")
            return self
        elif option == 2:
            disciplinas = self.aluno.busca_disciplinas_matriculadas()
            if disciplinas:
                print("Disciplina(s) matriculada(s):")
                for disciplina in disciplinas:
                    print(f". {disciplina}")
                print("> 1. Mostrar horário das disciplinas")
                sub_option = int(input("> Escolha uma opção: "))
                if sub_option == 1:
                    horarios = self.aluno.buscar_horarios()
                    if horarios:
                        for horario in horarios:
                            print(f". Disciplina: {horario.get('disciplina')}")
                            print("horários:")
                            for hora in horario.get('horarios'):
                                print(hora)
                    else:
                        print("Nenhum horário para as disciplinas")
                elif sub_option == 0:
                    return self
                else:
                    print("Opção inválida!")
                    return self
            else:
                print("O aluno não está matriculado em nenhuma disciplina!")
            return self
        elif option == 3:
            print("> 1. Exibir calendário do mês")
            print("> 2. Exibir calendário do ano")
            try:
                sub_option = int(input("> Escolha uma opção: "))
                if sub_option == 1:
                    self.calendario.exibir_calendario()
                elif sub_option == 2:
                    self.calendario.exibir_calendario_anual()
                else:
                    print("Opção inválida! Tente novamente")
            except ValueError:
                print("Opção inválida! Por favor, insira um número.")
            return self
        else:
            print("Opção inválida! Tente novamente")
            return self