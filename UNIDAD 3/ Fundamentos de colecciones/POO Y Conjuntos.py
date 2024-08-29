class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre


class Producto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.categorias = set()

    def agregar_categoria(self, categoria):
        self.categorias.add(categoria)

    def mostrar_categorias(self):
        for categoria in self.categorias:
            print(categoria.nombre)


# Ejemplo de uso
producto = Producto("Laptop")
producto.agregar_categoria(Categoria("Electrónica"))
producto.agregar_categoria(Categoria("Computadoras"))
producto.agregar_categoria(Categoria("Oficina"))

print("Categorías del producto:")
producto.mostrar_categorias()
