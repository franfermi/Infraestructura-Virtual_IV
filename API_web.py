#from flask import Flask, request
#from SubjectsGII_Bot.funcionesDB import *
#from flask_restful import Resource, Api
#import json

from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)


{
   "status": "OK"
}



@app.route("/")
def principal():
    return jsonify(status='OK')

@app.route("/status")
def docker():
    return jsonify(status='OK')

"""
@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)
"""

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug = True, use_reloader = True)
