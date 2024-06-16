from database import DataBase

class Authentication:
    def __init__(self) -> None:
        self._db = DataBase()

    def auth(self, collection_name : str, query : dict) -> bool:
        """Autenticador de login e senha: busca o par de login e senha no banco de dados

        Args:
            collection_name (str): nome da coleção onde estão salvas as informações de login e senha
            query (dict): dicionário com pares login e senha

        Returns:
            bool: true - autenticado com sucesso, false - autenticado sem sucesso
        """
        if self._db.query_data(collection_name, query):
            return True
        return False