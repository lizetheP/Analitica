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
        return self.costo * 1.2
    
    def mostrar(self):
        print("Código: " + self.codigo + ", Titulo: " + self.titulo + ", Año: " + str(self.anio))
        print("Disponible: " + str(self.disponible) + ", Costo: " + str(self.costo))
        print("Protagonistas: " + self.getInterprete() + ", Resolucion: " + str(self.getFormato()))

class CVerificador:
    
    def __init__(self, codigo):
        self.codigo = codigo
    
    def verificaResolucion(self):
        patron = "^(1|2)\d{3}[a-z]$"
        if re.match(patron, self.codigo) != None:
            return True
        else:
            return False
     
def main():
    resolucion = input("Introduce la resolución: ")
    v = CVerificador(resolucion)
    print("Es válida la resolución:", v.verificaResolucion())
    if v.verificaResolucion() == True:
        m = Musica("BAB2023", "Babylon", "2023", True, 182, "Margot Robbie y Brad Pitt", resolucion)
        print()
        print("PELICULA")
        m.mostrar()
    else:
        print("La resolución es incorrecta")
        
main()  