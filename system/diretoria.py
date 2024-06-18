from usuario import Usuario
import random
from itertools import islice
from datetime import datetime
from calendario import Calendario
from cadastro import *
from cadastroturma import *

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

    def inserir_em_turmas(infos, max_attempts):
        turmas = []

        for i in range(max_attempts):
            try:
                turma = input("Insira o nome da turma (ou 0 para cancelar): ").strip()
                if turma == "0":
                    break

                if any(t['nome'] == turma for t in infos):
                    turmas.append(turma)
                else:
                    print("Turma não encontrada. Tente novamente.")
            except Exception as e:
                print(f"Erro ao processar a entrada: {e}")

        return turmas

    def cadastrar_aluno(self) -> None:
        """Método utilizado para cadastrar um novo aluno no sistema
        """
        print("> Cadastro de novo aluno")
        print("> Digite 0 para cancelar a qualquer momento")
        print("Informações pessoais")

        nome = input("> Insira o nome do aluno: ")
        idade = int(input("> Insira a idade do aluno: "))
        endereco = input("> Insira o endereço do aluno: ")
        telefone = input("> Insira o telefone do aluno: ")
        email = input("> Insira o email do aluno: ")
        curso = input("> Insira o curso do aluno: ")

        print("Informações de cadastro no sistema")
        login = input("> Insira o login do aluno: ")
        senha = input("> Insira a senha para o aluno: ")
        
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

        print("> Selecione as turmas em que deseja matricular o aluno:")
        infos = self.db.query_data("Turmas")

        for e, info in enumerate(infos):
            print(f"{e+1}. {info.get('nome')}")

        turmas = self.inserir_em_turmas(infos, 5)

        print("Turmas adicionadas:", turmas)
        
        cadastroturma = CadastroAlunoTurma(nome, matricula, turmas)
        if cadastroturma.save():
            cadastroaluno = CadastroAluno(nome, idade, endereco, telefone, email, login, senha, curso, matricula, turmas)
            cadastroaluno.save()
        else:
            print("Não foi possível matricular o aluno!")
    
    def cadastrar_professor(self) -> None:
        """Método para cadastrar um novo professor no sistema
        """
        print("> Cadastro de novo professor")
        print("Informações pessoais")
        nome = input("> Insira o nome do professor: ")
        idade = int(input("> Insira a idade do professor: "))
        endereco = input("> Insira o endereço do professor: ")
        telefone = input("> Insira o telefone do professor: ")
        email = input("> Insira o email do professor: ")
        disciplina = input("> Insira a disciplina do professor: ")

        print("Informações de cadastro no sistema")
        login = input("> Insira o login do professor: ")
        senha = input("> Insira a senha para o professor: ")

        print("> Selecione as turmas em que deseja cadastrar o professor:")
        infos = self.db.query_data("Turmas")
        for e, info in enumerate(infos):
            print(f"{e+1}. {info.get('nome')}")
        print(">Insira o nome, um de cada vez, da turma em que deseja matricular o docente (0 para cancelar):")

        turmas = self.inserir_em_turmas(infos, 5)

        print("Turmas adicionadas:", turmas)
        professores_antigos = []
        for turma in turmas:
            infos = self.db.query_data("Turmas", {'nome': turma})
            professores_antigos.append(infos[0].get('professor'))

        cadastroturma = CadastroProfessorTurma(nome, turmas)
        if cadastroturma.save():
            cadastroprofessor = CadastroProfessor(nome, idade, endereco, telefone, email, login, senha, disciplina, turmas)
            cadastroprofessor.save()
            for professor in professores_antigos:
                self.db.update_data("Professores", {'nome': professor}, {'$set': {'turmas_matriculadas': None}})
        else:
            print("Não foi possível cadastrar o professor!")

    def inserir_evento_calendario(self) -> None:
        """Método para inserir um evento no calendário
        """
        try:
            nome = input("> Insira o nome do evento: ")
            horario = input("> Insira o horário do evento (hh:mm): ")
            data = input("> Insira a data do evento (dd/mm/aaaa): ")
            
            try:
                datetime.strptime(horario, '%H:%M')
            except ValueError:
                print("Formato de horário inválido. Use hh:mm.")
                return
            
            try:
                datetime.strptime(data, '%d/%m/%Y')
            except ValueError:
                print("Formato de data inválido. Use dd/mm/aaaa.")
                return
            
            evento_dict = {'nome': nome, 'horario': horario, 'data': data}
            self.calendario.insert_event(evento_dict)
            print("Evento inserido com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir evento no calendário: {e}")

    def modificar_evento_calendario(self) -> None:
        """Método para modificar um evento existente no calendário
        """
        try:
            nome = input("> Insira o nome do evento que quer alterar: ")

            eventos_encontrados = self.calendario.query_event({'nome': nome})
            if not eventos_encontrados:
                print("Evento não encontrado!")
                return
            else:
                for evento in eventos_encontrados:
                    print(f"{evento}")

            horario = input("> Insira o horário do evento (hh:mm) que quer alterar: ")
            try:
                datetime.strptime(horario, '%H:%M')
            except ValueError:
                print("Formato de horário inválido. Use hh:mm.")
                return

            data = input("> Insira a data do evento (dd/mm/aaaa) que quer alterar: ")
            try:
                datetime.strptime(data, '%d/%m/%Y')
            except ValueError:
                print("Formato de data inválido. Use dd/mm/aaaa.")
                return

            filtro_dict = {'nome': nome, 'horario': horario, 'data': data}

            eventos_encontrados = self.calendario.query_event(filtro_dict)
            if not eventos_encontrados:
                print("Evento com os critérios especificados não encontrado!")
                return

            nome_novo = input("> Insira o novo nome para o evento: ")
            horario_novo = input("> Insira o novo horário do evento (hh:mm): ")
            try:
                datetime.strptime(horario_novo, '%H:%M')
            except ValueError:
                print("Formato de horário novo inválido. Use hh:mm.")
                return

            data_novo = input("> Insira a nova data do evento (dd/mm/aaaa): ")
            try:
                datetime.strptime(data_novo, '%d/%m/%Y')
            except ValueError:
                print("Formato de data nova inválido. Use dd/mm/aaaa.")
                return

            novo_dict = {'nome': nome_novo, 'horario': horario_novo, 'data': data_novo}

            self.calendario.update_event(filtro_dict, novo_dict)
            print("Evento modificado com sucesso!")
        except Exception as e:
            print(f"Erro ao modificar evento no calendário: {e}")

    def apagar_evento_calendario(self) -> None:
        """Método para apagar um evento existente no calendário
        """
        try:
            nome = input("> Insira o nome do evento que quer apagar: ")

            eventos_encontrados = self.calendario.query_event({'nome': nome})
            if not eventos_encontrados:
                print("Evento não encontrado!")
                return
            else:
                for evento in eventos_encontrados:
                    print(f"{evento}")

            horario = input("> Insira o horário do evento (hh:mm) que quer apagar: ")
            try:
                datetime.strptime(horario, '%H:%M')
            except ValueError:
                print("Formato de horário inválido. Use hh:mm.")
                return

            data = input("> Insira a data do evento (dd/mm/aaaa) que quer apagar: ")
            try:
                datetime.strptime(data, '%d/%m/%Y')
            except ValueError:
                print("Formato de data inválido. Use dd/mm/aaaa.")
                return

            filtro_dict = {'nome': nome, 'horario': horario, 'data': data}

            eventos_encontrados = self.calendario.query_event(filtro_dict)
            if not eventos_encontrados:
                print("Evento com os critérios especificados não encontrado!")
                return

            self.calendario.delete_event(filtro_dict)
            print("Evento apagado com sucesso!")
        except Exception as e:
            print(f"Erro ao apagar evento no calendário: {e}")
    
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

            field_option = int(input())
            if field_option == 0:
                return
            if field_option < 1 or field_option >= len(selected_info):
                print("Opção inválida!")
                return

            keys = list(selected_info.keys())[1:]  # Ignora o primeiro campo
            key_to_edit = keys[field_option-1]

            change = input(f"> Insira o novo valor para {key_to_edit.capitalize()}: ")

            self.db.update_data(f"{tipo}", selected_info, {'$set': {key_to_edit: change}})
            print(f"Campo '{key_to_edit.capitalize()}' atualizado com sucesso!")
            
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")
        except Exception as e:
            print(f"Erro ao editar informações: {e}")
        
    #def consultar turmas
    #def calcular aprovados e reprovados
    
    def deletar_usuario(colecao, criterio) -> None:
        pass
