from database import DataBase

class Calendario:
    def __init__(self, nome : str = "Calendario") -> None:
        self.nome = nome
        self.db = DataBase()

    # Insere um evento no calendário escolar
    def insert_event(self, dict : dict) -> bool:
        if self.db.query_data(self.nome, dict):
            infos = self.db.query_data(self.nome, dict)
            if dict['nome'] == infos[0].get('nome'):
                print("Evento já existente!")
                return False
        
        self.db.insert_data(self.nome, dict)
        print("Evento criado com sucesso!")
        return True
    
    # Pesquisa eventos no calendário escolar
    def query_event(self, dict : dict = None) -> list:
        infos = []
        if dict:
            infos = self.db.query_data(self.nome, dict)
        else:
            infos = self.db.query_data(self.nome)
        return infos
    
    # Atualiza um evento no calendário escolar
    def update_event(self, dict : dict) -> None:
        self.db.update_data(self.nome, dict)

    # Deleta um evento no calendário escolar
    def delete_event(self, dict : dict) -> None:
        self.db.delete_data(self.nome, dict)
