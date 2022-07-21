from flask import Flask, jsonify, request as req, Response as res
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
from os import environ
from youtube_functions import get_audio_from_video

config = load_dotenv("../.env")

URI_DATABASE = environ.get("URI_DATABASE")

app = Flask(__name__)
CORS(app, origins="http://localhost:3000")
# MongoClient config
host = MongoClient(URI_DATABASE)
db = host["distros"]
collection = db["dists"]

@app.get("/")
def main():
    #distros_finded = collection.find_one({"name": "Arch Linux x64"}, {"_id": 0})
    return jsonify("Hello World!")

@app.post("/")
def send_main():
    bytes_to_string = req.data.decode("UTF-8")
    audio_file = get_audio_from_video(bytes_to_string)
    #charge_video = open("../videos/"[0])
    #print(charge_video)
    return audio_file