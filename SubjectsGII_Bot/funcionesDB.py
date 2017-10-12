#!/bin/usr/python
# -*- coding: utf-8 -*-

import psycopg2, psycopg2.extras
import os
import sqlite3
#import urlparse

def conexionBD():
    connect_db = sqlite3.connect('AsignaturasGII.db')
    cursor = connect_db.cursor()

    return cursor

def nombreAsignatura(nombAsig):
    connect_db = sqlite3.connect('AsignaturasGII.db')
    cursor = connect_db.cursor()
    asig = nombAsig

    cursor.execute("SELECT * FROM AsignaturasGII WHERE asignaturas = 'DBAS'")

    num_asig = len(cursor.fetchall())

    if num_asig != 0:
        return True

    connect_db.close()

    return False

def guiaDocenteDisponible(nombAsig):
    connect_db = sqlite3.connect('AsignaturasGII.db')
    cursor = connect_db.cursor()
    asig = nombAsig

    #cursor.execute("SELECT guia_docente FROM AsignaturasGII WHERE asignatura = %s", [asig])
    cursor.execute("SELECT guia_docente FROM AsignaturasGII WHERE asignatura = 'SE'")

    num_guia = len(cursor.fetchall())

    if num_guia != 0:
        return True

    connect_db.close()

    return False

def fechaExamenDisponible(nombAsig):
    connect_db = sqlite3.connect('AsignaturasGII.db')
    cursor = connect_db.cursor()
    asig = nombAsig

    cursor.execute("SELECT fecha_examen FROM AsignaturasGII WHERE asignatura = 'CPD'")

    num_fecha = len(cursor.fetchall())

    if num_fecha != 0:
        return True

    connect_db.close()

    return False

def numeroAsigDisponibles():
    connect_db = sqlite3.connect('AsignaturasGII.db')
    cursor = connect_db.cursor()
    cursor.execute("SELECT * FROM AsignaturasGII")

    num_asignaturas = len(cursor.fetchall())

    connect_db.close()

    return num_asignaturas

def mostrarAsigDisponibles():
    connect_db = sqlite3.connect('AsignaturasGII.db')
    cursor = connect_db.cursor()
    cursor.execute("SELECT asignaturas FROM AsignaturasGII")

    filas = len(cursor.fetchall())

    for i in filas:
        asigs += str(i[1]) + " " + str(i[2]) + " " + str(i[3]) + " " + str(i[4]) + "\n"

    connect_db.close()

    return asigs
