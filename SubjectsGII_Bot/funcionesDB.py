#!/bin/usr/python
# -*- coding: utf-8 -*-

import os
import psycopg2

db = os.environ['NAME_BD']
host_db = os.environ['HOST_BD']
usuario = os.environ['USER_BD']
pw = os.environ['PW_BD']

def conexionBD():
    connect_db = psycopg2.connect(database=db, user=usuario, password=pw, host=host_db)
    cursor = connect_db.cursor()

    return cursor

def nombreAsignatura(nombAsig):
    connect_db = psycopg2.connect(database=db, user=usuario, password=pw, host=host_db)
    cursor = connect_db.cursor()
    asig = nombAsig

    cursor.execute("SELECT * FROM AsignaturasGII WHERE asignatura = 'TR'")

    num_asig = len(cursor.fetchall())

    if num_asig != 0:
        return True

    connect_db.close()

    return False

def guiaDocenteDisponible(nombAsig):
    connect_db = psycopg2.connect(database=db, user=usuario, password=pw, host=host_db)
    cursor = connect_db.cursor()
    asig = nombAsig

    #cursor.execute("SELECT guia_docente FROM AsignaturasGII WHERE asignatura = %s", [asig])
    cursor.execute("SELECT guia_docente FROM AsignaturasGII WHERE asignatura = 'TR'")

    num_guia = len(cursor.fetchall())

    if num_guia != 0:
        return True

    connect_db.close()

    return False

def fechaExamenDisponible(nombAsig):
    connect_db = psycopg2.connect(database=db, user=usuario, password=pw, host=host_db)
    cursor = connect_db.cursor()
    asig = nombAsig

    cursor.execute("SELECT fecha_examen FROM AsignaturasGII WHERE asignatura = 'TR'")

    num_fecha = len(cursor.fetchall())

    if num_fecha != 0:
        return True

    connect_db.close()

    return False

def numeroAsigDisponibles():
    connect_db = psycopg2.connect(database=db, user=usuario, password=pw, host=host_db)
    cursor = connect_db.cursor()
    cursor.execute("SELECT * FROM AsignaturasGII")

    num_asignaturas = len(cursor.fetchall())

    connect_db.close()

    return num_asignaturas

def mostrarAsigDisponibles():
    connect_db = psycopg2.connect(database=db, user=usuario, password=pw, host=host_db)
    cursor = connect_db.cursor()
    cursor.execute("SELECT asignatura FROM AsignaturasGII")
    asigs = ""
    nums = cursor.fetchall()

    for i in nums:
        asigs += str(i) + "\n"

    connect_db.close()

    return asigs

def mostrarTodo():
    connect_db = psycopg2.connect(database=db, user=usuario, password=pw, host=host_db)
    cursor = connect_db.cursor()
    cursor.execute("SELECT * FROM AsignaturasGII")
    asigs = ""
    f = cursor.fetchall()

    for c in f:
        asigs += str(c[0]) + " " + str(c[1]) + " " + str(c[2]) + " " + str(c[3]) + "\n"

    connect_db.close()

    return asigs
