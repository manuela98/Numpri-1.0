# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 18:07:58 2019

@author: manuela
"""
from Numpri import primos
import unittest

class testPrimos(unittest.TestCase):
    
    def test_instanciado(self):
        try:
            primos.Primo()
        except NameError:
            raise AssertionError("La clase no esta definida")
            
        return True
    
    def test_numeroNegativo(self):
        try:
            primos.Primo().esPrimo(-3)
        except ValueError:
            return True
        raise AssertionError("No verifica si el numero ingresado es Natural")   
        
    def test_cero(self):
        try:
            primos.Primo().esPrimo(0)
        except ValueError:
            return True
        raise AssertionError("No verifica si el numero ingresado es Natural")   
        
    def test_4_esPrimo(self):
        primoSalida=primos.Primo().esPrimo(4)
        if primoSalida == True:
            raise AssertionError("No esta verificando si el numero ingresado es primo")
        else:
           return True
        
        
    def test_911_esPrimo(self):
        if primos.Primo().esPrimo(911) == False:
            raise AssertionError("No esta verificando si el numero ingresado es primo Correctamente")
        else:
            return True
            
    def test_numerosPrimos_0_1000(self):
        primosSalida = primos.Primo().calcularPrimos(0,1000)
        self.assertEqual(len(primosSalida),168)
  
    def test_primeros_10_primos(self):
        primosSalida = primos.Primo().calcularNprimos(10)
        listaPrimos = [2,3,5,7,11,13,17,19,23,29]
        self.assertEqual(listaPrimos,primosSalida)


    
if __name__=="__main__":
    unittest.main()
