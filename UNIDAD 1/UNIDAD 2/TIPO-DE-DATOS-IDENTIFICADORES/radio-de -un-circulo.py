# Programa para calcular el área de un círculo
# Este programa solicita al usuario que ingrese el radio de un círculo,
# calcula el área del círculo y muestra el resultado.

import math


def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    Parámetros:
    radio (float): El radio del círculo.

    Retorna:
    float: El área del círculo.
    """
    return math.pi * radio ** 2


def es_radio_valido(radio_str):
    """
    Verifica si el radio ingresado es un número válido.

    Parámetros:
    radio_str (str): El radio ingresado como cadena.

    Retorna:
    bool: True si el radio es válido, False en caso contrario.
    """
    try:
        radio = float(radio_str)
        return radio > 0
    except ValueError:
        return False


def main():
    """
    Función principal del programa.
    """
    print("Programa para calcular el área de un círculo.")
    radio_str = input("Por favor, ingrese el radio del círculo: ")

    if es_radio_valido(radio_str):
        radio = float(radio_str)
        area = calcular_area_circulo(radio)
        print(f"El área del círculo con radio {radio} es: {area:.2f}")
    else:
        print("El valor ingresado no es un radio válido. Por favor, ingrese un número positivo.")


if __name__ == "__main__":
    main()
