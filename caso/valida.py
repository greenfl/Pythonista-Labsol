#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""script valida"""
import caso.datos as datos

def reglas(dato, campo):
    print("El dato de valida es:",dato, " El campo de valida es: ",campo)
    if campo == "Carrera" and dato not in datos.carreras:   # Si el campo es igual a carrera y el dato no esta en carreras entonces regresa false
        return False                                        
    elif campo == "Semestre" and dato < 1:                  # Si el campo es igual a semestre y dato es menor que 1 regresa false
        return False
    elif campo == "Promedio" and (dato < 0 or dato > 10):   # Si el campo es igual a promedio y dato es menor que 0 o mayor que 10 entonces regresa false
        return False
    elif (campo in ("Nombre", "Primer Apellido") and (dato == "")):  # si el campo en nombre y Primer Apellido es vacio regresa false
        return False
    elif campo == "Segundo Apellido" and dato == "":              # Si el campo es igual a Segundo Apellido y es vacio entonces:
        while True:
            mensaje = "No ha ingresado el segundo apellido. ¿Es correcto? S/N: "        #Mientras sea verdad  Mostrar mensaje de confirmación de campo vacio y Teclado
            confirma = input(mensaje)                           
            if confirma.upper()  == "S":                                            #Si se confirma con s=S
                return True                                                        
            elif confirma.upper() == "N":                                           # Si se confirma n=N                    
                return False                                                       
    else:                                                         # Si se llenan todos los campos ya validados se retorna True
        return True
