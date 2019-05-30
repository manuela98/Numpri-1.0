#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 15:17:59 2019

@author: JoseMVergara
"""

import Numpri as npr
import unittest

class test_Numpri(unittest.TestCase):
    
    def test_instanciado(self):
        try:
            primo=npr.Primo()
        except NameError:
            raise AssertionError("La clase no esta definida")
            
        return True
    
    def test_numeroNegativo(self):
        try:
            primo=npr.Primo().esPrimo(-3)
        except ValueError:
            return True
        raise AssertionError("No verifica si el numero ingresado es Natural")   
        
    def test_cero(self):
        try:
            primo=npr.Primo().esPrimo(0)
        except ValueError:
            return True
        raise AssertionError("No verifica si el numero ingresado es Natural")   
        
    def test_4_esPrimo(self):
        primo=npr.Primo().esPrimo(4)
        if primo == True:
            raise AssertionError("No esta verificando si el numero ingresado es primo")
        else:
           return True
        
        
    def test_911_esPrimo(self):
        if npr.Primo().esPrimo(911) == False:
            raise AssertionError("No esta verificando si el numero ingresado es primo Correctamente")
        else:
            return True
            
    def test_numerosPrimos_0_1000(self):
        primos = npr.Primo().calcularPrimos(0,1000)
        self.assertEqual(len(primos),168)
  
    def test_primeros_10_primos(self):
        primos = npr.Primo().calcularNprimos(10)
        listaPrimos = [2,3,5,7,11,13,17,19,23,29]
        self.assertEqual(listaPrimos,primos)


    
if __name__=="__main__":
    unittest.main()