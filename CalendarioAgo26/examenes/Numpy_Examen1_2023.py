# Leer datos 2
import numpy as np
import pandas as pd
import csv

def leer_datos():
  df = pd.read_csv("videojuegos.csv")
  #print(df)
  # Crear una matriz en numpy
  matriz = np.array(df.values)
  #print(matriz)
  return matriz

def calificacion_mas_baja(m):
    lista = (m[:, 2])  # Extrae la columna 3 de tamaño
    l = np.array(lista, dtype = float)
    return np.min(l)

def calificacion_mas_alta(m):
    lista = (m[:, 2])  # Extrae la columna 3 de tamaño
    l = np.array(lista, dtype = float)
    return np.max(l)

def precio_promedio(m):
    lista = (m[:, 3])  # Extrae la columna 3 de tamaño
    l = np.array(lista, dtype = float)
    return np.mean(l)

def por_anio(m):
    lista = m[:, 0]
    myList = list(set(lista))
    #print(myList)
    myList.sort()
    print("\nAño \t Videojuegos")  
    for key in myList:
        condicion = ((m[:, 0]) == key)
        matriz = m[condicion]
        #print(matriz)
        arreglo = matriz[:, 1]
        #print(arreglo)
        print(key, "  \t", arreglo)
        
def por_clasificacion(m):
    lista = m[:, 4]
    rating = {'E': "Everyone" , 'T' : "Teen", 'M' : "Mature"}
    print("\nClasificación \t Videojuegos")  
    for key in rating:
        condicion = ((m[:, 4]) == key)
        matriz = m[condicion]
        #print(matriz)
        arreglo = matriz[:, 1]
        print(key, rating[key],"    \t", arreglo)

def por_review(m):
    lista = m[:, 2]
    myList = list(set(lista))
    #print(myList)
    myList.sort()
    print("\nReview \t Videojuegos")  
    for key in myList:
        condicion = ((m[:, 2]) == key)
        matriz = m[condicion]
        arreglo = matriz[:, 1]
        print(key, "  \t", arreglo)

def promedio_precio(m):
    lista = m[:, 4]
    rating = {'E': "Everyone" , 'T' : "Teen", 'M' : "Mature"}
    print("\nClasificación \t Promedio de precios")  
    for key in rating:
        condicion = ((m[:, 4]) == key)
        matriz = m[condicion]
        #print(matriz)
        arreglo = matriz[:, 3]
        promedio = np.mean(arreglo)
        print(key, rating[key],"    \t %.2f" % promedio)

def promedio_review(m):
    lista = m[:, 4]
    rating = {'E': "Everyone" , 'T' : "Teen", 'M' : "Mature"}
    print("\nClasificación \t Promedio de calificación")  
    for key in rating:
        condicion = ((m[:, 4]) == key)
        matriz = m[condicion]
        #print(matriz)
        arreglo = matriz[:, 2]
        promedio = np.mean(arreglo)
        print(key, rating[key],"    \t %.2f" % promedio)
        
def cantidad_videojuegos(m):
    lista = (m[:, 0])
    # El método set elimina elementos repetidos de una lista, tupla o string.
    myList = list(set(lista))
    #print(myList)
    myList.sort()
    #print(myList)
    print()
    print("Año", "\t", "#Videojuegos")
    for ele in myList:
        condicion = (m[:, 0] == ele)
        matriz = m[condicion]
        longitud = matriz.shape[0]
        print(ele, "  \t", longitud)

def main():
    m = leer_datos()
    #print(m)
    print()
    #print("La calificación más baja es:", calificacion_mas_baja(m))
    #print("La calificación más alta es:", calificacion_mas_alta(m))
    print("El precio promedio es: %.2f" % precio_promedio(m))
    por_anio(m)
    #por_clasificacion(m)
    #por_review(m)
    #promedio_precio(m)
    #cantidad_videojuegos(m)
    #promedio_review(m)
  
main()

