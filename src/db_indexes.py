from os import environ as env
from os.path import join, dirname
from dotenv import load_dotenv
from matplotlib import projections
from pymongo import MongoClient

import db_collections

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Client connects to "localhost" by default
client = MongoClient(env['MONGODB_CON_STR'])
# Create local "nobel" database on the fly
db = client.nobel