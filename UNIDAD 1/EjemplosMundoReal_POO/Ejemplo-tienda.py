# Definición de la clase Producto
class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio} - Stock disponible: {self.stock}"

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Venta realizada: {cantidad} unidades de {self.nombre}.")
        else:
            print(f"No hay suficiente stock de {self.nombre}. Stock disponible: {self.stock}")

    def reponer_stock(self, cantidad):
        self.stock += cantidad
        print(f"Se agregaron {cantidad} unidades al stock de {self.nombre}. Stock actualizado: {self.stock}")


# Ejemplo de uso del sistema de gestión de productos en una tienda
if __name__ == "__main__":
    # Crear productos
    producto1 = Producto("001", "Camiseta", 20.0, 50)
    producto2 = Producto("002", "Pantalón", 35.0, 30)

    # Mostrar información inicial de los productos
    print(producto1)
    print(producto2)

    # Vender productos
    producto1.vender(10)
    producto2.vender(5)

    # Reponer stock
    producto1.reponer_stock(20)

    # Mostrar información actualizada
    print(producto1)
    print(producto2)
