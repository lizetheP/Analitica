import re

texto = "(442)-442-153-32-42"

resultado = re.sub("\D", "", texto)
print(resultado)