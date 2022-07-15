from flask import Flask, jsonify, request as req, Response as res
from markupsafe import escape
from pprint import pprint
from os import path, environ
from pymongo import MongoClient
from dotenv import load_dotenv

config = load_dotenv("../.env")

URI_DATABASE = environ.get("URI_DATABASE")

app = Flask(__name__)

# MongoClient config
host = MongoClient(URI_DATABASE)
db = host["distros"]
collection = db["dists"]

@app.route("/")
def main():
    distros_finded = collection.find_one({"name": "Fedora 36 Workstation"}, {"_id": 0, "name": 1})
    return f"<h1>Distribucion encontrada segun por parametro de nombre {distros_finded['name']}</h1>"

@app.post("/")
def send_main():
    collection.insert_one(req.json)
    return f"Received! \n New data saved: \n \n {req.json}"

"""
    with open(path.join(path.dirname(__file__) + "/../logs/response.txt"), "a") as file:
        file.write(str(req.json))
"""