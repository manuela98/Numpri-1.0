# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 18:07:58 2019

@author: manuela
"""

import tkinter as tk
from PIL import Image,ImageTk
import unittest
from Numpri.interface import *  



class NumpriTests(unittest.TestCase):
    

    def test_instanciadoAplicacion(self):
        try:
            self.aplicacion = Aplicacion()  
        except NameError:
            raise AssertionError("La clase Aplicacion no esta definida")
            
        return True

    def test_crearVentanaPrincipal(self):
        self.aplicacion = Aplicacion()
        self.ventana = Aplicacion.crearVentanaPrincipal(self.aplicacion)
        return isinstance(self.ventana,tk.Tk)

            
    def test_crearNuevaVentana(self):
        self.aplicacion = Aplicacion()
        self.ventanaNueva = Aplicacion.crearNuevaVentana(self.aplicacion,"#3E8989")
        return isinstance(self.ventanaNueva,tk.Tk)

    def test_ponerBoton(self):
        self.aplicacion = Aplicacion()
        self.ventana = Aplicacion.crearVentanaPrincipal(self.aplicacion)
        boton = Aplicacion.ponerBoton(self.aplicacion,ventana=self.ventana,
        texto='Siguiente',comando=self.ventana.quit)
        try:
            boton.invoke()
        except NameError:
            raise AttributeError("El comando del boton no pudo ser ejecutado")
        return True
   

    def test_mostrarRecuadroSalida(self):
        self.aplicacion = Aplicacion()
        self.ventanaNueva = Aplicacion.crearNuevaVentana(self.aplicacion,"#3E8989")
        self.canvas = Aplicacion.mostrarRecuadroSalida(self.aplicacion,self.ventanaNueva,texto='Prueba Canvas')
        return isinstance(self.canvas,tk.Canvas)
     

    def test_actualizarEntrada(self):
        self.aplicacion = Aplicacion()
        self.ventanaNueva = Aplicacion.crearNuevaVentana(self.aplicacion,"#3E8989")
        cadenaEntrada = tk.StringVar(self.ventanaNueva)
        cadenaEntrada.set('prueba')
        cadenaSalida = Aplicacion.actualizarEntrada(self.aplicacion,cadenaEntrada)
        return self.assertEqual(cadenaSalida, cadenaEntrada.get())

    def test_insertarEntrada(self):
        self.aplicacion = Aplicacion()
        self.ventana = Aplicacion.crearVentanaPrincipal(self.aplicacion)
        recuadroEntrada = Aplicacion.insertarEntrada(self.aplicacion,self.ventana,'cadena de prueba')[1]
        return isinstance(recuadroEntrada,tk.Entry)

    def test_valorActual(self):
        self.aplicacion = Aplicacion()
        cadenaEntrada = tk.StringVar()
        cadenaEntrada.set('prueba')
        cadenaSalida = Aplicacion.valorActualEntrada(self.aplicacion,cadenaEntrada)
        return self.assertEqual(cadenaSalida.get(), cadenaEntrada.get())

    def test_crearMenu(self):
        self.aplicacion = Aplicacion()
        self.ventana = Aplicacion.crearVentanaPrincipal(self.aplicacion)
        botones = ['boton prueba 1']
        comandos = [tk.Entry]
        self.Menu = Aplicacion.crearMenu(self.aplicacion,self.ventana,botones,comandos)
        return isinstance(self.Menu[0],tk.Button)
        

   
    def test_instanciadoCalculadora(self):
        try:
            self.caculadora = Calculadora()  
        except NameError:
            raise AssertionError("La clase Calculadora no esta definida")    
        return True 

    def test_activarEsPrimo(self):
        self.calculadora = Calculadora() 
        self.ventana = Calculadora.crearNuevaVentana(self.calculadora,"#E9B872")
        variable = tk.StringVar(self.ventana)
        variable.set('7')
        self.calculadora.valorEntrada = variable
        salida = Calculadora.activarEsPrimo(self.calculadora,self.ventana)
        return self.assertEqual(salida,'7')

    
    def test_activarPrimosIntervalo(self):
        self.calculadora = Calculadora()  
        self.ventana = Calculadora.crearNuevaVentana(self.calculadora,"#E9B872")
        variable = tk.StringVar(self.ventana)
        variable.set('7,11')
        self.calculadora.valorEntrada = variable
        salidaIntervalo = Calculadora.activarPrimosIntervalo(self.calculadora,self.ventana)
        return self.assertEqual(salidaIntervalo,'7,11')

    def test_activarCalcularNprimos(self):
        
        self.calculadora = Calculadora()  
        self.ventana = Calculadora.crearNuevaVentana(self.calculadora,"#E9B872")
        variable = tk.StringVar(self.ventana)
        variable.set('6')
        self.calculadora.valorEntrada = variable
        salidaLista = Calculadora.activarCalcularNprimos(self.calculadora,self.ventana)
        listaPrimos = [2,3,5,7,11,13]
        return self.assertEqual(salidaLista,str(listaPrimos))
    

    def test_mostrarError(self):
        self.calculadora= Calculadora()
        ventana = Calculadora.mostrarError(self.calculadora,'Prueba')
        return isinstance(ventana,tk.Tk)
        

    def test_instanciadoConceptos(self):
        try:
            self.conceptos = Conceptos()  
        except NameError:
            raise AssertionError("La clase Conceptos no esta definida")    
        return True 
    
    def test_crearMenuConceptos(self):
        self.conceptos = Conceptos()  
        botones = ['botonPrueba']
        ventanaConceptos = Conceptos.crearNuevaVentana(self.conceptos,"#E9B872")
        comandoOpcion = partial(Conceptos.crearMenuTitulos,botones)
        menu = Conceptos.crearMenu(self.conceptos,ventanaConceptos,botones,[comandoOpcion])
        return isinstance(menu[0],tk.Button)
    
    def test_crearTitulos(self):
        self.conceptos = Conceptos()  
        titulosOpciones = ['titulo prueba 1','titulo prueba 2']
        botones = Conceptos.crearMenuTitulos(self.conceptos,titulosOpciones)
        return isinstance(botones[0],tk.Button)
    
if __name__=="__main__":
    unittest.NumpriTests()
          




        
        
  
    
        
   
    


    
