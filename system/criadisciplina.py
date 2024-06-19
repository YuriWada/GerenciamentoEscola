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
        """
        Verifica se uma disciplina já foi cadastrada em um mesmo horário para evitar conflitos.

        Esta função consulta todas as disciplinas cadastradas no banco de dados para verificar se
        alguma delas possui horários de aula idênticos aos da disciplina atual. Se encontrar um
        conflito de horários, imprime uma mensagem informando que a aula já está cadastrada no
        horário indicado e retorna False. Caso contrário, retorna True, indicando que os dados foram validados
        sem conflitos.

        Returns:
            bool: True se os dados foram validados com sucesso (sem conflitos de horário), False se houver conflitos.

        Raises:
            Exception: Se ocorrer algum erro durante a validação dos dados no banco de dados.
                    O erro específico é capturado e impresso na tela.
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
        """
        Salva os dados da Disciplina no banco de dados em duas coleções:

        1. Coleção 'Disciplinas': Contém todas as disciplinas cadastradas, cada uma representada por um documento
        contendo nome da disciplina, horários das aulas, nome do professor responsável e lista de alunos matriculados.

        2. Coleção 'Nome_da_Disciplina': Coleção específica para cada disciplina cadastrada, onde são armazenados os
        detalhes dos alunos matriculados, incluindo suas matrículas e notas.

        Esta função verifica a validação dos dados da disciplina atual usando o método `validacao_dados()`. Se os dados
        forem válidos (sem conflitos de horário com outras disciplinas), insere os dados da disciplina na coleção
        'Disciplinas' e cria uma coleção específica para a disciplina na forma 'Nome_da_Disciplina'. Se ocorrer algum
        erro durante o processo de inserção ou validação, imprime uma mensagem de erro.

        Raises:
            Exception: Se ocorrer algum erro durante o processo de inserção de dados no banco de dados.
                    O erro específico é capturado e impresso na tela.
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