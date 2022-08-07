import pymongo

mongoClient = pymongo.MongoClient("mongodb://localhost:27017")

def findOneEntry(client, database, collection):
    database = client[database]
    collection = database[collection]

    return collection.find_one()


found = findOneEntry(mongoClient, "pythondb", "programs")
print(found)

#find many

def findManyEntries(client, database, collection):
    database = client[database]
    collection = database[collection]
    all_data = list(collection.find())
    return all_data

collection = "programs"
found_many = findManyEntries(mongoClient, "pythondb", collection)
print(found_many)

collection = "programs2"
database = "pythondb"
client = mongoClient
found_programs = findManyEntries(client, database, collection)
print(found_programs)
print("\n\n")

#pass a query string

def findEntriesQueries(client, database, collection, query):
    database = client[database]
    collection = database[collection]
    all_data = list(collection.find(query))
    return all_data

my_query = {"address": 'Central st 954'}

find_programs = findEntriesQueries(client, database, collection, my_query)
print(find_programs)
my_query = {"full name":"duke lester"}
my_query = {"gender":"female"}
find_programs = findEntriesQueries(client, database, collection, my_query)
print(find_programs)

# Find documents where the address starts with the letter "S" or higher:
my_q = {"address": { "$gt": "S"}}
my_q = {"full name": { "$gt": "D"}}
find_programs = findEntriesQueries(client, database, collection, my_q)
print(find_programs)

# Filter With Regular Expressions

my_q_ = { "address": {"$regex": "^S"}}
find_programs = findEntriesQueries(client, database, collection, my_q_)
print(find_programs)

#Sort the Result
def sortedEntriesQueries(client, database, collection, query, sort_by):
    database = client[database]
    collection = database[collection]
    all_data = list(collection.find(query).sort(sort_by))
    return all_data

sort_by = "address"
sorted_ = sortedEntriesQueries(client, database, collection, my_q_,sort_by)
print(sorted_, '\n\n')

sort_by = "name"
sorted_ = sortedEntriesQueries(client, database, collection, my_q_,sort_by)
print(sorted_)

sort_by = "_id"
sorted_ = sortedEntriesQueries(client, database, collection, my_q_,sort_by)
print(sorted_, '\n\n')

#limit the results

def sortedLimitEntriesQueries(client, database, collection, query, sort_by, limit):
    database = client[database]
    collection = database[collection]
    all_data = list(collection.find(query).sort(sort_by).limit(limit))
    return all_data

sort_by = "_id"
limit = 5
sorted_limited = sortedLimitEntriesQueries(client, database, collection, my_q_,sort_by, limit)
print(sorted_limited)

#delete document 

# x = mycol.delete_many({})  ==> delete all
# mycol.delete_many(myquery) ==> deletes many using a query
#mycol.delete_one(myquery  ++ deletes one document based on the query


#delete collection
#mycol.drop() ==> delete a collection