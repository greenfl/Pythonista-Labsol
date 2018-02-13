import caso.datos as datos
""" Script de busqueda """
def buscarpor(cadena): #Se ingresa un argumento tipo String     1er función
    print("Coincidencias encontradas:".center(120))
    for registrodic in datos.alumnos:  #Obtiene todos los registros(dics) de la lista
        encontrar(registrodic,cadena)  #Se compara el registro obtenido con la cadena

def encontrar(registrodic,cadena):        #2da función
    buscapor = ("Nombre","Primer Apellido", "Segundo Apellido") #Elementos por lo que buscará
    for campoabuscar in buscapor:                               #Buscará el nombre que coincida
        if cadena.lower() in registrodic[campoabuscar].lower(): #Se hace coincidir la cadena con Nombre,Primer Apellido y Segundo Apellido  
            despliega_uno(registrodic)                        #Si la cadena esta dentro regresa True y despliega los dic's coincidentes
            print("\n")
def despliega_uno(registrodic):        # 3er función
    lista = []
    for campo in datos.orden:          # Despliega el campo y los registros coincidentes 
         lista.extend([campo+":"+ str(registrodic[campo])])
    tupla = tuple(lista)
    print(tupla)