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
    patron = "(https?:\/\/)?(www\.)?[a-zA-Z0-9.-_]+\.(com|net|com)(.mx)?"
    if re.match(patron, url) != None:
        return True
    else:
        return False

def es_valida_fecha(fecha):
    patron = "\d{2}-\d{2}-\d{4}"
    if re.match(patron, fecha) != None:
        return True
    else:
        return False
    
def main():
    texto = input("Dame un texto: ")
    #resultado = re.sub(r"\\n", "<br>", texto)
    #print("El nuevo texto es: ", resultado)
    resultado = re.sub(r"[\s.]", "-", texto)
    print("El nuevo texto es: ", resultado)
    
    
main()

#\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}
#^(https?:\/\/)?(www\.)?[a-zA-Z0-9.-]+\.(com|com\.mx|net)
#^(https?:\/\/)?(www\.)[a-zA-Z0-9.-_]+\.(com|net|com\.mx)$