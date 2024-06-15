class Clima:
    def obtener_informacion(self):
        raise NotImplementedError("Este método debe ser sobrescrito en las clases derivadas")


class ClimaDiario(Clima):
    def __init__(self, dia):
        self.__dia = dia
        self.__temperatura = None

    def ingresar_temperatura(self):
        temp = float(input(f"Introduce la temperatura del día {self.__dia}: "))
        self.__temperatura = temp

    def obtener_temperatura(self):
        return self.__temperatura

    def obtener_informacion(self):
        return f"Día {self.__dia}: {self.__temperatura}°C"


class SemanaClimatica:
    def __init__(self):
        self.dias_clima = [ClimaDiario(i + 1) for i in range(7)]

    def ingresar_temperaturas_semanales(self):
        for dia_clima in self.dias_clima:
            dia_clima.ingresar_temperatura()

    def calcular_promedio_semanal(self):
        total_temperatura = sum(dia_clima.obtener_temperatura() for dia_clima in self.dias_clima)
        promedio = total_temperatura / len(self.dias_clima)
        return promedio

    def mostrar_informacion_semanal(self):
        for dia_clima in self.dias_clima:
            print(dia_clima.obtener_informacion())


def main():
    print("Programa para calcular el promedio semanal de temperaturas usando POO")
    semana = SemanaClimatica()
    semana.ingresar_temperaturas_semanales()
    promedio = semana.calcular_promedio_semanal()
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}")
    semana.mostrar_informacion_semanal()


if __name__ == "__main__":
    main()
