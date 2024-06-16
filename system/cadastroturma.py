from database import DataBase
from abc import ABC, abstractmethod
from typing import List

class CadastroTurma(ABC):
    def __init__(self) -> None:
        self.db = DataBase()

    @abstractmethod
    def valida_dados(self) -> bool:
        pass

    @abstractmethod
    def save(self) -> bool:
        pass

class CadastroAlunoTurma(CadastroTurma):
    def __init__(self, aluno : str, matricula : str, turmas : List[str], nota : float = None) -> None:
        self.aluno = aluno
        self.matricula = matricula
        self.nota = nota
        self.turmas = turmas

    def valida_dados(self) -> bool:
        for turma in self.turmas:
            infos = self.db.query_data("Turmas", {"nome": turma})
            if not infos:
                return False
            for info in infos:
                for aluno in info.get('alunos'):
                    if self.aluno == aluno.get('nome'):
                        return False
        return True

    def save(self) -> bool:
        try:
            if not self.valida_dados():
                return False

            aluno = {"nome": self.aluno, "matricula": self.matricula}
            
            try:
                for turma in self.turmas:
                    self.db.update_data("Turmas", {"nome": turma}, {"$push": {"alunos": aluno}})
            except Exception as e:
                print(f"Erro ao atualizar a turma no banco de dados: {e}")
                return False
            
            aluno_com_nota = {"nome": self.aluno, "matricula": self.matricula, "nota": None}
            try:
                for turma in self.turmas:
                    self.db.insert_data(self.turma, aluno_com_nota)
            except Exception as e:
                print(f"Erro ao inserir aluno na turma: {e}")
                return False
            
            print(f"Aluno {self.aluno} adicionado à turma {self.turma} com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao salvar dados do aluno: {e}")
            return False

class CadastroProfessorTurma(CadastroTurma):
    def __init__(self, professor : str, turmas : List[str]) -> None:
        self.professor = professor
        self.turmas = turmas

    def valida_dados(self) -> bool:
        for turma in self.turmas:
            infos = self.db.query_data("Turmas", {"nome": turma})
            if not infos:
                return False
            for info in infos:
                if self.professor == info.get('professor'):
                    return False
        return True

    def save(self) -> bool:
        try:
            if not self.valida_dados():
                return False
            for turma in self.turmas:
                self.db.update_data("Turmas", {"nome": turma}, {"professor": self.professor})
                print(f"professor {self.professor} adicionado à turma {turma} com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao salvar dados do professor: {e}")
            return False
