from usuario import Usuario
from typing import List

class Aluno(Usuario):
    def __init__(self, nome : str, idade : int, endereco : str, telefone: str, email : str, login : str, curso : str, matricula : str, turmas_matriculadas : List[str] = None) -> None:
        """Construtor da classe Aluno

        Args:
            nome (str): nome do aluno
            idade (int): idade do aluno
            endereco (str): endereço do aluno
            telefone (str): telefone do aluno
            email (str): email do aluno
            login (str): login utilizado para logar no sistema
            curso (str): curso em que o aluno está matriculado
            matricula (str): matrícula do aluno
            turmas_matriculadas (List[str], optional): lista de turmas nas quais o aluno está matriculado. Defaults to None.
        """
        super().__init__(nome, idade, endereco, telefone, email, login)
        self.curso = curso
        self.matricula = matricula
        self.turmas_matriculadas = turmas_matriculadas
        
    def buscar_notas(self) -> list:
        """Método para buscar as notas de cada turma do aluno

        Returns:
            list: lista de dicionários com as notas do aluno. {"Turma", "nota"}
        """
        if not self.turmas_matriculadas:
            print(f"O aluno {self.nome} não está matriculado em nenhuma turma!")
            return []
        notas = []
        for turma in self.turmas_matriculadas:
            infos = self.db.query_data(turma, {"nome": self.nome})
            if infos:
                nota = {"turma": turma, "nota": infos[0].get('nota', 'Nota não encontrada')}
                notas.append(nota)
            else:
                print(f"Nenhuma informação encontrada para o aluno {self.nome} na turma {turma}.")
        return notas
    
    def buscar_horarios(self) -> list:
        """Método para buscar os horários de cada turma do aluno

        Returns:
            list: lista com os horários das turmas
        """
        if not self.turmas_matriculadas:
            print(f"O aluno {self.nome} não está matriculado em nenhuma turma!")
            return []
        horarios = []
        for turma in self.turmas_matriculadas:
            infos = self.db.query_data("Turmas", {"nome": self.nome})
            if infos:
                horario = {"turma": infos[0].get('nome'), "horarios": infos[0].get('horarios', 'Horarios não encontrados')}
                horarios.append(horario)
            else:
                print(f"Nenhuma informação encontrada para o aluno {self.nome} na turma {turma}.")
        return horarios

    def busca_turmas_matriculadas(self) -> list:
        """Método para buscar as turmas matriculadas do aluno

        Returns:
            list: turmas em que o aluno está matriculado
        """
        return self.turmas_matriculadas