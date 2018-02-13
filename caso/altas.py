#! /usr/bin/python3
# -*-coding: utf-8 -*-
import caso.datos as datos
import caso.valida as valida     
"""Módulo que contiene la funcion de altas."""
""""""


def alta():
    """Realiza las altas."""
    
    
    def ingresa(campo): #se asigna un parametro campo
        while True:
            mensaje = "Ingrese " + campo.lower() + ": " #  Guarda en identificador mensaje el objeto "Ingrese + campo en minuscula :" 
            dato = input(mensaje)                       #  Muestra la cadena y el teclado , se almacena en el identificador dato como cadena 
            print ("Ingresa:", datos.campos[campo](dato))
        

            if datos.campos[campo] != str:              #  Si los valores de la clave , correspondiente ala pregunta son clase Int,Bool o float entonces:
                try:                                              # identificación de codigo susceptible a errores
                    if eval(dato) == datos.campos[campo](dato):   #  Se evalua la respuesta  p/e 123 es igual a un campo que no existe entonces se regresa
                        dato = datos.campos[campo](dato)
                    else:
                        continue
                except:                                           # Si ocurre una excepción regresa de nuevo
                    continue                    
            if valida.reglas(dato, campo):                        # Si se valida el dato y el campo entonces es True, regresa dato
                return dato   
    return {campo: ingresa(campo) for campo in datos.orden}  # regresa true o false, si se inserto o no