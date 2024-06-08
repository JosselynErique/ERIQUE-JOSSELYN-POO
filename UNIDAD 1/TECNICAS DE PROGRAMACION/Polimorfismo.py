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