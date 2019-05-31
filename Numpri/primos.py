# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 18:07:58 2019

@author: manuela
"""
import numpy as np

class Primo(object):
            
    def esPrimo(self,numero):
        if isinstance(numero,int) and numero>0:
            self.numero = numero
        else:
            raise ValueError("Un numero primo debe ser Natural")
        if self.numero<2:
            return False 
        elif self.numero==2:
            return True
        else:
            for n in range(2,int(self.numero)):
                if self.numero%n == 0:
                    return False
                
        return True
    
    def calcularPrimos(self,a,b):
        numerosPrimos = []
        intervalo = np.linspace(a,b,b-a+1,dtype=int)
        intervalo = list(intervalo[intervalo%2!=0])
        if a<2:
            intervalo.insert(0,2)
        for n in intervalo:
            if  Primo.esPrimo(self,int(n)) == True:
                numerosPrimos += [n]
        return numerosPrimos
        
    def calcularNprimos(self,n):
        if n<1:
           raise ValueError("Un numero primo debe ser Natural")
        numerosPrimos = []
        numero = 2
        while len(numerosPrimos) < n:
            if Primo.esPrimo(self,numero) == True:
                numerosPrimos+=[numero]
            numero += 1
        return numerosPrimos

            
