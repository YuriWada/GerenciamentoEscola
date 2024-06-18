from usuario import *
from typing import Type
from professor import Professor
from menu import Menu

class MenuProfessor(Menu):
    def __init__(self, professor : Type[Professor]) -> None:
        """Construtor da classe MenuProfessor

        Args:
            professor (object): instância da classe Professor
        """
        self.professor = professor
        super().__init__(f"Olá, {professor.nome}!")
        self._options = ['Acessar Disciplinas', 'Acessar calendário']

    def next(self, option : int) -> None:
        """Método com o próximo menu
        Args:
            option (int): opção escolhida

        Returns:
            object: retorna um objeto do próximo menu
        """
        if option == 1:
            disciplinas = self.professor.buscar_disciplinas()
            if disciplinas:
                print(f"Lista de disciplinas para o(a) professor(a) {self.professor.nome}: ")
                for e, disciplina in enumerate(disciplinas):
                    print(f"{e+1}. {disciplina}")
                sub_option = int(input("Selecione a turma que deseja acessar (0 para cancelar): "))
                if sub_option == 0:
                    return self
                elif sub_option > len(disciplina):
                    print("Opção inválida, tente novamente!")
                    return self
                else:
                    infos = self._db.query_data(disciplinas[sub_option-1])
                    if infos:
                        for i, info in enumerate(infos):
                            print(f"{i+1}. {info.get('nome')}")
                            print(f"Matrícula: {info.get('matricula')}")
                            print(f"Nota: {info.get('nota')}")
                    else:
                        print(f"Nenhum aluno matriculado para a disciplina {disciplinas[sub_option-1]}")
                        return self
                    aluno = int(input("> Selecione uma opção (0 para cancelar): "))
                    if aluno == 0:
                        return self
                    else:
                        print(f"Aluno: {infos[aluno-1].get('nome')}")
                        print(f"Matrícula: {infos[aluno-1].get('matricula')}")
                        print(f"Nota: {infos[aluno-1].get('nota')}")
                    
                    print("> 1. Adicionar nota")
                    print("> 2. Remover nota")
                    print("> 3. Editar nota")
                    nota = int(input("> Selecione uma opção (0 para cancelar):"))
                    if nota == 0:
                        return
                    elif nota == 1:
                        self.professor.adicionar_notas(disciplinas[sub_option-1], infos[aluno-1].get('nome'))
                        return self
                    elif nota == 2:
                        self.professor.remover_nota(disciplinas[sub_option-1], infos[aluno-1].get('nome'))
                        return self
                    elif nota == 3:
                        self.professor.alterar_notas(disciplinas[sub_option-1], infos[aluno-1].get('nome'))
                        return self
                    else:
                        print("Opção inválida, tente novamente!")
                        return self
            else:
                print("Não foi possível encontrar nenhuma turma!")
            return self
        if option == 2:
            print("> 1. Exibir calendário do mês")
            print("> 2. Exibir calendário do ano")
            print("> 3. Inserir novo evento")
            print("> 4. Modificar evento")
            print("> 5. Apagar evento")
            sub_option = int(input("> Escolha uma opção: "))
            if sub_option == 1:
                self.calendario.exibir_calendario()
            elif sub_option == 2:
                self.calendario.exibir_calendario_anual()
            elif sub_option == 3:
                print("> Criar novo evento")
                self.calendario.inserir_evento_calendario()
            elif sub_option == 4:
                print("> Modificar evento")
                self.calendario.modificar_evento_calendario()
            elif sub_option == 5:
                print("Apagar evento")
                self.calendario.apagar_evento_calendario()
            else:
                print("Opção inválida!")
            return self