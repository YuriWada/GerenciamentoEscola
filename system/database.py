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
        """
        Procura e carrega as variáveis de ambiente de um arquivo .env no projeto.

        Utiliza a função `find_dotenv()` para localizar o arquivo .env no diretório do projeto e
        em seus subdiretórios. Em seguida, carrega as variáveis de ambiente definidas nesse arquivo
        utilizando a função `load_dotenv()`.

        Nota:
            Certifique-se de ter instalado o pacote python-dotenv para usar esta função.

        Raises:
            FileNotFoundError: Se nenhum arquivo .env for encontrado no projeto.
            Exception: Se ocorrer algum erro durante o carregamento das variáveis de ambiente.
                    O erro específico é capturado e impresso na tela.

        """
        load_dotenv(find_dotenv())

    def insert_data(self, collection_name : str, data : dict) -> None:
        """
        Insere um documento na coleção especificada no banco de dados.

        Args:
            collection_name (str): O nome da coleção onde os dados serão inseridos.
            data (dict): Um dicionário contendo os dados a serem inseridos como um documento na coleção.

        Raises:
            errors.PyMongoError: Se ocorrer um erro específico relacionado ao PyMongo durante a inserção.
            Exception: Qualquer outro erro não previsto durante a inserção.

        Example:
            ```
            data = {
                "nome": "João",
                "idade": 25,
                "cidade": "São Paulo"
            }
            obj.insert_data("usuarios", data)
            ```

        Prints:
            "Documento inserido com id: <inserted_id>" se a inserção for bem-sucedida.
            Mensagem de erro se houver algum problema durante a inserção.

        """
        try:
            collection = self.__school_system_db[collection_name]
            inserted_id = collection.insert_one(data).inserted_id
            print(f"Documento inserido com id: {inserted_id}")
        except errors.PyMongoError as e:
            print(f"Erro ao inserir dados no MongoDB: {e}")
        except Exception as e:
            print(f"Erro ao inserir dados: {e}")

    def query_data(self, collection_name : str, query : dict = None) -> list:
        """
        Realiza uma consulta de dados na coleção especificada do banco de dados.

        Args:
            collection_name (str): O nome da coleção onde os dados serão pesquisados.
            query (dict, optional): Um dicionário contendo os critérios de pesquisa. 
                                    Se não fornecido, retorna todos os documentos da coleção. (default: None)

        Returns:
            list: Uma lista contendo os documentos encontrados de acordo com a consulta.

        Raises:
            errors.PyMongoError: Se ocorrer um erro específico relacionado ao PyMongo durante a consulta.
            Exception: Qualquer outro erro não previsto durante a consulta.

        Example:
            ```
            # Consulta todos os documentos na coleção 'usuarios'
            result = obj.query_data("usuarios")

            # Consulta documentos na coleção 'produtos' com um critério específico
            query = {"categoria": "eletrônicos"}
            result = obj.query_data("produtos", query)
            ```
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
        """
        Deleta documentos da coleção especificada no banco de dados.

        Args:
            collection_name (str): O nome da coleção onde os documentos serão deletados.
            search_criteria (dict): Um dicionário contendo os critérios para localizar o documento a ser deletado.

        Raises:
            errors.PyMongoError: Se ocorrer um erro específico relacionado ao PyMongo durante a deleção.
            Exception: Qualquer outro erro não previsto durante a deleção.

        Example:
            ```
            # Deleta um documento na coleção 'alunos' com base no critério de busca
            search_criteria = {"nome": "João"}
            obj.delete_data("alunos", search_criteria)

            # Deleta documentos na coleção 'eventos' com um critério específico
            search_criteria = {"tipo": "reunião"}
            obj.delete_data("eventos", search_criteria)
            ```
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
        """
        Atualiza documentos na coleção especificada no banco de dados.

        Args:
            collection_name (str): O nome da coleção onde os documentos serão atualizados.
            search_criteria (dict): Um dicionário contendo os critérios para localizar o documento a ser atualizado.
            update_operations (dict): Um dicionário contendo as operações de atualização do MongoDB, como {'$set': {...}, '$push': {...}}.

        Raises:
            errors.PyMongoError: Se ocorrer um erro específico relacionado ao PyMongo durante a atualização.
            Exception: Qualquer outro erro não previsto durante a atualização.

        Example:
            ```
            # Atualiza um documento na coleção 'alunos' com base no critério de busca
            search_criteria = {"nome": "João"}
            update_operations = {"$set": {"idade": 25}}
            obj.update_data("alunos", search_criteria, update_operations)

            # Realiza um push de dados em um array na coleção 'disciplinas'
            search_criteria = {"nome": "Matemática"}
            update_operations = {"$push": {"alunos": {"nome": "Maria", "matricula": 12345}}}
            obj.update_data("disciplinas", search_criteria, update_operations)
            ```
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

    def empty_collection(self, collection_name: str) -> None:
        """
        Cria uma coleção vazia no banco de dados se ela ainda não existir.

        Args:
            collection_name (str): O nome da coleção a ser criada.

        Raises:
            errors.PyMongoError: Se ocorrer um erro específico relacionado ao PyMongo durante a criação da coleção.
            Exception: Qualquer outro erro não previsto durante a criação da coleção.

        Example:
            ```
            obj.empty_collection("novos_dados")
            ```
        """
        try:
            if collection_name not in self.__school_system_db.list_collection_names():
                collection = self.__school_system_db[collection_name]
                collection.create_index("fake_index")
                print(f"Coleção '{collection_name}' criada com sucesso.")
            else:
                print(f"Coleção '{collection_name}' já existe.")
        except errors.PyMongoError as e:
            print(f"Erro ao criar nova coleção no Banco de Dados: {e}")
        except Exception as e:
            print(f"Erro ao criar coleção: {e}")
