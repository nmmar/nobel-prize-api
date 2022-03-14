from os import environ as env
from os.path import join, dirname
from dotenv import load_dotenv
from matplotlib import projections
from pymongo import MongoClient

import db_collections

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Client
client = MongoClient(env['MONGODB_CON_STR'])
# Connect to nobel database
db = client.nobel

# Simple filters
db.laureates.count_documents({'gender': 'female'})

# Query operators and projections
db.laureates.count_documents({'birth.place.countryNow.en': {'$in': ['Finland']}})
db.laureates.find_one({'birth.place.countryNow.en': {'$in': ['Finland']}})
docs = db.laureates.find(filter = {'birth.place.countryNow.en': {'$in': ['Finland']}},\
    projection = {'knownName.en': 1, '_id': 0})
list(docs)

# Distinct
db.nobelPrizes.distinct('category')

# Sort
list(db.laureates.find(filter = {'birth.place.countryNow.en': {'$in': ['Finland']}},\
    projection = {'knownName.en': 1, 'nobelPrizes.awardYear': 1,\
        'nobelPrizes.category.en': 1, '_id': 0},\
        sort = [('nobelPrizes.awardYear', 1)]))