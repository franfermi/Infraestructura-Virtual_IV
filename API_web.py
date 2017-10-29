#from flask import Flask, request
#from SubjectsGII_Bot.funcionesDB import *
#from flask_restful import Resource, Api
#import json

from flask import Flask

app = Flask(__name__)
PORT = 5000
DEBUG = False
#api = Api(app)

@app.route("/", methods=['GET'])
def bienvenido():
    return ("Bienvenido al servicio web de SubjectsGII_Bot")

@app.route(404)
def not_found(error):
    return "Not Found."

if __name__ == "__main__":
    app.run(port = PORT, debug = DEBUG)
