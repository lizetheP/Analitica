import re
texto2 = """Hola Mundo.
Me gusta Python!!!!
Mi numero telefonico de casa es 442-130-45-12
Mi numero telefonico de celular es 442-241-37-46
Mi numero telefonico de oficina es 442-380-14-28"""

texto3 = """Juan López: 442-230-15-24 Bernardo Quintana 200
Pedro Pérez: 447-130-18-35 Epigmenio González 500
Luis Ramírez: 448-730-48-17 Carretas 150"""

# Extraer números telefónicos cuya lada sea 442 y que el número comience con 1 o 2

print(re.findall("44[12]", texto2, flags = re.M))
print(re.split("\n+", texto3))
lista = re.split("\n+", texto3)
for entrada in lista:
    print(re.split(":? ", entrada, 5))
