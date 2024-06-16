from database import DataBase

class Calendario:
    def __init__(self, nome : str = "Calendario") -> None:
        """Construtor da classe Calendário

        Args:
            nome (str, optional): nome da coleção no banco de dados. Defaults to "Calendario".
        """
        self.nome = nome
        self.db = DataBase()

    def insert_event(self, dict : dict) -> bool:
        """Insere um evento no calendário do banco de dados.

        Args:
            dict (dict): recebe um dicionário com os horarios no formato hh:mm dd/mm/aaaa

        Returns:
            bool: true - evento inserido com sucesso, false - evento não inserido
        """
        if self.db.query_data(self.nome, dict):
            infos = self.db.query_data(self.nome, dict)
            if dict['nome'] == infos[0].get('nome'):
                print("Evento já existente!")
                return False
        
        self.db.insert_data(self.nome, dict)
        print("Evento criado com sucesso!")
        return True
    
    def query_event(self, dict : dict = None) -> list:
        """Pesquisa eventos no calendário escolar

        Args:
            dict (dict, optional): dicionário contendo os critérios de busca no calendário. Defaults to None.

        Returns:
            list: retorna uma lista com os resultados da pesquisa
        """
        infos = []
        if dict:
            infos = self.db.query_data(self.nome, dict)
        else:
            infos = self.db.query_data(self.nome)
        return infos
    
    def update_event(self, dict : dict) -> None:
        """Atualiza um evento no calendário escolar

        Args:
            dict (dict): critérios de busca para atualização do evento
        """
        self.db.update_data(self.nome, dict)

    def delete_event(self, dict : dict) -> None:
        """Deleta um evento do calendário escolar

        Args:
            dict (dict): dicionário com os critérios de busca para exclusão do evento
        """
        self.db.delete_data(self.nome, dict)
