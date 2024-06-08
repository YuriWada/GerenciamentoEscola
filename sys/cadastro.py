"""
    Class Cadastro
    author @YuriWada
"""

import hashlib

class Cadastro:
    def __init__(self, nome : str, idade : int, endereco : str, telefone : str, email : str, login : str, senha : str) -> None:
        self._nome = nome
        self._idade = idade
        self._endereco = endereco
        self._telefone = telefone
        self._email = email
        self._login = login
        self._senha = senha
        self.validar_dados()

    # Validação dos dados
    def _validar_idade(self) -> None:
        if self._idade <= 0:
            raise ValueError("A idade deve ser maior que 0")
        
    def _validar_email(self) -> None:
        if "@" not in self._email or "." not in self._email:
            raise ValueError("E-mail inválido")
    
    def _validar_telefone(self) -> None:
        if not self._telefone.isdigit() or len(self._telefone) < 9:
            raise ValueError("Telefone Inválido")
        
    def _validar_login(self) -> None:
        if not self._login:
            raise ValueError("O campo login deve ser preenchido")
    
    # Método geral de validação
    def validar_dados(self) -> None:
        self._validar_idade()
        self._validar_email()
        self._validar_telefone()
        self._validar_login()

    # Hash para senha
    def _hash_senha(self, senha : str) -> str:
       return hashlib.sha256(senha.encode()).hexdigest()
    
    # Getters
    def _get_nome(self):
        return self._nome
    
    def _get_idade(self):
        return self._idade
    
    def _get_endereco(self):
        return self._endereco
    
    def _get_telefone(self):
        return self._telefone
    
    def _get_email(self):
        return self._email
    
    def _get_login(self):
        return self._login
    
    # Verifica senha
    def _verificar_senha(self, senha : str) -> bool:
        return self._senha == hashlib.sha256(senha.encode()).hexdigest()
    
    def exibir_informacoes(self):
        try:
            self.validar_dados()
        except ValueError as e:
            return f"Erro ao exibir informações: {e}"
        return f"Nome: {self._nome} \nIdade: {self._idade} \nEndereço: {self._endereco} \nTelefone: {self._telefone} \nE-mail: {self._email} \nLogin: {self._login}"
    

# Cadastro do Aluno
class CadastroAluno(Cadastro):
    def __init__(self, nome : str, idade : int, endereco : str, telefone : str, email : str, login : str, senha : str, curso : str, matricula : str) -> None:
        super().__init__(nome, idade, endereco, telefone, email, login, senha)
        self.curso = curso
        self.matricula = matricula

    def exibe_dados(self) -> None:
        info_basica = self.exibir_informacoes()
        print(f"{info_basica} \nCurso: {self.curso} \nMatrícula: {self.matricula}")