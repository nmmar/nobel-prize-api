import db_collections as custom

# Client 
nobelPrizeApi = custom.nobelPrizeApi()
client = nobelPrizeApi.connect_MongoDB()
# Connect to nobel database
db = client.nobel

# Count aggregation
list(db.laureates.aggregate([{'$match': {'birth.place.country.en': 'USA'}},\
    {'$count': 'n_USA-born-laureates'}]))

# How many prizes in total
list(db.laureates.aggregate([{'$project': {'n_prizes':\
    {'$size': '$nobelPrizes.portion'}}},\
        {'$group': {'_id': None, 'n_prizes_total': {'$sum': '$n_prizes'}}}]))


# Laureates by awardyear and category
list(db.nobelPrizes.aggregate([{'$project':\
    {'n_laureates': {'$size': {'$ifNull': ['$laureates.portion', []]}},\
        'awardYear': 1, 'category.en': 1, '_id': 0}}]))

# Laureates by category in descending order
list(db.nobelPrizes.aggregate([{'$project':\
    {'n_laureates': {'$size': {'$ifNull': ['$laureates.portion', []]}},\
        'category.en': 1}}, {'$group': {'_id': '$category.en', 'n_laureates':\
            {'$sum': '$n_laureates'}}}, {'$sort': {'n_laureates': -1}}]))

# Unwind
list(db.nobelPrizes.aggregate([{'$unwind': '$laureates'},\
    {'$group': {'_id': '$category.en', 'n_laureates': {'$sum': 1}}},\
        {'$sort': {'n_laureates': -1}}]))

# Lookup
list(db.nobelPrizes.aggregate([\
    {'$match': {'category.en': 'Literature'}},\
        {'$unwind': '$laureates'},\
            {'$lookup': {'from': 'laureates', 'foreignField': 'id',\
                'localField': 'laureates.id', 'as': 'laureate_bios'}},\
                    {'$unwind': '$laureate_bios'},\
                        {'$group': {'_id': None, 'bornCoutries':\
                            {'$addToSet': '$laureate_bios.birth.place.country.en'}
                            }}]))

db.laureates.distinct('birth.place.country.en',\
    {'nobelPrizes.category.en': 'Literature'})