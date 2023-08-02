import openai
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

openai.api_key = os.environ.get("api_key")


def summarize(text):
    # create prompt
    prompt = "Write a concise summary of the following content: \n"
    prompt += text

    # ping model and generate response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )

    return response.choices[0].message.content
