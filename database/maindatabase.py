from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")
connection_string = f'mongodb+srv://schoolsystem:{password}@schoolsystem.uxif63l.mongodb.net/?retryWrites=true&w=majority&appName=schoolsystem'
client = MongoClient(connection_string)

dbs = client.list_database_names()
school_system_db = client.SchoolSystem
collections = school_system_db.list_collection_names()
print(collections)