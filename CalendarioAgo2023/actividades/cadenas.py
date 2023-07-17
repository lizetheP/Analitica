def reemplaza(cadena, l1, l2):
    cadena2 = cadena.replace(l1, l2)
    return cadena2

frase = "Hola a todos"
a = 'a'
b = '*'
res = reemplaza(frase, a, b)
print(res)