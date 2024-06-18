from usuario import Usuario
from typing import List

class Professor(Usuario):
    def __init__(self, nome: str, idade: int, endereco: str, telefone: str, email: str, login: str, disciplinas : List[str]) -> None:
        super().__init__(nome, idade, endereco, telefone, email, login)
        self.disciplinas = disciplinas

    def buscar_disciplinas(self) -> list:
        if self.disciplinas:
            return self.disciplinas
        return []
    
    def adicionar_notas(self, turma: str, aluno: str) -> None:
        """Adiciona uma nota para um aluno em uma turma específica

        Args:
            turma (str): Turma em que o aluno está matriculado
            aluno (str): Aluno 
        """
        infos = self.db.query_data(turma, {"nome": aluno})
        if not infos:
            print(f"Aluno {aluno} não encontrado na turma {turma}.")
            return

        for info in infos:
            if info.get('nota') is not None:
                print(f"Já existe uma nota para o aluno {aluno}!")
            else:
                try:
                    nota = float(input(f"Insira a nota de {aluno}: "))
                    if nota < 0 or nota > 100:
                        print("Nota inválida! A nota deve estar entre 0 e 100.")
                        return
                except ValueError:
                    print("Entrada inválida! Tente novamente.")
                    return

                self.db.update_data(turma, {"nome": aluno}, {'$set': {'nota': nota}})
                print(f"Nota {nota} inserida com sucesso para o aluno {aluno}!")
        
        
    def alterar_notas(self, turma: str, aluno: str) -> None:
        """Altera a nota de um aluno em uma turma específica

        Args:
            turma (str): Turma em que o aluno está matriculado
            aluno (str): Aluno
        """
        infos = self.db.query_data(turma, {"nome": aluno})
        if not infos:
            print(f"Aluno {aluno} não encontrado na turma {turma}.")
            return

        for info in infos:
            if info.get('nota') is None:
                print(f"Não há uma nota existente para o aluno {aluno} para ser alterada!")
            else:
                try:
                    nova_nota = float(input(f"Insira a nova nota de {aluno}: "))
                    if nova_nota < 0 or nova_nota > 100: 
                        print("Nota inválida! A nota deve estar entre 0 e 100.")
                        return
                except ValueError:
                    print("Entrada inválida! Tente novamente.")
                    return

                self.db.update_data(turma, {"nome": aluno}, {'$set': {'nota': nova_nota}})
                print(f"Nota alterada com sucesso para {nova_nota} para o aluno {aluno}!")

    def remover_nota(self, turma: str, aluno: str) -> None:
        """Remove a nota de um aluno em uma turma específica.

        Args:
            turma (str): Nome da turma.
            aluno (str): Nome do aluno.
        """
        infos = self.db.query_data(turma, {"nome": aluno})
        if not infos:
            print(f"Aluno {aluno} não encontrado na turma {turma}.")
            return

        for info in infos:
            if info.get('nota') is None:
                print(f"Não há uma nota existente para o aluno {aluno} para ser removida!")
            else:
                self.db.update_data(turma, {"nome": aluno}, {'$unset': {'nota': ""}})
                print(f"Nota removida com sucesso para o aluno {aluno}!")