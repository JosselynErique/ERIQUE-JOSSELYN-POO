class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")


# Ejemplo de uso
persona = Persona("Josselyn", 29)
persona.mostrar_info()
