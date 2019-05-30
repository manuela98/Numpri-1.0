       
          

app = Aplicacion()
ventana = app.crearVentanaPrincipal()
app.insertarImagen(ventana,nombreImagen="../Img/ventanaInicial.ppm")
app.ponerBoton(ventana,'Siguiente',comando=ventana.iconify)
nuevaVentana = app.crearNuevaVentana("#F1E8B8")
app.insertarImagen(nuevaVentana,"../Img/numerosPrimos.ppm")
app.ponerBoton(nuevaVentana,'Calculadora',comando=nuevaVentana.iconify)
app.ponerBoton(nuevaVentana,'Juego',comando=nuevaVentana.iconify)
app.ponerBoton(nuevaVentana,'Conceptos',comando=nuevaVentana.iconify)


calculadora = Calculadora()
ventanaCalculadora = calculadora.crearNuevaVentana("#E9B872")
botonesCalculadora = ['Es primo','Primos entre 2 numeros','CalcularNprimos']
comandosCalculadora = [calculadora.activarEsPrimo,calculadora.activarPrimosIntervalo,\
calculadora.activarCalcularNprimos]
calculadora.insertarImagen(ventanaCalculadora,nombreImagen="../Img/calculadora.ppm")
calculadora.crearMenu(ventanaCalculadora,botonesCalculadora,comandosCalculadora)



'''
conceptos = Conceptos()
ventanaConceptos = conceptos.crearNuevaVentana("#E9B872")
botonesConceptos = ['Curiosidades','Conjeturas']
lista = ['Titulos1','Titulos2']
comandoOpcion = partial(conceptos.crearMenuTitulos,lista)
comandosConceptos = [comandoOpcion,comandoOpcion]
conceptos.crearMenu(ventanaConceptos,botonesConceptos,comandosConceptos)
'''




ventana.mainloop()
