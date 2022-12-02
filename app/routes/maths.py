from typing import List
from fastapi import APIRouter, Query

from app.utils.calcs import mcm, give_one

mathsrouter = APIRouter()

@mathsrouter.get('/squadmakers/api/maths/mcm')
def find_mcm(numbers: List[int] = Query(...)):
    #data = str_to_int_list(numbers)
    result = mcm(numbers)
    return {
        'Data entry': numbers,
        'Minimun common multiple': str(result)
        }

@mathsrouter.get('/squadmakers/api/maths/plus_one')
def plus_one(number: int = Query(...)):
    result = give_one(number)
    return {
        'Result': result
        }