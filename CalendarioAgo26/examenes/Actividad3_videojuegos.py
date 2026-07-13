import csv
import numpy as np

def leer_datos():
    nombre_archivo = "videojuegos.csv"
    file = open(nombre_archivo, "r")
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

def impuesto_maximo1(m):
    lista = []
    for ren in range(m.shape[0]): # Renglones
        for col in range(m.shape[1]):
            if col == 5:
                lista.append(m[ren, col])
    l = np.array(lista, dtype = int)
    return np.amax(l)
    
def impuesto_maximo2(m):
    lista = []
    for ren in range(m.shape[0]): # Renglones
        lista.append(m[ren, 5])
    l = np.array(lista, dtype = int)
    return np.amax(l)

def impuesto_maximo3(m):
    mayor = m[0, 5]
    for ren in range(m.shape[0]): # Renglones
        if m[ren, 5] > mayor:
            mayor = m[ren, 5]
    return mayor

def suma_impuestos(m):
    suma = 0
    for ren in range(m.shape[0]): # Renglones
        suma = suma + int(m[ren, 5])
    return suma

def cantidad_autos(m):
    lista = []
    for ren in range(m.shape[0]): # Renglones
        if m[ren, 0] not in lista:
            lista.append(m[ren,0])
    lista.sort()
    print(lista)
    diccionario = {}
    for ele in lista:
        diccionario.setdefault(ele, 0)
    print(diccionario)
    for key in diccionario:
        cont = 0
        for ren in range(m.shape[0]): 
            if m[ren, 0] == key:
                cont = cont + 1
        diccionario[key] = cont
    print(diccionario)
    print("Año  #Autos")
    for key in diccionario:
        print("%s : %i" % (key, diccionario[key]))
        
def promedio_millas(m):
    diccionario = {}
    for ele in range (1, 6):
        diccionario.setdefault(ele, 0)
    for key in diccionario:
        suma = 0
        cont = 0
        for ren in range(m.shape[0]):
            if int(m[ren, 4]) == key:
                suma = suma + float(m[ren, 3])
                cont = cont + 1
        promedio = suma / cont
        diccionario[key] = promedio
    print(diccionario)

    print("Tipo combustible : Promedio millas")
    for key in diccionario:
        print("%i : %.2f" % (key, diccionario[key]))

def millage_promedio(m):
    suma = 0
    cont = 0
    for ren in range(m.shape[0]): # Renglones
        suma = suma + float(m[ren, 6])
        cont = cont + 1
    return suma/cont

def menu():
    print()
    print("1. El impuesto máximo pagado por un automóvil")
    print("2. La suma de impuestos pagados por ese lote de automóviles")
    print("3. La cantidad de autos de cada año")
    print("4. El promedio de millas de cada tipo de combustible")
    print("5. El millaje por galón promedio del lote de autos")
    
def main():
    matriz = leer_datos()
    #print(matriz)
    # Crea una matriz en numpy
    m = np.array(matriz)
    imprime_matriz(m)
    continua = True
    while continua == True:
        menu()
        opcion = int(input("Introduce una opción: "))
        if opcion == 1:
            res = impuesto_maximo3(m)
            print("El impuesto máximo es:", res)
        elif opcion == 2:
            res = suma_impuestos(m)
            print("Suma de impuestos del lote:", res)
        elif opcion == 3:
            cantidad_autos(m)
        elif opcion == 4:
            promedio_millas(m)
        elif opcion == 5:
            res = millage_promedio(m)
            print("Millage por galón promedio:", res)
        elif opcion == 6:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")
        
main()

"""
    El impuesto máximo pagado por un automóvil
    La suma de impuestos pagados por ese lote de automóviles
    La cantidad de autos de cada año
    La promedio de millas de cada tipo de combustible
    El millaje por galón promedio del lote de autos
"""