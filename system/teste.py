from cadastro import *
from database import DataBase

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

# Testes

db = DataBase()

"""# Professores
professor1 = CadastroProfessor("Maria", 35, "Rua B, 456", "987654321", "maria@example.com", "maria123", "senha456", "Matemática")
professor1.save()

professor2 = CadastroProfessor("João", 40, "Avenida X, 789", "999888777", "joao@example.com", "joao456", "senha789", "Física")
professor2.save()

professor3 = CadastroProfessor("Ana", 30, "Travessa Y, 123", "111222333", "ana@example.com", "ana789", "senha123", "História")
professor3.save()

professor4 = CadastroProfessor("Pedro", 45, "Rua Z, 321", "777666555", "pedro@example.com", "pedro456", "senha321", "Biologia")
professor4.save()

professor5 = CadastroProfessor("Carla", 38, "Rua W, 654", "333444555", "carla@example.com", "carla123", "senha654", "Geografia")
professor5.save()

# Alunos
aluno1 = CadastroAluno("João", 20, "Rua A, 123", "123456789", "joao@example.com", "joao123", "senha123", "Engenharia", "2021001")
aluno1.save()

aluno2 = CadastroAluno("Maria", 22, "Avenida B, 456", "987654321", "maria@example.com", "maria456", "senha456", "Medicina", "2021002")
aluno2.save()

aluno3 = CadastroAluno("Ana", 21, "Travessa C, 789", "111222333", "ana@example.com", "ana789", "senha789", "Direito", "2021003")
aluno3.save()

aluno4 = CadastroAluno("Pedro", 23, "Rua D, 321", "777666555", "pedro@example.com", "pedro456", "senha321", "Administração", "2021004")
aluno4.save()

aluno5 = CadastroAluno("Carla", 19, "Rua E, 654", "333444555", "carla@example.com", "carla123", "senha654", "Psicologia", "2021005")
aluno5.save()

# Staff
staff1 = CadastroStaff("Carlos", 40, "Rua C, 789", "123987456", "carlos@example.com", "carlos123", "senha789", "Administrador")
staff1.save()

staff2 = CadastroStaff("Mariana", 35, "Avenida D, 456", "987654321", "mariana@example.com", "mariana456", "senha456", "Secretária")
staff2.save()

staff3 = CadastroStaff("Antônio", 38, "Travessa E, 789", "111222333", "antonio@example.com", "antonio789", "senha789", "Técnico de Informática")
staff3.save()

staff4 = CadastroStaff("Luciana", 42, "Rua F, 321", "777666555", "luciana@example.com", "luciana456", "senha321", "Bibliotecária")
staff4.save()

staff5 = CadastroStaff("Fernando", 37, "Rua G, 654", "333444555", "fernando@example.com", "fernando123", "senha654", "Contador")
staff5.save()
"""
# db.delete_data("Professores", {'nome': 'Maria'})

# db.update_data("Alunos", {'nome': 'João'}, {'idade': 21})

print("Informações de todos os Alunos")
info_data_all = db.query_data("Alunos")
print(info_data_all)
print("======================================================")
info_data = db.query_data("Alunos", {"nome": "Maria"})
print(info_data)
