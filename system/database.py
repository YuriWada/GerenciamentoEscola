from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient, errors

class DataBase:
    # Construtor com tratamento de erros para senha, conexão e inicialização do BD
    def __init__(self) -> None:
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

    # Procura o arquivo .env no projeto
    def envy(self) -> None:
        load_dotenv(find_dotenv())

    # Método para inserir dados no banco de dados
    def insert_data(self, collection_name : str, data: dict) -> None:
        try:
            collection = self.__school_system_db[collection_name]
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
            documents = list(collection.find(query))
            return documents
        except errors.PyMongoError as e:
            print(f"Erro ao consultar dados no MongoDB: {e}")
        except Exception as e:
            print(f"Erro inesperado ao consultar dados: {e}")

    # Método para deletar um documento
    def delete_data(self, collection_name: str, search_criteria: dict) -> None:
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
            print(f"Erro inesperado ao deletar documento: {e}")

    # Método para atualizar dados do banco de dados
    def update_data(self, collection_name: str, search_criteria: dict, update_fields: dict) -> None:
        try:
            collection = self.__school_system_db[collection_name]
            resultado = collection.update_one(search_criteria, {'$set': update_fields})
            if resultado.modified_count > 0:
                print(f"Alteração realizada com sucesso!")
            else:
                print("Nenhuma informação encontrada!")
        except errors.PyMongoError as e:
            print(f"Erro ao atualizar documento no Banco de Dados: {e}")
        except Exception as e:
            print(f"Erro inesperado ao atualizar documento: {e}")
