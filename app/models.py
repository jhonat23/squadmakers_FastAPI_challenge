from pydantic import BaseModel

# Models
class DadJoke(BaseModel):
    id: str
    joke: str

class ChuckFact(BaseModel):
    icon_url: str
    id: str
    url: str
    value: str