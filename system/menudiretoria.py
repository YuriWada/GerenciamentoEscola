from usuario import *
from typing import Type
from diretoria import Diretoria
from menu import Menu
from criadisciplina import CriaDisciplina
import re

class MenuDiretoria(Menu):
    def __init__(self, diretoria : Type[Diretoria]) -> None:
        self.funcionario = diretoria
        super().__init__(f"Olá, {diretoria.cargo}!")
        self._options = ['Alunos', 'Professores', 'Diretoria', 'Acessar Disciplinas', 'Acessar Calendário']

    def next(self, option : int) -> None:
        if option == 1:
            print("> 1. Exibir lista de alunos")
            print("> 2. Cadastrar novo aluno")
            print("> 3. Editar informações de aluno")
            sub_option = int(input("> Escolha uma opção:"))
            if sub_option == 1:
                print("================================")
                print("xxx Exibindo lista de alunos xxx")
                infos = self._db.query_data("Alunos")
                for e, info in enumerate(infos):
                    print("================================")
                    print(f"{e+1}. {info.get('nome')}")
                    print(f"Idade: {info.get('idade')}")
                    print(f"E-mail: {info.get('email')}")
                    print(f"Curso: {info.get('curso')}")
                    print(f"Matrícula: {info.get('matricula')}")
                    print("Disciplinas:")
                    if info.get('disciplinas_matriculadas'):
                        for disciplina in info.get('disciplinas_matriculadas'):
                            print(f". {disciplina}")
            elif sub_option == 2:
                self.funcionario.cadastrar_aluno()
            elif sub_option == 3:
                self.funcionario.editar_infos("Alunos")
            elif sub_option == 0:
                return self
            else:
                print("Opção inválida!")
            return self
        elif option == 2:
            print("> 1. Exibir lista de professores")
            print("> 2. Cadastrar novo professor")
            print("> 3. Editar informações de professor")
            sub_option = int(input("> Escolha uma opção:"))
            if sub_option == 1:
                print("======================================")
                print("xxx Exibindo lista de professores xxx")
                infos = self._db.query_data("Professores")
                for e, info in enumerate(infos):
                    print("======================================")
                    print(f"{e+1}. {info.get('nome')}")
                    print(f"Idade: {info.get('idade')}")
                    print(f"E-mail: {info.get('email')}")
                    print("Disciplinas:")
                    if info.get('disciplinas_matriculadas'):
                        for disciplina in info.get('disciplinas_matriculadas'):
                            print(f". {disciplina}")
            elif sub_option == 2:
                self.funcionario.cadastrar_professor()
            elif sub_option == 3:
                self.funcionario.editar_infos("Professores")
            elif sub_option == 0:
                return self
            else:
                print("Opção inválida!")
            return self
        elif option == 3:
            print("> 1. Exibir lista de funcionários")
            print("> 2. Editar informação de funcionário")
            sub_option = int(input("> Escolha uma opção:"))
            if sub_option == 1:
                print("======================================")
                print("xxx Exibindo lista de funcionários xxx")
                infos = self._db.query_data("Diretoria")
                for e, info in enumerate(infos):
                    print("======================================")
                    print(f"{e+1}. {info.get('nome')}")
                    print(f"Idade: {info.get('idade')}")
                    print(f"E-mail: {info.get('email')}")
                    print(f"Cargo: {info.get('cargo')}")
            elif sub_option == 2:
                self.funcionario.editar_infos("Diretoria")
            elif sub_option == 0:
                return self
            else:
                print("Opção inválida!")
            return self
        elif option == 4:
            print("> 1. Lista de disciplinas")
            print("> 2. Cadastrar aluno em disciplina")
            print("> 3. Cadastrar professor em disciplina")
            print("> 4. Criar nova disciplina")
            sub_option = int(input("> Escolha uma opção: "))
            if sub_option == 1:
                infos_disciplinas = sorted(self._db.query_data("Disciplinas"), key=lambda x:x['nome'])
                for e, info_disciplina in enumerate(infos_disciplinas, start=1):
                    print(f"{e}. {info_disciplina.get('nome')}")
                exibe_disc = int(input("> Digite o número da disciplina para exibir informações adicionais (0 para cancelar): "))
                if exibe_disc == 0:
                    return self
                elif exibe_disc > len(infos_disciplinas) or exibe_disc < 0:
                    print("Opção inválida!")
                    return self
                else:
                    self.funcionario.exibir_informações_disciplina(infos_disciplinas[exibe_disc-1].get('nome'))
                return self
            elif sub_option == 2:
                nome_aluno = input("> Insira o nome do aluno: ")
                nome_disciplina = input("> Insira o nome da disciplina: ")
                self.funcionario.cadastrar_aluno_em_disciplina(nome_disciplina, nome_aluno)
            elif sub_option == 3:
                nome_professor = input("> Insira o nome do professor: ")
                nome_disciplina = input("> Insira o nome da disciplina: ")
                self.funcionario.cadastrar_professor_em_disciplina(nome_professor, nome_disciplina)
                return self
            elif sub_option -- 4:
                nova_disciplina = input("> Insira o nome da nova disciplina: ").strip()
                
                while not nova_disciplina:
                    print("Nome da disciplina não pode ser vazio.")
                    nova_disciplina = input("> Insira o nome da nova disciplina: ").strip()
                nova_disciplina_horarios = []
                horarios = '1'
                while horarios != '0':
                    horarios = input("> Insira os horários da nova disciplina no formato (seg|ter|qua|qui|sex|sab|dom) hh:mm (0 para cancelar): ").strip()
                    if horarios == '0':
                        break
                    if re.match(r'^(seg|ter|qua|qui|sex|sab|dom) [0-2][0-9]:[0-5][0-9]$', horarios, re.IGNORECASE):
                        nova_disciplina_horarios.append(horarios)
                    else:
                        print("Horário inválido. Por favor, insira no formato dia_da_semana hh:mm.")
                if not nova_disciplina_horarios:
                    print("Nenhum horário válido inserido. Operação cancelada.")
                    return
                cria_disciplina = CriaDisciplina(nova_disciplina, nova_disciplina_horarios)
                cria_disciplina.save()
                print(f"Disciplina '{nova_disciplina}' criada com sucesso com os horários: {nova_disciplina_horarios}")
            elif sub_option == 0:
                return self
            else:
                print("Opção inválida, tente novamente!")
                return self
            return self
        elif option == 5:
            print("> 1. Exibir calendário do mês")
            print("> 2. Exibir calendário do ano")
            print("> 3. Inserir novo evento")
            print("> 4. Modificar evento")
            print("> 5. Apagar evento")
            try:
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
                elif sub_option == 0:
                    return self
                else:
                    print("Opção inválida! Tente novamente")
            except ValueError:
                print("Opção inválida! Por favor, insira um número.")
            return self
        else:
            print("Opção inválida! Tente novamente")
            return self