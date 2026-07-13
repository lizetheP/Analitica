import re

texto = "https://laurasanchezperez.com.mx"

resultado = re.search("^(https?:\/\/)?\w+.com.mx", texto)
print(resultado)
if resultado != None:
    print("url válida")
else:
    print("url inválida")
    
