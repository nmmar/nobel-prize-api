import db_collections as custom

# Client 
nobelPrizeApi = custom.nobelPrizeApi()
client = nobelPrizeApi.connect_MongoDB()
# Connect to nobel database
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