from usuario import Usuario
import random
from itertools import islice
from datetime import datetime
from calendario import Calendario
from cadastro import *
from cadastroaluno import CadastroAluno
from cadastroalunodisciplina import CadastroAlunoDisciplina
from cadastroprof import CadastroProfessor
from cadastroprofdisciplina import CadastroProfessorDisciplina

class Diretoria(Usuario):
    def __init__(self, nome: str, idade: int, endereco: str, telefone: str, email: str, login: str, cargo: str) -> None:
        """Construtor da classe Diretoria. Corpo constituído pelos funcionários da escola.

        Args:
            nome (str): nome do funcionário
            idade (int): idade do funcionário
            endereco (str): endereço do funcionário
            telefone (str): telefone do funcionário
            email (str): email do funcionário
            login (str): login a ser utilizado para logar no sistema
            cargo (str): cargo do funcionário
        """
        super().__init__(nome, idade, endereco, telefone, email, login)
        self.cargo = cargo
        self.calendario = Calendario()

    def inserir_em_disciplinas(self, infos : list, max_attempts : int) -> list:
        disciplinas = []

        for i in range(max_attempts):
            try:
                disciplina = input("Insira o nome da disciplina: ").strip()
                if int(disciplina) == 0:
                    break
                elif any(t['nome'] == disciplina for t in infos):
                    disciplinas.append(disciplina)
                else:
                    print("disciplina não encontrada. Tente novamente.")
            except Exception as e:
                print(f"Erro ao processar a entrada: {e}")

        return disciplinas

    def cadastrar_aluno(self) -> None:
        """Método utilizado para cadastrar um novo aluno no sistema
        """
        print("> Cadastro de novo aluno")
        print("> Digite 0 para cancelar a qualquer momento")
        print("Informações pessoais")

        nome = input("> Insira o nome do aluno: ")
        if nome == '0':
            print("Cadastro cancelado.")
            return

        idade = int(input("> Insira a idade do aluno: "))
        if idade == '0':
            print("Cadastro cancelado.")
            return
        while idade < 0:
            print("Idade inválida!")

        endereco = input("> Insira o endereço do aluno: ")
        if endereco == '0':
            print("Cadastro cancelado.")
            return

        telefone = input("> Insira o telefone do aluno: ")
        if telefone == '0':
            print("Cadastro cancelado.")
            return

        email = input("> Insira o email do aluno: ")
        if email == '0':
            print("Cadastro cancelado.")
            return

        curso = input("> Insira o curso do aluno: ")
        if curso == '0':
            print("Cadastro cancelado.")
            return

        print("Informações de cadastro no sistema")
        login = input("> Insira o login do aluno: ")
        if login == '0':
            print("Cadastro cancelado.")
            return

        senha = input("> Insira a senha para o aluno: ")
        if senha == '0':
            print("Cadastro cancelado.")
            return

        print("Gerando número de matrícula...")
        now = datetime.now()
        ano_corrente = now.year

        while True:
            numero_aleatorio = random.randint(100, 999)
            matricula = f"{ano_corrente}{numero_aleatorio}"

            # Verifica se a matrícula já existe no banco de dados
            if not self.db.query_data("Alunos", {"matricula": matricula}):
                break
        print(f"Número de matrícula gerado: {matricula}")

        print("> Selecione as disciplinas em que deseja matricular o aluno (0 para não matricular em disciplinas):")
        infos = self.db.query_data("Disciplinas")

        if infos:
            for e, info in enumerate(infos):
                print(f"{e+1}. {info.get('nome')}")
        
        disciplinas = self.inserir_em_disciplinas(infos, 5)
        if not disciplinas:
            print("O aluno não foi cadastrado em nenhuma disciplina!")
        else:
            print("Disciplinas adicionadas:", disciplinas)

        cadastroaluno = CadastroAluno(nome, idade, endereco, telefone, email, login, senha, curso, matricula)
        cadastroaluno.save()
        print("Aluno cadastrado com sucesso!")

        if disciplinas is not None and disciplinas != []:
            cadastrodisciplina = CadastroAlunoDisciplina(nome, matricula, disciplinas)
            cadastrodisciplina.save()
    
    def cadastrar_aluno_em_disciplina(self, disciplina : str, aluno : str) -> None:
        valida_disciplina = self.db.query_data("Disciplinas", {"nome": disciplina})
        valida_aluno = self.db.query_data("Alunos", {"nome": aluno})
        if not valida_disciplina or not valida_aluno:
            print("Disciplina ou aluno não existente! Tente de novo.")
            return
        try:
            cadastroaluno = CadastroAlunoDisciplina(aluno, valida_aluno[0].get('matricula'), [disciplina])
            cadastroaluno.save()
        except Exception as e:
            print(f"Não foi possível cadastrar o aluno na disciplina! {e}")

    def cadastrar_professor(self) -> None:
        """Método para cadastrar um novo professor no sistema
        """
        print("> Cadastro de novo professor")
        print("> Digite 0 para cancelar a qualquer momento")
        print("Informações pessoais")

        nome = input("> Insira o nome do professor: ")
        if nome == '0':
            print("Cadastro cancelado.")
            return

        idade = input("> Insira a idade do professor: ")
        if idade == '0':
            print("Cadastro cancelado.")
            return
        idade = int(idade)

        endereco = input("> Insira o endereço do professor: ")
        if endereco == '0':
            print("Cadastro cancelado.")
            return

        telefone = input("> Insira o telefone do professor: ")
        if telefone == '0':
            print("Cadastro cancelado.")
            return

        email = input("> Insira o email do professor: ")
        if email == '0':
            print("Cadastro cancelado.")
            return
        
        print("Informações de cadastro no sistema")
        login = input("> Insira o login do professor: ")
        if login == '0':
            print("Cadastro cancelado.")
            return

        senha = input("> Insira a senha para o professor: ")
        if senha == '0':
            print("Cadastro cancelado.")
            return

        print("> Selecione as disciplinas em que deseja cadastrar o professor:")
        infos = self.db.query_data("Disciplinas")

        if infos:
            for e, info in enumerate(infos):
                print(f"{e+1}. {info.get('nome')}")
            print(">Insira o nome, um de cada vez, da disciplina em que deseja matricular o docente (0 para cancelar):")

        disciplinas = self.inserir_em_disciplinas(infos, 5)
        if not disciplinas:
            print("O professor não foi cadastrado em nenhuma disciplina!")
        else:
            print("Disciplinas adicionadas:", disciplinas)

        professores_antigos = []
        for disciplina in disciplinas:
            infos = self.db.query_data("Disciplinas", {'nome': disciplina})
            professores_antigos.append(infos[0].get('professor'))

        cadastroprofessor = CadastroProfessor(nome, idade, endereco, telefone, email, login, senha, disciplinas)
        cadastroprofessor.save()

        if disciplinas is not None and disciplinas != []:
            cadastrodisciplina = CadastroProfessorDisciplina(nome, disciplinas)
            if cadastrodisciplina.save():
                for professor in professores_antigos:
                    self.db.update_data("Professores", {'nome': professor}, {'$set': {'disciplinas_matriculadas': None}})
            else:
                print("Não foi possível cadastrar o professor nas disciplinas!")
        
        print("Professor cadastrado com sucesso!")
    
    def cadastrar_professor_em_disciplina(self) -> None:
        pass

    def exibir_informações_disciplina(self) -> None:
        pass

    def calcula_aprovados(self) -> None:
        pass

    def calcula_reprovados(self) -> None:
        pass

    def editar_infos(self, tipo: str) -> None:
        try:
            infos = self.db.query_data(f"{tipo}")
            if not infos:
                print("Nenhuma informação encontrada!")
                return
            
            for e, info in enumerate(infos, start=1):
                index = list(info.items())
                print("=" * 60)
                print(f"{e}. {index[1][1]}")
                for key, value in islice(info.items(), 2, None):
                    print(f"{key.capitalize()}: {value}")
            
            print("> Escolha um número para editar (0 para cancelar): ")
            option = int(input())
            if option == 0:
                return
            if option < 1 or option > len(infos):
                print("Opção inválida!")
                return

            print("> Escolha o campo que deseja editar (0 para cancelar): ")
            selected_info = infos[option-1]
            for e, (key, value) in enumerate(islice(selected_info.items(), 1, None), start=1):
                print(f"{e}. {key.capitalize()}: {value}")

            field_option = int(input("> Insira um valor (0 para cancelar): "))
            if field_option == 0:
                return
            if field_option < 1 or field_option >= len(selected_info):
                print("Opção inválida!")
                return

            keys = list(selected_info.keys())[1:]  # Ignora o primeiro campo
            key_to_edit = keys[field_option-1]

            type_key_to_edit = selected_info.get(key_to_edit)
            if isinstance(type_key_to_edit, list):
                print("> Selecione uma operação (0 para cancelar):")
                print("> 1. Adicionar")
                print("> 2. Remover")
                sub_option = int(input())
                if sub_option == 1:
                    change = input(f"> Insira o novo valor para {key_to_edit.capitalize()} (0 para cancelar): ")
                    if change == '0':
                        return
                    if not selected_info.get(key_to_edit):
                        self.db.update_data(f"{tipo}", selected_info, {'$set': {key_to_edit: change}})
                    else:
                        self.db.update_data(f"{tipo}", selected_info, {'$push': {key_to_edit: change}})
                elif sub_option == 2:
                    if not selected_info.get(key_to_edit):
                        print("Não é possível remover itens de lista vazia!")
                        return
                    else:
                        change = input(f"> Insira o valor que deseja remover de {key_to_edit.capitalize()} (0 para cancelar): ")
                        if change == '0':
                            return
                        self.db.update_data(f"{tipo}", selected_info, {'$pull': {key_to_edit: change}})
                        if tipo == 'Professores' and key_to_edit == 'disciplinas_matriculadas':
                            info_disc = self.db.query_data("Disciplinas", {"nome": change})
                            if info_disc[0].get('professor') is not None:
                                self.db.update_data("Disciplinas", {"nome": change}, {'$set': {'professor': None}})                
                else:
                    print("Opção inválida!")
                    return
            else:
                change = input(f"> Insira o novo valor para {key_to_edit.capitalize()}: ")

                self.db.update_data(f"{tipo}", selected_info, {'$set': {key_to_edit: change}})
                print(f"Campo '{key_to_edit.capitalize()}' atualizado com sucesso!")
            
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")
        except Exception as e:
            print(f"Erro ao editar informações: {e}")