"""

def promedio_precio(m):
    lista = m[:, 4]
    rating = {'E': "Everyone" , 'T' : "Teen", 'M' : "Mature"}
    print("\nClasificación \t Promedio de precios")  
    for key in rating:
        condicion = ((m[:, 4]) == key)
        matriz = m[condicion]
        #print(matriz)
        arreglo = matriz[:, 3]
        promedio = np.mean(arreglo)
        print(key, rating[key],"    \t %.2f" % promedio)

def por_anio(m):
    lista = m[:, 0]
    myList = list(set(lista))
    print(myList)
    myList.sort()
    print("\nAño \t Videojuegos")  
    for key in myList:
        condicion = ((m[:, 0]) == key)
        matriz = m[condicion]
        arreglo = matriz[:, 1]
        print(key, "  \t", arreglo)


def main():
    m = leer_datos2()
    print(m)
    print("La calificación más baja es:", calificacion_mas_baja(m))
    print("La calificación más alta es:", calificacion_mas_alta(m))
    print("El precio promedio es: %.2f" % precio_promedio(m))
    por_anio(m)
    por_clasificacion(m)
    por_review(m)
    promedio_precio(m)
  
main()

def leer_datos():
    nombre_archivo = "videojuegos.csv"
    file = open("videojuegos.csv", "r")
    # Se crea un leector con csv.reader
    lector = csv.reader(file, delimiter=",") # Le pasamos el archivo y el delimitador
    #Omitir el encabezado
    next(lector, None)
    matriz = []
    for lista in lector: # Leemos línea por línea del lector como una lista
        # Tenemos la lista. En la 0 tenemos el nombre, en la 1 la calificación y en la 2 el precio
        matriz.append(lista)
    #print(matriz)
    return matriz

def imprime_matriz(m):
    for ren in range(m.shape[0]): # Renglones
        print(ren, end=" ")
        for col in range(m.shape[1]):
            print(m[ren, col], end=" ")
        print()

def imprime_matriz2(m):
    lista = ["Adobo", "Condimento", "Especia", "Hierba"]
    cont = 0
    print("\t\t Precio promedio Suma productos Tamaño máximo envase")
    for ren in range(m.shape[0]): # Renglones
        print(lista[cont], end=" ")
        cont = cont + 1
        for col in range(m.shape[1]):
            print("  \t %.1f " % m[ren, col], end=" ")
        print()
        
def envase_mas_peque(m):
    lista = (m[:, 4])  # Extrae la columna 4 de tamaño
    l = np.array(lista, dtype = int)
    return np.amin(l)

def envase_mas_grande(m):
    lista = (m[:, 4])  # Extrae la columna 4 de tamaño
    l = np.array(lista, dtype = int)
    return np.amax(l)

def precio_mas_alto(m):
    lista = (m[:, 3])  # Extrae la columna 3 de tamaño
    l = np.array(lista, dtype = float)
    return np.amax(l)

def suma_productos(m):
    lista = (m[:, 2]) # Extrae la columna 2 de cantidad en existencia
    #print(lista)
    l = np.array(lista, dtype = int)
    return np.sum(l)
     
def cantidad_productos(m):
    lista = (m[:, 6])
    # El método set elimina elementos repetidos de una lista, tupla o string.
    myList = list(set(lista))
    print(myList)

    myList.sort()
    #print(myList)
    print()
    print("Categoria", "\t", "#Productos")
    for ele in myList:
        condicion = (m[:, 6] == ele)
        matriz = m[condicion]
        longitud = matriz.shape[0]
        print(ele, "  \t", longitud)

def promedio_tamaño(m):
    envase = {'1': "Frasco" , '2' : "Sobre", '3' : "Botella", '4' : "Lata"}
    print("\nTipo envase \t Promedio tamaño")  
    for key in envase:
        condicion = ((m[:, 5]) == key)
        matriz = m[condicion]
        #print(matriz)
        listaf = matriz[:, 4]
        #print(listaf)
        l = np.array(listaf, dtype = int)
        if len(l) > 0:
            promedio = np.mean(l)
        else:
            promedio = 0
        print("%c. %s \t %.2f onzas" % (key, envase[key], promedio))
              
def promedio_precios(m):
    lista = (m[:, 3])
    #print(lista)
    l = np.array(lista, dtype = float)
    return np.mean(l)

def calculos(m, envase):
    matrizf = []
    lcondimentos = ["Adobo", "Condimento", "Especia", "Hierba"]
    for ele in lcondimentos:
        condicion = (m[:, 6] == ele) & (m[:, 5] == envase)
        matriz = m[condicion]
        #print(matriz)
        lista = []
        #"PRECIO PROMEDIO"
        print("Adobo, precio promedio, suma productos, tamaño envase")
        l_precio = matriz[:, 3]
        #print(l_precio)
        l = np.array(l_precio, dtype = float)
        if len(l) > 0:
            precio_promedio = np.mean(l)
        else:
            precio_promedio = 0
        #print("Precio promedio", precio_promedio)
        lista.append(precio_promedio)
    
        # SUMA PRODUCTOS
        l_suma = matriz[:, 2]
        #print(l_suma)
        l = np.array(l_suma, dtype = int)
        suma = np.sum(l)
        #print("Suma millajes", suma)
        lista.append(suma)

        # TAMAÑO MÁXIMO ENVASE
        l_max = matriz[:, 4]
        #print(l_max)

        l = np.array(l_max, dtype = int)
        maximo = np.amax(l)
        #print("Impuesto máximo", maximo)
        lista.append(maximo)
        #print(lista)
        matrizf.append(lista)
    return matrizf    

def main():
    matriz = leer_datos()
    #print(matriz)
    # Crea una matriz en numpy
    m = np.array(matriz)
    #imprime_matriz(m)
    res = envase_mas_peque(m)
    print("El envase de menor tamaño es de %i onzas" % res)
    res = envase_mas_grande(m)
    print("El envase de mayor tamaño es de %i onzas" % res)
    res = precio_mas_alto(m)
    print("El precio más alto de un prducto es de %.2f dólares" % res)
    res = suma_productos(m)
    print("La cantidad de productos en existencia es:", res)
    cantidad_productos(m)
    promedio_tamaño(m)
    res = promedio_precios(m)
    print("El promedio de precios de los productos es %.2f" % res)
    print("\nCONDIMENTOS  Envase: Frasco")
    mF = calculos(m, 1)
    mFrascos = np.array(mF)
    #print(mFrascos)
    imprime_matriz2(mFrascos)
    print("\nCONDIMENTOS  Envase: Sobre")
    mF = calculos(m, 1)
    mFrascos = np.array(mF)
    #print(mFrascos)
    imprime_matriz2(mFrascos)
"""
