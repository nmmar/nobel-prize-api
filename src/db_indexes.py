from os import environ as env
from os.path import join, dirname
from dotenv import load_dotenv
from matplotlib import projections
from pymongo import MongoClient

from timeit import timeit

import db_collections

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Client 
client = MongoClient(env['MONGODB_CON_STR'])
# Connect nobel database 
db = client.nobel

# Limiting
list(db.nobelPrizes.find({"awardYear": "1901"}, limit = 1))

# Create index
db.nobelPrizes.create_index([("awardYear", 1)])

db.laureates.index_information()
db.nobelPrizes.index_information()

for doc in list(db.nobelPrizes.find({"laureates.portion": "1"}, limit = 3)):
    print("{awardYear} {category}".format(**doc))