from usuario import Usuario
from typing import List

class Professor(Usuario):
    def __init__(self, nome: str, idade: int, endereco: str, telefone: str, email: str, login: str, disciplinas : List[str]) -> None:
        super().__init__(nome, idade, endereco, telefone, email, login)
        self.disciplinas = disciplinas

    def buscar_disciplinas(self) -> list:
        """
        Método que busca as disciplinas nas quais o professor está matriculado.

        Returns:
            list: Retorna a lista de disciplinas nas quais o professor está matriculado.
                Se o professor não estiver matriculado em nenhuma disciplina, retorna uma lista vazia ([]).
        """
        if self.disciplinas:
            return self.disciplinas
        return []
    
    def adicionar_notas(self, turma: str, aluno: str) -> None:
        """
        Adiciona uma nota para um aluno em uma turma específica.

        Args:
            turma (str): Nome da turma em que o aluno está matriculado.
            aluno (str): Nome do aluno para o qual a nota será adicionada.
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
        """
        Altera a nota de um aluno em uma turma específica.

        Args:
            turma (str): Nome da turma em que o aluno está matriculado.
            aluno (str): Nome do aluno cuja nota será alterada.
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
        """
        Remove a nota de um aluno em uma turma específica.

        Args:
            turma (str): Nome da turma em que o aluno está matriculado.
            aluno (str): Nome do aluno cuja nota será removida.
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

    def calcula_aprovados(self, disciplina: str) -> dict:
        """
        Calcula os alunos aprovados e reprovados em uma disciplina.

        Args:
            disciplina (str): Nome da disciplina.

        Returns:
            dict: Dicionário com duas listas de dicionários:
                - 'aprovados': Lista de alunos aprovados na forma {'nome': str, 'nota': float}.
                - 'reprovados': Lista de alunos reprovados na forma {'nome': str, 'nota': float}.
                Ambos os dicionários contêm o nome do aluno e sua nota na disciplina.
        """
        infos = self.db.query_data(disciplina)
        aprovados = []
        reprovados = []

        for info in infos:
            nome = info.get('nome')
            nota = info.get('nota')
            if nota is not None:
                if nota >= 60:
                    aprovados.append({'nome': nome, 'nota': nota})
                else:
                    reprovados.append({'nome': nome, 'nota': nota})

        alunos = {
            'aprovados': aprovados,
            'reprovados': reprovados
        }
        return alunos
    
    def calcula_media_disciplina(self, disciplina: str) -> float:
        """
        Calcula a média de notas de uma determinada disciplina.

        Args:
            disciplina (str): Nome da disciplina.

        Returns:
            float: Média das notas dos alunos na disciplina especificada.
                Retorna -1 se não houver notas registradas para a disciplina.
        """
        infos = self.db.query_data(disciplina)
        notas = [info.get('nota') for info in infos if info.get('nota') is not None]
        
        if not notas:
            print(f"Não há notas registradas para a disciplina {disciplina}.")
            return -1

        media = sum(notas) / len(notas)
        return media
