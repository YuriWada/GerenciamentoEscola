from database import DataBase
from disciplina import Disciplina
from calendario import Calendario
from cadastroaluno import CadastroAluno
from cadastroprof import CadastroProfessor
from cadastrodiretoria import CadastroDiretoria
from cadastroalunodisciplina import CadastroAlunoDisciplina
from criadisciplina import CriaDisciplina

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
            elif tipo == "diretoria":
                if cargo is None:
                    raise ValueError("Insira o cargo")
                cadastro = CadastroDiretoria(nome, idade, endereco, telefone, email, login, senha, cargo, self.db)
            else:
                raise ValueError("Tipo de cadastro inválido. Deve ser 'aluno', 'professor' ou 'diretoria'!!")
            
            cadastro.save()
            print(f"Cadastro de {tipo} testado com sucesso.")
        except Exception as e:
            print(f"Erro ao testar cadastro de {tipo}: {e}")

# Testes

db = DataBase()

"""# Professores
professor1 = CadastroProfessor("Maria", 35, "Rua B, 456", "987654321", "maria@example.com", "maria123", "senha456", ["Cálculo I", "Álgebra Linear"])
professor1.save()

professor2 = CadastroProfessor("João", 40, "Avenida X, 789", "999888777", "joao@example.com", "joao456", "senha789", ["Física I", "Física II"])
professor2.save()

professor3 = CadastroProfessor("Ana", 30, "Travessa Y, 123", "111222333", "ana@example.com", "ana789", "senha123", ["História do Direito", "Direito Constitucional"])
professor3.save()

professor4 = CadastroProfessor("Pedro", 45, "Rua Z, 321", "777666555", "pedro@example.com", "pedro456", "senha321", ["Biologia Celular", "Genética"])
professor4.save()

professor5 = CadastroProfessor("Carla", 38, "Rua W, 654", "333444555", "carla@example.com", "carla123", "senha654", ["Geografia", "Geologia"])
professor5.save()

professor6 = CadastroProfessor("Lucas", 50, "Rua K, 987", "444555666", "lucas@example.com", "lucas123", "senha987", ["Cálculo II", "Geometria Analítica"])
professor6.save()

professor7 = CadastroProfessor("Fernanda", 33, "Avenida M, 222", "555666777", "fernanda@example.com", "fernanda123", "senha654", ["Anatomia", "Fisiologia"])
professor7.save()

professor8 = CadastroProfessor("Ricardo", 42, "Travessa N, 333", "666777888", "ricardo@example.com", "ricardo456", "senha321", ["Direito Penal", "Direito Civil"])
professor8.save()

professor9 = CadastroProfessor("Patrícia", 37, "Rua O, 444", "777888999", "patricia@example.com", "patricia789", "senha987", ["Bioquímica", "Farmacologia"])
professor9.save()

professor10 = CadastroProfessor("Marcos", 48, "Avenida P, 555", "888999000", "marcos@example.com", "marcos123", "senha456", ["Física II", "Mecânica"])
professor10.save()"""

