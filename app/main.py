from fastapi import FastAPI, HTTPException
import requests
import json

app = FastAPI()

# Bases url's
joke_url = 'https://icanhazdadjoke.com/'
chuck_url = 'https://api.chucknorris.io/jokes/'

@app.get('/')
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

@app.get('/{chuck_or_joke}')
def get_some_funny_stuff(chuck_or_joke):
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
