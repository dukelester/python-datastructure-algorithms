import pymongo

# print(pymongo)

#Creating a Database

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
print(myclient.PORT)
mydatabase = myclient["pythondb"]

all_databases = myclient.list_database_names()
print(all_databases)

# Creating a Collection ==> same as a table in sql
mycollection = mydatabase["programs"]

bookmarks = myclient['bookmarks']
all_collections_bookmarks = bookmarks.list_collection_names()
print(all_collections_bookmarks)

all_collections = mydatabase.list_collection_names()
print(all_collections)

#A document in MongoDB is the same as a record in SQL databases.
#Insert Into Collection

mycollection.insert_one({
    "name": "Kemmy Mercy",
    "occupation":"coder",
    "Location":"Kenya"
})

mycollection.insert_many([{
        "name": "John Mark",
        "occupation":"farmer",
        "Location":"Kenya"
    },{
        "name": "Mary Wambui",
        "occupation":"Shopkeeper",
        "Location":"Uganda"
    },{
        "name": "John Mark",
        "occupation":"farmer",
        "Location":"Kenya"
    },{
        "name": "Kills Mark",
        "occupation":"Software Engineer",
        "Location":"Kenya"
    }])

all_databases = myclient.list_database_names()
print(all_databases)