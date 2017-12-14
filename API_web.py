#from flask import Flask, request
#from SubjectsGII_Bot.funcionesDB import *
#from flask_restful import Resource, Api
#import json

from flask import Flask, request, jsonify, render_template
import os
import json
import psycopg2

app = Flask(__name__)


{
   "status": "OK"
}

db = os.environ['NAME_BD']
host_db = os.environ['HOST_BD']
usuario = os.environ['USER_BD']
pw = os.environ['PW_BD']


def buscarAsignatura(nombAsig):
    connect_db = psycopg2.connect(database=db, user=usuario, password=pw, host=host_db)
    cursor = connect_db.cursor()

    cursor.execute("SELECT * FROM AsignaturasGII WHERE asignatura LIKE %s", [nombAsig])
    asig = gDocen = fExam = hTeo = ""
    vAsig = []
    f = cursor.fetchall()

    for c in f:
        asig = "-Asignatura: " + str(c[0]) 
        vAsig.append(asig)
        gDocen = " -Guía docente: " + str(c[1])
        vAsig.append(gDocen)
        fExam = " -Fecha exámen final: " + str(c[2]) 
        vAsig.append(fExam)
        hTeo  = " -Horario teoría: " + str(c[3])
        vAsig.append(hTeo)

    connect_db.close()

    return vAsig

@app.route("/")
def principal():
    return jsonify(status='OK')

@app.route("/status")
def docker():
    return jsonify(status='OK')

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/busqueda", methods=['POST'])
def busqueda():
	asig = request.form['asignatura']
	res = buscarAsignatura(asig)

	return render_template("result.html", resultado=res)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('http_404.html')

"""
@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)
"""

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug = True, use_reloader = True)


