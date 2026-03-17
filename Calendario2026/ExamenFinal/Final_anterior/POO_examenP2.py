import re

class Articulo:
    def __init__(self, codigo, titulo, anio, disponible, costo):
        self.codigo = codigo
        self.titulo = titulo
        self.anio = anio
        self.disponible = disponible
        self.costo = costo
    
    def calcula_precio(self):
        pass

    def mostrar(self):
        print("\nARTÍCULO")
        print("Código: " + self.codigo + ", Titulo: " + self.titulo + ", Año: " + str(self.anio))
        print("Disponible: " + str(self.disponible) + ", Costo: " + str(self.costo))
        
class Libro(Articulo):
    def __init__(self, codigo, titulo, anio, disponible, costo, autor, noPaginas):
        self.__autor = autor
        self.__noPaginas = noPaginas
        super().__init__(codigo, titulo, anio, disponible, costo)
    
    def getAutor(self):
        return self.__autor
    
    def getnoPaginas(self):
        return self.__noPaginas
    
    def setAutor(self, autor):
        self.__autor = autor
    
    def setnoPaginas(self, noPaginas):
        self.__noPaginas = noPaginas
    
    def calcularPrecio(self):
        return self.costo * 1.10
    
    def mostrar(self):
        print("Código: " + self.codigo + ", Titulo: " + self.titulo)
        print("Año: " + str(self.anio) + ", Disponible: " + str(self.disponible) + ", Costo: " + str(self.costo))
        print("Autor: " + self.getAutor() + ", Número de páginas: " + str(self.getnoPaginas()))

def main():
    print("LIBRO")
    b = Libro("HPOPF1997", "Harry Potter y la piedra filosofal", "1997", True, 621, "J. K Rowling", 309)
    b.mostrar()
    precio = b.calcularPrecio()
    print()
    print("El precio del libro es: %.2f" % precio)
        
main()  
