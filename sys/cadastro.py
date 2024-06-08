import hashlib

class Cadastro:
    def __init__(self, nome : str, idade : int, endereco : str, telefone : str, email : str, login : str, senha : str) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__endereco = endereco
        self.__telefone = telefone
        self.__email = email
        self.__login = login
        self.__senha = senha
        self.validar_dados()

    # Validação dos dados
    def __validar_idade(self) -> None:
        if self.__idade <= 0:
            raise ValueError("A idade deve ser maior que 0")
        
    def __validar_email(self) -> None:
        if "@" not in self.__email or "." not in self.__email:
            raise ValueError("E-mail inválido")
    
    def __validar_telefone(self) -> None:
        if not self._telefone.isdigit() or len(self.__telefone) < 9:
            raise ValueError("Telefone Inválido")
        
    def __validar_login(self) -> None:
        if not self.__login:
            raise ValueError("O campo login deve ser preenchido")
    
    # Método geral de validação
    def validar_dados(self) -> None:
        self.__validar_idade()
        self.__validar_email()
        self.__validar_telefone()
        self.__validar_login()

    # Hash para senha
    def __hash_senha(self, senha) -> str:
        return hashlib.sha256(senha.encode()).hexdigest()
    
    # Getters
    def __get_nome(self):
        return self.__nome
    
    def __get_idade(self):
        return self.__idade
    
    def __get_endereco(self):
        return self.__endereco
    
    def __get_telefone(self):
        return self.__telefone
    
    def __get_email(self):
        return self.__email
    
    def __get_login(self):
        return self.__login
    
    # Verifica senha
    def __verificar_senha(self, senha) -> bool:
        return self.__senha == hashlib.sha256(senha.encode()).hexdigest()