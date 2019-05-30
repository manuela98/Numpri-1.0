# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 18:07:58 2019

@author: manuela
"""

from functools import partial
import tkinter as tk
import unittest
from Numpri.__main__ import *

class mainTests(unittest.TestCase):
    
    def test_instanciadoAplicacion(self):
        try:
           AplicacionPrincipal()  
        except NameError:
            raise AssertionError("La clase Aplicacion no esta definida")
        return True

    def test_mostrarCalculadora(self):
        self.aplicacion =  AplicacionPrincipal()  
        ventanaCalculadora = AplicacionPrincipal.mostrarCalculadora(self.aplicacion)
        return isinstance(ventanaCalculadora,tk.Tk)

    def test_mostrarConceptos(self):
        self.aplicacion =  AplicacionPrincipal()  
        ventanaConceptos = AplicacionPrincipal.mostrarConceptos(self.aplicacion)
        return isinstance(ventanaConceptos,tk.Tk)
