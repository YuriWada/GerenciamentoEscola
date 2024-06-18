from cadastrodisciplina import CadastroDisciplina
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

    def valida_dados(self) -> bool:
        """Método para validar os dados do aluno.

        Returns:
            bool: retorna True se os dados são válidos. False se são inválidos.
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
        """Método para salvar os dados do aluno no banco de dados.

        Returns:
            bool: retorna True se os dados foram salvos. False se não foram salvos.
        """
        try:
            if not self.valida_dados():
                return False

            aluno = {"nome": self.aluno, "matricula": self.matricula}
            aluno_com_nota = {"nome": self.aluno, "matricula": self.matricula, "nota": None}

            for disciplina in self.disciplinas:
                try:
                    infos = self.db.query_data("Disciplinas", {"nome": disciplina})
                    if infos[0].get('alunos'):
                        self.db.update_data("Disciplinas", {"nome": disciplina}, {"$push": {"alunos": aluno}})
                    else:
                        self.db.update_data("Disciplinas", {"nome": disciplina}, {"$set": {"alunos": aluno}})
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