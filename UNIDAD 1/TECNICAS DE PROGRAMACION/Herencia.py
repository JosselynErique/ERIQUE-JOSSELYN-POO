# Clases derivadas: Herencia
class Guerrero(Personaje):
    def atacar(self, enemigo):
        enemigo.recibir_dano(self.ataque)
        print(f"{self.nombre} ha realizado {self.ataque} puntos de daño a {enemigo.nombre}")

class Mago(Personaje):
    def atacar(self, enemigo):
        enemigo.recibir_dano(self.ataque)
        print(f"{self.nombre} ha realizado {self.ataque} puntos de daño a {enemigo.nombre}")