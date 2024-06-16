from cadastro import *
from database import DataBase
from turma import Turma
from calendario import Calendario

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
professor1 = CadastroProfessor("Maria", 35, "Rua B, 456", "987654321", "maria@example.com", "maria123", "senha456", "Matemática", ["Turma001"])
professor1.save()

professor2 = CadastroProfessor("João", 40, "Avenida X, 789", "999888777", "joao@example.com", "joao456", "senha789", "Física", ["Turma002"])
professor2.save()

professor3 = CadastroProfessor("Ana", 30, "Travessa Y, 123", "111222333", "ana@example.com", "ana789", "senha123", "História", ["Turma003"])
professor3.save()

professor4 = CadastroProfessor("Pedro", 45, "Rua Z, 321", "777666555", "pedro@example.com", "pedro456", "senha321", "Biologia", ["Turma004"])
professor4.save()

professor5 = CadastroProfessor("Carla", 38, "Rua W, 654", "333444555", "carla@example.com", "carla123", "senha654", "Geografia", ["Turma005"])
professor5.save()

# Alunos
aluno1 = CadastroAluno("João", 20, "Rua A, 123", "123456789", "joao@example.com", "joao123", "senha123", "Engenharia", "2021001", ["Turma001", "Turma002", "Turma003"])
aluno1.save()

aluno2 = CadastroAluno("Maria", 22, "Avenida B, 456", "987654321", "maria@example.com", "maria456", "senha456", "Medicina", "2021002", ["Turma001", "Turma002", "Turma004"])
aluno2.save()

aluno3 = CadastroAluno("Ana", 21, "Travessa C, 789", "111222333", "ana@example.com", "ana789", "senha789", "Direito", "2021003", ["Turma001", "Turma002", "Turma003"])
aluno3.save()

aluno4 = CadastroAluno("Pedro", 23, "Rua D, 321", "777666555", "pedro@example.com", "pedro456", "senha321", "Administração", "2021004", ["Turma001", "Turma002", "Turma005"])
aluno4.save()

aluno5 = CadastroAluno("Carla", 19, "Rua E, 654", "333444555", "carla@example.com", "carla123", "senha654", "Psicologia", "2021005", ["Turma001", "Turma002", "Turma005"])
aluno5.save()"""

"""
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

"""print("Informações de todos os Alunos")
info_data_all = db.query_data("Alunos")
print(info_data_all)
print("======================================================")
info_data = db.query_data("Alunos", {"nome": "Maria"})
print(info_data)"""


# Horários para os casos de teste
horario1 = ["10:30 01/07/2024", "13:45 05/07/2024", "16:00 10/07/2024"]
horario2 = ["09:00 02/07/2024", "14:30 06/07/2024", "17:15 12/07/2024"]
horario3 = ["08:15 03/07/2024", "12:00 07/07/2024", "15:30 13/07/2024"]
horario4 = ["14:00 15/07/2024", "16:30 18/07/2024", "09:45 22/07/2024"]
horario5 = ["11:15 16/07/2024", "13:00 20/07/2024", "10:30 24/07/2024"]

alunos = [
    {"nome": "Maria", "matricula": "2021002"},
    {"nome": "Ana", "matricula": "2021003"},
    {"nome": "Pedro", "matricula": "2021004"},
    {"nome": "Carla", "matricula": "2021005"},
    {"nome": "João", "matricula": "2021001"}
]


"""# Caso de teste 1
turma1 = CadastroTurma("Turma001", "Matemática", horario1, "Maria", alunos)
turma1.save()

# Caso de teste 2
turma2 = CadastroTurma("Turma002", "Física", horario2, "João", alunos)
turma2.save()

# Caso de teste 3
turma3 = CadastroTurma("Turma003", "História", horario3, "Ana", alunos)
turma3.save()

# Caso de teste 4
turma4 = CadastroTurma("Turma004", "Química", horario4, "Pedro", alunos)
turma4.save()

# Caso de teste 5
turma5 = CadastroTurma("Turma005", "Biologia", horario5, "Carla", alunos)
turma5.save()"""
"""
db.insert_data("Turma001", {"nome": "João", "matricula": "2021001", "nota": None})
db.insert_data("Turma001", {"nome": "Maria", "matricula": "2021002", "nota": None})
db.insert_data("Turma001", {"nome": "Pedro", "matricula": "2021004", "nota": None})"""

"""turma1 = Turma("Turma001")
for nome in turma1.listagem_alunos():
    print(f"Nome: {nome}")

for horarios in turma1.horarios_turma():
    print(f"Horarios: {horarios}")"""

cal = Calendario()
"""cal.insert_event({'nome': 'Simulado Geral', 'data': '20/06/2024', 'hora': '10:00'})
cal.insert_event({'nome': 'Reunião de Pais', 'data': '25/06/2024', 'hora': '14:00'})"""
cal.exibir_calendario_anual()