"""# Alunos
aluno1 = CadastroAluno("João", 20, "Rua A, 123", "123456789", "joao@example.com", "joao123", "senha123", "Engenharia", "2021001", ["Cálculo I", "Física I"])
aluno1.save()

aluno2 = CadastroAluno("Maria", 22, "Avenida B, 456", "987654321", "maria@example.com", "maria456", "senha456", "Medicina", "2021002", ["Biologia Celular", "Anatomia"])
aluno2.save()

aluno3 = CadastroAluno("Ana", 21, "Travessa C, 789", "111222333", "ana@example.com", "ana789", "senha789", "Direito", "2021003", ["História do Direito", "Direito Penal"])
aluno3.save()

aluno4 = CadastroAluno("Pedro", 23, "Rua D, 321", "777666555", "pedro@example.com", "pedro456", "senha321", "Administração", "2021004", ["Geografia", "Geologia"])
aluno4.save()

aluno5 = CadastroAluno("Carla", 19, "Rua E, 654", "333444555", "carla@example.com", "carla123", "senha654", "Psicologia", "2021005", ["Bioquímica", "Fisiologia"])
aluno5.save()

aluno6 = CadastroAluno("Lucas", 24, "Rua F, 987", "444555666", "lucas@example.com", "lucas456", "senha987", "Engenharia", "2021006", ["Cálculo II", "Física II"])
aluno6.save()

aluno7 = CadastroAluno("Fernanda", 22, "Avenida G, 222", "555666777", "fernanda@example.com", "fernanda123", "senha654", "Medicina", "2021007", ["Genética", "Farmacologia"])
aluno7.save()

aluno8 = CadastroAluno("Ricardo", 25, "Travessa H, 333", "666777888", "ricardo@example.com", "ricardo456", "senha321", "Direito", "2021008", ["Direito Constitucional", "Direito Civil"])
aluno8.save()

aluno9 = CadastroAluno("Patrícia", 20, "Rua I, 444", "777888999", "patricia@example.com", "patricia789", "senha987", "Medicina", "2021009", ["Anatomia", "Bioquímica"])
aluno9.save()

aluno10 = CadastroAluno("Marcos", 21, "Avenida J, 555", "888999000", "marcos@example.com", "marcos123", "senha456", "Engenharia", "2021010", ["Mecânica", "Geometria Analítica"])
aluno10.save()"""

"""
# Diretoria
diretoria1 = CadastroDiretoria("Carlos", 40, "Rua C, 789", "123987456", "carlos@example.com", "carlos123", "senha789", "Administrador")
diretoria1.save()

diretoria2 = CadastroDiretoria("Mariana", 35, "Avenida D, 456", "987654321", "mariana@example.com", "mariana456", "senha456", "Secretária")
diretoria2.save()

diretoria3 = CadastroDiretoria("Antônio", 38, "Travessa E, 789", "111222333", "antonio@example.com", "antonio789", "senha789", "Técnico de Informática")
diretoria3.save()

diretoria4 = CadastroDiretoria("Luciana", 42, "Rua F, 321", "777666555", "luciana@example.com", "luciana456", "senha321", "Bibliotecária")
diretoria4.save()

diretoria5 = CadastroDiretoria("Fernando", 37, "Rua G, 654", "333444555", "fernando@example.com", "fernando123", "senha654", "Contador")
diretoria5.save()
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
Disciplina1 = CadastroDisciplina("Disciplina001", "Matemática", horario1, "Maria", alunos)
Disciplina1.save()

# Caso de teste 2
Disciplina2 = CadastroDisciplina("Disciplina002", "Física", horario2, "João", alunos)
Disciplina2.save()

# Caso de teste 3
Disciplina3 = CadastroDisciplina("Disciplina003", "História", horario3, "Ana", alunos)
Disciplina3.save()

# Caso de teste 4
Disciplina4 = CadastroDisciplina("Disciplina004", "Química", horario4, "Pedro", alunos)
Disciplina4.save()

# Caso de teste 5
Disciplina5 = CadastroDisciplina("Disciplina005", "Biologia", horario5, "Carla", alunos)
Disciplina5.save()"""
"""
db.insert_data("Disciplina001", {"nome": "João", "matricula": "2021001", "nota": None})
db.insert_data("Disciplina001", {"nome": "Maria", "matricula": "2021002", "nota": None})
db.insert_data("Disciplina001", {"nome": "Pedro", "matricula": "2021004", "nota": None})"""

"""Disciplina1 = Disciplina("Disciplina001")
for nome in Disciplina1.listagem_alunos():
    print(f"Nome: {nome}")

for horarios in Disciplina1.horarios_Disciplina():
    print(f"Horarios: {horarios}")"""

# cal = Calendario()
"""cal.insert_event({'nome': 'Simulado Geral', 'data': '20/06/2024', 'hora': '10:00'})
cal.insert_event({'nome': 'Reunião de Pais', 'data': '25/06/2024', 'hora': '14:00'})"""
# cal.exibir_calendario_anual()

