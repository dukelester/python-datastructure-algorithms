import pymongo

mongoClient = pymongo.MongoClient("mongodb://localhost:27017")

def allDatabases(client):
    all_databases = client.list_database_names()
    return all_databases

all_db = allDatabases(mongoClient)
print(all_db)
#['Todos', 'Users', 'admin', 'bookmarks', 'config', 'customers', 'local', 'pythondb', 'test']

#get collections based on a particular database

def getCollections(client,database):
    my_database = client[database]
    all_my_collections = my_database.list_collection_names()

    return all_my_collections

collections = getCollections(mongoClient, "bookmarks")
print(collections)

collections = getCollections(mongoClient, "pythondb")
print(collections)

#insert document into a collection
def insertOneIntoCollection(client,data, database, collection):
    database = client[database]
    collection = database[collection]
    inserted = collection.insert_one(data)
    return inserted.inserted_id

data = {
    "name":"justione Maina",
    "age": 67,
    "location": "kiambu",
    "party": "independent"
}
insert = insertOneIntoCollection(mongoClient, data, "pythondb", "programs")
print(insert)


#insert multiple data to the  collection

def insertMultiple(client, database, collection, multi_data):
    database = client[database]
    collection = database[collection]
    muilti_inserted = collection.insert_many(multi_data)

    return muilti_inserted


multi_data = [
    {
        "full name": "Peter Kenny", 
        "address": "Lowstreet 27" ,
        "age": 60,
        "gender": "male"
    },
    {
        "full name": "Mercy Kirunda", 
        "address": "Safana 27" ,
        "age": 34,
        "gender": "female"
    },
    {
        "full name": "Kiami Karima", 
        "address": "Korokata 27" ,
        "age": 35,
        "gender": "male"
    },
    {
        "full name": "Kim Modes", 
        "address": "Safari Park 27" ,
        "age": 12,
        "gender": "male"
    },
    { "name": "Amy", "address": "Apple st 652"},
    { "name": "Hannah", "address": "Mountain 21"},
    { "name": "Michael", "address": "Valley 345"},
    { "name": "Sandy", "address": "Ocean blvd 2"},
    { "name": "Betty", "address": "Green Grass 1"},
    { "name": "Richard", "address": "Sky st 331"},
    { "name": "Susan", "address": "One way 98"},
    { "name": "Vicky", "address": "Yellow Garden 2"},
    { "name": "Ben", "address": "Park Lane 38"},
    { "name": "William", "address": "Central st 954"},
    { "name": "Chuck", "address": "Main Road 989"},
    { "name": "Viola", "address": "Sideway 1633"}
]
insert = insertMultiple(mongoClient, "pythondb", "programs2", multi_data)
print(insert.inserted_ids)
#given a database get the records (documents in the database)

