import os
import pymongo
from dotenv import load_dotenv

load_dotenv()

def get_db():
    client = pymongo.MongoClient(os.getenv("MONGO_URI"))
    return client["lab_page"]

def insert_data(collection, data):
    db = get_db()
    db[collection].insert_one(data)

def get_all(collection):
    db = get_db()
    return list(db[collection].find({}))
