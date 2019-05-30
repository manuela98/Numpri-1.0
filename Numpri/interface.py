# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 18:07:58 2019

@author: manuela
"""

import tkinter as tk
from PIL import Image,ImageTk
from time import sleep
from Numpri import primos
from functools import partial


class Aplicacion(object):

    ''' 
        Establece los elementos para la interface grafica para Numpri.
    '''


    def __init__(self):
       self.ventanaInicial = None

    def crearVentanaPrincipal(self):
       self.ventanaInicial = tk.Tk()
       self.ventanaInicial.title('Numpri')
       self.ventanaInicial.geometry("1366x768+0+0")
       self.ventanaInicial.config(bg="#3E8989")
       return self.ventanaInicial  


    def crearNuevaVentana(self,color):
       self.ventanaNueva = tk.Toplevel()  
       self.ventanaNueva.geometry("1366x768+0+0")
       self.ventanaNueva.config(bg=color)
       return self.ventanaNueva


    def mostrarRecuadroSalida(self,ventana,texto):
       self.canvasTexto = tk.Canvas(ventana, width= 500, height=80)
       self.canvasTexto.pack()
       self.canvasTexto.create_text(250,40,text=texto,fill="darkblue",\
       font="Times 20 italic bold")
       return self.canvasTexto

    def ponerBoton(self,ventana,texto,comando):
       self.boton = tk.Button(ventana, text=texto, command=comando) 
       self.boton.pack()
       return self.boton

    def actualizarEntrada(self,cadenaEntrada):
        print(cadenaEntrada.get()) 
        return cadenaEntrada.get() 
    def insertarEntrada(self,ventana,inicial):

       entrada = tk.StringVar(ventana)       
       self.entradaTk = tk.Entry(ventana,textvariable=entrada)
       
       entrada.trace("w", lambda actualizar, index, mode,\
       entrda=entrada:Aplicacion.actualizarEntrada(self,entrada))
       self.entradaTk.pack()
       entrada.set(inicial)
       return entrada.get(),self.entradaTk

    def crearMenu(self,ventana,botones,comandos):
        self.Botones = []
        for opcion in range(len(botones)):
            comandoOpcion = partial(comandos[opcion],ventana)
            self.Botones += [Aplicacion.ponerBoton(self,\
            ventana,botones[opcion],comando=comandoOpcion)]
        return self.Botones 
    
    def insertarImagen(self,ventana,nombreImagen):   
       imagen = Image.open(nombreImagen)
       anchoImagen, largoImagen = imagen.size
       self.canvasImagen = tk.Canvas(ventana, width= anchoImagen,\
       height=largoImagen)
       self.canvasImagen.pack()
       imagenTk = tk.PhotoImage(file=nombreImagen)       
       self.canvasImagen.create_image(anchoImagen/2.,largoImagen/2.,\
       image=imagenTk) 
       self.canvasImagen.image = imagenTk
       return self.canvasImagen 
   

   

    



class Calculadora(Aplicacion):

    def __init___(self):
        self.valorEntrada = None 
    

    def activarEsPrimo(self,ventanaCalculadora):
        numeroInicial = '7'
        self.primo = primos.Primo()
        self.valorEntrada = Aplicacion.insertarEntrada(self,ventanaCalculadora,numeroInicial)[0]
        print(int(self.valorEntrada))
        if primos.Primo.esPrimo(self.primo,int(self.valorEntrada))==True:
           Aplicacion.mostrarRecuadroSalida(self,ventanaCalculadora,'El número  es primo')
        else:
           Aplicacion.mostrarRecuadroSalida(self,ventanaCalculadora,'El número no es primo')
        return int(self.valorEntrada)

    def activarPrimosIntervalo(self,ventanaCalculadora):
        self.primo = primos.Primo()
        self.calculadora = Calculadora()
        intervaloInicial = '7,11'
        self.valorEntrada = Aplicacion.insertarEntrada(self.calculadora,ventanaCalculadora,intervaloInicial)[0]
        intervalo = str(self.valorEntrada).split(',')
        numerosIntervalo = primos.Primo.calcularPrimos(self.primo,int(intervalo[0]),int(intervalo[1]))
        Aplicacion.mostrarRecuadroSalida(self.calculadora,ventanaCalculadora,str(numerosIntervalo))
        return intervalo
      
    def activarCalcularNprimos(self,ventanaCalculadora):
       n = '6'
       self.primo = primos.Primo()
       self.valorEntrada = Aplicacion.insertarEntrada(self,ventanaCalculadora,n)[0]
       listaPrimos = primos.Primo.calcularNprimos(self.primo,int(self.valorEntrada))
       Aplicacion.mostrarRecuadroSalida(self,ventanaCalculadora,str(listaPrimos))
       return listaPrimos
       
class  Conceptos(Aplicacion):

    def __init__(self):
        self.titulosOpciones = None 

    def crearMenu(self,ventana,botones,comandos):
        self.Botones = []
        for opcion in range(len(botones)):
            self.Botones += [Aplicacion.ponerBoton(self,\
            ventana,botones[opcion],comando=comandos[opcion])]
        return self.Botones 

    def crearMenuTitulos(self,titulosOpciones):
        self.titulosOpciones = titulosOpciones
        ventanaOpcion = Aplicacion.crearNuevaVentana(self,"#F1E8B8")

        for opcion in range(len(titulosOpciones)):
            comandoOpcion = partial(Aplicacion.insertarImagen,self,ventanaOpcion,"../Img/calculadora.ppm")
            accionesTitulos = [comandoOpcion,comandoOpcion]
            Aplicacion.ponerBoton(self,ventanaOpcion,titulosOpciones[opcion],comando=accionesTitulos[opcion])
       

       
           
        
     




 

  

    
     
    
            
    
        




  

