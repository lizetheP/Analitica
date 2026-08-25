class Articulo:
    def __init__(self, codigo, nombre, anio, disponible, costo):
        self.codigo = codigo
        self.nombre = nombre
        self.anio = anio
        self.disponible = disponible
        self.costo = costo
    
    def calcularPrecio(self):
        pass

    def mostrar(self):
        print("Código: " + self.codigo + ", Nombre: " + self.nombre)
        print("Año: " + str(self.anio) + ", Disponible: " + str(self.disponible) + ", Costo: " + str(self.costo))
        

def main():
    a = Articulo("NGhwX23", "National Geographic", "2023", True, 94.36)
    print()
    print("ARTÍCULO")
    a.mostrar()
    
main()  
