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
        return cadenaEntrada.get() 

    def insertarEntrada(self,ventana,inicial):

       entrada = tk.StringVar(ventana)       
       self.entradaTk = tk.Entry(ventana,width=50,textvariable=entrada)
       self.entradaTk.place(x=120,y=62)
       self.entradaTk.pack()
       entrada.set(inicial)
       return entrada,self.entradaTk

    def valorActualEntrada(self,variable):
        variable.trace("w", lambda actualizar, index, mode,\
        variable=variable:Aplicacion.actualizarEntrada(self,variable))
        return variable

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
    
    def mostrarError(self,mensaje): 
       self.ventanaError = tk.Tk()
       self.ventanaError.title("Error")
       self.ventanaError.geometry("350x100+540+284")
       self.ventanaError.config(bg="#F1E8B8")
       tk.Label(self.ventanaError,text=mensaje,font='Arial 10 bold', bg="white").place(x=15,y=20)
       tk.Button(self.ventanaError, text="Entendido!", command=self.ventanaError.destroy,\
       background="#CE0000",font='Arial 11 bold').place(x=140,y=60)
       return self.ventanaError

   

    


class Calculadora(Aplicacion):

    def __init___(self):
        self.valorEntrada =  tk.StringVar()
    
    def entradaCalculadora(self,ventanaCalculadora,inicial):
        self.valorEntrada = Aplicacion.insertarEntrada(self,ventanaCalculadora,inicial)[0] 
        return self.valorEntrada

    def activarEsPrimo(self,ventanaCalculadora):
        self.primo = primos.Primo()
        self.valorEntrada = Aplicacion.valorActualEntrada(self,self.valorEntrada)
        try:
            numero = int(self.valorEntrada.get())
            if primos.Primo.esPrimo(self.primo,numero)==True:
               Aplicacion.mostrarRecuadroSalida(self,ventanaCalculadora,'El número  es primo')
            else:
               Aplicacion.mostrarRecuadroSalida(self,ventanaCalculadora,'El número no es primo')
            
        except:
             Aplicacion.mostrarError(self,'Debe Ingresar un número Natural. Ej : 7')
                        
        return self.valorEntrada.get()      
            

    def activarPrimosIntervalo(self,ventanaCalculadora):
        self.primo = primos.Primo()
        self.calculadora = Calculadora()
        self.valorEntrada = Aplicacion.valorActualEntrada(self,self.valorEntrada)
        try:
            intervalo = str(self.valorEntrada.get()).split(',')
            numerosIntervalo = primos.Primo.calcularPrimos(self.primo,int(intervalo[0]),int(intervalo[1]))
            Aplicacion.mostrarRecuadroSalida(self.calculadora,ventanaCalculadora,str(numerosIntervalo))
        except:
             Aplicacion.mostrarError(self,'Debe Ingresar un intervalo. Ej : 2,17')

        return  self.valorEntrada.get()
      
    def activarCalcularNprimos(self,ventanaCalculadora):
       self.primo = primos.Primo()
       self.valorEntrada = Aplicacion.valorActualEntrada(self,self.valorEntrada)
       try:
           numero = int(self.valorEntrada.get())
           listaPrimos = primos.Primo.calcularNprimos(self.primo,numero)
           Aplicacion.mostrarRecuadroSalida(self,ventanaCalculadora,str(listaPrimos))
       except:
           Aplicacion.mostrarError(self,'Debe Ingresar un número Natural. Ej : 7')
       return  str(listaPrimos)
       
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
        self.Botones = []
        for opcion in range(len(titulosOpciones)):
            comandoOpcion = partial(Aplicacion.insertarImagen,self,ventanaOpcion,"Img/"+titulosOpciones[opcion]+".ppm")
            self.Botones += [Aplicacion.ponerBoton(self,ventanaOpcion,titulosOpciones[opcion],comando=comandoOpcion)]
        return self.Botones
