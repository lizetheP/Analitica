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
        print("Código: " + self.codigo + ", Titulo: " + self.titulo)
        print("Año: " + str(self.anio) + ", Disponible: " + str(self.disponible) + ", Costo: " + str(self.costo))
        

def main():
    a = Articulo("BAB2023", "Babylon", "2023", True, 219)
    print()
    print("ARTÍCULO")
    a.mostrar()
    
main()  
