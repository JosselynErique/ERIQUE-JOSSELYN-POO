class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

class Zoo:
    def __init__(self):
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def mostrar_animales(self):
        for animal in self.animales:
            print(f'Nombre: {animal.nombre}, Especie: {animal.especie}')


# Ejemplo de uso
zoo = Zoo()
zoo.agregar_animal(Animal("Leo", "León"))
zoo.agregar_animal(Animal("Luna", "Elefante"))

print("Animales en el zoológico:")
zoo.mostrar_animales()
