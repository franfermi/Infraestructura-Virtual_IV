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