# Disciplinas dos cursos de Engenharia, Medicina e Direito com seus respectivos horários e professores

"""# Engenharia
disciplina1 = CriaDisciplina(
    nome="Cálculo I",
    horarios=["seg 08:00", "qua 10:00", "sex 14:00"],
)
disciplina1.save()

disciplina2 = CriaDisciplina(
    nome="Física I",
    horarios=["ter 09:00", "qui 11:00", "sex 16:00"],
)
disciplina2.save()

disciplina3 = CriaDisciplina(
    nome="Cálculo II",
    horarios=["seg 10:00", "qua 08:00", "sex 12:00"],
)
disciplina3.save()

disciplina4 = CriaDisciplina(
    nome="Geometria Analítica",
    horarios=["ter 08:00", "qui 10:00", "sex 09:00"],
)
disciplina4.save()

# Medicina
disciplina5 = CriaDisciplina(
    nome="Bioquímica",
    horarios=["seg 09:00", "qua 14:00", "sex 08:00"],
)
disciplina5.save()

disciplina6 = CriaDisciplina(
    nome="Anatomia",
    horarios=["ter 10:00", "qui 12:00", "sex 15:00"],
)
disciplina6.save()

disciplina7 = CriaDisciplina(
    nome="Farmacologia",
    horarios=["seg 13:00", "qua 16:00", "sex 10:00"],
)
disciplina7.save()

disciplina8 = CriaDisciplina(
    nome="Genética",
    horarios=["ter 14:00", "qui 09:00", "sex 13:00"],
)
disciplina8.save()

# Direito
disciplina9 = CriaDisciplina(
    nome="História do Direito",
    horarios=["seg 14:00", "qua 12:00", "sex 15:00"],
)
disciplina9.save()

disciplina10 = CriaDisciplina(
    nome="Direito Penal",
    horarios=["ter 15:00", "qui 11:00", "sex 10:00"],
)
disciplina10.save()

disciplina11 = CriaDisciplina(
    nome="Direito Constitucional",
    horarios=["seg 09:00", "qua 10:00", "sex 14:00"],
)
disciplina11.save()

disciplina12 = CriaDisciplina(
    nome="Direito Civil",
    horarios=["ter 09:00", "qui 13:00", "sex 16:00"],
)
disciplina12.save()"""


"""# Alunos com disciplinas dos cursos de Engenharia, Medicina e Direito
cadastroaluno1 = CadastroAlunoDisciplina("João", "2021001", ["Cálculo I", "Física I"])
cadastroaluno1.save()

cadastroaluno2 = CadastroAlunoDisciplina("Maria", "2021002", ["Biologia Celular", "Anatomia"])
cadastroaluno2.save()

cadastroaluno3 = CadastroAlunoDisciplina("Ana", "2021003", ["História do Direito", "Direito Penal"])
cadastroaluno3.save()

cadastroaluno4 = CadastroAlunoDisciplina("Pedro", "2021004", ["Geografia", "Geologia"])
cadastroaluno4.save()

cadastroaluno5 = CadastroAlunoDisciplina("Carla", "2021005", ["Bioquímica", "Fisiologia"])
cadastroaluno5.save()

cadastroaluno6 = CadastroAlunoDisciplina("Lucas", "2021006", ["Cálculo II", "Física II"])
cadastroaluno6.save()

cadastroaluno7 = CadastroAlunoDisciplina("Fernanda", "2021007", ["Genética", "Farmacologia"])
cadastroaluno7.save()

cadastroaluno8 = CadastroAlunoDisciplina("Ricardo", "2021008", ["Direito Constitucional", "Direito Civil"])
cadastroaluno8.save()

cadastroaluno9 = CadastroAlunoDisciplina("Patrícia", "2021009", ["Anatomia", "Bioquímica"])
cadastroaluno9.save()

cadastroaluno10 = CadastroAlunoDisciplina("Marcos", "2021010", ["Mecânica", "Geometria Analítica"])
cadastroaluno10.save()"""
