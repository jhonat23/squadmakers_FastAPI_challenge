from typing import Optional
from pydantic import BaseModel

# Models
class Joke(BaseModel):
    joke_id: Optional[int] = None
    joke: str

# class ChuckFact(BaseModel):
#     icon_url: str
#     joke_id: str
#     url: str
#     value: str