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
        """
        Método auxiliar para obter os nomes das disciplinas em que um professor ou aluno será matriculado.

        Este método auxilia na coleta dos nomes das disciplinas que um professor ou aluno deve ser 
        matriculado. Ele permite ao usuário inserir os nomes das disciplinas, validando se essas disciplinas 
        existem na lista fornecida e garantindo que as inserções não excedam um número máximo de tentativas.

        Args:
            infos (list): Lista de disciplinas disponíveis, cada uma representada por um dicionário contendo 
                        ao menos a chave 'nome'.
            max_attempts (int): Número máximo de tentativas permitidas para inserir os nomes das disciplinas.

        Returns:
            list: Lista com os nomes das disciplinas em que o professor ou aluno será matriculado. 
                Se o usuário digitar '0', o processo de inserção é interrompido e a lista atual de 
                disciplinas é retornada.

        Exceções:
            Qualquer exceção gerada durante o processamento das entradas será capturada e uma mensagem 
            de erro será exibida.
        """
        disciplinas = []

        for i in range(max_attempts):
            try:
                disciplina = input("Insira o nome da disciplina: ").strip()
                if disciplina == '0':
                    return disciplinas
                elif any(t['nome'] == disciplina for t in infos):
                    disciplinas.append(disciplina)
                else:
                    print("disciplina não encontrada. Tente novamente.")
            except Exception as e:
                print(f"Erro ao processar a entrada: {e}")

        return disciplinas

    def cadastrar_aluno(self) -> None:
        """
        Método utilizado para cadastrar um novo aluno no sistema.

        Este método interage com o usuário para coletar todas as informações necessárias para cadastrar 
        um novo aluno no sistema. O usuário pode cancelar o cadastro a qualquer momento digitando '0'. 
        O processo envolve a coleta de dados pessoais, informações de login, geração de um número de 
        matrícula único, e a possibilidade de matricular o aluno em disciplinas.

        Procedimento:
        1. Coleta informações pessoais do aluno: nome, idade, endereço, telefone, email, curso.
        2. Coleta informações de cadastro no sistema: login e senha.
        3. Gera um número de matrícula único para o aluno.
        4. Permite a matrícula do aluno em disciplinas, se desejado.
        5. Salva os dados do aluno e das disciplinas no banco de dados.

        Exceções:
            Se qualquer entrada for '0', o cadastro será cancelado e uma mensagem será exibida.
            Verificações de validação são realizadas para a idade e a existência de disciplinas.
            Se um erro ocorrer durante o processamento, uma mensagem de erro será exibida.

        Returns:
            None
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
        """
        Cadastra um aluno em uma disciplina.

        Este método busca verificar a existência da disciplina e do aluno no banco de dados antes de proceder com o 
        cadastro do aluno na disciplina especificada. Se a disciplina ou o aluno não existirem, o método informa ao 
        usuário e termina. Caso contrário, tenta realizar o cadastro e lida com possíveis exceções.

        Args:
            disciplina (str): Nome da disciplina em que o aluno será matriculado.
            aluno (str): Nome do aluno que será matriculado na disciplina.

        Procedimento:
        1. Verifica a existência da disciplina no banco de dados.
        2. Verifica a existência do aluno no banco de dados.
        3. Se a disciplina ou o aluno não existirem, exibe uma mensagem de erro e retorna.
        4. Caso ambos existam, tenta cadastrar o aluno na disciplina.
        5. Em caso de erro durante o cadastro, exibe uma mensagem de erro específica.

        Exceções:
            Se qualquer etapa de verificação ou cadastro falhar, uma mensagem de erro será exibida.

        Returns:
            None
        """
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
        """
        Método para cadastrar um novo professor no sistema.

        Este método guia o usuário pelo processo de cadastro de um novo professor, incluindo a coleta de informações pessoais,
        detalhes de login e senha, e disciplinas em que o professor lecionará. O método também permite cancelar o cadastro em
        qualquer momento.

        Procedimento:
        1. Solicita e coleta informações pessoais do professor (nome, idade, endereço, telefone, email).
        2. Solicita e coleta informações de cadastro no sistema (login e senha).
        3. Exibe uma lista de disciplinas disponíveis e permite selecionar aquelas em que o professor lecionará.
        4. Se a lista de disciplinas não estiver vazia, prossegue com o cadastro do professor nas disciplinas.
        5. Salva as informações do professor no sistema.
        6. Exibe mensagens apropriadas em caso de sucesso ou cancelamento do cadastro.

        Args:
            None

        Exceções:
            Se qualquer entrada for '0', o processo de cadastro será cancelado e uma mensagem será exibida.

        Returns:
            None
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
            print("> Insira o nome, um de cada vez, da disciplina em que deseja matricular o docente (0 para cancelar):")

        disciplinas = self.inserir_em_disciplinas(infos, len(infos))
        if not disciplinas:
            print("O professor não foi cadastrado em nenhuma disciplina!")
        else:
            print("Disciplinas adicionadas:", disciplinas)

        professores_antigos = []
        for disciplina in disciplinas:
            infos = self.db.query_data("Disciplinas", {'nome': disciplina})
            professores_antigos.append(infos[0].get('professor'))

        cadastroprofessor = CadastroProfessor(nome, idade, endereco, telefone, email, login, senha)
        cadastroprofessor.save()

        if disciplinas is not None and disciplinas != []:
            cadastrodisciplina = CadastroProfessorDisciplina(nome, disciplinas)
            cadastrodisciplina.save()
        else:
            print("Não foi possível cadastrar o professor em disciplinas!")
            return
        
        print("Professor cadastrado com sucesso!")
    
    def cadastrar_professor_em_disciplina(self, professor : str, disciplina : str) -> None:
        """
        Método para cadastrar um professor em uma disciplina específica.

        Este método verifica a existência do professor e da disciplina no banco de dados. Se ambos existirem,
        o professor é cadastrado na disciplina. Em caso de erro ou se o professor/disciplina não existirem,
        uma mensagem apropriada é exibida.

        Args:
            professor (str): Nome do professor a ser cadastrado na disciplina.
            disciplina (str): Nome da disciplina na qual o professor será cadastrado.

        Procedimento:
        1. Verifica se a disciplina e o professor existem no banco de dados.
        2. Se qualquer um não existir, exibe uma mensagem de erro e encerra o processo.
        3. Se ambos existirem, tenta cadastrar o professor na disciplina.
        4. Em caso de sucesso, o professor é cadastrado na disciplina.
        5. Em caso de erro, exibe uma mensagem de erro apropriada.

        Exceptions:
            Exibe uma mensagem de erro se não for possível cadastrar o professor na disciplina.

        Returns:
            None
        """
        valida_disciplina = self.db.query_data("Disciplinas", {"nome": disciplina})
        valida_professor = self.db.query_data("Professores", {"nome": professor})
        if not valida_disciplina or not valida_professor:
            print("Disciplina ou professor não existente! Tente de novo.")
            return
        try:
            cadastroprofessor = CadastroProfessorDisciplina(professor, [disciplina])
            cadastroprofessor.save()
        except Exception as e:
            print(f"Não foi possível cadastrar o professor na disciplina! {e}")

    def exibir_informações_disciplina(self, disciplina : str) -> None:
        """
        Exibe informações completas sobre uma disciplina, incluindo nome, professor, horários e lista de alunos matriculados.

        Este método consulta o banco de dados para obter informações sobre a disciplina especificada.
        Em seguida, exibe o nome da disciplina, o nome do professor responsável e os horários das aulas.
        O usuário pode optar por exibir informações sobre os alunos matriculados na disciplina.

        Args:
            disciplina (str): Nome da disciplina cujas informações serão exibidas.

        Procedimento:
        1. Consulta o banco de dados para obter informações completas sobre a disciplina especificada.
        2. Exibe o nome da disciplina, o nome do professor responsável e os horários das aulas.
        3. Solicita ao usuário que digite uma opção para exibir informações detalhadas sobre os alunos matriculados.
        4. Se o usuário escolher a opção '1', exibe uma lista dos alunos matriculados na disciplina.
        5. Se o usuário escolher a opção '0', o processo é encerrado.
        6. Se o usuário inserir uma opção inválida, exibe uma mensagem de erro apropriada.

        Returns:
            None
        """
        infos = self.db.query_data("Disciplinas", {"nome": disciplina})
        info = infos[0]
        print(f"> Nome: {info.get('nome')}")
        print(f"Professor(a): {info.get('professor')}")
        print("Horários:")
        for horario in info.get('horarios'):
            print(f". {horario}")
        option = int(input("> Digite 1 para exibir informações dos alunos (0 para cancelar): "))
        if option == 0:
            return
        elif option > 1 or option < 1:
            print("Opção inválida!")
            return
        else:
            if info.get('alunos'):
                print("Lista de alunos matriculados na disciplina:")
                for aluno in info.get('alunos'):
                    print(f". {aluno['nome']}, {aluno['matricula']}")
            else:
                print("Não há alunos matriculados nesta disciplina!")

    def editar_infos(self, tipo: str) -> None:
        """
        Método geral para editar informações de qualquer coleção no sistema.

        Este método permite ao usuário selecionar uma coleção específica (como 'Alunos', 'Professores' ou 'Disciplinas')
        e, em seguida, escolher um item dessa coleção para editar. O usuário pode optar por editar qualquer campo de informação
        dentro do item selecionado, incluindo listas, onde é possível adicionar ou remover elementos.

        Args:
            tipo (str): Nome da coleção no banco de dados que contém as informações a serem editadas ('Alunos', 'Professores', 'Disciplinas', etc.).

        Procedimento:
        1. Consulta o banco de dados para obter todas as informações da coleção especificada por 'tipo'.
        2. Exibe uma lista numerada de itens encontrados na coleção, permitindo ao usuário escolher qual item editar.
        3. Solicita ao usuário que selecione o campo dentro do item escolhido que deseja editar.
        4. Se o campo escolhido for uma lista, oferece opções para adicionar ou remover elementos dessa lista.
        5. Realiza a edição no banco de dados, atualizando o valor do campo conforme especificado pelo usuário.
        6. Exibe mensagens de confirmação após a edição bem-sucedida de um campo.

        Returns:
            None

        Raises:
            ValueError: Se a entrada do usuário não for um número válido.
            Exception: Qualquer outro erro que possa ocorrer ao tentar editar as informações no banco de dados.
        """
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
