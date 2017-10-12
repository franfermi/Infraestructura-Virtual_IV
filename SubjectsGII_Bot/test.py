#!/bin/usr/python
# -*- coding: utf-8 -*-

import unittest
import math
import funcionesDB

#def devuelveTrue():
#    return True

#def cuadrado(a):
#    if(not(type(a)is int)):
#        return -1
#    else:
#        return a**2;

#def raiz(a):
#    if(not(type(a)is int)):
#        return -1
#    elif a >= 0:
#        return math.sqrt(a)
#    else:
#        raise ValueError, "a debe ser >= 0"

class TestMetodos(unittest.TestCase):

#    def testDevuelveTrue(self):
#        self.assertTrue(devuelveTrue(), "Es True")

#    def testCuadrado(self):
#        self.assertEqual(cuadrado(2), 4, "El cuadrado de 2 es 4")
        #self.assertEqual(cuadrado(3), 6, "El cuadrado de 3 NO es 6")

#    def testRaiz(self):
#        self.assertEqual(raiz(9), 3, "La raiz de 9 es 3")
        #self.assertEqual(raiz(-1), IndexError)


    """ Test que comprueba que una asignatura está disponible"""
    def test_asig_disponible(self):
        num_asig = funcionesDB.nombreAsignatura("CPD")
        self.assertTrue(num_asig)

    """ Test que comprueba que la guía docente está disponible"""
    def test_guia_disponible(self):
        num_guia = funcionesDB.guiaDocenteDisponible("TR")
        self.assertTrue(num_guia)

    """ Test que comprueba que la fecha exámen está disponible"""
    def test_fechaEx_disponible(self):
        num_fecha = funcionesDB.fechaExamenDisponible("SE")
        self.assertTrue(num_fecha)

    """ Test que comprueba el total de asignaturas disponibles"""
    def test_numAsig_disponibles(self):
        num_asigs = funcionesDB.numeroAsigDisponibles()
        self.assertNotEqual(num_asigs, 0)


if __name__ == '__main__':
   unittest.main()
