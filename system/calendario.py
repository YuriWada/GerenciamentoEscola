from database import DataBase

class Calendario:
    def __init__(self, nome : str = "Calendario") -> None:
        self.nome = nome
        self.db = DataBase()

    # Insere um evento no calendário escolar
    def insert_event(self, dict : dict) -> bool:
        if self.db.query_data("Calendario", dict):
            infos = self.db.query_data("Calendario", dict)
            if dict['nome'] == infos[0]['nome']:
                print("Evento já existente!")
                return False
        
        self.db.insert_data("Calendario", dict)
        print("Evento criado com sucesso!")
        return True
    
    # Pesquisa eventos no calendário escolar
    def query_event(self, dict : dict = None) -> list:
        infos = []
        if dict:
            infos = self.db.query_data("Calendario", dict)
        else:
            infos = self.db.query_data("Calendario")
        return infos
    
    # Atualiza um evento no calendário escolar
    def update_event(self, dict : dict) -> None:
        self.db.update_data("Calendario", dict)

    # Deleta um evento no calendário escolar
    def delete_event(self, dict : dict) -> None:
        self.db.delete_data("Calendario", dict)
