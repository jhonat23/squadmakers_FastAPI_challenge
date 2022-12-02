import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Using env variables
load_dotenv()
database_password = os.getenv('MONGO_URI_PASSWORD')

# creating client
client = MongoClient('mongodb+srv://joosorio:' + database_password + '@cluster0.iiho54y.mongodb.net/?retryWrites=true&w=majority')

# Pointing to database and database collection
db = client.squadmakers_db
joke_collection = db.jokes

# Creating unique index for jokes
index = joke_collection.create_index([('joke_id', pymongo.ASCENDING)], unique=True)

# Database operations
def _get_max_id(collection):

    try:
        data = collection.find().sort('joke_id', pymongo.DESCENDING)[0]
    except IndexError:
        return 0
    else: 
         return data['joke_id']

# Add a new joke
def add_joke(joke: dict) -> str:

    joke_index = _get_max_id(joke_collection)
    joke['joke_id'] = joke_index + 1
    result = joke_collection.insert_one(joke).inserted_id

    return result

# Update a joke by id
def update_joke_by_id(id: str, joke: str):

    result = joke_collection.find_one_and_update({'joke_id': id}, {'$set': {'joke': joke}})

    return result

# Delete joke by id
def delete_joke_by_id(id: str):

    result = joke_collection.delete_one({'joke_id': id})

    return result

# Entry point
if __name__ == '__main__':
    
    res = _get_max_id(joke_collection)
    print(res)

    res1 = update_joke_by_id(2, 'Yesterday a clown held a door open for me. I thought it was a nice jester.')
    print(res1)

    res2 = delete_joke_by_id(3)
    print(res2)

