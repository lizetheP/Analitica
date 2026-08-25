import re

def es_valida_IP(ip):
    patron = "(((25[0-5])|(2[0-4][0-9])|([01]?[0-9][0-9]?))\.){3}(((25[0-5])|(2[0-4][0-9])|([01]?[0-9][0-9]?)))"
    if re.match(patron, ip) != None:
        return True
    else:
        return False

def es_valido_correo(mail):
    patron = "[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-z][a-z]+"
    if re.match(patron, mail) != None:
        return True
    else:
        return False
    
def es_valida_url(url):
    patron = "r(https?:\/\/)?(www\.)[a-zA-Z0-9.-_]+\.(com|net|com\.mx)?"
    if re.match(patron, url) != None:
        return True
    else:
        return False

def es_valida_fecha(fecha):
    patron = "(0?[1-9]|[12][0-9]|3[01])\/(0?[1-9]|1[012])\/((19|20)\d\d)"
    if re.search(patron, fecha) != None:
        return True
    else:
        return False

texto = """
Laura Sánchez
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
www.juan_sanchez.net

https:/www.pedrop.com

01/09/2022
50/09/2022
10/30/2022
01/09/3022
2022/13/04
14/09/74
"""

def encuentra_fechas():
    patron = "(0?[1-9]|[12][0-9]|3[01])\/(0?[1-9]|1[012])\/((19|20)\d\d)"
    lista = re.findall(patron, texto, flags = re.M)
    print(lista)
    
def main():
    ip = input("Dame una IP: ")
    print("La ip es válida: ", es_valida_IP(ip))
    #correo = input("Dame tu correo: ")
    #print("El correo es válido: ", es_valido_correo(correo))
    #url = input("Dame tu url: ")
    #print("La url es válida: ", es_valida_url(url))
    #fecha = input("Dame tu fecha: ")
    #print("La fecha es válida: ", es_valida_fecha(fecha))
    #encuentra_fechas()
    
main()

#\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}
#^(https?:\/\/)?(www\.)?[a-zA-Z0-9.-]+\.(com|com\.mx|net)
#^(https?:\/\/)?(www\.)[a-zA-Z0-9.-_]+\.(com|net|com\.mx)$
#(0?[1-9]|[12][0-9]|3[01])\/(0?[1-9]|1[012])\/((19|20)\d\d) CORRECTO
"""
01/09/2022
50/09/2022
10/30/2022
01/09/3022
2022/13/04
14/09/74"""