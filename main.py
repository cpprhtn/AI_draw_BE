from flask import Flask
from flask import request, send_file
from flask_cors import CORS
# from openai import OpenAI
import openai
import os

import requests
from io import BytesIO

app = Flask(__name__)
CORS(app)

API_KEY= os.getenv("API_KEY")

client = openai

@app.route("/api/text", methods=["POST"])
def ImageMaker(API_KEY=API_KEY):    
    input = request.get_json()
    
    text = input["text"]
    openai.api_key = API_KEY

    response = client.images.generate(
    model="dall-e-3",
    prompt=text,
    size="1024x1024",
    quality="standard",
    n=1,
    )
    
    image_url = response.data[0].url

    image = requests.get(image_url)
    image_data = BytesIO(image.content)

    return send_file(image_data, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host = '127.0.0.1', debug=True, port=5000)
