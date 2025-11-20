import os
import requests
from dotenv import load_dotenv


load_dotenv()
HF_TOKEN=os.getenv("HF_TOKEN")
print(HF_TOKEN)

def predict_emotion(text):
    
    API_URL = "https://router.huggingface.co/hf-inference/models/nlptown/bert-base-multilingual-uncased-sentiment"
    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
    }

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    output = query({
        "inputs": text,
    })
    return output