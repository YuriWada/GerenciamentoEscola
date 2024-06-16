from database import DataBase
from typing import List

# Cria da Turma
class CriaTurma:
    def __init__(self, nome : str, materia : str, horarios : List[str], professor : str = None, alunos : List[dict] = None) -> None:
        """Construtor da classe CriaTurma

        Args:
            nome (str): nome da turma
            materia (str): materia associada à turma
            horarios (List[str]): lista de horários da turma
            professor (str): nome do professor associado à turma
            alunos (List[dict], optional): lista de alunos matriculados na turma. Defaults to None.
        """
        self.nome = nome
        self.materia = materia
        self.horarios = horarios
        self.professor = professor
        self.alunos = alunos
        self.db = DataBase()
        # self.calendario = Calendario()

    def validacao_dados(self) -> bool:
        """Verifica se uma turma já foi cadastrada em um mesmo horário, para não haver conflitos.

        Returns:
            bool: true - se os dados foram validados com sucesso (não há conflito), false - se não foram validados
        """
        try:
            turmas = self.db.query_data("Turmas")
            lista_horarios = []
            if turmas:
                for turma in turmas:
                    lista_horarios.append(turma["horarios"])
            for horarios in lista_horarios:
                if sorted(self.horarios) == sorted(horarios):
                    print("Aula já cadastrada em horário indicado!")
                    return False
            return True
        except Exception as e:
            print(f"Erro ao validar dados: {e}")

    def save(self) -> None:
        """Salva os dados da turma no banco de dados em duas coleções:
        Turmas: coleção com todas as turmas, indicando para cada turma
        nome, matéria, lista de horarios, profesor e alunos matriculados.
        Turma[digito]: coleção própria para a turma, contendo alunos (com matricula) e notas.
        """
        try:
            if self.validacao_dados():
                data = {
                    "nome": self.nome,
                    "materia": self.materia,
                    "horarios": self.horarios,
                    "professor": self.professor,
                    "alunos": self.alunos
                }
                self.db.insert_data("Turmas", data)
                self.db.empty_collection(self.nome)
                print("Turma cadastrada com sucesso!")
            else:
                print("Turma não cadastrada, tente novamente!")
        except Exception as e:
            print(f"Erro ao cadastrar: {e}")