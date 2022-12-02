from fastapi import FastAPI
from app.routes.jokes import jokerouter
from app.routes.maths import mathsrouter
import requests
import json

app = FastAPI()
app.include_router(jokerouter, tags=['Joke'])
app.include_router(mathsrouter, tags=['Maths'])

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