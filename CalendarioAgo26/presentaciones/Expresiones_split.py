import re

texto = """Podrá nublarse el sol eternamente; 
Podrá secarse en un instante el mar; 
Podrá romperse el eje de la tierra 
como un débil cristal. 
¡todo sucederá! Podrá la muerte 
cubrirme con su fúnebre crespón; 
Pero jamás en mí podrá apagarse 
la llama de tu amor."""

# Dividir el texto por caracteres que no son alfanuméricos

lista = re.split("\W+", texto)
print(lista)