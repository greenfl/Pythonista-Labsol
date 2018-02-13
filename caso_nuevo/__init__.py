#! /usr/bin/python3
# -*- coding: utf-8 -*-

"""Ejemplo de modulos en el curso de Python"""
import caso_nuevo.altas as altas
import caso_nuevo.archivos as archivos

def principal():
    while True:
        try:
            alumnos = input("Número de alumnos:")
            alumnos = int(alumnos)
            print()
        except (ValueError) as error:
            print(error)
            continue
        else:
            break
    for contador in range(alumnos):
        print("\nAlumno nuevo", contador + 1)
        archivos.agrega_uno(altas.alta())         #Agrega el registro dado de alta al archivo de texto
    archivos.despliega_todos()
    