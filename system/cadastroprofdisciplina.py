from cadastrodisciplina import CadastroDisciplina
from typing import List

class CadastroProfessorDisciplina(CadastroDisciplina):
    def __init__(self, professor : str, disciplinas : List[str] = None) -> None:
        """Construtor da classe CadastroProfessordisciplina. Classe utilizada para
    cadastrar um professor em uma ou várias disciplinas.

        Args:
            professor (str): nome do professor
            disciplinas (List[str], optional): lista de disciplinas em que será cadastrado. Defaults to None.
        """
        super().__init__()
        self.professor = professor
        self.disciplinas = disciplinas

    def valida_dados(self) -> bool:
        """Método utilizado para validar os dados.

        Returns:
            bool: retorna True se os dados são válidos. False se são inválidos.
        """
        for disciplina in self.disciplinas:
            infos = self.db.query_data("Disciplinas", {"nome": disciplina})
            if not infos:
                return False
            for info in infos:
                if info.get('professor'):
                    if self.professor == info.get('professor'):
                        return False
        return True

    def save(self) -> bool:
        """Método para salvar os dados do professor no banco de dados.

        Returns:
            bool: retorna True se os dados foram salvos. False se não foram salvos.
        """
        try:
            if not self.valida_dados():
                return False
            for disciplina in self.disciplinas:
                self.db.update_data("Disciplinas", {"nome": disciplina}, {'$set': {"professor": self.professor}})
                print(f"professor {self.professor} adicionado à disciplina {disciplina} com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao salvar dados do professor: {e}")
            return False