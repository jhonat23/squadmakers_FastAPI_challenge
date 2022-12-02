from fastapi import APIRouter, HTTPException, Path, Body
from app.database import add_joke, update_joke_by_id, delete_joke_by_id
from app.models import Joke
import requests
import json

# Bases url's
joke_url = 'https://icanhazdadjoke.com/'
chuck_url = 'https://api.chucknorris.io/jokes/'

jokerouter = APIRouter()

# GET a joke
@jokerouter.get('/squadmakers/api/joke/{chuck_or_joke}')
def get_some_funny_stuff(chuck_or_joke: str = Path(...)):
    
    url = 'http://'
    if chuck_or_joke == 'Chuck':
        url = chuck_url + 'random'
    elif chuck_or_joke == 'Dad':
        url = joke_url
    else:
        raise HTTPException(404, detail={
            "error": 'Not found', 
            "code": 404, 
            "message": 'data not found, please try again'
            })

    res = requests.get(url, headers={'Accept': 'application/json'}).text

    return json.loads(res)

# Post a joke in mongodb database
@jokerouter.post('/squadmakers/api/joke/new_joke/{joke}')
def post_joke(joke: str = Path(...), my_joke: Joke = Body(...)):

    my_joke.joke = joke
    joke_id_inserted = add_joke(my_joke.dict())

    return {'Result': 'Joke posted! :D'}
    
# Update a joke with number param
@jokerouter.put('/squadmakers/api/joke/update_joke/{id}/{joke}')
def update_joke(id: int = Path(...), my_joke: Joke = Body(...)):

    my_joke.joke_id = id
    new_joke = update_joke_by_id(id, my_joke.joke)

    return {'Result': 'Joke updated! :D'}

# Delete a joke with number param
@jokerouter.delete('/squadmakers/api/joke/delete_joke/{id}')
def delete_joke(id: int = Path(...)):

    result = delete_joke_by_id(id)

    return {'Result': 'Joke deleted! D:'}