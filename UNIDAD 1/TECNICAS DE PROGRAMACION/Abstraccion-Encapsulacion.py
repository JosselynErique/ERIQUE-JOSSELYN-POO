# Clase base: Abstracción y Encapsulación
class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque

    def mostrar_atributos(self):
        print(f"{self.nombre} - Vida: {self.vida} - Ataque: {self.ataque}")

    def esta_vivo(self):
        return self.vida > 0

    def recibir_dano(self, cantidad):
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0
        if not self.esta_vivo():
            print(f"{self.nombre} ha muerto")
