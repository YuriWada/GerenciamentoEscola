import calendar
from datetime import datetime
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
        """
        Insere um evento no calendário do banco de dados.

        Args:
            dict (dict): Dicionário contendo informações do evento com as chaves 'nome', 'horarios' e 'data'.

        Returns:
            bool: True se o evento foi inserido com sucesso, False se o evento já existe ou ocorrer algum erro.
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
        """
        Pesquisa eventos no calendário escolar.

        Args:
            dict (dict, optional): Dicionário contendo os critérios de busca no calendário. 
                Defaults to None.

        Returns:
            list: Lista com os resultados da pesquisa. Retorna uma lista vazia se nenhum evento for encontrado.
        """
        infos = []
        if dict:
            infos = self.db.query_data(self.nome, dict)
        else:
            infos = self.db.query_data(self.nome)
        return infos
    
    def update_event(self, search_criteria : dict, dict : dict) -> None:
        """
        Atualiza um evento no calendário.

        Args:
            search_criteria (dict): Critérios de busca para encontrar o evento que se quer alterar.
            dict (dict): Campos atualizados do evento a serem aplicados.

        Returns:
            None
        """
        self.db.update_data(self.nome, search_criteria, {'$set': dict})

    def delete_event(self, dict : dict) -> None:
        """Deleta um evento do calendário escolar

        Args:
            dict (dict): dicionário com os critérios de busca para exclusão do evento
        """
        self.db.delete_data(self.nome, dict)
        print(f"> Evento {dict} apagado com sucesso!")

    def exibir_calendario(self) -> None:
        """
        Exibe o calendário do mês atual com eventos registrados.

        Retorna:
            None
        """
        now = datetime.now()
        ano = now.year
        mes = now.month
        cal = calendar.TextCalendar(calendar.SUNDAY)
        cal_str = cal.formatmonth(ano, mes)
        print(cal_str)
        eventos = self.query_event()
        eventos_do_mes = [evento for evento in eventos if datetime.strptime(evento['data'], '%d/%m/%Y').month == mes and datetime.strptime(evento['data'], '%d/%m/%Y').year == ano]
        if eventos_do_mes:
            print("\nEventos Registrados:")
            for evento in sorted(eventos_do_mes, key=lambda e: datetime.strptime(f"{e['data']} {e.get('horario', '00:00')}", '%d/%m/%Y %H:%M')):
                print(f"{evento['data']} {evento.get('horario', '00:00')}: {evento['nome']}")
        else:
            print("\nNenhum evento registrado para este mês.")
    
    def exibir_calendario_anual(self) -> None:
        """
        Exibe o calendário anual com eventos registrados.

        Retorna:
            None
        """
        now = datetime.now()
        ano = now.year
        cal = calendar.TextCalendar(calendar.SUNDAY)
        eventos = self.query_event()
        for mes in range(1, 13):
            cal_str = cal.formatmonth(ano, mes)
            print(cal_str)
            eventos_do_mes = [evento for evento in eventos if datetime.strptime(evento['data'], '%d/%m/%Y').month == mes and datetime.strptime(evento['data'], '%d/%m/%Y').year == ano]
            if eventos_do_mes:
                print("\nEventos Registrados:")
                for evento in sorted(eventos_do_mes, key=lambda e: datetime.strptime(f"{e['data']} {e['horario']}", '%d/%m/%Y %H:%M')):
                    print(f"{evento['data']} {evento['horario']}: {evento['nome']}")
            else:
                print("Nenhum evento registrado para este mês.")
            print("\n" + "="*40 + "\n")

    def inserir_evento_calendario(self) -> None:
        """
        Método para inserir um evento no calendário.

        O método solicita ao usuário o nome, horário e data do evento. Verifica se o formato do horário
        (hh:mm) e da data (dd/mm/aaaa) estão corretos antes de inserir o evento no banco de dados.

        Raises:
            ValueError: Se o formato do horário ou da data inseridos pelo usuário estiverem incorretos.

        Returns:
            None
        """
        try:
            nome = input("> Insira o nome do evento: ")
            horario = input("> Insira o horário do evento (hh:mm): ")
            data = input("> Insira a data do evento (dd/mm/aaaa): ")
            
            try:
                datetime.strptime(horario, '%H:%M')
            except ValueError:
                print("Formato de horário inválido. Use hh:mm.")
                return
            
            try:
                datetime.strptime(data, '%d/%m/%Y')
            except ValueError:
                print("Formato de data inválido. Use dd/mm/aaaa.")
                return
            
            evento_dict = {'nome': nome, 'horario': horario, 'data': data}
            self.insert_event(evento_dict)
            print("Evento inserido com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir evento no calendário: {e}")

    def modificar_evento_calendario(self) -> None:
        """
        Método para modificar um evento existente no calendário.

        O método leva o usuário por alguns de prompts a buscar o evento a ser modificado,
        especificando nome, horário e data. Ele valida os formatos de horário (hh:mm) e data (dd/mm/aaaa)
        inseridos pelo usuário antes de atualizar o evento no calendário.

        Raises:
            ValueError: Se o formato do horário ou da data inseridos pelo usuário estiverem incorretos.

        Returns:
            None
        """
        try:
            nome = input("> Insira o nome do evento que quer alterar: ")

            eventos_encontrados = self.query_event({'nome': nome})
            if not eventos_encontrados:
                print("Evento não encontrado!")
                return
            else:
                for evento in eventos_encontrados:
                    print(f"{evento}")

            horario = input("> Insira o horário do evento (hh:mm) que quer alterar: ")
            try:
                datetime.strptime(horario, '%H:%M')
            except ValueError:
                print("Formato de horário inválido. Use hh:mm.")
                return

            data = input("> Insira a data do evento (dd/mm/aaaa) que quer alterar: ")
            try:
                datetime.strptime(data, '%d/%m/%Y')
            except ValueError:
                print("Formato de data inválido. Use dd/mm/aaaa.")
                return

            filtro_dict = {'nome': nome, 'horario': horario, 'data': data}

            eventos_encontrados = self.query_event(filtro_dict)
            if not eventos_encontrados:
                print("Evento com os critérios especificados não encontrado!")
                return

            nome_novo = input("> Insira o novo nome para o evento: ")
            horario_novo = input("> Insira o novo horário do evento (hh:mm): ")
            try:
                datetime.strptime(horario_novo, '%H:%M')
            except ValueError:
                print("Formato de horário novo inválido. Use hh:mm.")
                return

            data_novo = input("> Insira a nova data do evento (dd/mm/aaaa): ")
            try:
                datetime.strptime(data_novo, '%d/%m/%Y')
            except ValueError:
                print("Formato de data nova inválido. Use dd/mm/aaaa.")
                return

            novo_dict = {'nome': nome_novo, 'horario': horario_novo, 'data': data_novo}

            self.update_event(filtro_dict, novo_dict)
            print("Evento modificado com sucesso!")
        except Exception as e:
            print(f"Erro ao modificar evento no calendário: {e}")

    def apagar_evento_calendario(self) -> None:
        """
        Método para apagar um evento existente no calendário.

        Este método busca o evento a ser apagado, especificando nome, horário e data. 
        Ele valida os formatos de horário (hh:mm) e data (dd/mm/aaaa) inseridos pelo usuário 
        antes de remover o evento do calendário.

        Raises:
            ValueError: Se o formato do horário ou da data inseridos pelo usuário estiverem incorretos.

        Returns:
            None
        """
        try:
            nome = input("> Insira o nome do evento que quer apagar: ")

            eventos_encontrados = self.query_event({'nome': nome})
            if not eventos_encontrados:
                print("Evento não encontrado!")
                return
            else:
                for evento in eventos_encontrados:
                    print(f"{evento}")

            horario = input("> Insira o horário do evento (hh:mm) que quer apagar: ")
            try:
                datetime.strptime(horario, '%H:%M')
            except ValueError:
                print("Formato de horário inválido. Use hh:mm.")
                return

            data = input("> Insira a data do evento (dd/mm/aaaa) que quer apagar: ")
            try:
                datetime.strptime(data, '%d/%m/%Y')
            except ValueError:
                print("Formato de data inválido. Use dd/mm/aaaa.")
                return

            filtro_dict = {'nome': nome, 'horario': horario, 'data': data}

            eventos_encontrados = self.query_event(filtro_dict)
            if not eventos_encontrados:
                print("Evento com os critérios especificados não encontrado!")
                return

            self.delete_event(filtro_dict)
            print("Evento apagado com sucesso!")
        except Exception as e:
            print(f"Erro ao apagar evento no calendário: {e}")
