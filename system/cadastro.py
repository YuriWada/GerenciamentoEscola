"""
    Class Cadastro
    author @YuriWada
"""

import hashlib
from abc import ABC, abstractmethod

class Cadastro(ABC):
    def __init__(self, nome : str, idade : int, endereco : str, telefone : str, email : str, login : str) -> None:
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self._login = login
        self.validar_dados()

    # Validação dos dados
    def validar_idade(self) -> None:
        if self.idade <= 0:
            raise ValueError("A idade deve ser maior que 0")
        
    def validar_email(self) -> None:
        if "@" not in self.email or "." not in self.email:
            raise ValueError("E-mail inválido")
    
    def validar_telefone(self) -> None:
        if not self.telefone.isdigit() or len(self.telefone) < 9:
            raise ValueError("Telefone Inválido")
        
    def _validar_login(self) -> None:
        if not self._login:
            raise ValueError("O campo login deve ser preenchido")
    
    # Método geral de validação
    def validar_dados(self) -> None:
        self.validar_idade()
        self.validar_email()
        self.validar_telefone()
        self._validar_login()
    
    # Getters
    def get_nome(self) -> str:
        return self.nome
    
    def get_idade(self) -> int:
        return self.idade
    
    def get_endereco(self) -> str:
        return self.endereco
    
    def get_telefone(self) -> str:
        return self.telefone
    
    def get_email(self) -> str:
        return self.email
    
    def _get_login(self) -> str:
        return self._login
    
    @abstractmethod
    def _verificar_senha(self, senha : str) -> bool:
        pass
    
    @abstractmethod
    def exibir_informacoes(self) -> None:
        pass
    

# Cadastro do Aluno
class CadastroAluno(Cadastro):
    def __init__(self, nome : str, idade : int, endereco : str, telefone : str, email : str, login : str, senha : str, curso : str, matricula : str) -> None:
        super().__init__(nome, idade, endereco, telefone, email, login)
        self.curso = curso
        self.matricula = matricula
        self.__senha = senha

    ## Implementar no banco de dados
    # Hash para senha
    def _hash_senha(self, senha : str) -> str:
       return hashlib.sha256(senha.encode()).hexdigest()
    
    def _verificar_senha(self, senha : str) -> bool:
        return self.__senha == hashlib.sha256(senha.encode()).hexdigest()
