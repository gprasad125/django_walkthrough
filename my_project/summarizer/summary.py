import requests
from dotenv import load_dotenv, find_dotenv
import os

# load from .env file
load_dotenv(find_dotenv())

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

# huggingface api key should be from your .env file
headers = {"Authorization": f"Bearer {os.environ.get('huggingface_api_key')}"}


# summarize using the huggingface inference api
def summarize(text):
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()[0]["summary_text"]
