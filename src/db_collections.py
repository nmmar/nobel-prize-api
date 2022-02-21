from os import environ as env
from os.path import join, dirname
from dotenv import load_dotenv
import requests
from pymongo import MongoClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

def connectMongoDB():
    # Client connects to "localhost" by default
    client = MongoClient(env['MONGODB_CON_STR'])

    return client

def createNobelDB():

    client = connectMongoDB()
    # Create local "nobel" database on the fly
    db = client["nobel"]
    
    for collection_name in ["nobelPrizes", "laureates"]:
        # collect the data from the API
        response = requests.get("http://api.nobelprize.org/2.1/{}?limit=2000".format(collection_name))
        # convert the data to json
        documents = response.json()[collection_name]
        # Create collections on the fly
        db[collection_name].insert_many(documents)

    return None

