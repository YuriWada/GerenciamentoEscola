from cadastro import *
from database import DataBase

db = DataBase()
    
aluno = CadastroAluno("João", 20, "Rua A, 123", "123456789", "joao@example.com", "joao123", "senha123", "Engenharia", "2021001", db)
aluno.save()

professor = CadastroProfessor("Maria", 35, "Rua B, 456", "987654321", "maria@example.com", "maria123", "senha456", "Matemática", db)
professor.save()

staff = CadastroStaff("Carlos", 40, "Rua C, 789", "123987456", "carlos@example.com", "carlos123", "senha789", "Administrador", db)
staff.save()