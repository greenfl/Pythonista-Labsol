#! /usr/bin/python3
# -*- coding: utf-8 -*-
import caso.datos as datos


def despliega_uno(elemento):                                      #Asigna parametro elemento = {'Nombre': 'Eduardo', 'Primer Apellido': 'Sánchez', 'Segundo Apellido': 'Ramos', 'Carrera': 'Sistemas', 'Semestre': 6, 'Promedio': 7.5, 'Al Corriente': True}
    for campo in datos.orden:                                     #Para cada elemento de la tupla despliega la clave y el valor asociado
        print(campo + ": " + str(elemento[campo]))                #Despliega "Nombre: Eduardo,luego Primer Apellido : Sanchez, ... etc"


def despliega_todos():                                            # Funcion despliega todos
    contador = 0                                                  # Despliega Alumno: 1
    for alumno in datos.alumnos:
        contador += 1
        print("\nAlumno: ", contador)
        despliega_uno(alumno)                                     # Se pasa el diccionario 0 de la lista como elemento. y lo hace hasta que encuentre todos los elementos de alumnos (depende de cuantos alumnos se haya insertado)