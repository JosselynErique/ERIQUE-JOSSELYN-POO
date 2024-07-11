class EjemploDestructor:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f'Objeto {self.nombre} creado.')

    def __del__(self):
        print(f'Objeto {self.nombre} destruido.')

# Ejemplo de uso
def ejemplo_uso():
    objeto1 = EjemploDestructor('objeto1')
    objeto2 = EjemploDestructor('objeto2')

ejemplo_uso()
