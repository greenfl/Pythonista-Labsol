#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Ejemplo de modulos en el curso de Python"""
import caso.altas as altas        #renombrando modulo altas.py como altas  --- contiene: función alta que a su vez anida una función ingresa y valida el dato ingresado
import caso.listado as listado    #renombrando modulo listado.py como listado --- contiene: función despliega_uno y despliega_todos
import caso.datos as datos        #renombrando modulo datos.py como datos --- contiene: carreras,nombre,campos y alumnos

def principal():                    # definiendo la función principal
    while True:                     # mientras sea verdadero
        try:                        # identificación de codigo susceptible a errores
            alumnos = input("Número de alumnos:")   # Identificador alumnos se le asigna el objeto capturado por el teclado (tipo cadena) o la entrada estandar
            alumnos = int(alumnos)                  # El resultado de alumnos se convierte a tipo númerico entero
            print()
        except (ValueError) as error:                # Si no es posible convertir a numerico se gestiona la excepción
            print(error)                             # Despliega el error en caso de no ser númerico entero
            continue                                 # Continua la ejecución devolviendose al inicio
        else:                                        # Si el número que se inserto fue correcto entonces:
            break                                    # Acaba la función
    for contador in range(alumnos):                  # For para despliegue dependiendo del numero de alumnos que se inserte
        print("\nAlumno nuevo", contador + 1)        # Despliega "Alumno nuevo [0+1]"
        datos.alumnos.append(altas.alta())           # Se manda a llamar la función alta de altas y se escriben al final del dic de alumnos los datos de los alumnos
    listado.despliega_todos()                        # Se despliegan todos los alumnos de la lista mas los dado de alta -- fuera del for