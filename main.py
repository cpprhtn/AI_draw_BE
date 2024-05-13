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

# @app.route("/api/text", methods=["POST"])
# def ImageMaker(API_KEY=API_KEY):    
#     input = request.get_json()
    
#     text = input["text"]
#     openai.api_key = API_KEY

#     response = client.images.generate(
#     model="dall-e-3",
#     prompt=text,
#     size="1024x1024",
#     quality="standard",
#     n=1,
#     )
    
#     image_url = response.data[0].url

#     image = requests.get(image_url)
#     image_data = BytesIO(image.content)

#     return send_file(image_data, mimetype='image/jpeg')


@app.route("/api/website", methods=["POST"])
def generate_website_image():
    input_data = request.get_json()

    website_data = input_data["website"]

    website_prompt = f"Website purpose: {website_data['purpose']}\n"
    website_prompt += f"Target audience: {website_data['targer']}\n"
    website_prompt += f"Design style: {website_data['design']['designStyle']}\n"
    website_prompt += f"Main color: {website_data['design']['mainColor']}\n"
    website_prompt += f"Content: {website_data['content']}\n"

    openai.api_key = API_KEY

    website_response = openai.Image.create(
        model="text-davinci-003",
        prompt=website_prompt,
        max_tokens=50,
        stop=["\n"],
        temperature=0.5
    )
    website_image_url = website_response['images'][0]['url']

    website_image = requests.get(website_image_url)

    website_image_data = BytesIO(website_image.content)

    return send_file(website_image_data, mimetype='image/jpeg')

@app.route("/api/logo", methods=["POST"])
def generate_logo_image():
    input_data = request.get_json()

    logo_data = input_data["logo"]

    logo_prompt = f"Brand name: {logo_data['brandInfo']['name']}\n"
    logo_prompt += f"Business area: {logo_data['brandInfo']['businessArea']}\n"
    logo_prompt += f"Design symbol: {logo_data['design']['symbol']}\n"
    logo_prompt += f"Design style: {logo_data['design']['designStyle']}\n"
    logo_prompt += f"Main color: {logo_data['design']['mainColor']}\n"

    openai.api_key = API_KEY

    logo_response = openai.Image.create(
        model="text-davinci-003",
        prompt=logo_prompt,
        max_tokens=50,
        stop=["\n"],
        temperature=0.5
    )
    logo_image_url = logo_response['images'][0]['url']

    logo_image = requests.get(logo_image_url)

    logo_image_data = BytesIO(logo_image.content)

    return send_file(logo_image_data, mimetype='image/jpeg')

@app.route("/api/webtoon", methods=["POST"])
def generate_webtoon_cover_image():
    input_data = request.get_json()

    webtoon_data = input_data["webtoonCover"]

    webtoon_prompt = f"Webtoon name: {webtoon_data['webtoonInfo']['name']}\n"
    webtoon_prompt += f"Genre: {webtoon_data['webtoonInfo']['genre']}\n"
    webtoon_prompt += f"Main characters: {webtoon_data['character']['Character1']} and {webtoon_data['character']['Character2']}\n"
    webtoon_prompt += f"Background: {webtoon_data['background']}\n"
    webtoon_prompt += f"Main color: {webtoon_data['design']['mainColor']}\n"
    webtoon_prompt += f"Mood: {webtoon_data['design']['mood']}\n"
    webtoon_prompt += f"Text style: {webtoon_data['design']['textStyle']}\n"

    openai.api_key = API_KEY

    webtoon_response = openai.Image.create(
        model="text-davinci-003",
        prompt=webtoon_prompt,
        max_tokens=50,
        stop=["\n"],
        temperature=0.5
    )
    webtoon_image_url = webtoon_response['images'][0]['url']

    webtoon_image = requests.get(webtoon_image_url)

    webtoon_image_data = BytesIO(webtoon_image.content)

    return send_file(webtoon_image_data, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host = '127.0.0.1', debug=True, port=5000)
