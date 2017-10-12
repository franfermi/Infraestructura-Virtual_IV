#!/bin/usr/python
# -*- coding: utf-8 -*-

import os
#import urlparse
import funcionesDB
import sqlite3

#Prueba de conexión y respuesta de la BD
respuesta = funcionesDB.nombreAsignatura("DBA")

if respuesta is False:
    print ("La asignatura no se encuentra en la BD")
else:
    print ("Asignatura encontrada")
