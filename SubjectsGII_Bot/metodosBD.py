#!/bin/usr/python
# -*- coding: utf-8 -*-

import psycopg2, psycopg2.extras
import os
#import urlparse

#db = os.environ["NAME_BD"]
#host_db = os.environ["HOST_BD"]
#user_bd = os.environ["USER_BD"]
#pw_bd = os.environ["PW_BD"]


def conexionBD():
    connect_db = psycopg2.connect(dbname='postgres', user='postgres', password='12345', host='localhost')
    cursor = connect_db.cursor()

    return cursor

def nombreAsignatura(nombAsig):
    connect_db = psycopg2.connect(dbname='postgres', user='postgres', password='12345', host='localhost')
    cursor = connect_db.cursor()
    asig = nombAsig

    cursor.execute("SELECT * FROM subjectsgii WHERE asignatura = %s", [asig])

    num_asig = len(cursor.fetchall())

    if num_asig != 0:
        return True

    connect_db.close()

    return False

def guiaDocenteDisponible(nombAsig):
    connect_db = psycopg2.connect(dbname='postgres', user='postgres', password='12345', host='localhost')
    cursor = connect_db.cursor()
    asig = nombAsig

    cursor.execute("SELECT guia_docente FROM subjectsgii WHERE asignatura = %s", [asig])

    num_guia = len(cursor.fetchall())

    if num_guia != 0:
        return True

    connect_db.close()

    return False

def fechaExamenDisponible(nombAsig):
    connect_db = psycopg2.connect(dbname='postgres', user='postgres', password='12345', host='localhost')
    cursor = connect_db.cursor()
    asig = nombAsig

    cursor.execute("SELECT fecha_examen FROM subjectsgii WHERE asignatura = %s", [asig])

    num_fecha = len(cursor.fetchall())

    if num_fecha != 0:
        return True

    connect_db.close()

    return False

def numeroAsigDisponibles():
    connect_db = psycopg2.connect(dbname='postgres', user='postgres', password='12345', host='localhost')
    cursor = connect_db.cursor()
    cursor.execute("SELECT * FROM subjectsgii")

    num_asignaturas = len(cursor.fetchall())

    connect_db.close()

    return num_asignaturas

def mostrarAsigDisponibles():
    connect_db = psycopg2.connect(dbname='postgres', user='postgres', password='12345', host='localhost')
    cursor = connect_db.cursor()
    cursor.execute("SELECT asignatura FROM subjectsgii")

    filas = len(cursor.fetchall())

    for i in filas:
        asigs += str(i[1]) + " " + str(i[2]) + " " + str(i[3]) + " " + str(i[4]) + "\n"

    connect_db.close()

    return asigs

