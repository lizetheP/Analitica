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
    
    def calcula_precio(self):
        return self.costo * 1.10
    
    def mostrar(self):
        print("\nLIBRO")
        print("Código: " + self.codigo + ", Titulo: " + self.titulo + ", Año: " + str(self.anio))
        print("Disponible: " + str(self.disponible) + ", Costo: " + str(self.costo))
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
    
    def calcula_precio(self):
        return self.costo * 1.15
    
    def mostrar(self):
        print("\nMUSICA")
        print("Código: " + self.codigo + ", Titulo: " + self.titulo + ", Año: " + str(self.anio))
        print("Disponible: " + str(self.disponible) + ", Costo: " + str(self.costo))
        print("Intérprete: " + self.getInterprete() + ", Formato: " + str(self.getFormato()))

class CVerificador:
    
    def __init__(self, codigo, nombre, anio):
        self.codigo = codigo
        self.nombre = nombre
        self.anio = anio
    
    def verificaCodigo(self):
        patron = "^[A-Z][A-Za-z]+\d{3}$"
        if re.match(patron, self.codigo) != None:
            return True
        else:
            return False
     
    def verificaNombre(self):
        patron = "^[A-Z][A-Za-z0-9áéíóúÁÉÍÓÚ\s]+$"
        if re.match(patron, self.nombre) != None:
            return True
        else:
            return False
    
    def verificaAnio(self):
        patron = "(19\d{2})|(20[01][0-9])|(202[12])"
        if re.match(patron, self.anio) != None:
            return True
        else:
            return False

def main():
    codigo = input("Introduce el código: ")
    nombre = input("Introduce el nombre: ")
    anio = input("Introduce el anio: ")
    v = CVerificador(codigo,nombre, anio)
    print("Es válido el código: ", v.verificaCodigo())
    print("Es válido el nombre: ", v.verificaNombre())
    print("Es válido el año: ", v.verificaAnio())
    if v.verificaCodigo() == True and v.verificaNombre() == True and v.verificaAnio() == True:
        a = Articulo(codigo, "Harry Potter y la piedra filosofal", "1997", True, 621)
        a.mostrar()
    
        l = Libro("A52430", "Harry Potter y la piedra filosofal", "1997", True, 621, "J. K Rowling", 309)
        l.mostrar()
        precio = l.calcula_precio()
        print("El precio del libro es: %.2f" % precio)
    
        m = Musica("MU21987", "The Joshua Tree", "1987", True, 3200, "U2", "DVD")
        m.mostrar()
        precio = m.calcula_precio()
        print("El precio del disco es: %.2f" % precio)
    else:
        print("El código es incorrecto")
        
main()  
