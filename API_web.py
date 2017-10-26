from flask import Flask, request
from SubjectsGII_Bot.funcionesDB import *
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route("/")
def bienvenido():
    return ("Bienvenido al servicio web de SubjectsGII_Bot")

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug = True)
