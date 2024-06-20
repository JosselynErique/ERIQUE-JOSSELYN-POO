# Definición de la clase Empleado
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        self.email = nombre.lower() + "@empresa.com"  # Generamos el email automáticamente

    def __str__(self):
        return f"Empleado: {self.nombre}, Salario: {self.salario}"

    def aplicar_aumento(self, aumento):
        self.salario = self.salario + aumento
        print(f"Se aplicó un aumento de {aumento} al salario de {self.nombre}. Salario actualizado: {self.salario}")


# Ejemplo de uso del sistema de gestión de empleados
if __name__ == "__main__":
    # Crear empleados
    empleado1 = Empleado("Juan Pérez", 500)
    empleado2 = Empleado("María López", 650)

    # Mostrar información inicial de los empleados
    print(empleado1)
    print(empleado2)

    # Aplicar aumento de salario a María
    empleado2.aplicar_aumento(500)

    # Mostrar información actualizada
    print(empleado1)
    print(empleado2)
