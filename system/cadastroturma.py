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
        super().__init__()
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
            aluno_com_nota = {"nome": self.aluno, "matricula": self.matricula, "nota": None}

            for turma in self.turmas:
                try:
                    self.db.update_data("Turmas", {"nome": turma}, {"$push": {"alunos": aluno}})
                except Exception as e:
                    print(f"Erro ao atualizar a turma {turma} no banco de dados: {e}")
                    return False

                try:
                    self.db.insert_data(turma, aluno_com_nota)
                except Exception as e:
                    print(f"Erro ao inserir aluno na turma {turma}: {e}")
                    return False

            print(f"Aluno {self.aluno} adicionado às turmas com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao salvar dados do aluno: {e}")
            return False


class CadastroProfessorTurma(CadastroTurma):
    def __init__(self, professor : str, turmas : List[str] = None) -> None:
        super().__init__()
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
                self.db.update_data("Turmas", {"nome": turma}, {'$set': {"professor": self.professor}})
                print(f"professor {self.professor} adicionado à turma {turma} com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao salvar dados do professor: {e}")
            return False
