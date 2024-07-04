# Definición de la clase base 'Animal'
class Animal:
    def __init__(self, nombre, edad):
        # Atributos protegidos
        self._nombre = nombre
        self._edad = edad

    # Método abstracto para hacer sonido
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las clases derivadas")

    def __str__(self):
        return f"{self._nombre}, {self._edad} años"

# Definición de la clase derivada 'Perro' que hereda de 'Animal'
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        # Inicializar atributos heredados usando super()
        super().__init__(nombre, edad)
        # Atributo protegido específico de la clase 'Perro'
        self._raza = raza

    # Sobrescritura del método hacer_sonido (polimorfismo)
    def hacer_sonido(self):
        return "Guau"

    def __str__(self):
        return f"{self._nombre}, {self._edad} años, Raza: {self._raza}"

# Definición de la clase derivada 'Gato' que hereda de 'Animal'
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        # Inicializar atributos heredados usando super()
        super().__init__(nombre, edad)
        # Atributo privado específico de la clase 'Gato' (doble guión bajo)
        self.__color = color

    # Sobrescritura del método hacer_sonido (polimorfismo)
    def hacer_sonido(self):
        return "Miau"

    # Método público para acceder al atributo privado __color
    def obtener_color(self):
        return self.__color

    def __str__(self):
        return f"{self._nombre}, {self._edad} años, Color: {self.__color}"

# Función principal para crear instancias y demostrar la funcionalidad del programa
def main():
    # Crear instancia de Perro
    perro = Perro("BRUNO", 5, "PITBULL")
    # Crear instancia de Gato
    gato = Gato("MISIFUS", 3, "AMARILLO")

    # Demostración de polimorfismo: usar el mismo método hacer_sonido en diferentes clases
    animales = [perro, gato]
    for animal in animales:
        print(f"{animal} dice {animal.hacer_sonido()}")

    # Demostración de encapsulación: acceder al atributo privado __color mediante un método público
    print(f"El color del gato es: {gato.obtener_color()}")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
