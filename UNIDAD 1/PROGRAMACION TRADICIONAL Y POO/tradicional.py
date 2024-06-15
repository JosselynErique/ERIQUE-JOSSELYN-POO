# Función para obtener las temperaturas diarias
def obtener_temperaturas_diarias():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Introduce la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal de temperaturas
def calcular_promedio_semanal(temperaturas):
    total = sum(temperaturas)
    promedio = total / len(temperaturas)
    return promedio

# Función principal para ejecutar el programa
def main():
    print("Programa para calcular el promedio semanal de temperaturas")
    temperaturas = obtener_temperaturas_diarias()
    promedio = calcular_promedio_semanal(temperaturas)
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}")

# Ejecución del programa principal
if __name__ == "__main__":
    main()
