from abc import ABC, abstractmethod
from database import DataBase
from turma import Turma
from typing import List

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
        super().__init__(nome, idade, endereco, telefone, email, login)
        self.curso = curso
        self.matricula = matricula
        self.turmas_matriculadas = turmas_matriculadas
        
    # Busca as notas de cada turma do aluno e retorna uma lista com as notas
    def buscar_notas(self) -> list:
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
    
    # Busca os horarios de cada turma do aluno e retorna uma lista com os horarios
    def buscar_horarios(self) -> list:
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
    
    @property
    def turmas_matriculadas(self) -> list:
        return self.turmas_matriculadas

class Professor(Usuario):
    def __init__(self, nome: str, idade: int, endereco: str, telefone: str, email: str, login: str, salario: str, turmas : List[str], nivel : int) -> None:
        super().__init__(nome, idade, endereco, telefone, email, login, salario, nivel)
        self.salario = salario
        self.turmas = turmas
    
    def adicionar_notas(self, turma : str, aluno : str) -> None:
        pass
        """if turma in self.turmas:
            self.db.query_data(turma, {"nome"})"""
        
        
    '''def alterar_notas()'''

class Staff(Usuario):
    def __init__(self, nome: str, idade: int, endereco: str, telefone: str, email: str, login: str, cargo: str, salario: str) -> None:
        super().__init__(nome, idade, endereco, telefone, email, login, salario)
        self.cargo = cargo
    
    def deletar_usuario(colecao, criterio) -> None:
        pass

