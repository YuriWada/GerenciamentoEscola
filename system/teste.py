from cadastro import *
from database import DataBase
from turmas import Turmas

class TesteCadastro:
    def testar_cadastro(self, tipo : str, nome : str, idade : int, endereco : str, telefone : str, email : str, login : str,
                        senha : str, curso : str = None, matricula : str = None, disciplina : str = None, cargo : str = None) -> None:
        try:
            if tipo == "aluno":
                if curso is None or matricula is None:
                    raise ValueError("Insira curso e matrícula")
                cadastro = CadastroAluno(nome, idade, endereco, telefone, email, login, senha, curso, matricula, self.db)
            elif tipo == "professor":
                if disciplina is None:
                    raise ValueError("Insira disciplina")
                cadastro = CadastroProfessor(nome, idade, endereco, telefone, email, login, senha, disciplina, self.db)
            elif tipo == "staff":
                if cargo is None:
                    raise ValueError("Insira o cargo")
                cadastro = CadastroStaff(nome, idade, endereco, telefone, email, login, senha, cargo, self.db)
            else:
                raise ValueError("Tipo de cadastro inválido. Deve ser 'aluno', 'professor' ou 'staff'!!")
            
            cadastro.save()
            print(f"Cadastro de {tipo} testado com sucesso.")
        except Exception as e:
            print(f"Erro ao testar cadastro de {tipo}: {e}")

"""aluno = CadastroAluno("João", 20, "Rua A, 123", "123456789", "joao@example.com", "joao123", "senha123", "Engenharia", "2021001")
aluno.save()

professor = CadastroProfessor("Maria", 35, "Rua B, 456", "987654321", "maria@example.com", "maria123", "senha456", "Matemática")
professor.save()

staff = CadastroStaff("Carlos", 40, "Rua C, 789", "123987456", "carlos@example.com", "carlos123", "senha789", "Administrador")
staff.save()"""

db = DataBase()
# db.delete_data("Professores", {'nome': 'Maria'})

# db.update_data("Alunos", {'nome': 'João'}, {'idade': 21})

info = db.query_data("Alunos", {'nome': 'João'})
print(info)
