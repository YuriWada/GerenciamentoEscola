from database import DataBase
from typing import List

# Cria da Disciplina
class CriaDisciplina:
    def __init__(self, nome : str, horarios : List[str], professor : str = None, alunos : List[dict] = []) -> None:
        """Construtor da classe CriaDisciplina

        Args:
            nome (str): nome da Disciplina
            Disciplina (str): Disciplina associada à Disciplina
            horarios (List[str]): lista de horários da Disciplina no formato: dia_da_semana (seg, ter, quart etc.) hh:mm
            professor (str): nome do professor associado à Disciplina
            alunos (List[dict], optional): lista de alunos matriculados na Disciplina. Defaults to None.
        """
        self.nome = nome
        self.horarios = horarios
        self.professor = professor
        self.alunos = alunos
        self.db = DataBase()
        # self.calendario = Calendario()

    def validacao_dados(self) -> bool:
        """Verifica se uma Disciplina já foi cadastrada em um mesmo horário, para não haver conflitos.

        Returns:
            bool: true - se os dados foram validados com sucesso (não há conflito), false - se não foram validados
        """
        try:
            disciplinas = self.db.query_data("Disciplinas")
            lista_horarios = []
            if disciplinas:
                for disciplina in disciplinas:
                    lista_horarios.append(disciplina["horarios"])
            for horarios in lista_horarios:
                if sorted(self.horarios) == sorted(horarios):
                    print("Aula já cadastrada em horário indicado!")
                    return False
            return True
        except Exception as e:
            print(f"Erro ao validar dados: {e}")

    def save(self) -> None:
        """Salva os dados da Disciplina no banco de dados em duas coleções:
        Disciplinas: coleção com todas as Disciplinas, indicando para cada Disciplina
        nome, Disciplina, lista de horarios, profesor e alunos matriculados.
        Disciplina[digito]: coleção própria para a Disciplina, contendo alunos (com matricula) e notas.
        """
        try:
            if self.validacao_dados():
                data = {
                    "nome": self.nome,
                    "horarios": self.horarios,
                    "professor": self.professor,
                    "alunos": self.alunos
                }
                self.db.insert_data("Disciplinas", data)
                self.db.empty_collection(self.nome)
                print("Disciplina cadastrada com sucesso!")
            else:
                print("Disciplina não cadastrada, tente novamente!")
        except Exception as e:
            print(f"Erro ao cadastrar: {e}")