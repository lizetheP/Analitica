import csv
import numpy as np

def leer_datos():
    nombre_archivo = "inventario.csv"
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
            print("Precio promedio  Suma de los millajes  Impuesto máximo")
            m2 = calculos3(m, '2018')
            m2018 = np.array(m2)
            print(m2018)
        elif opcion == 7:
            print("Adiós")
            continua = False
        else:
            print("Opción inválida")
"""     
main()

"""
    El impuesto máximo pagado por un automóvil
    La suma de impuestos pagados por ese lote de automóviles
    La cantidad de autos de cada año
    La promedio de millas de cada tipo de combustible
    El millaje por galón promedio del lote de autos
"""