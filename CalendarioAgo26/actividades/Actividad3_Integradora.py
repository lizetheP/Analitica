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

def envase_mas_peque(m):
    lista = (m[:, 4])  # Extrae la columna 4 de tamaño
    l = np.array(lista, dtype = int)
    return np.amin(l)

def envase_mas_grande(m):
    lista = (m[:, 4])  # Extrae la columna 4 de tamaño
    l = np.array(lista, dtype = int)
    return np.amax(l)

def suma_productos(m):
    lista = (m[:, 2]) # Extrae la columna 2 de cantidad en existencia
    print(lista)
    l = np.array(lista, dtype = int)
    return np.sum(l)

def cantidad_productos(m):
    lista = (m[:, 0])
    myList = list(set(lista)) 
    myList.sort()
    print(myList)
    for ele in myList:
        condicion = (m[:, 0] == ele)
        matriz = m[condicion]
        listaf = matriz[:, 0]
        longitud = len(listaf)
        print("%s : %i" % (ele, longitud))

def cantidad_productos1(m):
    lista = (m[:, 6])
    myList = list(set(lista)) 
    myList.sort()
    print(myList)
    diccionario = {}
    for ele in myList:
        diccionario.setdefault(ele, 0)
    print(diccionario)
    for key in diccionario:
        cont = 0
        for ren in range(m.shape[0]): 
            if m[ren, 6] == key:
                cont = cont + 1
        diccionario[key] = cont
    print(diccionario)
    print()
    print("Categoria", "\t", "#Productos")
    for key in diccionario:
        print(key,": \t ", diccionario[key])
        
def cantidad_productos2(m):
    lista = (m[:, 6])
    myList = list(set(lista)) 
    myList.sort()
    print(myList)
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
        print("%c. %s \t %.2f" % (key, envase[key], promedio))
        
def promedio_millas(m):
    fuelType = {'1': "Disel" , '2' : "Eléctrico", '3' : "Híbrido", '4' : "Otro", '5' : "Gasolina"}
    print("fuelType : promedioMillas")  
    for key in fuelType:
        condicion = ((m[:, 4]) == key)
        matriz = m[condicion]
        #print(matriz)
        listaf = matriz[:, 3]
        #print(listaf)
        l = np.array(listaf, dtype = int)
        if len(l) > 0:
            promedio = np.mean(l)
        else:
            promedio = 0
        print("%c. %s: \t %.2f" % (key, fuelType[key], promedio))
        
def millage_promedio(m):
    lista = (m[:, 3])
    print(lista)
    l = np.array(lista, dtype = float)
    return np.mean(l)

def calculos(m, year):
    matrizf = []
    transmission = ['1', '2', '3']
    for ele in transmission:
        condicion = (m[:, 2] == ele) & (m[:, 0] == year)
        matriz = m[condicion]
        #print(matriz)
        lista = []
   
        # PRECIO PROMEDIO"
        l_precio = matriz[:, 1]
        #print(l_precio)
        l = np.array(l_precio, dtype = int)
        if len(l) > 0:
            precio_promedio = np.mean(l)
        else:
            promedio = 0
        #print("Precio promedio", precio_promedio)
        lista.append(precio_promedio)
    
        # SUMA MILLAJES
        l_suma = matriz[:, 3]
        #print(l_suma)
        l = np.array(l_suma, dtype = int)
        suma = np.sum(l)
        #print("Suma millajes", suma)
        lista.append(suma)
    
        # IMPUESTO MAXIMO
        l_max = matriz[:, 5]
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
    print(matriz)
    # Crea una matriz en numpy
    m = np.array(matriz)
    #imprime_matriz(m)
    res = envase_mas_peque(m)
    print("El envase de menor tamaño es de %i onzas" % res)
    res = envase_mas_grande(m)
    print("El envase de mayor tamaño es de %i onzas" % res)
    res = suma_productos(m)
    print("La cantidad de productos en existencia es:", res)
    cantidad_productos1(m)
    cantidad_productos2(m)
    promedio_tamaño(m)
"""
        elif opcion == 3:
            cantidad_autos3(m)
        elif opcion == 4:
            promedio_millas3(m)
        elif opcion == 5:
            res = millage_promedio2(m)
            print("Millage por galón promedio: %.2f" % res)
        elif opcion == 6:
            print("Tipo transmisión 1, 2, 3  Año 2016")
            print("Precio promedio  Suma de los millajes  Impuesto máximo")
            m1 = calculos3(m, '2016')
            m2016 = np.array(m1, )
            print(m2016)
            print("Tipo transmisión 1, 2, 3  Año 2018")
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