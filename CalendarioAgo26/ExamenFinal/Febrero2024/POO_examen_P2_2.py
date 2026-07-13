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
        return self.costo * 1.15
    
    def mostrar(self):
        print("Código: " + self.codigo + ", Titulo: " + self.titulo)
        print("Año: " + str(self.anio) + ", Disponible: " + str(self.disponible) + ", Costo: " + str(self.costo))
        print("Intérprete: " + self.getInterprete() + ", Formato: " + str(self.getFormato()))

def main():
    m = Musica("TJOTREE1987", "The Joshua Tree", "1987", True, 1200, "U-2", "CD")
    print("\nMUSICA")
    m.mostrar()
    print()
    precio = m.calcularPrecio()
    print("El precio del disco es: %.2f" % precio)
    print()
    autor = input("Dame el nombre del intérprete: ")
    formato = input("Dame el formato: ")
    m.setInterprete(autor)
    m.setFormato(formato)
    print("MUSICA")
    m.mostrar()
            
main()  
