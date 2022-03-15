import db_collections as custom

# Client 
nobelPrizeApi = custom.nobelPrizeApi()
client = nobelPrizeApi.connect_MongoDB()
# Connect to nobel database
db = client.nobel

# Limiting
list(db.nobelPrizes.find({"awardYear": "1901"}, limit = 1))

# Create index
db.nobelPrizes.create_index([("awardYear", 1)])

db.laureates.index_information()
db.nobelPrizes.index_information()

for doc in list(db.nobelPrizes.find({"laureates.portion": "1"}, limit = 3)):
    print("{awardYear} {category}".format(**doc))