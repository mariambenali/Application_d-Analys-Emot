from fastapi import FastAPI,Header,HTTPException
from dotenv import load_dotenv
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
import os
from jose import jwt
import requests
from app.emotion import predict_emotion

app= FastAPI()
ALGORITHM= "HS256"
SECRET_KEY="KJSDNKjbhugiuGIUGvlgUIGUBLJGFUGvbhbjh"
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













'''


API_URL = "https://router.huggingface.co/hf-inference/models/nlptown/bert-base-multilingual-uncased-sentiment"
headers = {"Authorization": f"Bearer {os.environ['HF_TOKEN']}"}

load_dotenv()
#get sercret-key and algorithm from env variable
SECRET_KEY= os.getenv("SECRET_KEY")
ALGORITHM= os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 30



##### Security #####
#hash the password : fct CryptContext() transform pwd to char uncomprehensible, using algo "bcrypt"
pwd_context= CryptContext(schemes=["bcrypt"],deprecated="auto")
#verify the token 
oauth_scheme= OAuth2PasswordBearer(tokenUrl="token")


##### model DB test #####
user={
    "mariben":{
        "username":"mariben",
        "fullname":"mariamben",
        "email":"miriam.bena@gmail.com",
        # this hash for pwd "secret" because i test without using db
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWrn3um3nDnXWbqEOSE.w0r7nCe7w.",
        "disabled": False,
    }
}
##### model pydantic #####
class Token(BaseModel):
    access_token: str
    token_type : str
class User(BaseModel):
    username: str
    email: str
    full_name: str
    
class UserDb(BaseModel):
    hashed_password : str


##### util function #####
def get_user(db, username:str):
    if username in db:
        user_dict=db[username]
        return UserDb(**user_dict)
    return None

#authentification function
def create_access_token(data :dict): #definir function -- attend un dict en input contient Payload du JWT
    to_encode=data.copy() #prepare data (payload)
    expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) #on modifie en ajoutant exprired time
    to_encode.update({})

'''
'''def create_access_token(data: dict,expires_delta:timedelta=None):
    to_encore = data.copy() #to save the original data

    if expires_delta:
        expires = datetime.utcnow()+ expires_delta
    else:
        expires = datetime.utcnow()+timedelta(minutes=30)'''




'''
@app.post("/login")
def login_user(log: LoginRequest):
    return {"username":log.username, "password":log.password}


'''