#from flask import Flask, request
#from SubjectsGII_Bot.funcionesDB import *
#from flask_restful import Resource, Api
#import json

from flask import Flask
import os

app = Flask(__name__)
#api = Api(app)

@app.route("/")
def bienvenido():
    return ("Bienvenido al servicio web de SubjectsGII_Bot")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug = True, use_reloader = True)
