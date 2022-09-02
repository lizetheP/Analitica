import re
texto2 = """Hola Mundo.
Me gusta Python!!!!
Mi numero telefonico de casa es 442-130-45-12
Mi numero telefonico de celular es 442-241-37-46
Mi numero telefonico de oficina es 442-380-14-28"""

texto3 = """Juan López: 442-230-15-24 Bernardo Quintana 200
Pedro Pérez: 447-130-18-35 Epigmenio González 500
Luis Ramírez: 448-730-48-17 Carretas 150"""

texto = """Laura Sánchez
442-153-32-42
laura.sanch@hotmail-mx.com
http://www.laurasan.com

Pedro LÓPEZ
448 342 33 12
pedro-lopez54@gmail.com
https://www.pedro.lopez.com.mx

Violeta Pérez
123.214.43.72
violeta_45@outlook.com
www.violeta.net

Juan Sánchez
juan_sanchez@gmail.com.mx
345 234-34-12
www.juan_sanchez.net"""

# Extraer números telefónicos cuya lada sea 442 y que el número comience con 1 o 2

print(re.findall("(^(https?:\/\/)?(www\.)[a-zA-Z\.\-_]+\.(com|net|com\.mx)$)", texto, flags = re.M))
#print(re.findall("\d{3}[-.\s]\d{3}[-.\s]\d{2}[-.\s]\d{2}", texto, flags = re.M))
#print(re.findall("[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-z][a-z]+", texto, flags = re.M))


#print(re.split("\n+", texto3))
#lista = re.split("\n+", texto3)
#for entrada in lista:
#    print(re.split(":? ", entrada, 5))
