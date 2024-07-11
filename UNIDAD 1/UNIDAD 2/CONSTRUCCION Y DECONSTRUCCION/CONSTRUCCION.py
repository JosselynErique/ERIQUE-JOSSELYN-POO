class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")


# Ejemplo de uso
def ejemplo_uso():
    persona1 = Persona(" JOSSELYN", 30)
    persona1.mostrar_informacion()

    persona2 = Persona("MATIAS", 11)
    persona2.mostrar_informacion()


ejemplo_uso()
