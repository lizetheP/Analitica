import re

class Articulo:
    def __init__(self, codigo, nombre, anio, disponible, costo):
        self.codigo = codigo
        self.nombre = nombre
        self.anio = anio
        self.disponible = disponible
        self.costo = costo
    
    def calcula_precio(self):
        pass

    def mostrar(self):
        print("\nARTÍCULO")
        print("Código: " + self.codigo + ", Nombre: " + self.nombre + ", Año: " + str(self.anio))
        print("Disponible: " + str(self.disponible) + ", Costo: " + str(self.costo))
        
class Libro(Articulo):
    def __init__(self, codigo, nombre, anio, disponible, costo, titulo, noPaginas):
        self.__titulo = titulo
        self.__noPaginas = noPaginas
        super().__init__(codigo, nombre, anio, disponible, costo)
    
    def getTitulo(self):
        return self.__titulo
    
    def getnoPaginas(self):
        return self.__noPaginas
    
    def setTitulo(self, titulo):
        self.__titulo = titulo
    
    def setnoPaginas(self, noPaginas):
        self.__noPaginas = noPaginas
    
    def calcularPrecio(self):
        return self.costo * 1.08
    
    def mostrar(self):
        print("Código: " + self.codigo + ", Nombre: " + self.nombre)
        print("Año: " + str(self.anio) + ", Disponible: " + str(self.disponible) + ", Costo: " + str(self.costo))
        print("Titulo: " + self.getTitulo() + ", Número de páginas: " + str(self.getnoPaginas()))

def main():
    print("REVISTA")
    b = Libro("NGhXwY23", "National Geographic", "2023", True, 94.36, "La música nos hace más humanos", 32)
    b.mostrar()
    precio = b.calcularPrecio()
    print()
    print("El precio del libro es: %.2f" % precio)
    print()
    titulo = input("Dame el nombre del titulo: ")
    paginas = input("Dame el número de páginas: ")
    b.setTitulo(titulo)
    b.setnoPaginas(paginas)
    print()
    print("REVISTA")
    b.mostrar()
    
    
        
main()  
