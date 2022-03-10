from os import environ as env
from os.path import join, dirname
from dotenv import load_dotenv
from pymongo import MongoClient

import db_collections

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Client connects to "localhost" by default
client = MongoClient(env['MONGODB_CON_STR'])
# Create local "nobel" database on the fly
db = client.nobel

filter = {}
# Count documents in a collection
n_prizes = db.nobelPrizes.count_documents(filter)
n_laureates = db.laureates.count_documents(filter)

# Retrieve sample prize and laureate documents
prize = db.nobelPrizes.find_one()
laureate = db.laureates.find_one()

# Print the sample prize and laureate documents
print(prize)
print(laureate)
print(type(laureate))

# Get the fields present in each type of document
prize_fields = list(prize.keys())
laureate_fields = list(laureate.keys())

print(prize_fields)
print(laureate_fields)