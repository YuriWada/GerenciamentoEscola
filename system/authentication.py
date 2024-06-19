from database import DataBase

class Authentication:
    def __init__(self) -> None:
        """
        Inicializa a classe e cria uma instância da classe DataBase para manipulação de dados.
        """
        self._db = DataBase()

    def auth(self, collection_name : str, query : dict) -> bool:
        """
        Autenticador de login e senha: busca o par de login e senha no banco de dados.

        Args:
            collection_name (str): Nome da coleção onde estão salvas as informações de login e senha.
            query (dict): Dicionário com pares login e senha.

        Returns:
            bool: True se autenticado com sucesso, False se não autenticado com sucesso.
        """
        if self._db.query_data(collection_name, query):
            return True
        return False