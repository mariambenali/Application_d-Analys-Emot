from pydantic import BaseModel

class Users(BaseModel):
    username : str
    password : str


class PredictionRequest(BaseModel):
    text : str
