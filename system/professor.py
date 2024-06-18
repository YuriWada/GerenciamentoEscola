from usuario import Usuario
from typing import List

class Professor(Usuario):
    def __init__(self, nome: str, idade: int, endereco: str, telefone: str, email: str, login: str, disciplina : str, turmas : List[str]) -> None:
        super().__init__(nome, idade, endereco, telefone, email, login)
        self.disciplina = disciplina
        self.turmas = turmas
    
    def adicionar_notas(self, turma : str, aluno : str) -> None:
        pass
        """if turma in self.turmas:
            self.db.query_data(turma, {"nome"})"""
        
        
    '''def alterar_notas()'''

      #def enviar notificação de notas