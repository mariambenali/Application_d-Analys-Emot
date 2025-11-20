from fastapi import FastAPI,Header,HTTPException
from dotenv import load_dotenv
from pydantic import BaseModel
from jose import jwt
from app.emotion import predict_emotion
from app.config import SECRET_KEY, ALGORITHM

app= FastAPI()
payload={}

class Users(BaseModel):
    username : str
    password : str

data={
    "username" :"mariam",
    "password" :"mariam"
}

@app.post("/login")
def login(db:Users):
    if db.username==data["username"] and db.password==data["password"]:
        payload={"username":db.username}
        token= jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)
        return token
    else:
        return "not working!!!"

    
@app.get("/data")
def get_token(token:str=Header()):
    print("TOKEN RECEIVED RAW:", token) 
    try:
        token=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    except Exception as e:
        print("DECODE ERROR:", e)
        raise HTTPException(status_code=401,detail="this is not ok")
    return token


@app.post("/predict")
def get_emotion(text:str):
    pred=predict_emotion(text)
    label=pred[0][0]["label"]
    score=pred[0][0]["score"]
    if score >= 2:
        var= "negatif"
    elif score == 3:
        var= "neutre"
    else:
        var = "positif"
    
    return {"score":score, "var":var}

