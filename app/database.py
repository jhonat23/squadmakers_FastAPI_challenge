from pymongo import MongoClient

client = MongoClient('mongodb+srv://joosorio:ZeApuBjz04iq4bzi@cluster0.iiho54y.mongodb.net/?retryWrites=true&w=majority')

db = client.squadmakers_db
joke_collection = db.jokes

# Database operations
def add_joke(joke: str) -> None:
    result = joke_collection.insert_one({"joke": joke}).inserted_id
    return result

if __name__ == '__main__':

    doc = {
    "id": "tcFBIm3gyd",
    "joke": "What's brown and sticky? A stick.",
    "status": 200
    }

    joke_id = joke_collection.insert_one(doc)
    print(joke_id)
    print(joke_collection.find_one())