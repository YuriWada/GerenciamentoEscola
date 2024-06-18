from usuario import Usuario
from typing import List

class Aluno(Usuario):
    def __init__(self, nome : str, idade : int, endereco : str, telefone: str, email : str, login : str, curso : str, matricula : str, disciplinas_matriculadas : List[str] = None) -> None:
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
            disciplinas_matriculadas (List[str], optional): lista de disciplinas nas quais o aluno está matriculado. Defaults to None.
        """
        super().__init__(nome, idade, endereco, telefone, email, login)
        self.curso = curso
        self.matricula = matricula
        self.disciplinas_matriculadas = disciplinas_matriculadas
        
    def buscar_notas(self) -> list:
        """Método para buscar as notas de cada disciplina do aluno

        Returns:
            list: lista de dicionários com as notas do aluno. {"disciplina", "nota"}
        """
        if not self.disciplinas_matriculadas:
            print(f"O aluno {self.nome} não está matriculado em nenhuma disciplina!")
            return []
        notas = []
        for disciplina in self.disciplinas_matriculadas:
            infos = self.db.query_data(disciplina, {"nome": self.nome})
            if infos:
                valor_nota = infos[0].get('nota', 'Nota não encontrada')
                if valor_nota == None:
                    valor_nota = "Nenhuma nota no sistema"
                nota = {"disciplina": disciplina, "nota": valor_nota}
                notas.append(nota)
            else:
                print(f"Nenhuma informação encontrada para o aluno {self.nome} na disciplina {disciplina}.")
        return notas
    
    def buscar_horarios(self) -> list:
        """Método para buscar os horários de cada disciplina do aluno

        Returns:
            list: lista com os horários das disciplinas
        """
        if not self.disciplinas_matriculadas:
            print(f"O aluno {self.nome} não está matriculado em nenhuma disciplina!")
            return []
        horarios = []
        for disciplina in self.disciplinas_matriculadas:
            infos = self.db.query_data("Disciplinas", {"nome": disciplina})
            if infos:
                horario = {"disciplina": infos[0].get('nome'), "horarios": infos[0].get('horarios', 'Horarios não encontrados')}
                horarios.append(horario)
            else:
                print(f"Nenhuma informação encontrada para o aluno {self.nome} na disciplina {disciplina}.")
        return horarios

    def busca_disciplinas_matriculadas(self) -> list:
        """Método para buscar as disciplinas matriculadas do aluno

        Returns:
            list: disciplinas em que o aluno está matriculado
        """
        return self.disciplinas_matriculadas