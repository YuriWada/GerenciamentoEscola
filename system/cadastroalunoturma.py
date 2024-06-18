from cadastroturma import CadastroTurma
from typing import List

class CadastroAlunoTurma(CadastroTurma):
    def __init__(self, aluno : str, matricula : str, turmas : List[str], nota : float = None) -> None:
        """Construtor da classe CadastroAlunoTurma. Classe para cadastrar os alunos em uma turma.

        Args:
            aluno (str): nome do aluno
            matricula (str): número de matrícula do aluno
            turmas (List[str]): turmas em que o aluno será matriculado
            nota (float, optional): nota do aluno. Defaults to None.
        """
        super().__init__()
        self.aluno = aluno
        self.matricula = matricula
        self.nota = nota
        self.turmas = turmas

    def valida_dados(self) -> bool:
        """Método para validar os dados do aluno.

        Returns:
            bool: retorna True se os dados são válidos. False se são inválidos.
        """
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
        """Método para salvar os dados do aluno no banco de dados.

        Returns:
            bool: retorna True se os dados foram salvos. False se não foram salvos.
        """
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