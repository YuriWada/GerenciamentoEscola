from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient

class DataBase:
    def __init__(self) -> None:
        self.envy()
        self.__password = os.environ.get("MONGODB_PWD")
        self.__connection_string = f'mongodb+srv://schoolsystem:{self.__password}@schoolsystem.uxif63l.mongodb.net/?retryWrites=true&w=majority&appName=schoolsystem'
        self.__client = MongoClient(self.__connection_string)
        self.__dbs = self.__client.list_database_names()
        self.__school_system_db = self.__client.SchoolSystem
        self.__collections = self.__school_system_db.list_collection_names()
    
    def envy(self) -> None:
       load_dotenv(find_dotenv())

    def insert_data(self) -> None:
        collection = self.__school_system_db.SchoolSystem
        test_document = {
            "name": "Yuri",
            "type": "Test"
        }
        inserted_id = collection.insert_one(test_document).inserted_id
        print(inserted_id)

    def run(self) -> None:
        collection = self.__school_system_db.SchoolSystem
        query = {"type": "Test"}
        documents = collection.find(query)
        for doc in documents:
            pprint.pprint(doc)