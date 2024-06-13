from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient, errors

class DataBase:
    # Construtor com tratamento de erros para senha, conexão e inicialização do BD
    def __init__(self) -> None:
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

    # Procura o arquivo .env no projeto
    def envy(self) -> None:
        load_dotenv(find_dotenv())

    # Método para inserir dados no banco de dados
    def insert_data(self, data: dict) -> None:
        try:
            collection = self.__school_system_db.SchoolSystem
            inserted_id = collection.insert_one(data).inserted_id
            print(f"Documento inserido com id: {inserted_id}")
        except errors.PyMongoError as e:
            print(f"Erro ao inserir dados no MongoDB: {e}")
        except Exception as e:
            print(f"Erro inesperado ao inserir dados: {e}")

    # Método para fazer consultas no banco de dados
    def query_data(self, collection_name : str, query: dict) -> None:
        try:
            collection = self.__school_system_db[collection_name]
            documents = collection.find(query)
            for doc in documents:
                #imprime os documentos de forma legível
                pprint.pprint(doc)
        except errors.PyMongoError as e:
            print(f"Erro ao consultar dados no MongoDB: {e}")
        except Exception as e:
            print(f"Erro inesperado ao consultar dados: {e}")