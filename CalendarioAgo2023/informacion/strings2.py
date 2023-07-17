cadena = "Computacion"
sub_cadena = cadena[0 : 3]
print(sub_cadena)

sub_cadena = cadena[ : 3]
print(sub_cadena)

sub_cadena = cadena[3]
print(sub_cadena)

sub_cadena = cadena[6 : ]
print(sub_cadena)

sub_cadena = cadena[-6 : ]
print(sub_cadena)

res = cadena.find('o')
print(res)

cadena2 = cadena.replace('o', 'u')
print(cadena2)

cadena2 = cadena.upper()
print(cadena2)

cadena2 = cadena.lower()
print(cadena2)

cadena = "C o m p u t a c i o n"
cadena2 = cadena.split(" ") 
print(cadena2)

cadena = "C o m p u t a c i o n"
cadena2 = cadena.split(' ')
print(cadena2)



"""
print(cadena.find('o'))
print(cadena.replace('o', 'u'))
print(cadena.upper())
print(cadena.lower())
print(cadena.capitalize())
print('u' in cadena)"""