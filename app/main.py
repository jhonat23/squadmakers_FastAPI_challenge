from fastapi import FastAPI, HTTPException, Body, Path
import requests
import json
from app.database import add_joke, update_joke_by_id, delete_joke_by_id
from app.models import Joke
app = FastAPI()

# Bases url's
joke_url = 'https://icanhazdadjoke.com/'
chuck_url = 'https://api.chucknorris.io/jokes/'

# Root 
@app.get('/squadmakers/api/')
def root():

    res = requests.get(joke_url, headers={'Accept': 'application/json'}).text
    
    return {
            'message':{
                'main message': 'Hi!, this is the FastAPI challenge by squadmakers', 
                'Presented by': 'Jonathan Osorio',
                'Position': 'Python-FastAPI backend developer'
            },
            'random joke':
                json.loads(res)
            }

# GET a joke
@app.get('/squadmakers/api/{chuck_or_joke}')
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
@app.post('/squadmakers/api/new_joke/{joke}')
def post_joke(joke: str = Path(...), my_joke: Joke = Body(...)):
    my_joke.joke = joke
    joke_id_inserted = add_joke(my_joke.dict())
    return {'res': 'success'}
    
# Update a joke with number param
@app.put('/squadmakers/api/update_joke/{id}')
def update_joke(id: int = Path(...), my_joke: Joke = Body(...)):
    new_joke = update_joke_by_id(id, my_joke.joke)
    return {'res': 'success'}

# Delete a joke with number param
@app.delete('/squadmakers/api/delete_joke/{id}')
def delete_joke(id: int = Path(...)):
    result = delete_joke_by_id(id)
    return {'res': 'success'}
