import re

class Articulo:
    def __init__(self, codigo, titulo, anio, disponible, costo):
        self.codigo = codigo
        self.titulo = titulo
        self.anio = anio
        self.disponible = disponible
        self.costo = costo
    
    def calcularPrecio(self):
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

class Musica(Articulo):
    def __init__(self, codigo, titulo, anio, disponible, costo, interprete, formato):
        self.__interprete = interprete
        self.__formato = formato
        super().__init__(codigo, titulo, anio, disponible, costo)
    
    def getInterprete(self):
        return self.__interprete
    
    def getFormato(self):
        return self.__formato
    
    def setInterprete(self, interprete):
        self.__interprete = interprete
    
    def setFormato(self, formato):
        self.__formato = formato
    
    def calcularPrecio(self):
        return self.costo * 1.15
    
    def mostrar(self):
        print("Código: " + self.codigo + ", Titulo: " + self.titulo + ", Año: " + str(self.anio))
        print("Disponible: " + str(self.disponible) + ", Costo: " + str(self.costo))
        print("Intérprete: " + self.getInterprete() + ", Formato: " + str(self.getFormato()))

class CVerificador:
    
    def __init__(self, codigo):
        self.codigo = codigo
    
    def verificaCodigo(self):
        patron = "^[A-Z][A-Za-z]+\d{4}$"
        if re.match(patron, self.codigo) != None:
            return True
        else:
            return False
     
def main():
    codigo = input("Introduce el código: ")
    v = CVerificador(codigo)
    print("Es válido el código:", v.verificaCodigo())
    if v.verificaCodigo() == True:
        b = Libro(codigo, "Harry Potter y la piedra filosofal", "1997", True, 621, "J. K Rowling", 309)
        print("LIBRO")
        b.mostrar()
    else:
        print("El código es incorrecto")
        
main()  
