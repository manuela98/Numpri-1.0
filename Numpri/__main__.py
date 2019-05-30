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
        comandoOpcionCalculadora = partial(AplicacionPrincipal.mostrarCalculadora,self)
        aplicacion.ponerBoton(ventanaSecundaria,'Calculadora',comando=comandoOpcionCalculadora)
        aplicacion.ponerBoton(ventanaSecundaria,'Juego',comando=ventanaSecundaria.iconify)
        comandoOpcionConceptos = partial(AplicacionPrincipal.mostrarConceptos,self)
        aplicacion.ponerBoton(ventanaSecundaria,'Conceptos',comando=comandoOpcionConceptos)
        ventanaPrincipal.mainloop()

    def mostrarCalculadora(self):
        calculadora = interface.Calculadora()
        ventanaCalculadora = calculadora.crearNuevaVentana("#E9B872")
        botonesCalculadora = ['Es primo','Primos entre 2 numeros','CalcularNprimos']
        comandosCalculadora = [calculadora.activarEsPrimo,calculadora.activarPrimosIntervalo,\
        calculadora.activarCalcularNprimos]
        calculadora.insertarImagen(ventanaCalculadora,nombreImagen="Img/calculadora.ppm")
        calculadora.crearMenu(ventanaCalculadora,botonesCalculadora,comandosCalculadora)
        return ventanaCalculadora

    def mostrarConceptos(self):
        conceptos = interface.Conceptos()
        ventanaConceptos = conceptos.crearNuevaVentana("#E9B872")
        botonesConceptos = ['Curiosidades','Conjeturas']
        lista = ['Titulos1','Titulos2']
        comandoOpcion = partial(conceptos.crearMenuTitulos,lista)
        comandosConceptos = [comandoOpcion,comandoOpcion]
        conceptos.crearMenu(ventanaConceptos,botonesConceptos,comandosConceptos)
        return ventanaConceptos

if __name__=="__main__":
   numpriAplicacion = AplicacionPrincipal()
   numpriAplicacion.mostrarAplicacion()








