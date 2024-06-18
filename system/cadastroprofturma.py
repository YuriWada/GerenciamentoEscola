from cadastroturma import CadastroTurma
from typing import List

class CadastroProfessorTurma(CadastroTurma):
    def __init__(self, professor : str, turmas : List[str] = None) -> None:
        """Construtor da classe CadastroProfessorTurma. Classe utilizada para
    cadastrar um professor em uma ou várias turmas.

        Args:
            professor (str): nome do professor
            turmas (List[str], optional): lista de turmas em que será cadastrado. Defaults to None.
        """
        super().__init__()
        self.professor = professor
        self.turmas = turmas

    def valida_dados(self) -> bool:
        """Método utilizado para validar os dados.

        Returns:
            bool: retorna True se os dados são válidos. False se são inválidos.
        """
        for turma in self.turmas:
            infos = self.db.query_data("Turmas", {"nome": turma})
            if not infos:
                return False
            for info in infos:
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
            for turma in self.turmas:
                self.db.update_data("Turmas", {"nome": turma}, {'$set': {"professor": self.professor}})
                print(f"professor {self.professor} adicionado à turma {turma} com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao salvar dados do professor: {e}")
            return False