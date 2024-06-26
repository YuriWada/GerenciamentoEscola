from cadastrodisciplina import CadastroDisciplina
from database import DataBase
from typing import List

class CadastroAlunoDisciplina(CadastroDisciplina):
    def __init__(self, aluno : str, matricula : str, disciplinas : List[str], nota : float = None) -> None:
        """Construtor da classe CadastroAlunodisciplina. Classe para cadastrar os alunos em uma disciplina.

        Args:
            aluno (str): nome do aluno
            matricula (str): número de matrícula do aluno
            disciplinas (List[str]): disciplinas em que o aluno será matriculado
            nota (float, optional): nota do aluno. Defaults to None.
        """
        super().__init__()
        self.aluno = aluno
        self.matricula = matricula
        self.nota = nota
        self.disciplinas = disciplinas
        self.db = DataBase()

    def valida_dados(self) -> bool:
        """
        Método para validar os dados do aluno, verificando se o aluno já está matriculado em alguma disciplina.

        Returns:
            bool: True se os dados são válidos (aluno não está matriculado em nenhuma disciplina), False se são inválidos.
        """
        for disciplina in self.disciplinas:
            infos = self.db.query_data("Disciplinas", {"nome": disciplina})
            if not infos:
                return False
            for info in infos:
                if info.get('alunos'):
                    for aluno in info.get('alunos'):
                        if self.aluno == aluno.get('nome'):
                            return False
        return True

    def save(self) -> bool:
        """
        Método para salvar os dados do aluno no banco de dados, matriculando-o nas disciplinas especificadas.

        Returns:
            bool: True se os dados foram salvos com sucesso, False se ocorrer algum erro durante o processo.
        """
        try:
            if not self.valida_dados():
                print("Não foi possível matricular o aluno na disciplina!")
                return False
            aluno = {"nome": self.aluno, "matricula": self.matricula}
            aluno_com_nota = {"nome": self.aluno, "matricula": self.matricula, "nota": None}
            for disciplina in self.disciplinas:
                try:
                    self.db.update_data("Disciplinas", {"nome": disciplina}, {"$push": {"alunos": aluno}})
                    self.db.update_data("Alunos", {"nome": self.aluno}, {"$push": {"disciplinas_matriculadas": disciplina}})
                except Exception as e:
                    print(f"Erro ao atualizar a disciplina {disciplina} no banco de dados: {e}")
                    return False
                try:
                    self.db.insert_data(disciplina, aluno_com_nota)
                except Exception as e:
                    print(f"Erro ao inserir aluno na disciplina {disciplina}: {e}")
                    return False

            print(f"Aluno {self.aluno} adicionado às disciplinas com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao salvar dados do aluno: {e}")
            return False