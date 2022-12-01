import pymongo
from pymongo import MongoClient

# creating client
client = MongoClient('mongodb+srv://joosorio:ZeApuBjz04iq4bzi@cluster0.iiho54y.mongodb.net/?retryWrites=true&w=majority')

# Pointing to database and database collection
db = client.squadmakers_db
joke_collection = db.jokes

# Creating unique index for jokes
index = joke_collection.create_index([('joke_id', pymongo.ASCENDING)], unique=True)

# Database operations
def _get_max_id(collection):
    data = collection.find().sort('joke_id', pymongo.DESCENDING)[0]
    return data['joke_id']

def add_joke(joke: dict) -> str:
    joke_index = _get_max_id(joke_collection)
    joke['joke_id'] = joke_index + 1
    result = joke_collection.insert_one(joke).inserted_id
    return result

def update_joke_by_id(id: str, joke: str):
    result = joke_collection.find_one_and_update({'joke_id': id}, {'$set': {'joke': joke}})
    return result

def delete_joke_by_id(id: str):
    result = joke_collection.delete_one({'joke_id': id})
    return result
if __name__ == '__main__':
    res = _get_max_id(joke_collection)
    print(res)

    res1 = update_joke_by_id(2, 'mimimiimim')
    print(res1)

    res2 = delete_joke_by_id(3)
    print(res2)

