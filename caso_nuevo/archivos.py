#! /usr/bin/python3
# -*- coding: utf-8 -*-
import caso_nuevo.datos as datos


def despliega_uno(elemento):
    for campo in datos.orden:
        print(campo + ": " + str(elemento[campo]))

        
def despliega_todos(ruta=datos.ruta):
    with open(ruta, 'r') as archivo:                    # Abre la ruta del archivo en modo seguro de text en modo lectura y despliega todos (uno por uno)
        contador = 0
        for alumno in archivo:
            alumno = eval(alumno)
            contador += 1
            print("\nAlumno: ", contador)
            despliega_uno(alumno)
        
        
def agrega_uno(elemento, ruta=datos.ruta):                            # Agrega el elemento dado de alta al archivo
    with open(ruta, 'a') as archivo:                                  # Abrir en modo seguro el archivo en modo escritura, escribiendo al final el registro
        archivo.writelines(str(elemento) + '\n')