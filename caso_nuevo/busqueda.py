""" script busqueda"""
import caso_nuevo.datos as datos2
def buscarpor(cadena): #Se ingresa un argumento tipo String     1er función
    print("Coincidencias encontradas:".center(120))
    with open(datos2.ruta, 'r') as archivo:              #Abrimos en modo seguro de lectura
        for registrodic in archivo:  #Obtiene todos los registros(dics) de la list
            registrodic = eval(registrodic)
            encontrar(registrodic,cadena)  #Se compara el registro obtenido con la cadena

def encontrar(registrodic,cadena):        #2da función
    buscapor = ("Nombre","Primer Apellido", "Segundo Apellido") #Elementos por lo que buscará
    for campoabuscar in buscapor:                               #Buscará el nombre que coincida
        if cadena.lower() in registrodic[campoabuscar].lower(): #Se hace coincidir la cadena con Nombre,Primer Apellido y Segundo Apellido  
            despliega_uno(registrodic)                        #Si la cadena esta dentro regresa True y despliega los dic's coincidentes
            print("\n")
def despliega_uno(registrodic):        # 3er función
    lista = []
    for campo in datos2.orden:          # Despliega el campo y los registros coincidentes 
         lista.extend([campo+":"+ str(registrodic[campo])])
    tupla = tuple(lista)
    print(tupla)