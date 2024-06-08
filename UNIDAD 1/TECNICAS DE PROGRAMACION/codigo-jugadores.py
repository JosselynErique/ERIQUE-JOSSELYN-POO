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

# Clases derivadas: Herencia
class Guerrero(Personaje):
    def atacar(self, enemigo):
        enemigo.recibir_dano(self.ataque)
        print(f"{self.nombre} ha realizado {self.ataque} puntos de daño a {enemigo.nombre}")

class Mago(Personaje):
    def atacar(self, enemigo):
        enemigo.recibir_dano(self.ataque)
        print(f"{self.nombre} ha realizado {self.ataque} puntos de daño a {enemigo.nombre}")

# Función que demuestra Polimorfismo
def combate(jugador_1, jugador_2):
    turno = 1
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print(f"\nTurno {turno}:")
        print(f"Acción de {jugador_1.nombre}:")
        jugador_1.atacar(jugador_2)
        if jugador_2.esta_vivo():
            print(f"Acción de {jugador_2.nombre}:")
            jugador_2.atacar(jugador_1)
        turno += 1
    if jugador_1.esta_vivo():
        print(f"\n{jugador_1.nombre} ha ganado el combate")
    else:
        print(f"\n{jugador_2.nombre} ha ganado el combate")

# Ejemplos de uso
if __name__ == "__main__":
    personaje_1 = Guerrero("Leonidas", 50, 10)
    personaje_2 = Mago("Bruno", 40, 8)

    print("Atributos de los personajes:")
    personaje_1.mostrar_atributos()
    personaje_2.mostrar_atributos()

    print("\n¡Comienza el combate!")
    combate(personaje_1, personaje_2)
