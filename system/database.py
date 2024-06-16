from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient, errors

class DataBase:
    def __init__(self) -> None:
        """Construtor para configuração do banco de dados

        Raises:
            ValueError: senha não encontrada no arquivo de configurações ambientes (.env)
        """
        # Database setup
        try:
            self.envy()
            self.__password = os.environ.get("MONGODB_PWD")
            if not self.__password:
                raise ValueError("ERRO: A senha do MongoDB não foi encontrada no arquivo .env")
            self.__connection_string = f'mongodb+srv://schoolsystem:{self.__password}@schoolsystem.uxif63l.mongodb.net/?retryWrites=true&w=majority&appName=schoolsystem'
            self.__client = MongoClient(self.__connection_string)
            self.__school_system_db = self.__client.SchoolSystem
        except errors.ConnectionError as e:
            print(f"Erro de conexão com o MongoDB: {e}")
        except Exception as e:
            print(f"Erro ao inicializar o Banco de Dados: {e}")

    def envy(self) -> None:
        """Procura o arquivo .env no projeto
        """
        load_dotenv(find_dotenv())

    def insert_data(self, collection_name : str, data : dict) -> None:
        """Insere dados no banco de dados

        Args:
            collection_name (str): nome da coleção na qual se quer inserir os dados
            data (dict): dados inseridos
        """
        try:
            collection = self.__school_system_db[collection_name]
            inserted_id = collection.insert_one(data).inserted_id
            print(f"Documento inserido com id: {inserted_id}")
        except errors.PyMongoError as e:
            print(f"Erro ao inserir dados no MongoDB: {e}")
        except Exception as e:
            print(f"Erro ao inserir dados: {e}")

    def query_data(self, collection_name : str, query : dict = None) -> dict:
        """Faz pesquisa de dados no banco de dados

        Args:
            collection_name (str): nome da coleção na qual se quer pesquisar
            query (dict, optional): dados pesquisados. Defaults to None.

        Returns:
            dict: uma lista com os dados encontrados
        """
        try:
            collection = self.__school_system_db[collection_name]
            if query:
                documents = list(collection.find(query))
            else:
                documents = list(collection.find())
            return documents
        except errors.PyMongoError as e:
            print(f"Erro ao consultar dados no MongoDB: {e}")
        except Exception as e:
            print(f"Erro ao consultar dados: {e}")

    def delete_data(self, collection_name : str, search_criteria : dict) -> None:
        """Método para deletar informações do banco de dados

        Args:
            collection_name (str): nome da coleção na qual se quer deletar
            search_criteria (dict): critérios de buscar para deletar as informações
        """
        try:
            collection = self.__school_system_db[collection_name]
            document = collection.find_one(search_criteria)
            if document:
                document_id = document['_id']
                filtro = {'_id': document_id}
                resultado = collection.delete_one(filtro)
                if resultado.deleted_count == 1:
                    print(f"Documento com id {document_id} deletado com sucesso!")
                else:
                    print("Nenhuma informação foi deletada!")
            else:
                print("Nenhum documento encontrado para os critérios de busca fornecidos.")
        except errors.PyMongoError as e:
            print(f"Erro ao deletar documento no Banco de Dados: {e}")
        except Exception as e:
            print(f"Erro ao deletar documento: {e}")

    def update_data(self, collection_name : str, search_criteria : dict, update_operations : dict) -> None:
        """Método para atualizar informações no banco de dados

        Args:
            collection_name (str): nome da coleção na qual se quer editar
            search_criteria (dict): critérios de busca
            update_operations (dict): operações de atualização do MongoDB (ex: {'$set': {...}, '$push': {...}})
        """
        try:
            collection = self.__school_system_db[collection_name]
            resultado = collection.update_one(search_criteria, update_operations)
            if resultado.modified_count > 0:
                print("Alteração realizada com sucesso!")
            else:
                print("Nenhuma informação encontrada!")
        except errors.PyMongoError as e:
            print(f"Erro ao atualizar documento no Banco de Dados: {e}")
        except Exception as e:
            print(f"Erro ao atualizar documento: {e}")

    def empty_collection(self, collection_name : str) -> None:
        """Cria uma coleção vazia no banco de dados

        Args:
            collection_name (str): nome da coleção nova
        """
        try:
            collection = self.__school_system_db[collection_name]
            collection.create_index("fake_index")
        except errors.PyMongoError as e:
            print(f"Erro ao criar nova coleção no Banco de Dados: {e}")
        except Exception as e:
            print(f"Erro ao criar coleção: {e}")
