#!/bin/usr/python
# -*- coding: utf-8 -*-

import unittest
#import metodosBD

class TestMetodos(unittest.TestCase):

    """ Test que comprueba que una asignatura está disponible
    def test_asig_disponible(self, nombAsig):
        num_asig = metodosBD.nombreAsignatura(nombAsig)
        self.assertTrue(num_asig)"""

    """ Test que comprueba que la guía docente está disponible
    def test_guia_disponible(self, nombAsig):
        num_guia = metodosBD.guiaDocenteDisponible(nombAsig)
        self.assertTrue(num_guia)"""

    """ Test que comprueba que la fecha exámen está disponible
    def test_fechaEx_disponible(self, nombAsig):
        num_fecha = metodosBD.fechaExamenDisponible(nombAsig)
        self.assertTrue(num_fecha)"""

    """ Test que comprueba el total de asignaturas disponibles
    def test_numAsig_disponibles(self):
        num_asigs = metodosBD.numeroAsigDisponibles()
        self.assertNotEqual(num_asigs, 0)"""

    """ Test que comprueba que se muestran las asignaturas disponibles
    def test_mostrarAsig_disponibles(self):
        filas = metodosBD.mostrarAsigDisponibles()
        self.assertNotEqual(filas, 0)"""

if __name__ == '__main__':
   unittest.main()
