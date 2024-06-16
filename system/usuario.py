import random
from datetime import datetime
from abc import ABC, abstractmethod
from database import DataBase
from turma import Turma
from typing import List
from cadastro import *
from cadastroturma import *

class Usuario(ABC):
    def __init__(self, nome: str, idade: int, endereco: str, telefone: str, email: str, login: str) -> None:
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self._login = login
        self.db = DataBase()

class Aluno(Usuario):
    def __init__(self, nome : str, idade : int, endereco : str, telefone: str, email : str, login : str, curso : str, matricula : str, turmas_matriculadas : List[str] = None) -> None:
        """Construtor da classe Aluno

        Args:
            nome (str): nome do aluno
            idade (int): idade do aluno
            endereco (str): endereço do aluno
            telefone (str): telefone do aluno
            email (str): email do aluno
            login (str): login utilizado para logar no sistema
            curso (str): curso em que o aluno está matriculado
            matricula (str): matrícula do aluno
            turmas_matriculadas (List[str], optional): lista de turmas nas quais o aluno está matriculado. Defaults to None.
        """
        super().__init__(nome, idade, endereco, telefone, email, login)
        self.curso = curso
        self.matricula = matricula
        self.turmas_matriculadas = turmas_matriculadas
        
    def buscar_notas(self) -> list:
        """Método para buscar as notas de cada turma do aluno

        Returns:
            list: lista de dicionários com as notas do aluno. {"Turma", "nota"}
        """
        if not self.turmas_matriculadas:
            print(f"O aluno {self.nome} não está matriculado em nenhuma turma!")
            return []
        notas = []
        for turma in self.turmas_matriculadas:
            infos = self.db.query_data(turma, {"nome": self.nome})
            if infos:
                nota = {"turma": turma, "nota": infos[0].get('nota', 'Nota não encontrada')}
                notas.append(nota)
            else:
                print(f"Nenhuma informação encontrada para o aluno {self.nome} na turma {turma}.")
        return notas
    
    def buscar_horarios(self) -> list:
        """Método para buscar os horários de cada turma do aluno

        Returns:
            list: lista com os horários das turmas
        """
        if not self.turmas_matriculadas:
            print(f"O aluno {self.nome} não está matriculado em nenhuma turma!")
            return []
        horarios = []
        for turma in self.turmas_matriculadas:
            infos = self.db.query_data("Turmas", {"nome": self.nome})
            if infos:
                horario = {"turma": infos[0].get('nome'), "horarios": infos[0].get('horarios', 'Horarios não encontrados')}
                horarios.append(horario)
            else:
                print(f"Nenhuma informação encontrada para o aluno {self.nome} na turma {turma}.")
        return horarios

    def busca_turmas_matriculadas(self) -> list:
        """Método para buscar as turmas matriculadas do aluno

        Returns:
            list: turmas em que o aluno está matriculado
        """
        return self.turmas_matriculadas

class Professor(Usuario):
    def __init__(self, nome: str, idade: int, endereco: str, telefone: str, email: str, login: str, disciplina : str, turmas : List[str]) -> None:
        super().__init__(nome, idade, endereco, telefone, email, login)
        self.disciplina = disciplina
        self.turmas = turmas
    
    def adicionar_notas(self, turma : str, aluno : str) -> None:
        pass
        """if turma in self.turmas:
            self.db.query_data(turma, {"nome"})"""
        
        
    '''def alterar_notas()'''

class Diretoria(Usuario):
    def __init__(self, nome: str, idade: int, endereco: str, telefone: str, email: str, login: str, cargo: str) -> None:
        super().__init__(nome, idade, endereco, telefone, email, login)
        self.cargo = cargo

    def cadastrar_aluno(self) -> None:
        print("> Cadastro de novo aluno")
        print("Informações pessoais")
        nome = input("> Insira o nome do aluno:")
        idade = int(input("> Insira a idade do aluno:"))
        endereco = input("> Insira o endereço do aluno:")
        telefone = input("> Insira o telefone do aluno")
        email = input("> Insira o email do aluno:")
        curso = input("> Insira o curso do aluno:")

        print("Informações de cadastro no sistema")
        login = input("> Insira o login do aluno:")
        senha = input("> Insira a senha para o aluno:")
        
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
        print(">Insira o nome, um de cada vez, da turma em que deseja matricular o estudante (0 para cancelar):")
        turmas = []
        while True:
            turma = input()
            if turma == 0:
                break
            turmas.append(turma)
        
        cadastroturma = CadastroAlunoTurma(nome, matricula, turmas)
        if cadastroturma.save():
            cadastroaluno = CadastroAluno(nome, idade, endereco, telefone, email, login, senha, curso, matricula, turmas)
            cadastroaluno.save()
        else:
            print("Não foi possível matricular o aluno!")
    
    def cadastrar_professor(self) -> None:
        print("> Cadastro de novo professor")
        print("Informações pessoais")
        nome = input("> Insira o nome do professor:")
        idade = int(input("> Insira a idade do professor:"))
        endereco = input("> Insira o endereço do professor:")
        telefone = input("> Insira o telefone do professor")
        email = input("> Insira o email do professor:")
        disciplina = input("> Insira a disciplina do professor:")

        print("Informações de cadastro no sistema")
        login = input("> Insira o login do professor:")
        senha = input("> Insira a senha para o professor:")

        print("> Selecione as turmas em que deseja cadastrar o professor:")
        infos = self.db.query_data("Turmas")
        for e, info in enumerate(infos):
            print(f"{e+1}. {info.get('nome')}")
        print(">Insira o nome, um de cada vez, da turma em que deseja matricular o docente (0 para cancelar):")
        turmas = []
        while True:
            turma = input()
            if turma == 0:
                break
            turmas.append(turma)

        cadastroturma = CadastroProfessorTurma(nome, turmas)
        if cadastroturma.save():
            cadastroprofessor = CadastroProfessor(nome, idade, endereco, telefone, email, login, senha, disciplina, turmas)
            cadastroprofessor.save()
        else:
            print("Não foi possível cadastrar o professor!")
    
    def deletar_usuario(colecao, criterio) -> None:
        pass

