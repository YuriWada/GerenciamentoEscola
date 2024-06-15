from database import DataBase

class Authentication:
    def __init__(self) -> None:
        self._db = DataBase()

    # Autenticador de login e senha: busca o par de login e senha no banco de dados
    def auth(self, collection : str, query : dict) -> bool:
        if self._db.query_data(collection, query):
            return True
        return False