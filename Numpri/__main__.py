from Numpri import interface
from functools import partial



class AplicacionPrincipal(object):

    def mostrarAplicacion(self):
        aplicacion = interface.Aplicacion()
        ventanaPrincipal = aplicacion.crearVentanaPrincipal()
        aplicacion.insertarImagen(ventanaPrincipal,nombreImagen="Img/ventanaInicial.ppm")
        aplicacion.ponerBoton(ventanaPrincipal,'Siguiente',comando=ventanaPrincipal.iconify)
        ventanaSecundaria = aplicacion.crearNuevaVentana("#F1E8B8")
        aplicacion.insertarImagen(ventanaSecundaria,"Img/numerosPrimos.ppm")
        boton = aplicacion.ponerBoton(ventanaSecundaria,'Juego',comando=ventanaSecundaria.iconify)
        boton.configure(state='disabled')
        comandoOpcionCalculadora = partial(AplicacionPrincipal.mostrarCalculadora,self)
        aplicacion.ponerBoton(ventanaSecundaria,'Calculadora',comando=comandoOpcionCalculadora)
        comandoOpcionConceptos = partial(AplicacionPrincipal.mostrarConceptos,self)
        aplicacion.ponerBoton(ventanaSecundaria,'Conceptos',comando=comandoOpcionConceptos)

        if __name__=="__main__":
            ventanaPrincipal.mainloop()
        return ventanaPrincipal,ventanaSecundaria

    def mostrarCalculadora(self):
        calculadora = interface.Calculadora()
        ventanaCalculadora = calculadora.crearNuevaVentana("#E9B872")
        inicial = '7'
        botonesCalculadora = ['Es primo','Primos entre 2 numeros','CalcularNprimos']
        comandosCalculadora = [calculadora.activarEsPrimo,calculadora.activarPrimosIntervalo,\
        calculadora.activarCalcularNprimos]
        calculadora.insertarImagen(ventanaCalculadora,nombreImagen="Img/calculadora.ppm")
        calculadora.entradaCalculadora(ventanaCalculadora,inicial)
        calculadora.crearMenu(ventanaCalculadora,botonesCalculadora,comandosCalculadora)
        return ventanaCalculadora

    def mostrarConceptos(self):
        conceptos = interface.Conceptos()
        ventanaConceptos = conceptos.crearNuevaVentana("#E9B872")
        botonesConceptos = ['Curiosidades','Teoremas']
        listaCuriosidades = ['Descomposicion','Equivalente']
        comandoCuriosidades = partial(conceptos.crearMenuTitulos,listaCuriosidades)
        listaConjeturas = ['Fundamental','Eratostenes']
        comandoConceptos = partial(conceptos.crearMenuTitulos,listaConjeturas)
        comandosConceptos = [comandoCuriosidades,comandoConceptos]
        conceptos.crearMenu(ventanaConceptos,botonesConceptos,comandosConceptos)
        return ventanaConceptos

if __name__=="__main__":
   numpriAplicacion = AplicacionPrincipal()
   numpriAplicacion.mostrarAplicacion()








