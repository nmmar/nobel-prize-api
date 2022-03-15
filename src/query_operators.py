import db_collections as custom

# Client 
nobelPrizeApi = custom.nobelPrizeApi()
client = nobelPrizeApi.connect_MongoDB()
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