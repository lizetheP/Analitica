import re

texto = """Laura Sánchez
442 153-32-42
lasanch@hotmail.com
http://www.laurasan.com

Pedro López
448 342 33 12
pedrolo54@gmail.com
https://www.pedro.lopez.com.mx

Violeta Pérez
443 214 43 72
violeta45@outlook.com
violeta.net
"""

print(re.findall("[a-zA-Z]", texto, flags=re.M ))